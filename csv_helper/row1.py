import csv_helper

class row1:
    """
    Description: Class that takes as input a sentence and generates the first row of the csv format.
    """

    def __init__(self, inp):
        """
        Arguments: input sentence
        """
        self.inp = inp
        self.output = ''

    def get_row(self):
        """
        Description: Takes the sentence breaks it to tokens and returns the row
        """
        self.output = ''
        for chunk in self.inp.split(","):
            words = chunk.split()
            if len(words) != 0:
                result = self.generate_row(words)
                self.output += result + ','
        return self.output

    def generate_row(self, words):
        """
        Description: Takes as inputs the tokens and matches the appropriate symbols to each token
        """
        words[0] = words[0].split('(')[1]
        words[-1] = words[-1].split(')')[0]
        out = ""
        file = ""
        count = 1
        inp = []
        pos = []
        if len(words) == 1: # If there is only one word in the sentence given
            out += words[0] + "_0"
        else:
            for i in range(len(words)): # Iterating over all the words
                flag = 0
                if words[i] in csv_helper.val_dict["NUMBERS"]: # If the word is a number
                    if words[i + 1] in csv_helper.val_dict["MEASUREMENT"]:
                        out += words[i] + "#" + words[i + 1]
                    else:
                        out += words[i] + "~"
                    flag = 1
                if words[i] in csv_helper.val_dict["PARTICLE"]: # If the word is a participle
                    out += "*" + words[i]
                    flag = 1
                if words[i] in csv_helper.val_dict["MEASUREMENT"]: # If the word is a measurement type
                    if i != len(words) - 1:
                        out += "@"
                    flag = 1
                if words[i] in csv_helper.val_dict["ORDINAL"] or words[i] in csv_helper.val_dict["QUANTIFIERS"]: # if the word is an ordinal or quantifier
                    out += words[i] + "~"
                    flag = 1
                    
                for item in ["VIBHAKTI", "TAM"]:
                    for index in range(len(csv_helper.val_dict[item])): # Iterating over all vibhaktis in the known list
                        if words[i: i + len(csv_helper.val_dict[item][index])] == csv_helper.val_dict[item][index]: # If any vibhakti utterance is found in sentence
                            if i != 0:
                                l = len(out)
                                out = out[:l - 1] + "_" + words[i] # Join with underscore
                            else:
                                out += words[i] + "_"
                            flag = 1
                        elif words[i] == csv_helper.val_dict[item][index]:
                            if i != 0:
                                l = len(out)
                                out = out[:l - 1] + "_" + words[i]
                            else:
                                out += words[i] + "_"
                            flag = 1
                    
                if flag == 0 and i != len(words) - 1:
                    out += words[i] + "_"
                elif flag == 0:
                    out += words[i]
                    
        return out