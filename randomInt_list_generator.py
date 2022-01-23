from random import randint

elements=[]

elements_count = int(input("How many elements should the list contain?: "))

while elements_count > 0:
    new_element = randint(0, 100)
    elements.append(new_element)
    elements_count = elements_count - 1

print(elements)
