# 16 Team Tournament Schedule

import random
from decimal import Decimal
class TeamData:
    def __init__(self,n,w,l,opp,h):
        self.name =n
        self.won = w
        self.lost = l
        self.opp = []
        self.history = h

    def buchhwolz(self):
        ow,ol = 0,0
        for i in (self.opp):
            ow += i.won
            ol += i.lost
        buchhscore=ow/ol
        return buchhscore
    def ranking_score(self):
        return self.history

def history_compiler(name,y):
    fib=[1,1,2,3,5,8,13,21,34,55]
    wt_mul=list(reversed(fib[:y]))
    year=2019
    tw,tl=0,0

    for i in range(y):
        print("Enter wins of Team",name,"in",year-i-1,": ",end="")
        if auto:
            wins=random.randint(10,100)
            print(wins)
        else:
            wins=int(input())
        tw+=wins*wt_mul[i]
        print("Enter losses of Team",name,"in",year-i-1,": ",end="")
        if auto:
            losses=random.randint(1,90)
            print(losses)
        else:
            losses=int(input())
        tl+=losses*wt_mul[i]
    print()
    return tw/tl

def ranking_display(teams,n): 
        print("\n\t RANKINGS - 2019") 
        print("Rank\tName\tW/L Score\tTournament Seed") 
        for i in range(n):
            if i in [0,1]:
            
                print(str(i+1)+"\t"+teams[i].name+"\t"+str(round(Decimal(teams[i].ranking_score()),3))+"\t\t "+"Round 2(High)") 
            elif i in [14,15]:
            
                 print(str(i+1)+"\t"+teams[i].name+"\t"+str(round(Decimal(teams[i].ranking_score()),3))+"\t\t "+"Round 2(Low)")
            elif i>15:
              print(str(i+1)+"\t"+teams[i].name+"\t"+str(round(Decimal(teams[i].ranking_score()),3))+"\t\t "+"Not Qualified")
            else:
              print(str(i+1)+"\t"+teams[i].name+"\t"+str(round(Decimal(teams[i].ranking_score()),3))+"\t\t "+"Round 1")


def score_sort(teams,n):
        for i in range(0,n-1):
            for j in range(i+1,n):
                if teams[i].ranking_score()<teams[j].ranking_score():
                    teams[i],teams[j]=teams[j],teams[i]
        teams[0].won=1
        teams[1].won=1
        teams[14].lost=1
        teams[15].lost=1
        return teams

def points_table(teamslist):
        print("\n\t\tPOINTS TABLE")
        
        print("Name\tPlayed\tWins\tLosses\tStatus")
        netscores={3:[],2:[],1:[],0:[],-1:[],-2:[],-3:[]}
        for i in teamslist:
            netscores[i.won-i.lost].append(i)
    
        for i in netscores:
            for j in netscores[i]:
                print(j.name+"\t"+str(j.won+j.lost)+"\t"+str(j.won)+"\t"+str(j.lost)+"\t", end='')
                if j.won==3:
                    print("QUALIFIED")
                elif j.lost==3:
                    print("ELIMINATED")
                else:
                    print("-")

def random_match_generator(teams,n):
    
        random.shuffle(teams)
        matches=list((teams[i],teams[i+1]) for i in range(0,n,2))
        random.shuffle(matches)
    
        for j in range(int(n/2)):
            print('\t', matches[j][0].name, "	vs	", matches[j][1].name)
        return matches

def sort_buchhwolz(group,number):
        for i in range(0,number-1):
            for j in range(i+1,number):
                if group[i].buchhwolz()<group[j].buchhwolz():
                    group[i],group[j]=group[j],group[i]
        return group

def match_result_compiler(matches):
        for i in matches:
            i[0].opp.append(i[1])
            i[1].opp.append(i[0])
            print("Enter winner of", i[0].name,'vs',i[1].name,": (", i[0].name,"= 1,",i[1].name,"= 2 )")
            if auto:
                r=random.randint(1,2)
                print(r)
            else:
                r=int(input())
            while (r!=1) and (r!=2):
                print("Invalid result. Try again.(", i[0].name,"= 1,",i[1].name,"= 2 )")
                r=int(input())
            if r==1:
                    i[0].won+=1
                    i[1].lost+=1
            elif r==2:
                    i[1].won+=1
                    i[0].lost+=1

