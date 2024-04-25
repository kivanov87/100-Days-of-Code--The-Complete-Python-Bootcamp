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
print("Welcome, brave adventurer, to the perilous shores of Treasure Island. \nYour quest is to navigate the treacherous terrain, outwit cunning traps, and uncover the hidden treasure. \nChoose your actions wisely, for each turn can lead to fortune or folly.")
print("Your mission is to find the treasure.") 

print ("You find yourself standing on a golden beach, the wreck of your ship behind you. \nAhead lies a dense jungle with two paths.")

firstDecision =str(input("Which path you choose, Left or Right?\n"))
if firstDecision=="Left":
    print("Left path leads you to the dark caves where you got attacked by bear.")
    print("Fail to overcome the island's challenges and become another lost soul.")
elif firstDecision=="Right":
    print("Right path takes you deeper into the jungle.")
    print("After surviving the treacherous paths of the jungle entrance, you find yourself at a crossroads. \nThe jungle canopy thickens above, and the air grows heavy with the scent of earth and mystery. \nTwo distinct paths lie before you, each promising its own dangers and rewards. ")
    secondDecision =str(input("Which path you choose, Climb or Forge ahead\n?"))
    if secondDecision == "Climb":
        print('''            .        +          .      .          .
     .            _        .                    .
  ,              /;-._,-.____        ,-----.__
 ((        .    (_:#::_.:::. `-._   /:, /-._, `._,
  `                 \   _|`"=:_::.`.);  \ __/ /
                      ,    `./  \:. `.   )==-'  .
    .      ., ,-=-.  ,\, +#./`   \:.  / /           .
.           \/:/`-' , ,\ '` ` `   ): , /_  -o
       .    /:+- - + +- : :- + + -:'  /(o-) \)     .
  .      ,=':  \    ` `/` ' , , ,:' `'--".--"---._/`7
   `.   (    \: \,-._` ` + '\, ,"   _,--._,---":.__/
              \:  `  X` _| _,\/'   .-'
.               ":._:`\____  /:'  /      .           .
                    \::.  :\/:'  /              +
   .                 `.:.  /:'  }      .
           .           ):_(:;   \           .
                      /:. _/ ,  |
                   . (|::.     ,`                  .
     .                |::.    {\
                      |::.\  \ `.
                      |:::(\    |
              O       |:::/{ }  |                  (o
               )  ___/#\::`/ (O "==._____   O, (O  /`
          ~~~w/w~"~~,\` `:/,-(~`"~~~~~~~~"~o~\~/~w|/~
      ~~~~~~~~~~~~~~~~~~~~~~~\\W~~~~~~~~~~~~\|/~~''')
        print("The towering tree before you seems like a sentinel, its highest branches offering a clear view of the island. \nPerhaps from above, you could spot the glint of treasure or the ancient temple you seek.")
        print('''                  ___            %.
           __  __/__/I__  ______% %%'
          / __/_[___]/_/I--.   /%%%%
         / /  I_/=/I__I/  /I  // )(
        / /____/=/ /_____//  //
       /  I___/=/ /_____I/  //
      /______/=/ /_________//
      I_____/=/ /_________I/MJP
           /=/_/''')
        print("With the temple’s location now clear, you carefully descend the tree, your resolve strengthened. \nThe journey through the jungle is treacherous, but the sight of the temple guides you forward. \nYou dodge venomous snakes, avoid hidden pits, and push through thick vines.") 
        print("Finally, as twilight descends, you stand before the temple. \nIts massive doors are adorned with carvings of fearsome deities and tales of lost adventurers. \nThe air is heavy with the scent of moss and ancient secrets. \nYou step into the shadow of the temple, where four doors await, each a gateway to untold peril and promise.")        
        thirdDecision =str(input("Which path you choose, Climb or Forge ahead\n?"))
        print("As you emerge from the dense jungle, the ancient temple looms before you, its stones weathered by time and the relentless growth of the jungle. \nThe air is still, as if the very island is holding its breath, awaiting your next move. \nThe temple’s entrance is flanked by statues of forgotten gods, their eyes seeming to follow your every step.")
        print("Ahead, the corridor splits into four, each leading to a door of a different hue. \nThe Blue Door, with its promise of water’s secrets; the Yellow Door, hiding cunning mechanical traps; the Red Door, with the heat of fire’s embrace; and the Green Door, radiating a strange and inviting light.")
        print("Your heart beats faster as you realize the treasure is near, but so too is the danger. The choices you’ve made have led you to this moment, and now, one final decision remains. \nWith a deep breath, you choose a door, your hand resting on the ancient wood, ready to push it open and face the destiny that awaits you on Perilous Treasure Island. 🏴‍☠️🗝️")
        thirdDecision =str(input("Which door you choose, Blue Door, Yellow Door, Red Door or Green Door  \n?"))
        if thirdDecision == "Blue Door":
            print("The sound of rushing water grows louder as you open the door, revealing a subterranean river. \nHowever, as you step forward, the ground gives way, plunging you into the icy depths. \nThe strong current pulls you under, and there is no escape.")             
        elif thirdDecision == "Yellow Door":
            print("Creaking open the yellow door reveals a room filled with intricate puzzles and traps. \nWalls lined with hieroglyphs hint at the solutions. \nYour wit and intelligence shine as you solve each puzzle, one by one, disarming traps and unlocking secrets. \nFinally, a hidden compartment opens, revealing the legendary treasure of Treasure Island—a chest of gold and precious gems beyond imagination.")     
        elif thirdDecision == "Red Door":
            print("The red door opens to a chamber of smoldering coals and bursts of flame. \nYou take a step forward, but the floor collapses, sending you into a pit of fire below. \nThere is no chance of survival.")   
        elif thirdDecision == "Green Door":
            print("The green door opens to reveal a luminous garden, bathed in an ethereal light. \nAs you step forward, the plants come to life, their vines ensnaring you, pulling you into the depths of the garden from which there is no escape.")
            print('''___...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   \
             \_________\####/_________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.\uuu/.-'    __/ \__ |
              |==== .'.'^'.'.====|
          jgs |  _\o/   __  {.' __  '.} _   _\o/  _|
              `""""-""""""""""""""""""""""""""-""""`''')
        else:
            print("You have failed to find treasure")
    else:
        print("Fail to overcome the island's challenges and become another lost soul.")
