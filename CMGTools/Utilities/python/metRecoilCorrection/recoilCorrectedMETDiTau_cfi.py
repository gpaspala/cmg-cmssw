import FWCore.ParameterSet.Config as cms

from CMGTools.Utilities.metRecoilCorrection.rootfile_dir import rootfile_dir

recoilCorrectedMETDiTau  = cms.EDProducer(
    "RecoilCorrectedMETProducerDiTau",
    # metSrc = cms.InputTag('cmgPFMET'),
    # the tau is on the first leg and the muon on the second leg
    recBosonSrc = cms.InputTag('cmgDiTauSel'),
    genBosonSrc = cms.InputTag('genWorZ'),
    jetSrc = cms.InputTag('cmgPFJetForRecoil'),
    # 1: lepton is on leg1; 2: lepton is on leg2;
    # 0: take both legs as leptons, and sum them up 
    leptonLeg = cms.int32(0),
    # 1: type 1; 2 : type 2; 0 : all (use 1)
    correctionType = cms.int32(2),
    fileCorrectTo = cms.string(rootfile_dir + 'recoilfit_ztt53X_20pv_njet.root'),
    # you should not have to change the files below
    #fileZmmData = cms.string(rootfile_dir + 'recoilfit_datamm53X_20pv_njet.root'),
    #fileZmmMC = cms.string(rootfile_dir + 'recoilfit_zmm53X_20pv_njet.root'),
    fileZmmData = cms.string(rootfile_dir + 'recoilfit_datamm53XRR_2012_njet.root'),
    fileZmmMC = cms.string(rootfile_dir + 'recoilfit_zmm53XRR_2012_njet.root'),
    enable = cms.bool(True),
    force = cms.bool(False),
    verbose = cms.untracked.bool( False )
    )

