# woord_1 = "surf"

spelen = input("Beginnen aan galgje ja/nee:")

print ("het woord is:" + " " + "_" + " " + "_" + " " + "_" + " " + "_")

while spelen != "nee":
    foute_letters = [] 
    letter_1 = input ("kies een letter: ")
    if letter_1 == "s" or "u" or "r" or "f":
        if letter_1 == "s":
            print("DEZE LETTER IS GOED")
            print("s" + "_" + " " + "_" + " " + "_")
        elif letter_1 == "u":
            print("DEZE LETTER IS GOED")
            print ("_" + " " + "u" + "_" + " " + "_")
        elif letter_1 == "r":
            print ("DEZE LETTER IS GOED")
            print("_" + " " + "_" + "r" + " " + "_")
        else:
            foute_letters.insert(0, letter_1)
            print("helemaal fout")
            print("je foute letters zijn nu:" + " " + str(foute_letters))
