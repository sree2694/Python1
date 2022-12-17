
dictionary = {1:'one',2:'two',3:'three'}

print(dictionary)

print("\ndictionary.popitem()")
dictionary.popitem()
print(dictionary)

dictionary1 = {7: 'seven', 8: 'eight', 9: 'nine'}

print("\ndictionary.update(dictionary1)")
dictionary.update(dictionary1)
print(dictionary)

print("\ndictionary.keys()")
print(dictionary.keys())

dictionary[3] = 'four'
print("\nlistNumbers[3] = 'four'")
print(dictionary)

print('\ndictionary[1]')
print(dictionary[1])

print("\ndictionary.get(1)")
print(dictionary.get(1))

print("\ndictionary.clear()")
dictionary.clear()
print(dictionary)