import random
l=["rock","scissor","paper"]
'''rock vs paper->paper wins
   rock vs scissor->rock wins
   paper vs scissor->scissor wins'''
while True:
    Ccount=0
    ucount=0
    uc=int(input("Game Start....\n 1 Yes\n 2 No/Exit"))
    if uc==1:
        for a in range(1,6):
            userInput=int(input(" 1 rock\n 2 paper\n 3 scissor"))
            if userInput==1:
                uchoice="rock"
            elif userInput==2:
                uchoice="paper"
            elif userInput==3:
                uchoice="scissor"
            Cchoice=random.choice(l)
            if Cchoice==uchoice:
                print("computre value",Cchoice)
                print("user value",uchoice)
                print("Game Draw")
                ucount=ucount+1
                Ccount=Ccount+1
            elif (uchoice=="rock" and Cchoice=="scissor") or  (uchoice=="paper" and Cchoice=="rock") or (uchoice=="scissor" and Cchoice=="paper"):
                print("computre value",Cchoice)
                print("user value",uchoice)
                print("you win")
                ucount=ucount+1
            else:    
                print("computre value",Cchoice)
                print("user value",uchoice)
                print("computer win")
                Ccount=Ccount+1
        if ucount==Ccount:
            print("Final Game Draw....")
            print("user score",ucount)
            print("computer score",Ccount)
        elif ucount>Ccount:
            print("Final you win the Game....")
            print("user score",ucount)
            print("computer score",Ccount)   
            
        else:
            print("Final computer win the Game....")
            print("user score",ucount)
            print("computer score",Ccount)   
            
                
    else:
        break
            
