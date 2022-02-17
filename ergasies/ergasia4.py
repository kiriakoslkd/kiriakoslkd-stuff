import random

xartia = []
figures = ["J", "Q", "K"]
xarti = [i for i in range(1, 11)] + figures
color = ["H", "S", "C", "D"]
win1=0
win2=0
win3=0 
for x in range(100):
    for i in xarti:
        for j in color:
            xartia.append([i,j])
    random.shuffle(xartia)
    player1=[]
    sum1=0
    while sum1<16:
        sum1=0
        player1.append(xartia.pop())
        # print (player1)
        for card in player1:
            if card[0] in figures:
                sum1=sum1+10
            else:
                sum1=sum1+card[0]
       # print(sum1)
    if sum1>21:
        #print("P2 wins!")
        win2=win2+1
    else:
        '''
        sxolia pollwn
        grammwn
        '''

       # print("P2 joins the game") #let me add one more player
        player2=[]
        sum2=0
        while sum2<16:
            sum2=0
            player2.append(xartia.pop())
            # print (player2)
            for card in player2:
                if card[0] in figures:
                    sum2=sum2+10
                else:
                    sum2=sum2+card[0]
           # print(sum2)
        if sum2>21:
            sum2=0
        if sum1>sum2:
           # print("P1 wins!")
            win1=win1+1
        elif sum2>sum1:
           # print("P2 wins!")
            win2=win2+1
        else:
           # print("draw!")
            win3=win3+1
print("                  APOTELESMATA")
print("                       ↧")
print("")
print (" TA STATISTIKA TOY PRWTOU PAIXNIDIOU EINAI TA EKSHS:")  
print ("             O P1 kerdise ",win1," paixnidia!")   
print ("             O P2 kerdise ",win2," paixnidia!")
print ("           Issopalia vghkane",win3," paixnidia!")  
print("-------------------------------------------------------")     
        



xartia = []
figures = ["J", "Q", "K"]
goods =[10,"J", "Q", "K"]
xarti = [i for i in range(1, 11)] + figures
color = ["H", "S", "C", "D"]
win1=0
win2=0
win3=0 

for x in range(100):
    c1=random.choice(goods)    
    c2=random.choice(color)
    c3=random.randrange(1,10)
    c4=random.choice(color)
   
    for i in xarti:
        for j in color:
            xartia.append([i,j])
    random.shuffle(xartia)
   # print("P1 joins the game")
    player1=[]
    sum1=0
    flag=False
    while sum1<16:
        sum1=0
        if flag==False:
            flag=True
            player1.append([c1,c2])
           # print (player1)
            for m in range (0,len(xartia)):
               
                if xartia[m]==[c1,c2]:
                    yo=m
           
            xartia.pop(yo)
        else:    
            player1.append(xartia.pop())
        # print (player1)
        for card in player1:
            if card[0] in figures:
                sum1=sum1+10
            else:
                sum1=sum1+card[0]
       # print(sum1)
    if sum1>21:
       # print("P2 wins!")
        win2=win2+1
    else:
        '''
        sxolia pollwn
        grammwn
        '''

       # print("P2 joins the game") #let me add one more player
        player2=[]
        sum2=0
        flag=False
        while sum2<16:
            sum2=0
            if flag==False:
                flag=True
                player2.append([c3,c4])
               # print (player2)
                for n in range (0,len(xartia)):
                    if xartia[n]==[c3,c4]:
                        yo=n
                xartia.pop(yo)   
            else: 
                xartia.pop()
                player2.append(xartia.pop())
            #print (player2)
            for card in player2:
                if card[0] in figures:
                    sum2=sum2+10
                else:
                    sum2=sum2+card[0]
           # print(sum2)
        if sum2>21:
            sum2=0
        if sum1>sum2:
           # print("P1 wins!")
            win1=win1+1
        elif sum2>sum1:
            #print("P2 wins!")
            win2=win2+1
        else:
           # print("draw!")
            win3=win3+1
print (" TA STATISTIKA TOU DEYTEROU PAIXNIDIOU EINAI TA EKSHS:")  
print ("             O P1 kerdise ",win1," paixnidia!")   
print ("             O P2 kerdise ",win2," paixnidia!")
print ("           Issopalia vghkane",win3," paixnidia!")        

