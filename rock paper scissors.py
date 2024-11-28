import random
play1= str(input("rock,paper or scissor?")).capitalize()
play2= random.randint(1,3)

if play2==1:
    play2="rock"
elif play2==2:
    play2="paper"
elif play2==3:
    play2="scissor"
    
print("bot: ",play2)

if play1==play2:
   print("its a tie")
    
elif (play1=="rock" and play2=="scissor")or (play1=="paper" and play2=="rock")or(play1=="scissor"and play2=="paper"):
    
   print("you win")

else:
    print("you loose")
    