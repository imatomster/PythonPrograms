textFile = open('afaridOfTheDark.txt','r')
madlibText = textFile.readlines()

pluralNoun = input("Please type a plural noun: ")
verbing = input("Please type a verb ending in ing: ")
bodyPart = input("Please type a body part (single): ")
bodyParts = input("Please type a body part (plural): ")
noun = input("Please type a noun: ")
adverb = input("Please type an adverb: ")

for line in madlibText:
  line = line.replace("PLURAL_NOUN", pluralNoun)
  line = line.replace("VERB_ENDING_IN_ING", verbing)
  line = line.replace("PART_OF_THE_BODY_PLURAL", bodyParts)
  line = line.replace("PART_OF_THE_BODY", bodyPart)
  line = line.replace("NOUN", noun)
  line = line.replace("ADVERB", adverb)
  print(line)
