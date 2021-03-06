#!/usr/bin/python

import os
import re
import sys
import fileinput
import getopt
import subprocess
import socket
#Configuration options that usually don't change
files_per_job = 5

#Absolute path that precedes '/store...'
# The script checks whether it is an absolute path or not

if (socket.gethostname().find('brux')>=0) :
    brux=bool(True)
    print "Submitting jobs at Brown"
    sePath='\'file://'
    storePath='/mnt/hadoop'
    setupString='source \/state\/partition1\/osg_app\/cmssoft\/cms\/cmsset_default.csh'
elif (socket.gethostname().find('fnal')>=0):
    brux=bool(False)
    print "Submitting jobs at FNAL"
    sePath='\'dcache:///pnfs/cms/WAX/11' 
    storePath=''
    setupString='source \/uscmst1\/prod\/sw\/cms\/cshrc prod'
else:
    print "Script not done for ", socket.gethostname()
    exit()

#JSON file stored in LJMet/Com/data/json/ 
#json='Cert_190456-196531_8TeV_13Jul2012ReReco_Collisions12_JSON_v2.txt'
#json='Cert_190456-206940_8TeV_PromptReco_Collisions12_JSON.txt'
#Folder in LJMet where the lists of file names are kepy
#localFileDir='LJMet/Com/python/Samples_2012/Dilepton/'
#Use the absolute path now

#Configuration options parsed from arguments
#Switching to getopt for compatibility with older python
try:
    opts, args = getopt.getopt(sys.argv[1:], "", ["useMC=", "sample=","dataType=","fileList=", "outDir=","submit=","json=","jec="])
except getopt.GetoptError as err:
    print str(err)
    sys.exit(1)

useMC    = bool(False)
prefix   = str('None')
dataType = str('None')
fileList = str('None')
outDir   = str('None')
json     = str('None')
submit   = bool(False)
jec      = str('Total')
changeJEC= bool(False)

for o, a in opts:
    print o, a
    if o == "--useMC":
        checkUseMC = a in ['True', 'False']
        if not checkUseMC:
            print '--useMC must be True or False!'
            print 'Setting useMC to False'
        else:
            useMC = a
            print 'useMC = ' + useMC
    elif o == "--sample":   prefix   = str(a)
    elif o == "--dataType": dataType = str(a)
    elif o == "--fileList": fileList = str(a)
    elif o == "--outDir":   outDir   = str(a)
    elif o == "--json":     json   = str(a)
    elif o == "--jec":
        jec   = str(a)
	changeJEC = True
	prefix = jec
    elif o == "--submit":
        if a == 'True':     submit = True

if dataType == 'MuEl': dataType = 'ElMu'
checkDataType = dataType in ['ElEl', 'ElMu', 'MuMu']

if (not checkDataType and not useMC):
    print '--dataType for real data must be ElEl, ElMu or MuMu!'
    sys.exit(1)

relBase = os.environ['CMSSW_BASE']

#fileDir = relBase+'/src/'+localFileDir

files = fileList 

if (not os.path.isfile(files)):
    print 'File with input root files '+ fileList +' not found. Please give absolute path'
    sys.exit(1)

outputdir = os.path.abspath('.')
if str(outDir) != 'None': outputdir = outDir
else:                     print 'Output dir not specified. Setting it to current directory.'
#if changeJEC: outputdir = outputdir+'/'+jec

if submit: print 'Will submit jobs to Condor'
else:      print 'Will not submit jobs to Condor'

dir = outputdir+'/'+prefix

if os.path.exists(dir):
    print 'Output directory already exists!'
    sys.exit(1)
else: os.makedirs(dir)

def get_input(num, list):
    result = ''
    file_list = open(files)
    file_count = 0
    for line in file_list:
        if line.find('root')>0:
            file_count=file_count+1
            if file_count>(num-1) and file_count<(num+files_per_job):
                #print line
		#print f_name
                result=result+ sePath
		if (line.strip()[:6]=='/store'):
		    result=result+ storePath
                result=result+line.strip()+'\',\n'
    file_list.close()
    #print result
    return result

j = 1
nfiles = 1

py_file = open(dir+"/"+prefix+"_"+str(j)+".py","w")

print 'CONDOR work dir: '+dir

count = 0
file_list = open(files)
for line in file_list:
    if line.find('root')>0:
        count = count + 1

file_list.close()
        
int_file = open(dir+'/'+'interactive.csh','w')

while ( nfiles <= count ):    
    
    py_templ_file = open(relBase+'/src/LJMet/Dilepton/condor/DileptonTemplate.py')
    
    py_file = open(dir+'/'+prefix+'_'+str(j)+'.py','w')

    #Avoid calling the get_input function once per line in template
    singleFileList = get_input(nfiles, files)
    
    for line in py_templ_file:
        line=line.replace('CONDOR_ISMC',     useMC)
        line=line.replace('CONDOR_DATATYPE', dataType)
        line=line.replace('CONDOR_RELBASE',  relBase)
        line=line.replace('CONDOR_JSON',     json)
        line=line.replace('CONDOR_FILELIST', singleFileList)
        line=line.replace('CONDOR_OUTFILE',  prefix+'_'+str(j))
        if (changeJEC): line=line.replace('Total',  jec)
        py_file.write(line)
    py_file.close()

    if (j == 1): int_file.write('date >  xtimelog.txt; ljmet '+prefix+'_'+str(j)+'.py >& out'+str(j)+'.txt\n')
    else:        int_file.write('date >> xtimelog.txt; ljmet '+prefix+'_'+str(j)+'.py >& out'+str(j)+'.txt\n')
        
    j = j + 1
    nfiles = nfiles + files_per_job
    py_templ_file.close()

int_file.write('date')
int_file.close()
os.system('chmod +x '+dir+'/'+'interactive.csh')

njobs = j - 1

jdl_templ_file = open(relBase+'/src/LJMet/Dilepton/condor/DileptonTemplate.jdl')
jdl_file       = open(dir+'/'+prefix+'.jdl','w')


for line in jdl_templ_file:
    line=line.replace('PREFIX',     prefix)
    line=line.replace('OUTPUT_DIR', dir)
    line=line.replace('CMSSWBASE',  relBase)
    line=line.replace('NJOBS',      str(njobs))
    jdl_file.write(line)

jdl_file.close()

os.system('sed -e \'s/SETUP/'+setupString+'/g\' DileptonTemplate.csh > '+dir+'/'+prefix+'.csh')

if (submit):
    savedPath = os.getcwd()
    os.chdir(dir)
    print njobs
    proc = subprocess.Popen(['condor_submit', prefix+'.jdl'], stdout=subprocess.PIPE) 
    (out, err) = proc.communicate()
    print "condor output:", out
    if (brux):
	print out.splitlines()[-1]
	nbr = out.splitlines()[-1].split(' ')[-1]
	print "job number", nbr[:-1]
	print "job file ", '/home/speer/jobs/'+nbr[:-1]
	job_file = open('/home/speer/jobs/'+nbr[:-1],'w')
	job_file.write(prefix + " "+str(njobs))
	job_file.close()
	#os.system('condor_prio -10 '+nbr[:-1])

    #os.system('condor_submit '+prefix+'.jdl')
    os.chdir(savedPath)
