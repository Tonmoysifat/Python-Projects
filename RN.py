i=1
while i<=6:
  print()
  i+=1
import time
print("                                                          Welcome to the Random Number game\n\n")
time.sleep(3)
print("                                                       This game is played between two players\n\n")
Player1=input("   Name of player 1: ")
Player2=input("   Name of player 2: ") 
print(f"\n\n                                                         {Player1} vs {Player2}\n")
import random
lst=[1,2,3,4,5,6]
round=0
P1_score=0
P2_score=0
while round<10:
  round+=1
  ran1=random.choice(lst)
  P1_score=P1_score+ran1
  ran2=random.choice(lst)
  P2_score=P2_score+ran2
  print("  Round:",round)
  print(f"\n    To activate {Player1}'s turn press 1 then Enter")
  press=int(input("     "))
  if press==1:
    print(f"                   {Player1} scored's {ran1}\n")
  else:
    print("Error")  
  print(f"    To activate {Player2}'s turn press 2 then Enter")
  press=int(input("     "))
  if press==2:
    print(f"                   {Player2} scored's {ran2}\n")
    time.sleep(3)
  else:
    print("Error")  
  print(" After Round:",round)
  print(f"    {Player1}'s score is {P1_score}\n    {Player2}'s score is {P2_score}\n")
if P1_score==P2_score:
  print("                                                                     Match Tie")
elif P1_score>P2_score:
  print(f"                                                   {Player1} wins by {P1_score-P2_score} scores")
else:
  print(f"                                                   {Player2} wins by {P2_score-P1_score} scores")
input()