def playoff_brackets(playoffs,semis,finals,champs):
        a=TeamData('-',0,0,[],h)
        if semis==[]:
         semis=[a,a,a,a]
        if finals==[]:
         finals=[a,a]
        print("Quarter-Finals #1________")
        print(" "+playoffs[0].name+" vs "+playoffs[-1].name+"\t\t |")
        print("\t\t\t |______Semi-Finals #1______")
        print("\t\t\t |\t"+semis[0].name+" vs "+semis[1].name+"\t   |")
        print("Quarter-Finals #2________|\t\t\t|")
        print(" "+playoffs[3].name+" vs "+playoffs[-4].name+"\t\t\t\t\t")
        if champs==[]:
             print("\t\t\t\t\t\t |_____ Finals ")
             print("\t\t\t\t\t\t |\t "+finals[0].name+" V/S "+finals[1].name)
        else:
             print("\t\t\t\t\t\t |_____ Finals ______ !!CHAMPIONS!!")
             print("\t\t\t\t\t\t |\t "+finals[0].name+" V/S "+finals[1].name+"\t\t Team "+champs[0].name)
        print("Quarter-Finals #3________\t\t\t |")
        print(" "+playoffs[2].name+" vs "+playoffs[-3].name+"\t\t |\t\t\t|")
        
        print("\t\t\t |______Semi-Finals #2______|")
        print("\t\t\t |\t"+semis[2].name+" vs "+semis[3].name)
        print("Quarter-Finals #4________|")
        print(" "+playoffs[1].name+" vs "+playoffs[-2].name)
        print("\n")
            
teamslist=[]
dummyteams=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    
print("16 Team Tournament Scheduler\n")
t= int(input("Enter number of teams: "))
while t<16:
        print("Please enter a number greater than or equal to 16.")
        t= int(input("Enter number of teams: "))
if t==16:
        y= int(input("Enter the number of years of history to be considered (0-10): "))
else:
        y= int(input("Enter the number of years of history to be considered (1-10): "))
while not y>=0 or not y<=10:
        print("Invalid input. Try Again.")
        y = int(input("Enter the number of years of history to be considered (0-10): "))
print()
auto_names=True
if input("For customized team names, Enter 1: ")=='1':
        auto_names=False
if y!=0:
        auto=False
        if input("For randomized input of team history, Enter 1: ")=='1':
            auto=True
print("\n")
    
for i in range(t):
        print("Enter the name of team" ,i+1, ": ",end='')
        if auto_names:
            name=dummyteams[i]
            print(name)
        else:
            name=input()
    
        if (y!=0):
            h=history_compiler(name,y)
        else:
            h=0
        teamslist.append(TeamData(name,0,0,[],h))
if y!=0:
        teamslist=score_sort(teamslist,t)
        ranking_display(teamslist,t)
        teamslist=teamslist[:16]
auto=False
print("\n")
if input("For randomized simulation of group stage, Enter 1: ")=='1':
        auto=True
input("\nPress Enter to start to Round 1: ")

#ROUND 1

print("\n\n\t	ROUND 1\n\t	(0-0)")
r1teams=[]
r1matches=[]
for i in teamslist:
    if i.won==0 and i.lost==0:
        r1teams.append(i)
if y==0:
    r1matches=random_match_generator(r1teams,len(r1teams))
else:
    for i in range(0,12,2):
        r1matches.append(list((r1teams[i],r1teams[i+1])))
    for j in range(int(6)):
        print('\t', r1matches[j][0].name, "	vs	", r1matches[j][1].name)
    print()
    for i in r1matches:
        i[0].opp.append(i[1])
        i[1].opp.append(i[0])
        print("Enter winner of", i[0].name,'vs',i[1].name,": (", i[0].name,"= 1,",i[1].name,"= 2 )")
        if auto:
            r=random.randint(1,2)
            print(r)
        else:
            r=int(input())
        while (r!=1) and (r!=2):
            print("Invalid result. Try again.(", i[0].name,"= 1,",i[1].name,"= 2 )")
            r=int(input())
        if r==1:
            i[0].won+=1
            i[1].lost+=1
        elif r==2:
            i[1].won+=1
            i[0].lost+=1

