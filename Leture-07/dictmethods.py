phonebook = {'Anirach': '777-1111', 'Mickey': '777-2222', 
             'Donald': '777-3333', 'Pluto': '777-4444'}

heroesdict = {}
heroesdict['Hulk'] = '888-1111'
heroesdict['Iron Man'] = '888-2222'
print(heroesdict.get('Halk', 'Key not found'))  # Output: 888-1111
print(heroesdict.get('Hulk', 'Key not found'))  # key not found

for key, value in phonebook.items():
    print(key, value)

print(phonebook.keys())  # Output: dict_keys(['Anirach', 'Mickey', 'Donald', 'Pluto'])
print(phonebook.values())  # Output: dict_values(['777-1111', '777-2222', '777-3333', '777-4444'])

print(phonebook.pop('Mike', 'Element not found'))  # Output: Element not found
print(phonebook.pop('Mickey', 'Element not found'))  # Output: 777-2222
print(phonebook)  # Output: {'Anirach': '777-1111', 'Donald': '777-3333', 'Pluto': '777-4444'}
print(phonebook.popitem())  # Output: ('Pluto', '777-4444') (or another key-value pair)
print(phonebook)  # Output: {'Anirach': '777-1111', 'Donald': '777-3333'} (remaining items in the dictionary)
print(phonebook.clear())  # Output: None (clears the dictionary)
print('After clear')
print(phonebook)  # Output: {} (empty dictionary)