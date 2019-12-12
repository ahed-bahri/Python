#Asking the usser to insert the name
my_name= input("Please Enter Your Name ? : ")
#show the name entered
print (my_name)
#insert the total and replace the dollar sign with white space,and convert the result to float
the_total=float(input("The total of the bill ? : ").replace('$',' '))
#print the total on screen
print (the_total)
#calculating when the tip is 15% and save the result on tip_15 variable
tip_15 = the_total*0.15
#calculating when the tip is 18% and save the result on tip_18 variable
tip_18 = the_total*0.18
#calculating when the tip is 20% and save the result on tip_20 variable
tip_20 = the_total*0.20
#show the 15 % tip on screen with 2 numbers after cama on the right
print(f"when the tip is 15%  {tip_15:.2f} $")
#show the 18 % tip on screen with 2 numbers after cama on the right
print(f"when the tip is 18%  {tip_18:.2f} $")
#show the 20 % tip on screen with 2 numbers after cama on the right
print(f"when the tip is 20%  {tip_20:.2f} $")