points_table(teamslist)

input("\nPress Enter to continue to Round 2: ")

#ROUND 2

print("\n\n\t	ROUND 2\n")
r2highteams=[]
r2lowteams=[]
for i in teamslist:
    if i.won==1 and i.lost==0:
        r2highteams.append(i)
    if i.won==0 and i.lost==1:
        r2lowteams.append(i)

print("\t	High\n\t	(1-0)")
r2highmatches=random_match_generator(r2highteams,8)

print("\n\t	Low\n\t	(0-1)")
r2lowmatches=random_match_generator(r2lowteams,8)
print()

r2matches=r2highmatches+r2lowmatches
match_result_compiler(r2matches)

points_table(teamslist)

input("\nPress Enter to continue to Round 3: ")

#ROUND 3

print("\n\n\t	ROUND 3\n")
r3highteams=[]
r3midteams=[]
r3lowteams=[]
for i in teamslist:
    if i.won==2 and i.lost==0:
        r3highteams.append(i)
    if i.won==1 and i.lost==1:
        r3midteams.append(i)
    if i.won==0 and i.lost==2:
        r3lowteams.append(i)

print("\t	High\n\t	(2-0)")
r3highmatches=random_match_generator(r3highteams,4)

print("\n\t	Mid\n\t	(1-1)")
r3midmatches=random_match_generator(r3midteams,8)

print("\n\t	Low\n\t	(0-2)")
r3lowmatches=random_match_generator(r3lowteams,4)
print()

r3matches=r3highmatches+r3midmatches+r3lowmatches 
match_result_compiler(r3matches)

points_table(teamslist)

input("Press Enter to continue to Round 4: ")

#ROUND 4

print("\n\n\t	ROUND 4\n")
r4highteams=[]
r4midteams=[]
r4lowteams=[]
for i in teamslist:
    if i.won==2 and i.lost==1:
        r4highteams.append(i)
    if i.won==1 and i.lost==2:
        r4lowteams.append(i)

print("\t	High\n\t	(2-1)")
r4highmatches=random_match_generator(r4highteams,6)

print("\n\t	Low\n\t	(1-2)")
r4lowmatches=random_match_generator(r4lowteams,6)
print()

r4matches=r4highmatches+r4lowmatches
match_result_compiler(r4matches)

points_table(teamslist)

input("Press Enter to continue to Round 5: ")

#ROUND 5

print("\n\n\t	ROUND 5\n\t	(2-2)")
r5teams=[]
for i in teamslist:
    if i.won==2 and i.lost==2:
        r5teams.append(i)
r5matches=random_match_generator(r5teams,6)
match_result_compiler(r5matches)

points_table(teamslist)
print("\n")

#PLAYOFFS

playoffs=[]
semis=[]
finals=[]
champs=[]

g1,g2,g3=[],[],[]
for i in teamslist:
    if i.won==3 and i.lost==0:
        g1.append(i)
    if i.won==3 and i.lost==1:
        g2.append(i)
    if i.won==3 and i.lost==2:
        g3.append(i)
g1=sort_buchhwolz(g1,2)
g2=sort_buchhwolz(g2,3)
g3=sort_buchhwolz(g3,3)

print("\tTeam Rankings for PLAYOFFS")

print("\n\tGroup 1 (3-0)")
for i in range(2):
    playoffs.append(g1[i])
    print("#"+str(i+1)+": \t"+g1[i].name+"("+str(round(Decimal(g1[i].buchhwolz()),3))+")")

print("\n\tGroup 2 (3-1)")
for i in range(3):
    playoffs.append(g2[i])
    print("#"+str(i+3)+": \t"+g2[i].name+"("+str(round(Decimal(g2[i].buchhwolz()),3))+")")

