import csv_helper

class row3:
    def __init__(self, inp):
        self.inp = inp
        self.output = list()

    def get_row(self):
        for num, elem in enumerate(self.inp):
            self.output.append(num + 1)
        return self.output