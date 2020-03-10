print("Betlesky,Robert,Blue,Lion,Jets: ")
inputString = input()
comma1= inputString.find(",")
comma2= inputString.find(",",comma1 + 1)
comma3= inputString.find(",",comma2 + 2)
comma4= inputString.find(",",comma3 + 3)
inputStringLength= len(userString)
lastName= inputString[0:comma1]
firstName= inputString[comma1+1:comma2]
favColor= inputString[comma2+1:comma3]
favAnimal= inputString[comma3+1:comma4]
favTeam= inputString[comma4+1:inputStringLength]
print("My name is " + firstName + " " + lastName + ", my favorite color is " + favColor + ", my favorite animal is a " + favAnimal + ", and my favorite team is the " + favTeam)
                