print("\n\tGroup 3 (3-2)")
for i in range(3):
    playoffs.append(g3[i])
    print("#"+str(i+6)+": \t"+g3[i].name+"("+str(round(Decimal(g3[i].buchhwolz()),3))+")")
print("\n")

auto=False
if input("For randomized simulation of playoffs, Enter 1: ")==1:
    auto=True
input("\nPress Enter to continue to Quarter-Finals: ")

#Quarter Finals

print("\n\n\tQuarter-Finals #1")
print('\t', playoffs[0].name, " vs ", playoffs[-1].name)

print("\n\tQuarter-Finals #2")
print('\t', playoffs[3].name, " vs ", playoffs[-4].name)

print("\n\tQuarter-Finals #3")
print('\t', playoffs[2].name, " vs ", playoffs[-3].name)

print("\n\tQuarter-Finals #4")
print('\t', playoffs[1].name, "	vs	", playoffs[-2].name)
print("\n")

playoff_brackets(playoffs,semis,finals,champs)
c=1
for j in range(0,10,3):
    i=j%4
    print("Enter winner of Quarter-Finals #"+str(c)+": (", playoffs[i].name,"= 1,",playoffs[-i-
    1].name,"= 2 )")
    if auto:
        r=random.randint(1,2)
        print(r)
    else:
        while True:
            try:
                r=int(input())
            except:
                print("Invalid result. Try again.(", playoffs[i].name,"= 1,",playoffs[-i-1].name,"= 2)")
                continue
            break
        while (r!=1) and (r!=2):
            print("Invalid result. Try again.(", playoffs[i].name,"= 1,",playoffs[-i-1].name,"= 2 )")
            r=int(input())
    if r==1:
        semis.append(playoffs[i])
    if r==2:
        semis.append(playoffs[-i-1])
    c+=1

input("\nPress Enter to continue to Semi-Finals: ")

#Semi Finals

print("\n\n\tSemi-Finals #1") 
print('\t', semis[0].name, " vs ", semis[1].name)

print("\n\tSemi-Finals #2")
print('\t', semis[2].name, " vs ", semis[3].name)
print("\n")
playoff_brackets(playoffs,semis,finals,champs)
c=1
for i in range(0,4,2):
    print("Enter winner of Semi-Finals #"+str(c)+": (", semis[i].name,"= 1,",semis[i+1].name,"= 2 )")
    if auto:
        r=random.randint(1,2)
        print(r)
    else:
        while True:
            try:
                r=int(input())
            except:
                print("Invalid result. Try again.(", playoffs[i].name,"= 1,",playoffs[-i-1].name,"= 2)")
                continue
            break
        while (r!=1) and (r!=2):
            print("Invalid result. Try again.(", playoffs[i].name,"= 1,",playoffs[-i-1].name,"= 2 )")
            r=int(input())
    if r==1:
        finals.append(semis[i])
    if r==2:
        finals.append(semis[i+1])
    c+=1

input("\nPress Enter to continue: ")

#Finals

print("\n\n\t~~~~~~FINALS~~~~~~\n\n")
print('\t', finals[0].name, "	V/S	", finals[1].name)
print("\n")

playoff_brackets(playoffs,semis,finals,champs)

print("Enter winner of the FINALS: (", finals[0].name,"= 1,",finals[1].name,"= 2 )")
while True:
    try:
        r=int(input())
    except:
        print("Invalid result. Try again.(", finals[0].name,"= 1,",finals[1].name,"= 2 )") 
        continue
    break

while (r!=1) and (r!=2):
    print("Invalid result. Try again.(", finals[0].name,"= 1,",finals[1].name,"= 2 )")
    r=int(input())
if r==1:
    champs.append(finals[0])
if r==2:
    champs.append(finals[1])
print("\n\n!!!Team "+champs[0].name+" are the CHAMPIONS of the tournament!!!\n\n")
playoff_brackets(playoffs,semis,finals,champs)



