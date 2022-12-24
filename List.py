fruit = ["apples","oranges","bananas"]
print(fruit[1])
#oranges

print(len(fruit))
#3

print(fruit[-1])
#bananas
print(fruit[-2])
#oranges


#You can add, update, delete and reorder elements in a list.

fruit.append("kiwi")
print(fruit)
#['apples', 'oranges', 'bananas', 'kiwi']

fruit.insert(2, "passion fruit")
print(fruit)
#['apples', 'oranges', 'passion fruit', 'bananas', 'kiwi']


#Organizing a listHeader anchor link
#The elements in a list are not sorted automatically.

#If you want to return information which is sorted, but retain the original order of the list, you can use the sorted() function.

print(sorted(fruit))
['apples', 'bananas', 'kiwi', 'oranges', 'passion fruit']
print(fruit)
['apples', 'oranges', 'passion fruit', 'bananas', 'kiwi']


#In the example above you can see that the sorted() function return a sorted list, but does not alter the original order of the list.

#If you want to permanently sort the list, you should use the sort() method.

#Try the following:

fruit.sort()
print(fruit)
#['apples', 'bananas', 'kiwi', 'oranges', 'passion fruit']


#To reverse the order of a list you can use the reverse() method. This will permanently reverse the order of the list.

fruit.reverse()
print(fruit)
#['passion fruit', 'oranges', 'kiwi', 'bananas', 'apples']

#Delete
#You can remove elements from a list using the del statement if you know the index position.


del fruit[1]
print(fruit)
#['passion fruit', 'kiwi', 'bananas', 'apples']

#If you use del the element is deleted, so you can no longer use it, for example if you had a list of users, you might want to delete a user.

#If you want to use the value after removing it from a list you use the pop() method. To use pop(), you need to store the value you have removed from the list inside another variable.



favorite_fruit = fruit.pop()
print(favorite_fruit)
#apples

fresh_fruit = fruit.pop(1)
print(fresh_fruit)
#kiwi


#If you don't know the index position, or you don't want to remove the last item in the list, 
#you can use the remove() method to specify the value of the element you want to remove.

fruit.remove('bananas')
print(fruit)
#['passion fruit']


