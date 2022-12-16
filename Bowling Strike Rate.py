#Bowling Srike Rate
#Bowling strike rate is defined for a bowler as the average number of balls bowled per wicket taken.

name=input("Enter the name of the bowler: ")
b=input("Enter the number of balls bowled by the bowler :  ")
b=int(b)
w=input("Enter the number of wickets taken by the bowler : ")
w=int(w)
bowlingStrikeRate=b/w
print("The bowling strike rate of ",name, "is",bowlingStrikeRate)
