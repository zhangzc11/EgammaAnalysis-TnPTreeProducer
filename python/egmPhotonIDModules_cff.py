import FWCore.ParameterSet.Config as cms

###################################################################
## ID MODULES
###################################################################

from PhysicsTools.SelectorUtils.tools.vid_id_tools import *

def setIDs(process, options):

    dataFormat = DataFormat.MiniAOD
    phoProducer = "PatPhotonSelectorByValueMap"
    if (options['useAOD']):
        dataFormat = DataFormat.AOD
        phoProducer = "PhotonSelectorByValueMap"

    switchOnVIDPhotonIdProducer(process, dataFormat)
        
    # define which IDs we want to produce
    my_id_modules = ['RecoEgamma.PhotonIdentification.Identification.cutBasedPhotonID_Spring16_V2p2_cff'   ,
                     'RecoEgamma.PhotonIdentification.Identification.cutBasedPhotonID_Spring16_V2p2_delayedphoton_cff',
                     'RecoEgamma.PhotonIdentification.Identification.cutBasedPhotonID_Spring16_V2p2_delayedphotonOOT_cff',
                     #'RecoEgamma.PhotonIdentification.Identification.mvaPhotonID_Spring16_nonTrig_V1_cff',
                     #'RecoEgamma.PhotonIdentification.Identification.cutBasedPhotonID_Fall17_94X_V1_cff',
                     #'RecoEgamma.PhotonIdentification.Identification.mvaPhotonID_Fall17_94X_V1_cff',
                     #'RecoEgamma.PhotonIdentification.Identification.mvaPhotonID_Fall17_94X_V2_cff',
                     #'RecoEgamma.PhotonIdentification.Identification.cutBasedPhotonID_Fall17_100X_V2_cff'
                     ]
                 
    for idmod in my_id_modules:
        setupAllVIDIdsInModule(process, idmod, setupVIDPhotonSelection)

    process.egmPhotonIDs.physicsObjectSrc        = cms.InputTag(options['PHOTON_COLL'])
    process.photonIDValueMapProducer.srcMiniAOD  = cms.InputTag(options['PHOTON_COLL'])
    process.photonMVAValueMapProducer.srcMiniAOD = cms.InputTag(options['PHOTON_COLL'])
#    process.photonMVAValueMapProducer.src        = cms.InputTag(options['PHOTON_COLL'])


    process.probePhoCutBasedLoose = cms.EDProducer( phoProducer,
                                                    input     = cms.InputTag("goodPhotons"),
                                                    cut       = cms.string(options['PHOTON_CUTS']),
                                                    selection = cms.InputTag("egmPhotonIDs:cutBasedPhotonID-Spring16-V2p2-loose"),
                                                    id_cut    = cms.bool(True)
                                                    )

    process.probePhoCutBasedMedium = process.probePhoCutBasedLoose.clone()
    process.probePhoCutBasedMedium.selection = cms.InputTag("egmPhotonIDs:cutBasedPhotonID-Spring16-V2p2-medium")
    process.probePhoCutBasedTight = process.probePhoCutBasedLoose.clone()
    process.probePhoCutBasedTight.selection = cms.InputTag("egmPhotonIDs:cutBasedPhotonID-Spring16-V2p2-tight")

    process.probePhoCutBasedLoose80X  = process.probePhoCutBasedLoose.clone()
    process.probePhoCutBasedMedium80X = process.probePhoCutBasedLoose.clone()
    process.probePhoCutBasedTight80X  = process.probePhoCutBasedLoose.clone()
    process.probePhoCutBasedLooseDelayedPhotonGED  = process.probePhoCutBasedLoose.clone()
    process.probePhoCutBasedMediumDelayedPhotonGED = process.probePhoCutBasedLoose.clone()
    process.probePhoCutBasedTightDelayedPhotonGED  = process.probePhoCutBasedLoose.clone()
    process.probePhoCutBasedLooseDelayedPhotonOOT  = process.probePhoCutBasedLoose.clone()
    process.probePhoCutBasedMediumDelayedPhotonOOT = process.probePhoCutBasedLoose.clone()
    process.probePhoCutBasedTightDelayedPhotonOOT  = process.probePhoCutBasedLoose.clone()
    process.probePhoCutBasedLoose80X.selection  = cms.InputTag("egmPhotonIDs:cutBasedPhotonID-Spring16-V2p2-loose"  )
    process.probePhoCutBasedMedium80X.selection = cms.InputTag("egmPhotonIDs:cutBasedPhotonID-Spring16-V2p2-medium" )
    process.probePhoCutBasedTight80X.selection  = cms.InputTag("egmPhotonIDs:cutBasedPhotonID-Spring16-V2p2-tight"  )
    process.probePhoCutBasedLooseDelayedPhotonGED.selection  = cms.InputTag("egmPhotonIDs:cutBasedPhotonID-Spring16-V2p2-delayedphoton-loose"  )
    process.probePhoCutBasedMediumDelayedPhotonGED.selection = cms.InputTag("egmPhotonIDs:cutBasedPhotonID-Spring16-V2p2-delayedphoton-medium" )
    process.probePhoCutBasedTightDelayedPhotonGED.selection  = cms.InputTag("egmPhotonIDs:cutBasedPhotonID-Spring16-V2p2-delayedphoton-tight"  )
    process.probePhoCutBasedLooseDelayedPhotonOOT.selection  = cms.InputTag("egmPhotonIDs:cutBasedPhotonID-Spring16-V2p2-delayedphotonOOT-loose"  )
    process.probePhoCutBasedMediumDelayedPhotonOOT.selection = cms.InputTag("egmPhotonIDs:cutBasedPhotonID-Spring16-V2p2-delayedphotonOOT-medium" )
    process.probePhoCutBasedTightDelayedPhotonOOT.selection  = cms.InputTag("egmPhotonIDs:cutBasedPhotonID-Spring16-V2p2-delayedphotonOOT-tight"  )

