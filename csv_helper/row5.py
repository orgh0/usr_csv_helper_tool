import csv_helper

class row5:
    def __init__(self, inp):
        self.inp = inp
        self.out = list()

    def get_row(self):
        tokens = self.inp.split(",")
        tokens = tokens[:-1]
        for token in tokens:
            temp = token.split("_")
            if(temp[1] == "hI" or temp[1]) == "Bi" or temp[1] == "0" or temp[1] in csv_helper.val_dict["VIBHAKTI"]:
                print(temp[0]) # Decide what to do with these entries now
                gender = input("Enter the Gender m/f/n/-: ")
                gender = str(gender)
                number = input("Enter the Number sg/pl/-: ")
                number = str(number)
                person = input("Enter the person u/m/a/-: ")
                person = str(person)
                val = [gender, number, person]
                self.out.append(val)
        return self.out
    
