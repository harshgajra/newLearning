# str1 = "this is a string.\n also print in next line"           #mostly used
# str2 = 'this is also string'
# # final = str1 + str2
# # print(len(str2))
# # print(final)

# #length of string
# # print(len(str1))
# # print(len(str2))
# # print(len(final))

# # #indexing (indexing always starts with 0 | we cannot manipulate in indexing)
# # ch = str1[5]                    #syntax - variable = str[]
# # print(ch)
# # print(str2[3])

# #slicing(accessing a part of strings | )

# # print(str1[0:2])                    #syntax - str[starting_index : ending_index]
# # print(str2[0:len(str2)])
# # print(str1[:8])                     #this means starting index is 0 
# # print(str2[0:])                     #this means ending index is 19

# # print(str2[-11:-1])                 #here strings will be counting from right to left starting from -1 to -11

# #String functions

# # print(str2.endswith("ng"))             #syntax - str.endswith("") #endswith function findsout words ending with in string 
# # print(str2.capitalize())               #this will only realise result string in capitalize

# #if str variable needs to capitalize then

# # str2 = str2.capitalize()                #sytnax - str.capitalize() #this will capitalize our original string
# # print(str2)

# #replace function

# # print(str2.replace("o" , "a"))          #syntax - str.replace("oldvalue" , "new value")#this replaces o to a 
# # print(str2.replace("also" , "a"))       #this replaces also to a

# #Find function

# # print(str2.find("also"))                    #syntax - str.find("value") #this will find the index of 1st occurance

# #count function

# # print(str2.count("i"))                      #syntax - str.count("value") #this will count the value occurance in string
 

# #first program in Lecture 2

# # a = str(input("Enter your name:"))
# # print(len(a))

# #second program in lecture 2

# # test = str(input("Enter $ as per your requirement"))
# # print("occurance of $ in test is : " , test.count("$"))

# #Conditional statement

# light = "black"

# if(light == "Red"):
#     print("Stop")
# elif(light == "Green"):
#     print("Go")
# elif(light == "Yellow"):
#     print("Wait")
# else:
#     print("check light")

# age = 1

# if(age >= 18):
#     print("can vote and drive")             #here spaces in print statement is called indentation
# elif(age <= 18):
#     print("Cannot")
# else:
#     print("enter valid age")

#program to write grade students

# Grade = float(input("Enter Grade: "))

# if(Grade >= 90):
#     print("Grade A")
# elif(Grade >= 80):
#     print("Grade B")
# elif(Grade >= 70):
#     print("Grade C")
# else:
#     print("Grade D")


#Nesting - when if statement consists of another if statement

# age = 98

# if(age >= 18):
#     if(age >= 80):
#         print("Cannot drive")
#     else:
#         print("can drive")
# else:
#     print("Cannot drive")

#practice programs

# num = int(input("enter the number:"))

# if(num % 2 == 0):
#     print("Number is even")
# elif(num % 2 == 1):
#     print("Number is odd")
# else:
#     print("Enter valid number")

#second program

# num1 = float(input("Enter number 1:"))
# num2 = float(input("Enter number 2:"))
# num3 = float(input("Enter number 3:"))

# if(num1 > num2 and num1 > num3):
#     print("Number 1 is greater", num1)
# elif(num2 > num3):
#     print("Number 2 is greater", num2)
# else:
#     print("Number 3 is greater", num3)

#third program

# num = int(input("enter the number:"))

# if(num % 7 == 0):
#     print("Number is multiple of 7")
# else:
#     print("Number is not multiple of 7")

#how work program

num1 = float(input("Enter number 1:"))
num2 = float(input("Enter number 2:"))
num3 = float(input("Enter number 3:"))
num4 = float(input("Enter number 4:"))

if(num1 > num2 and num1 > num3 and num1 > num4):
    print("Number 1 is greater", num1)
elif(num2 > num3 and num2 > num4):
    print("Number 2 is greater", num2)
elif(num3 > num4):
    print("Number 3 is greater", num3)
else:
    print("Number 4 is greater", num4)