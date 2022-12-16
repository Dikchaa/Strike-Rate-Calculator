#Batting Strike Rate Calculator
#Batting strike rate (s/r) is defined for a batter as the average number of runs scored per 100 balls faced. 
name=input("Enter the name of the batsman: ")
r=input("Enter the run scored by the batsman :  ")
r=int(r)
b=input("The number of balls faced by the batsman : ")
b=int(b)
avg=r/b
sr=avg*100
print("The batting strike rate of ",name, "is",sr)
