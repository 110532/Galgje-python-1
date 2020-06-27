import random

def printtussenstand ():
  teradenletters=0
  tussenstand=" "
  for letter in hetwoord:
    geraden=goedeletters.count (letter)
    if geraden > 0:
      tussenstand= tussenstand + letter
    else:
      tussenstand= tussenstand + "_" 
      teradenletters=teradenletters+1
    tussenstand= tussenstand + " "
  print(tussenstand)
  return teradenletters

woordenlijst=["informatica", "informatiekunde", "spelletje", "aardigheidje", "scholier", "fotografie", "waardebepaling", "specialiteit", "verzekering", "universiteit", "heesterperk"]

spelen="ja"

while spelen=="ja":

  fouten=0

  willekeuriggetal= random.randint(0,10)

  hetwoord= woordenlijst [willekeuriggetal]
  #hetwoord="sap"
  teradenletters=len(hetwoord)  

  goedeletters=[]
  fouteletters=[]

  print("Welkom bij galgje, je mag 5 fouten maken om het woord te raden, succes.")
  print("het woord dat je kan raden bestaat uit:", teradenletters, "letters")



  printtussenstand ()


  while teradenletters > 0 and fouten < 5:
    nieuweletter = input ("kies een letter:") 
    goed=hetwoord.count(nieuweletter)
    if goed > 0:
      print("JA, deze letter is goed")
      goedeletters.append(nieuweletter)
    else: 
      print("fout...")
      fouteletters.append(nieuweletter)
      fouten=fouten+1 
      print("Je mag nog", 5-fouten, "fouten maken")

    teradenletters=printtussenstand()
  
    print("foute letters", fouteletters)


  if teradenletters==0:
    print("gefelciciteerd, je hebt het woord geraden")
  else:
    print("jammer, het woord had moeten zijn:", hetwoord)
  
  print()
  spelen = input("Begin opnieuw aan galgje ja/nee:")
  print()
  print()

print("Tot ziens...")

#for (goedeletters) print ("gefeliciteerd")
#for (fouteletters) print ("jammer, verloren")