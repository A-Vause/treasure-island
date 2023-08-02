print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 


road = input("You are at a cross roads. Turn left or right?\n").lower()
if road == "left":
  boat = input('You come to a lake with an island in the middle. Type wait to wait for a boat or type swim to try and swim.\n').lower()
  if boat == "wait":
    door = input("On the island you find a house with 3 doors. Type ""Red"" to open the red door. Type ""blue"" to open the blue door and type ""green"" to open the green door. Which will you choose?\n").lower()
    if door == "blue":
        print("You Win!")
    elif door == "red":
        print("You are eaten by beasts, Game over.")
    elif door == "green":
        print("you are burned by fire, Game over.")
    else:
        print("Game over.")  
  else:
    print("You are attacked by a trout, Game over.")   
else:  
  print("You fell into a hole, Game over.")