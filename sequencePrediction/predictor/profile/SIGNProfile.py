from sequencePrediction.predictor.profile.Profile import Profile

class SIGNProfile(Profile):
    # def Apply(self):
    #     self.parameters["sequenceMinSize"] = "10"
    #     self.parameters["sequenceMaxSize"] = "999"
    #     self.parameters["removeDuplicatesMethod"] = "1"
    #     self.parameters["consequentSize"] = "3"
    #     self.parameters["windowSize"] = "7"
    #
    #     # /////////////
    #     # CPT parameters
    #     # Training
    #     self.parameters["splitMethod"] = "0"  # 0 for no split", "1 for basicSplit", "2 for complexSplit
    #     self.parameters["splitLength"] = "20"  # max tree height
    #     self.parameters["minSup"] = "0.3"  # SEI compression, minSup to remove low supporting items
    #     # CCF compression
    #     self.parameters["CCFmin"] = "2"
    #     self.parameters["CCFmax"] = "4"
    #     self.parameters["CCFsup"] = "2"
    #     # Prediction
    #     self.parameters["recursiveDividerMin"] = "3"  # should be >= 0 and < recursiveDividerMax
    #     self.parameters["recursiveDividerMax"] = "99"  # should be > recusiveDividerMax and < windowSize
    #     self.parameters["minPredictionRatio"] = "1.0"  # should be over 0
    #     self.parameters["noiseRatio"] = "1.0"  # should be in the range ]0,1]
    def Apply(self):
        self.parameters["sequenceMinSize"] = "8"
        self.parameters["sequenceMaxSize"] = "999"
        self.parameters["removeDuplicatesMethod"] = "1"
        self.parameters["consequentSize"] = "3"
        self.parameters["windowSize"] = "5"

        # /////////////
        # CPT parameters
        # Training
        self.parameters["splitMethod"] = "1"  # 0 for no split", "1 for basicSplit", "2 for complexSplit
        self.parameters["splitLength"] = "22"  # max tree height
        self.parameters["minSup"] = "0.0005"  # SEI compression, minSup to remove low supporting items
        # CCF compression
        self.parameters["CCFmin"] = "2"
        self.parameters["CCFmax"] = "4"
        self.parameters["CCFsup"] = "2"
        # Prediction
        self.parameters["recursiveDividerMin"] = "3"  # should be >= 0 and < recursiveDividerMax
        self.parameters["recursiveDividerMax"] = "99"  # should be > recusiveDividerMax and < windowSize
        self.parameters["minPredictionRatio"] = "1.0"  # should be over 0
        self.parameters["noiseRatio"] = "1.0"  # should be in the range ]0,1]