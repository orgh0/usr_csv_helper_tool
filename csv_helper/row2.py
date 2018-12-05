import csv_helper


class row2:
    def __init__(self, inp):
        self.inp = inp
        self.output = list()
        
    def get_row(self):
        tokens = self.inp.split(",")
        tokens = tokens[:-1]
        print("These are the tokens", tokens)
        for token in tokens:
            temp = token.split("_")
            temp_token = temp[0]
            if temp_token in csv_helper.concept_variations.keys():
                c_ids = csv_helper.concept_variations[temp_token]
                concepts = list()
                for c_id in c_ids:
                    var = temp_token + "_" + c_id
                    concepts.append(var)
                print("The following are your choices:")
                for index, c in enumerate(concepts):
                    print(index, c, csv_helper.concept_dict[c])
                user_inp = input("Enter Input: ")
                user_inp = int(user_inp)
                final_token = concepts[user_inp]
                self.output.append(final_token)
            else:
                c = temp_token + "_1"
                # csv_helper.concept_dict[c] =
                # Use hindi English Dict of sense dict here
                self.output.append(c)
        return self.output 

        