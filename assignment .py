#Ask for the name
my_name= input("Please Enter Your Name ? : ")
print (my_name)
#replacing
the_total=float(input("whats The total ? : ").replace('$',' '))
print (the_total)
#calculating
tip_15 = the_total*0.15
tip_18 = the_total*0.18
tip_20 = the_total*0.20
#Type it on screen
print(f"15% is $ {tip_15:.2f}")
print(f"18% is $ {tip_18:.2f}")
print(f"20% is $ {tip_20:.2f}")