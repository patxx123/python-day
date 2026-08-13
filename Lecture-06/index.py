animals = ["cat" , "dog" , "rabbit" , "hamster" , "dog" , "parrot"]
first_fog_index = animals.index("dog")
print(f"The first occurrence of 'dog' is at index: {first_fog_index}")

second_dog_index = animals.index("dog" , first_fog_index + 1)
print(f"The second occurrence of 'dog' is at index: {second_dog_index}")