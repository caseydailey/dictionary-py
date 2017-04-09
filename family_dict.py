#Define a dictionary that contains information about several members of your family. 
my_family = {
    'mother': {
        'name': 'Bonnie',
        'age': 65
    },
    'father': {
        'name': 'Clarence',
        'age': 77
    },
    'sister': {
    	'name': 'Lacy',
    	'age': 36
    },
    'brother': {
    	'name': 'Doni',
    	'age': 33
    },
}

#Using a dictionary comprehension, 
#produce output that looks like this: "Krista is my sister and is 42 years old"
family_dictionary = {
	value['name'] + ' is my ' + key + ' and is ' + str(value['age']) + ' years old' 
	for (key, value) in my_family.items()
}
print(family_dictionary)
