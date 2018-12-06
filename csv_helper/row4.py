import csv_helper


class row4:
    def __init__(self, inp):
        self.inp = inp
        self.output = list()

    def get_out(self):
        tokens = self.inp.split(",")
        tokens = tokens[:-1]
        for token in tokens:
            temp_token = token.split("_")
            print("Is {} a mass or a def").format(temp_token[0])
            usr_inp = input("Enter 1 for mass or 2 def: ")
            if usr_inp == 1:
                self.output.append("mass")
            else:
                self.output.append("def")
        return self.output