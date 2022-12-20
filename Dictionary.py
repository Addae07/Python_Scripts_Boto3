#A dictionary is a way of storing related information in key-value pairs. It uses a key as an identifier and a value to store the information. For example, the key could be first_name and the value could be Ada.

#A dictionary when written in python would look like {"first_name":"Ada"}. A dictionary in python is abbreviated to dict and has the following syntax {"key":"value"}. The key is a string providing an identifier and the value can be the same kind of values you would store in a variable.

#Dictionaries are very common in AWS, so you will see them frequently.

#They are used to exchange information between different services and functions
#They are returned by Application Programming Interfaces (API)
#They are used as Tag values
#Creating, Reading, Updating and Deleting values in a dictionary
#Create
#Dictionaries can be created by assigning the key-values you want to store in the dictionary.

#Using the python interactive mode, try the following:
#1
#2
#3
>>> user = {"first_name":"Ada"}
>>> print(user)
{'first_name': 'Ada'}

or if you are going to be adding the contents of the dictionary later, you can declare an empty dictionary. You can create an empty dictionary in two ways:

Assigning {} to a variable, for example:

account_details = {}

or use the dict() constructor:

account_details = dict()

#Read
#To read the value associated with a key, you need to provide the name of the dictionary and the the value of the key inside square brackets.

#Try the following:
#1
#2
#3
>>> user = {"first_name":"Ada"}
>>> print(user["first_name"])
Ada

#Update
#Add a key-value
#Dictionaries are mutable, which means they can be changed after you create them. You can add, update or delete the key-value pairs in a dictionary.

#To add an additional key-value to a dictionary, provide the dictionary name, the new key in [] and a value after an = sign.

#1
#2
#3
>>>user["family_name"] = "Byron"
>>>print(user)
{'first_name': 'Ada', 'family_name': 'Byron'}

#Modify a value
#To modify a value in a similar way to adding it. You provide the new value after the = sign.

#Try the following:
#1
#2
#3
user["family_name"] = "Lovelace"
print(user)
{'first_name': 'Ada', 'family_name': 'Lovelace'}

#Delete a Key-Value Pair
#To remove a key-value pair you use the del statement with the name of the dictionary and the key you want to delete.

#1
#2
#3
>>> del user["family_name"]
>>> print(user)
{'first_name': 'Ada'}

#Summary
#A dictionary, like a variable can contain other data types, including other dictionaries and lists. {}`. You will use dictionaries a lot in AWS as input and outputs.

