lumi_selection = "ev: ev.IsCertified"
trigger_selection = "ev: ev.IsTriggered"
filter_selection = "ev: (ev.Flag_goodVertices>0.5) & "\
                       "(ev.Flag_globalTightHalo2016Filter>0.5) & "\
                       "(ev.Flag_HBHENoiseFilter>0.5) & "\
                       "(ev.Flag_HBHENoiseIsoFilter>0.5) & "\
                       "(ev.Flag_EcalDeadCellTriggerPrimitiveFilter>0.5) & "\
                       "(ev.Flag_eeBadScFilter>0.5)"
met_selection = "ev: ev.METnoX.pt > 200."
dphi_jet_met_selection = "ev: ev.MinDPhiJ1234METnoX > 0.5"
dcalo_pfmet_selection = "ev: ev.MET_dCaloMET < 0.5"
jet_selection = "ev: (ev.JetSelectionClean.size > 0) & "\
                    "(ev.JetSelectionClean.size == ev.JetVetoClean.size) & "\
                    "(ev.LeadJetSelectionClean.pt > 200.) & "\
                    "(ev.LeadJetSelectionClean.chHEF > 0.1) & "\
                    "(ev.LeadJetSelectionClean.chHEF < 0.95)"
muon_selection = "ev: (ev.MuonSelection.size == ev.MuonVeto.size) & (ev.MuonVeto.size == {})"
ele_selection = "ev: (ev.ElectronSelection.size == ev.ElectronVeto.size) & (ev.ElectronVeto.size == {})"
pho_veto = "ev: (ev.PhotonSelection.size == ev.PhotonVeto.size) & (ev.PhotonVeto.size == 0)"
nbjet_veto = "ev: (ev.nBJetSelectionCleanMedium == 0)"
tau_veto = "ev: (ev.TauSelectionClean.size == ev.TauVetoClean.size) & (ev.TauVetoClean.size == 0)"
mtw_selection = "ev: (ev.MTW >= 30.) & (ev.MTW < 125.)"
mll_selection = "ev: (ev.MLL >= 71.) & (ev.MLL < 111.)"

# Selections
data_selection = [
    lumi_selection,
    trigger_selection,
]

mc_selection = []

baseline_selection = [
    filter_selection,
    met_selection,
    dphi_jet_met_selection,
    dcalo_pfmet_selection,
    jet_selection,
    pho_veto,
    nbjet_veto,
    tau_veto,
]

monojet_selection = [
    muon_selection.format(0),
    ele_selection.format(0),
]

singlemuon_selection = [
    muon_selection.format(1),
    ele_selection.format(0),
    mtw_selection,
]

doublemuon_selection = [
    muon_selection.format(2),
    ele_selection.format(0),
    mll_selection,
]
