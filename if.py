#first_method
"""answer = input("Do you want to hear my joke? ")
if answer == "Yes":
    print("I'm against picketing, but I don't know how to show it.")
#RIP
elif answer == "No":
    print("Fine")
else:
    print("I donn't understand")"""

    #Second method
""" 
answer = input("Do you want to hear a joke? ")

if answer == "Yes" or answer == "yes":
    print("I'm against picketing, but I don't know how to show it.")
   #RIP
elif answer == "No" or answer == "no" :
    print("Fine")
else:
    print("I donn't understand")
 """
#third_method

answer = input("Do you want to hear a joke? ")

affirmative_responses = ["yes", "y"]
negative_responses = ["no", "n"]

if answer.lower() in affirmative_responses:
    print("I'm against picketing, but I don't know how to show it.")
#RIP
elif answer.lower() in negative_responses:
    print("Fine")
else:
    print("I donn't understand")

