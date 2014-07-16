import FWCore.ParameterSet.Config as cms
import FWCore.PythonUtilities.LumiList as LumiList
import FWCore.ParameterSet.Types as CfgTypes

process = cms.Process("LJMetCom")

#Arguments from condor submit script which are used more than once
condorIsMC = bool(CONDOR_ISMC)
relBase    = str('CONDOR_RELBASE')
condorJSON = str('CONDOR_JSON')

# Dilepton calculator options
process.load('LJMet.Com.DileptonCalc_cfi')
process.DileptonCalc.isMc     = condorIsMC
process.DileptonCalc.dataType = cms.string('CONDOR_DATATYPE')
process.load('LJMet.Com.PdfCalc_cfi')

############################################################
#
# FWLite application options
#
process.ljmet = cms.PSet(
    isMc = cms.bool(condorIsMC),
    runs = cms.vint32([])
)

#Exclude unnecessary calculators
process.ljmet.excluded_calculators = cms.vstring(
    'WprimeCalc',
    'LjetsTopoCalc',
    'LjetsTopoCalcNew',
    'StopCalc',
    'PdfCalc',
    'TprimeCalc',
    'ChargedHiggsCalc',
    'TopEventReweightCalc',
    'JetSubCalc'
    ) 
############################################################
#
# Event selector options
#
process.event_selector = cms.PSet(

    selection = cms.string('DileptonSelector'),
    isMc      = cms.bool(condorIsMC),

    # cuts
    #HLT
    trigger_cut              = cms.bool(True),
    dump_trigger             = cms.bool(False),

    #Can use same trigger paths for data and MC since MC is always one of the data versions
    trigger_path_ee          = cms.vstring('HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v15',
                                           'HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v16',
                                           'HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v17',
                                           'HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v18',
                                           'HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v19'),
    
    trigger_path_em          = cms.vstring('HLT_Mu8_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v4', 'HLT_Mu8_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v5',
                                           'HLT_Mu8_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v6', 'HLT_Mu8_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v7',
                                           'HLT_Mu8_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v8', 'HLT_Mu8_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v9',
                                           'HLT_Mu17_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v4', 'HLT_Mu17_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v5',
                                           'HLT_Mu17_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v6', 'HLT_Mu17_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v7',
                                           'HLT_Mu17_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v8', 'HLT_Mu17_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v9'),

    trigger_path_mm          = cms.vstring('HLT_Mu17_Mu8_v16', 'HLT_Mu17_Mu8_v17', 'HLT_Mu17_Mu8_v18',
                                           'HLT_Mu17_Mu8_v19', 'HLT_Mu17_Mu8_v21', 'HLT_Mu17_Mu8_v22',
                                           'HLT_Mu17_TkMu8_v9',  'HLT_Mu17_TkMu8_v10', 'HLT_Mu17_TkMu8_v11',
                                           'HLT_Mu17_TkMu8_v12', 'HLT_Mu17_TkMu8_v13', 'HLT_Mu17_TkMu8_v14'),    

    pv_cut                   = cms.bool(True),
    hbhe_cut                 = cms.bool(True),

    jet_cuts                 = cms.bool(False),
    jet_minpt                = cms.double(20.0),
    jet_maxeta               = cms.double(5),
    min_jet                  = cms.int32(0),
    max_jet                  = cms.int32(4000),

    muon_cuts                = cms.bool(True),
    min_muon                 = cms.int32(0),
    muon_minpt               = cms.double(10.0),
    muon_maxeta              = cms.double(2.5),
    max_muon                 = cms.int32(20),

    electron_cuts            = cms.bool(True),
    min_electron             = cms.int32(0),
    electron_minpt           = cms.double(10.0),
    electron_maxeta          = cms.double(2.5),
    max_electron             = cms.int32(20),

    min_lepton               = cms.int32(2),

    met_cuts                 = cms.bool(False),
    min_met                  = cms.double(0.0),

    btag_cuts                = cms.bool(False),
    btagOP                   = cms.string("CSVL"),
    btag_1                   = cms.bool(True),
    btag_2                   = cms.bool(True),
    btag_3                   = cms.bool(False),

    trigger_collection       = cms.InputTag('TriggerResults::HLT'),
    pv_collection            = cms.InputTag('goodOfflinePrimaryVertices'),
    jet_collection           = cms.InputTag('goodPatJetsPFlow'),
    muon_collection          = cms.InputTag('selectedPatMuonsPFlowLoose'),
    electron_collection      = cms.InputTag('selectedPatElectronsPFlowLoose'),
    met_collection           = cms.InputTag('patMETsPFlow'),

    JEC_txtfile = cms.string(relBase+'/src/LJMet/Dilepton/JEC/uncertainties/Summer13_V5_DATA_UncertaintySources_AK5PFchs.txt'),
    JEC_source  = cms.string("Total"),
    JECup		     = cms.bool(False),
    JECdown                  = cms.bool(False),
    JERup                    = cms.bool(False),
    JERdown                  = cms.bool(False),
    METup                    = cms.bool(False),
    METdown                  = cms.bool(False),
    METuncert                = cms.double(0.1),

#    BTagUncertBcUp                  = cms.bool(False),
    do53xJEC                 = cms.bool(True),

    MCL1JetPar = cms.string(relBase+'/src/LJMet/Dilepton/JEC/Summer13_V4_MC_txts_fromDB/Summer13_V4_MC_L1FastJet_AK5PFchs.txt'),
    MCL2JetPar = cms.string(relBase+'/src/LJMet/Dilepton/JEC/Summer13_V4_MC_txts_fromDB/Summer13_V4_MC_L2Relative_AK5PFchs.txt'),
    MCL3JetPar = cms.string(relBase+'/src/LJMet/Dilepton/JEC/Summer13_V4_MC_txts_fromDB/Summer13_V4_MC_L3Absolute_AK5PFchs.txt'),

    DataL1JetPar = cms.string(relBase+'/src/LJMet/Dilepton/JEC/Summer13_V4_DATA_txts_fromDB/Summer13_V4_DATA_L1FastJet_AK5PFchs.txt'),
    DataL2JetPar = cms.string(relBase+'/src/LJMet/Dilepton/JEC/Summer13_V4_DATA_txts_fromDB/Summer13_V4_DATA_L2Relative_AK5PFchs.txt'),
    DataL3JetPar = cms.string(relBase+'/src/LJMet/Dilepton/JEC/Summer13_V4_DATA_txts_fromDB/Summer13_V4_DATA_L3Absolute_AK5PFchs.txt'),
    DataResJetPar = cms.string(relBase+'/src/LJMet/Dilepton/JEC/Summer13_V4_DATA_txts_fromDB/Summer13_V4_DATA_L2L3Residual_AK5PFchs.txt')
)

