while True:
  print("\n1: sart")
  print("\n2: print the lst entry")
  print("\n3: Exit")
  choice = float(input("\nEnter your chice: "))
  if choice == 3:
    print("\n okey bye and thank for being here")
    break
    
  
  if choice == 1:
    notDone = True
    allcharacters = []
    while notDone:
      charList =[]
      developer= input("\nwhat is developer of the show?") 
      charList.append(developer)
      date = input("when did the show start?")
      charList.append(date)
      character = input("what is your favorite character?") 
      charList.append(character)
      name = input("what is the name of the main character")
      charList.append(name)
      element= input("what element does the character use's? ")
      charList.append(element)
      Nation = input("what Nation is the main character from? ")
      charList.append(Nation)
      allcharacters.append(charList)
      print(f"""
      """)
        
      answer1 = input("you want out:")
      if answer1 == "Yes":
        notDone = False
      else: 
        print("\nokey time for another one :) : ")
        
            
  if choice == 2:
      print("\n your latest entery into out catlgue was")            
      print("\n*__*__*__*__*__*__*__*__*__*__*__*__*__*__*__*__*__*__*")
      print("\ndeveloper: ") 
      print("\ndate: ")
      print("\ncharacter: ")
      print("\nname: ")
      print("\nelement: ")
      print("\nNationn: ")
      print("\n*__*__*__*__*__*__*__*__*__*__*__*__*__*__*__*__*__*__*")

    

      answer = input("\n if you want to go back to the manu? type Yes:")
      if answer == "Yes":
        notDone = False
        print("\nokey nice choice")
      else:              
         break 
