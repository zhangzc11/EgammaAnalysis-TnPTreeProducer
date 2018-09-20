from CRABClient.UserUtilities import config, getUsernameFromSiteDB
import sys
config = config()

submitVersion = "egmNtuple_V2ID_2016"

doEleTree = 'doEleID=True'
doPhoTree = 'doPhoID=True'
doHLTTree = 'doTrigger=False'
doRECO    = 'doRECO=False'

mainOutputDir = '/store/group/phys_egamma/swmukher/%s' % submitVersion

config.General.transferLogs = False

config.JobType.pluginName  = 'Analysis'

# Name of the CMSSW configuration file
config.JobType.psetName  = '/afs/cern.ch/user/s/swmukher/work/NtupleProd_2016/CMSSW_10_2_5/src/EgammaAnalysis/TnPTreeProducer/python/TnPTreeProducer_cfg.py'
config.Data.allowNonValidInputDataset = False

config.Data.inputDBS = 'global'
config.Data.publication = False

#config.Data.publishDataName = 
config.Site.storageSite = 'T2_CH_CERN'


if __name__ == '__main__':

    from CRABAPI.RawCommand import crabCommand
    from CRABClient.ClientExceptions import ClientException
    from httplib import HTTPException

    # We want to put all the CRAB project directories from the tasks we submit here into one common directory.
    # That's why we need to set this parameter (here or above in the configuration file, it does not matter, we will not overwrite it).
    config.General.workArea = 'crab_%s' % submitVersion

    def submit(config):
        try:
            crabCommand('submit', config = config)
        except HTTPException as hte:
            print "Failed submitting task: %s" % (hte.headers)
        except ClientException as cle:
            print "Failed submitting task: %s" % (cle)


    ##### now submit DATA
    config.Data.outLFNDirBase = '%s/%s/' % (mainOutputDir,'data')
    config.Data.splitting     = 'LumiBased'
    config.Data.lumiMask      = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions16/13TeV/ReReco/Final/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt'
    config.Data.unitsPerJob   = 90
    config.JobType.pyCfgParams  = ['isMC=False','isAOD=True',doEleTree,doPhoTree,doHLTTree,doRECO,'GT=80X_dataRun2_2016LegacyRepro_v4']

#    config.General.requestName  = 'RunB_1'
#    config.Data.inputDataset    = '/SingleElectron/Run2016B-07Aug17_ver1-v1/AOD'
#    submit(config)

#    config.General.requestName  = 'RunB_2'
#    config.Data.inputDataset    = '/SingleElectron/Run2016B-07Aug17_ver2-v2/AOD'
#    submit(config)

#    config.General.requestName  = 'RunC'
#    config.Data.inputDataset    = '/SingleElectron/Run2016C-07Aug17-v1/AOD'
#    submit(config)

#    config.General.requestName  = 'RunD'
#    config.Data.inputDataset    = '/SingleElectron/Run2016D-07Aug17-v1/AOD'
#    submit(config)

#    config.General.requestName  = 'RunE'
#    config.Data.inputDataset    = '/SingleElectron/Run2016E-07Aug17-v1/AOD'
#    submit(config)

#    config.General.requestName  = 'RunF'
#    config.Data.inputDataset    = '/SingleElectron/Run2016F-07Aug17-v1/AOD'
#    submit(config)

#    config.General.requestName  = 'RunG'
#    config.Data.inputDataset    = '/SingleElectron/Run2016G-07Aug17-v1/AOD'
#    submit(config)

    config.General.requestName  = 'RunG'
    config.Data.inputDataset    = '/SingleElectron/Run2016H-07Aug17-v1/AOD'
    submit(config)




    
