while True:
  print("1 sart")
  print("\n2 print the lst entry")
  print("Exit")
choice = float(input("\nEnter your chice: "))

if choice ==1:
    notDone = True
    allcharacters = []
    while notDone:
        charList =[]
        developer= input("what is developer of the show?") 
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
        allcharacters.append(charList)
        print(f"""
              {charList}""")
    answer = input("Do you want out?")
    if answer == "Yes":
        notDone = False       
    
    else:
     print("ok her we go agian you dum")
print(allcharacters)


if choice ==3:
    print("\n your latest entery into out catlgue was")
    print("\n*__*__*__*__*__*__*__*__*__*__*__*__*__*__*__*__*__*__*")
    print("\ndeveloper: ", )
    print("\nname: ",charList.append[name] )
    print("\nelement: ", charList.append[element])
    print("\nNationn: ",charList.append[Nation])
    print("\n*__*__*__*__*__*__*__*__*__*__*__*__*__*__*__*__*__*__*")


answer = input("\n if you want to go back to the manu? type Yes")
if answer == "Yes":
        print("\n cya")


else:
     print("ok her we go agian for the millionth time")