process.load('LJMet.Com.TopEventReweightCalc_cfi')
process.TopEventReweightCalc.isMc     = condorIsMC
process.TopEventReweightCalc.reweightBSemiLeptDecyas = cms.bool(False)
process.TopEventReweightCalc.nuDecayFractionSource = cms.double(0.25)
process.TopEventReweightCalc.nuDecayFractionTarget = cms.double(0.239)
process.TopEventReweightCalc.reweightBfragmentation = cms.bool(False)
process.TopEventReweightCalc.fragSourceFile = cms.string(relBase+'/src/LJMet/Dilepton/data/TopUtils_data_MC_BJES_TuneZ2star.root')
process.TopEventReweightCalc.fragTargetFile = cms.string(relBase+'/src/LJMet/Dilepton/data/TopUtils_data_MC_BJES_TuneZ2star_rbLEP.root')


#######################################################
#
# Input files
#
process.inputs = cms.PSet (
    nEvents    = cms.int32(-1),
    skipEvents = cms.int32(0),
    useHcalLaserEventFilter = cms.bool(True),
    lumisToProcess = CfgTypes.untracked(CfgTypes.VLuminosityBlockRange()),
    fileNames  = cms.vstring(
CONDOR_FILELIST
    )
)

# JSON
if not condorIsMC:
    JsonFile = relBase+'/src/LJMet/singletPrime/json/'+condorJSON
    myList   = LumiList.LumiList(filename=JsonFile).getCMSSWString().split(',')
    process.inputs.lumisToProcess.extend(myList)
        
        
        
#######################################################
#
# Output
#
process.outputs = cms.PSet (
    outputName = cms.string('CONDOR_OUTFILE'),
    treeName   = cms.string('ljmet'),
)

#######################################################
#
# Object selector options
#

# Primary vertex
process.load('PhysicsTools.SelectorUtils.pvSelector_cfi')
process.pvSelector.pvSrc   = cms.InputTag('goodOfflinePrimaryVertices')
process.pvSelector.minNdof = cms.double(4.0)
process.pvSelector.maxZ    = cms.double(24.0)
process.pvSelector.maxRho  = cms.double(2.0)

# jets
process.load('PhysicsTools.SelectorUtils.pfJetIDSelector_cfi') 
process.pfJetIDSelector.version = cms.string('FIRSTDATA')
process.pfJetIDSelector.quality = cms.string('LOOSE')