'''
    process.probePhoCutBasedLoose94X  = process.probePhoCutBasedLoose.clone()
    process.probePhoCutBasedMedium94X = process.probePhoCutBasedLoose.clone()
    process.probePhoCutBasedTight94X  = process.probePhoCutBasedLoose.clone()
    process.probePhoCutBasedLoose94X.selection  = cms.InputTag("egmPhotonIDs:cutBasedPhotonID-Fall17-94X-V1-loose"  )
    process.probePhoCutBasedMedium94X.selection = cms.InputTag("egmPhotonIDs:cutBasedPhotonID-Fall17-94X-V1-medium" )
    process.probePhoCutBasedTight94X.selection  = cms.InputTag("egmPhotonIDs:cutBasedPhotonID-Fall17-94X-V1-tight"  )

    process.probePhoCutBasedLoose100XV2  = process.probePhoCutBasedLoose.clone()
    process.probePhoCutBasedMedium100XV2 = process.probePhoCutBasedLoose.clone()
    process.probePhoCutBasedTight100XV2  = process.probePhoCutBasedLoose.clone()
    process.probePhoCutBasedLoose100XV2.selection  = cms.InputTag("egmPhotonIDs:cutBasedPhotonID-Fall17-100X-V2-loose"  )
    process.probePhoCutBasedMedium100XV2.selection = cms.InputTag("egmPhotonIDs:cutBasedPhotonID-Fall17-100X-V2-medium" )
    process.probePhoCutBasedTight100XV2.selection  = cms.InputTag("egmPhotonIDs:cutBasedPhotonID-Fall17-100X-V2-tight"  )

    process.probePhoMVA = process.probePhoCutBasedLoose.clone()
    process.probePhoMVA.selection = cms.InputTag("egmPhotonIDs:mvaPhoID-Spring16-nonTrig-V1-wp90")    
    process.probePhoMVA80Xwp90 = process.probePhoCutBasedLoose.clone()
    process.probePhoMVA80Xwp80 = process.probePhoCutBasedLoose.clone()
    process.probePhoMVA80Xwp90.selection = cms.InputTag("egmPhotonIDs:mvaPhoID-Spring16-nonTrig-V1-wp90")    
    process.probePhoMVA80Xwp80.selection = cms.InputTag("egmPhotonIDs:mvaPhoID-Spring16-nonTrig-V1-wp80")    

    process.probePhoMVA94Xwp90 = process.probePhoCutBasedLoose.clone()
    process.probePhoMVA94Xwp80 = process.probePhoCutBasedLoose.clone()
    process.probePhoMVA94Xwp90.selection = cms.InputTag("egmPhotonIDs:mvaPhoID-RunIIFall17-v1-wp90")    
    process.probePhoMVA94Xwp80.selection = cms.InputTag("egmPhotonIDs:mvaPhoID-RunIIFall17-v1-wp80")    

    process.probePhoMVA94XV2wp90 = process.probePhoCutBasedLoose.clone()
    process.probePhoMVA94XV2wp80 = process.probePhoCutBasedLoose.clone()
    process.probePhoMVA94XV2wp90.selection = cms.InputTag("egmPhotonIDs:mvaPhoID-RunIIFall17-v2-wp90")    
    process.probePhoMVA94XV2wp80.selection = cms.InputTag("egmPhotonIDs:mvaPhoID-RunIIFall17-v2-wp80")    
'''
#    process.probePhoMVA94Xwp90.selection = cms.InputTag("egmPhotonIDs:mvaPhoID-Spring16-nonTrig-V1-wp90")    
#    process.probePhoMVA94Xwp80.selection = cms.InputTag("egmPhotonIDs:mvaPhoID-Spring16-nonTrig-V1-wp90")    
