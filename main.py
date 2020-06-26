# woord_1 = "surf"
import random



woordenlijst=["informatica", "informatiekunde", "spelletje", "aardigheidje", "scholier", "fotografie", "waardebepaling", "specialiteit", "verzekering", "universiteit", "heesterperk"]


willekeuriggetal= random.randint(0,10)

hetwoord= woordenlijst [willekeuriggetal]
goedeletters=[]
fouteletters=[]

print("Welkom bij galgje, je mag 5 fouten maken om het woord te raden, succes.")
print("het woord dat je kan raden bestaat uit:", len(hetwoord), "letters")

def printtussenstand ():
  
  tussenstand=" "
  for letter in hetwoord:
    geraden=goedeletters.count (letter)
    if geraden > 0:
      tussenstand= tussenstand + letter
    else:
      tussenstand= tussenstand + "_" 
    tussenstand= tussenstand + " "
  print(tussenstand)

printtussenstand ()

while len(goedeletters) < len (hetwoord) and len(fouteletters) < 5:
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

print("EINDE")


spelen = input("Begin opnieuw aan galgje ja/nee:")
