#Instead of using a for loop to add elements to a list you can do this:
mylist=[letter for letter in "Junior"]
print(mylist)
#ANother example (YOu can even do operations on list comprehensions)
mynumlist=[num for num in range(1,10)]
print(mynumlist)
#You can even add if statements to the list comprehensions
myexample=[x for x in range(0,11) if x%2==0]
#^ Would print 0,2,4,6,10
print(myexample)

#You can use else statements in list comprehensions
#The syntax is different
anotherone=[x if x%2==0 else 'ODD' for x in [1,2,3,4,5,6,7,8]]
print(anotherone)

#You can even have nested for loops
nested=[x*y for x in [2,4,6] for y in [1,10,100]]
print(nested)
