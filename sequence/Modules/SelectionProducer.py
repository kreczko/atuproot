import sequence.event_selection as es
from utils.Lambda import Lambda

import numpy as np

class SelectionProducer(object):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self.debug = False

    def begin(self, event):
        self.isdata = event.config.dataset.isdata

        baseline = es.data_selection if self.isdata else es.mc_selection
        self.selections = {
            "Monojet": baseline + es.baseline_selection + es.monojet_selection,
            "SingleMuon": baseline + es.baseline_selection + es.singlemuon_selection,
            "DoubleMuon": baseline + es.baseline_selection + es.doublemuon_selection,
        }

        self.selections_lambda = {cutflow: [Lambda(cut) for cut in selection]
                                  for cutflow, selection in self.selections.items()}

    def event(self, event):
        if self.debug:
            results = [cut(event) for cut in self.selections_lambda["SingleMuon"]]
            for idx in range(len(results)-1):
                results[idx+1] = results[idx+1] & results[idx]
            for idx in range(len(self.selections_lambda["SingleMuon"])):
                print(self.selections_lambda["SingleMuon"][idx].function, results[idx])
            exit()

        for cutflow, selection in self.selections_lambda.items():
            setattr(event, "Cutflow_{}".format(cutflow),
                    reduce(lambda x, y: x & y, [cut(event) for cut in selection]))

    def end(self):
        self.selections_lambda = {}
