# woord_1 = "surf"

spelen = input("Beginnen aan galgje ja/nee:")

hetwoord=["s","a","p"]
goedeletters=[]
fouteletters=[]

while len(goedeletters) < len (hetwoord):
  nieuweletter = input ("kies een letter:")
  goed=hetwoord.count(nieuweletter)
  if goed > 0:
    print("JA, deze letter is goed")
    goedeletters.append(nieuweletter)
  else:
    print("fout...")
    fouteletters.append(nieuweletter)
  

  print("foute letters", fouteletters)
  print("goede letters", goedeletters)

print("einde, het woord was: SAP")