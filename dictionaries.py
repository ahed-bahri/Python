states = {'NY': 'New York', 'PA': 'Pennsylvania', 'CA': 'California'}
print(states['NY'])
print(states['PA'])
print(states['CA'])

peoples = {"ahed","jack"}

print(type(states))
print(type(peoples))

print(states.get('TN', "Sorry Not Found"))
print(states.get('NY', "Sorry Not Found"))

print(states.keys())
print(states.values())
states['TN']= "Tunisia"
print(states)


user= {'name' :'ahed', 'height' : '160', 'shoes' : '38', 'hair':'brown'}
print(user['name'])


#dictionary and list can be each other

animal_sounds = {
   "cat": ["meow","purk"],
   "dog": ["woof","bark"],
   "fox": []
}

ahed= {'name' :'ahed', 'height' : '160', 'shoes' : '38', 'eyes':'brown'}
jdoula= {'name' :'jdoula', 'height' : '180', 'shoes' : '43', 'eyes':'blue'}
elhem= {'name' :'elhem', 'height' : '170', 'shoes' : '40', 'eyes':'black'}

people = [ahed,jdoula,elhem]
print(people)

for person in people:
    print(person['height'])
    print(person.get('height','Sorry Not Found'))
