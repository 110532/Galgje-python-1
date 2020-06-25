# woord_1 = "surf"


hetwoord=["s","a","p"]
goedeletters=[]
fouteletters=[]


def printtussenstand ():
  print("goede letters", goedeletters)
  tussenstand=" "
  for letter in hetwoord:
    geraden=goedeletters.count (letter)
    if geraden > 0:
      tussenstand= tussenstand + letter
    else:
      tussenstand= tussenstand + "_" 
    tussenstand= tussenstand + " "
  print(tussenstand)


while len(goedeletters) < len (hetwoord):
  nieuweletter = input ("kies een letter:")
  goed=hetwoord.count(nieuweletter)
  if goed > 0:
    print("JA, deze letter is goed")
    goedeletters.append(nieuweletter)
  else:
    print("fout...")
    fouteletters.append(nieuweletter)
  printtussenstand()

  print("foute letters", fouteletters)

print("einde, het woord was: SAP")


spelen = input("Begin opnieuw aan galgje ja/nee:")
