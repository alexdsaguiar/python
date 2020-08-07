def pet_species(pet_name):
	result = ""
	for pet, name in pet_name.items():
		result += f"My {pet} name is {name}!" + "\n"
	return result

print(pet_species({"dog":"Nick", "cat":"Simba"}))

def count_letters(text):
  result = {}

  for letter in text:
	  if letter in "0123456789.!?+-= " :
		  continue
	  elif letter in result:
		  result[letter] += 1
	  else:
		  result[letter.lower()] = 1
	  
  return result

print(count_letters("AaBbCc")) # Should be {'a': 2, 'b': 2, 'c': 2}
print(count_letters("Math is fun! 2+2=4")) # Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}
print(count_letters("This is a sentence.")) # Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}
