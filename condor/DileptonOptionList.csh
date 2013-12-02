#!/bin/tcsh

#### Possible options
#### --useMC    Use MC (True) or not (False)
#### --sample   Type of sample (e.g. TTbar)
#### --dataType Type of real data (ElEl, ElMu or MuMu). Not required for MC
#### --listFile File with a list of root files to be processed
#### --outDir   Directory to put output of script
#### --submit   Whether to submit the jobs to condor (True or False)

###Monte-Carlo
#Signal
#python DileptonSubmit.py --useMC True --sample T53T53_550  --fileList T53T53_550_8TeV_Summer12_TLBSM_53X_v2.txt  --submit True
#python DileptonSubmit.py --useMC True --sample T53T53_600  --fileList T53T53_600_8TeV_Summer12_TLBSM_53X_v2.txt  --submit True
#python DileptonSubmit.py --useMC True --sample T53T53_650  --fileList T53T53_650_8TeV_Summer12_TLBSM_53X_v2.txt  --submit True
#python DileptonSubmit.py --useMC True --sample T53T53_700  --fileList T53T53_700_8TeV_Summer12_TLBSM_53X_v2.txt  --submit True
#python DileptonSubmit.py --useMC True --sample T53T53_750  --fileList T53T53_750_8TeV_Summer12_TLBSM_53X_v2.txt  --submit True

#python DileptonSubmit.py --useMC True --sample T53T53_800  --fileList T53T53_800_8TeV_Summer12_TLBSM_53X_v2.txt  --submit True
#python DileptonSubmit.py --useMC True --sample T53T53_850  --fileList T53T53_850_8TeV_Summer12_TLBSM_53X_v2.txt  --submit True
#python DileptonSubmit.py --useMC True --sample T53T53_900  --fileList T53T53_900_8TeV_Summer12_TLBSM_53X_v2.txt  --submit True
#python DileptonSubmit.py --useMC True --sample T53T53_950  --fileList T53T53_950_8TeV_Summer12_TLBSM_53X_v2.txt  --submit True
#python DileptonSubmit.py --useMC True --sample T53T53_1000 --fileList T53T53_1000_8TeV_Summer12_TLBSM_53X_v2.txt --submit True

#Same-sign backgrounds
#python DileptonSubmit.py --useMC True --sample WWWJets  --fileList WWWJets_MadGraph_8TeV_Summer12_TLBSM_53X_v2.txt      --submit True
#python DileptonSubmit.py --useMC True --sample WZJets   --fileList WZJetsTo3LNu_MadGraph_8TeV_Summer12_TLBSM_53X_v2.txt --submit True
#python DileptonSubmit.py --useMC True --sample WmWmqq   --fileList WmWmqq_MadGraph_8TeV_Summer12_TLBSM_53X_v2.txt       --submit True
#python DileptonSubmit.py --useMC True --sample WpWpqq   --fileList WpWpqq_MadGraph_8TeV_Summer12_TLBSM_53X_v2.txt       --submit True
#python DileptonSubmit.py --useMC True --sample ZZJets   --fileList ZZJetsTo4L_MadGraph_8TeV_Summer12_TLBSM_53X_v2.txt   --submit True

#python DileptonSubmit.py --useMC True --sample TTWJets  --fileList TTWJets_MadGraph_8TeV_Summer12_TLBSM_53X_v2.txt      --submit True
#python DileptonSubmit.py --useMC True --sample TTWWJets --fileList TTWWJets_MadGraph_8TeV_Summer12_TLBSM_53X_v2.txt     --submit True

#Data
#python DileptonSubmit.py --useMC False --sample DoubleMu_Run2012A_13Jul2012 --dataType MuMu --json Cert_190456-196531_8TeV_13Jul2012ReReco_Collisions12_JSON_v2.txt --fileList DoubleMuon_Run2012A-13Jul2012.txt --submit True
#python DileptonSubmit.py --useMC False --sample DoubleMu_Run2012B_13Jul2012 --dataType MuMu --json Cert_190456-196531_8TeV_13Jul2012ReReco_Collisions12_JSON_v2.txt --fileList DoubleMuon_Run2012B-13Jul2012.txt --submit True
#python DileptonSubmit.py --useMC False --sample DoubleMu_Run2012C_Prompt_v1 --dataType MuMu --json Cert_190456-207898_8TeV_PromptReco_Collisions12_JSON.txt --fileList DoubleMuon_Run2012C-PromptReco-v1.txt --submit True
#python DileptonSubmit.py --useMC False --sample DoubleMu_Run2012C_Prompt_v2 --dataType MuMu --json Cert_190456-207898_8TeV_PromptReco_Collisions12_JSON.txt --fileList DoubleMuon_Run2012C-PromptReco-v2.txt --submit True

