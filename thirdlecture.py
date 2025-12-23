#Lists in python

# marks = [94.8,98,89.2,55.5,73.5,"harsh"]                #lists are nutable or changeable
# print(marks)
# print(len(marks))
# print(marks[0],marks[2],marks[5])

# print(marks[1:4])                                       #slicing is same as strings
# print(marks[-3:])
# print(marks[:-3])

#list methods

number = [2,1,3,5.5,9.9]

# number.append(5)                                           #append method
# print(number)

# number.sort()                                               #this sorts number in ascending
# print(number)
# print(number.sort())                                        #this will print none as list.sort() doesnot prints anything
# print(number.append())                                      #this will print none as list.append() doesnot prints anything
# number.sort()                                               #this will print in descending
# print(number)

number.reverse()                                              #reverse the list
print(number)

# number.insert(3,6.5)                                          #this will add element 6.5 on index 3
# print(number)

# number.remove(3)                                                #this will remove value 3 from list
# print(number)

# number.pop(3)                                                  #this will remove index value 3 from list
# print(number)

#tuples

# tup = (1,3,5,9,8,10,3,3,3,3,3)
# tup1 = (1,)                                                 #if we write tup = (1), it will consider as integer
# print(type(tup))
# print(tup1)

# #tuple slicing

# print(tup[:3])                                              #output will value from 0 to 2

# #tuple methods

# print(tup.index(5))                                          #this will result in index value of element

# print(tup.count(3))                                           #this will result in count of element occured in tuple

#third lecture program

# movie1 = str(input("Enter you favourite movie 1"))
# movie2 = str(input("Enter you favourite movie 2"))
# movie3 = str(input("Enter you favourite movie 3"))
# fav = []
# fav.append(movie3)
# fav.append(movie1)
# fav.append(movie2)
# fav.sort()
# print(fav)

#or

# movie = []

# movie.append(input("Enter first movie :"))
# movie.append(input("Enter second movie :"))
# movie.append(input("Enter third movie : "))

# movie.sort()

# print(movie)

#third lecture second program          

list = []

list.append(input("Enter data for list 1 :"))
list.append(input("Enter data for list 2:"))
list.append(input("Enter data for list 3:"))

store = list.copy()
store1 = list.reverse() 

if(list == store):
    print("This is palindrome")
elif(list == ''):
    print("Please enter data")
else:
    print("This is not")


 #fourth program

# list = ["c","c","a","b","d",]

# list.sort()
# print(list)

