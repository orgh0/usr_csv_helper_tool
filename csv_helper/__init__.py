import sys
import os

PATHS = ["./resources/tam.txt", "./resources/measurement", "./resources/numbers", "./resources/ordinal", "./resources/other", "./resources/particle.txt", "./resources/quantifiers", "./resources/vibhakti.txt", "./resources/comparative"]
NAMES = ["TAM", "MEASUREMENT", "NUMBERS", "ORDINAL", "OTHER", "PARTICLE", "QUANTIFIERS", "VIBHAKTI", "COMPARATIVE"]
CONCEPT_DICT = "./resources/concept_dictionary_user.txt"
val_dict = dict()
concept_dict = dict()
concept_variations = {}

def converter():
    for index, path in enumerate(PATHS):
      f = open(path).readlines()
      f = [s.replace("\n", "") for s in f]
      if path == "./vibhakti.txt" or path == "./tam.txt":
        f = [s.split("_") for s in f]
      val_dict[NAMES[index]] = f

converter()

def load_concept_dict():
  f = open(CONCEPT_DICT).readlines()
  f = [s.split(",") for s in f]
  for s in f:
    concept_dict[s[0]] = s[2]
  f = [s[0] for s in f]
  f = [s.split("_") for s in f]
  f.pop(0)
  for s in f:
    if s[0] in concept_variations.keys():
      concept_variations[s[0]].append(s[1])
    else:
      concept_variations.setdefault(s[0], [s[1]])

load_concept_dict()
        

        

# def process_sentence(sentence):
#     output = ''
#     for chunk in sentence.split(","):
#         words = chunk.split()
#         if len(words) != 0:
#             result = generate_row(words)
#             output += result + ','
#     return output