#python DileptonSubmit.py --useMC False --sample MuEG_Run2012A_13Jul2012 --dataType ElMu --json Cert_190456-196531_8TeV_13Jul2012ReReco_Collisions12_JSON_v2.txt --fileList MuEG_Run2012A-13Jul2012.txt --submit True
#python DileptonSubmit.py --useMC False --sample MuEG_Run2012B_13Jul2012 --dataType ElMu --json Cert_190456-196531_8TeV_13Jul2012ReReco_Collisions12_JSON_v2.txt --fileList MuEG_Run2012B-13Jul2012.txt --submit True
#python DileptonSubmit.py --useMC False --sample MuEG_Run2012C_Prompt_v1 --dataType ElMu --json Cert_190456-207898_8TeV_PromptReco_Collisions12_JSON.txt --fileList MuEG_Run2012C-PromptReco-v1.txt --submit True
#python DileptonSubmit.py --useMC False --sample MuEG_Run2012C_Prompt_v2 --dataType ElMu --json Cert_190456-207898_8TeV_PromptReco_Collisions12_JSON.txt --fileList MuEG_Run2012C-PromptReco-v2.txt --submit True

#python DileptonSubmit.py --useMC False --sample DoubleElectron_Run2012A_13Jul2012   --dataType ElEl --json Cert_190456-196531_8TeV_13Jul2012ReReco_Collisions12_JSON_v2.txt --fileList DoubleElectron_Run2012A-13Jul2012.txt --submit True
#python DileptonSubmit.py --useMC False --sample DoubleElectron_Run2012B_13Jul2012_1 --dataType ElEl --json Cert_190456-196531_8TeV_13Jul2012ReReco_Collisions12_JSON_v2.txt --fileList DoubleElectron_Run2012B-13Jul2012_1.txt --submit True
#python DileptonSubmit.py --useMC False --sample DoubleElectron_Run2012B_13Jul2012_2 --dataType ElEl --json Cert_190456-196531_8TeV_13Jul2012ReReco_Collisions12_JSON_v2.txt --fileList DoubleElectron_Run2012B-13Jul2012_2.txt --submit True
#python DileptonSubmit.py --useMC False --sample DoubleElectron_Run2012C_Prompt_v1_1 --dataType ElEl --json Cert_190456-207898_8TeV_PromptReco_Collisions12_JSON.txt --fileList DoubleElectron_Run2012C-PromptReco-v1_1.txt --submit True
#python DileptonSubmit.py --useMC False --sample DoubleElectron_Run2012C_Prompt_v1_2 --dataType ElEl --json Cert_190456-207898_8TeV_PromptReco_Collisions12_JSON.txt --fileList DoubleElectron_Run2012C-PromptReco-v1_2.txt --submit True
#python DileptonSubmit.py --useMC False --sample DoubleElectron_Run2012C_Prompt_v2_1 --dataType ElEl --json Cert_190456-207898_8TeV_PromptReco_Collisions12_JSON.txt --fileList DoubleElectron_Run2012C-PromptReco-v2_1.txt --submit True
#python DileptonSubmit.py --useMC False --sample DoubleElectron_Run2012C_Prompt_v2_2 --dataType ElEl --json Cert_190456-207898_8TeV_PromptReco_Collisions12_JSON.txt --fileList DoubleElectron_Run2012C-PromptReco-v2_2.txt --submit True

#For fake rate
#python DileptonSubmit.py --useMC True --sample ZJets_OneLep --fileList DYJetsToLL_M-50_TuneZ2Star_8TeV_Summer12_TLBSM_53X_v2.txt                        --outDir /uscmst1b_scratch/lpc1/lpcphys/avetisya/TopPartners/SingleLepton --submit True
#python DileptonSubmit.py --useMC True --sample WJets_OneLep --fileList WJetsToLNu_TuneZ2Star_8TeV_Summer12_TLBSM_53X_v2.txt                             --outDir /uscmst1b_scratch/lpc1/lpcphys/avetisya/TopPartners/SingleLepton --submit True
#python DileptonSubmit.py --useMC True --sample TTbar_OneLep --fileList TTJets_MassiveBinDECAY_TuneZ2star_8TeV-madgraph-tauola_Summer12_TLBSM_53X_v2.txt --outDir /uscmst1b_scratch/lpc1/lpcphys/avetisya/TopPartners/SingleLepton --submit True

#python DileptonSubmit.py --useMC True --sample TTbar --fileList TTJets_MassiveBinDECAY_TuneZ2star_8TeV-madgraph-tauola_Summer12_TLBSM_53X_v2.txt --submit True
