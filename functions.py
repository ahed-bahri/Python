def greet(name):
    return f"hey {name}"

def concat(word1, word2):
    return word1 + word2


print(concat("ahed","bahri"))

def age_in_dog_years(age):
    res = age * 7
    return res

print(greet("ahed"))
print(greet("Love"))
print(age_in_dog_years(20))

print(concat(word1="ahed",word2="bahri"))

name="mattan"

def print_different_name():
    name="chris"
    print(name)

print(name)
print_different_name()
print(name)


#upper case Challange answer

def reverse (word):
    return word[::-1]

def uppercase_reverse(word):
    return reverse(word.upper())

print (uppercase_reverse("banana"))





