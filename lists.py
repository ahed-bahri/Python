the_count = [1, 2, 3, 4, 5]
phones = ["Apple", "Microsoft", "Windows"]
random_mix = ["phone", 88, "sac", 1/4, ["Oh another list", "A list inside a list"]]


# looping
for x in the_count:
    print("this is count", x)


for ph in phones:
    print("types of phones",ph)

for rdmX in random_mix:
    print("Mixed list",rdmX)

people = []

people.append("ahed")
people.append("chedy")
people.append("fedi")
print(people)

people.remove("chedy")
print(people)

for person in people:
    print ("The person is : ", person)

#list of animals
animals = ['dog', 'cat', 'tiger', 'dolphin']
first_animal = animals[0]

print(first_animal)

third_animal = animals[2]

print(third_animal)

second_animal = animals[1]

print(second_animal)


print("There are this many things:", len(random_mix))
print("this is a : ",type(random_mix))


another_list = random_mix[-1]
print(another_list)
print(type(another_list))