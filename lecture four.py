#dictionary and sets

# info = {                                                                    #here info is dictionary
#     "key" : "1",
#     "name" : "harsh",
#     "learning" : "python",
#     "age" : 28,
#     "subjected" : ["java" , "python"],
#     "topics" : ("lists" , "tuples")
# }

# info["surname"] = "gajra"
# print(info)

#nested dictionary

student = {                                                                    #here info is dictionary
    "key" : "1",
    "name" : "harsh",
    "learning" : "python",
    "age" : 28,
    "topics" : ("coding" , "programming"),
    "subjected" : {
        "phy" : 25,
        "chem" : 30
    }
}

# print(student["subjected"])                                     # this will print subjected dictionary
# print(student["subjected"]["chem"])                             # this will print the value from subjected dictionary

#dictionary methods

# print(student.keys())                                               #this will print all the keys in dictionary and not nested dictionary

#type casting

# print(len(list(student.keys())))                                #this will print length of student dictionary and this will type cast into list format

# print(len(student))                                             #this will print length of student dictionary

# print(student.values())                                            #this wil return all values from dictionary

# student["name"] = "gajra"
# print(student)

# pairs = list(student.items())                           #returns all key,value pairs as tuples
# print(pairs[2])

# print(student["name"])
# print(student.get("age"))                       #get will returns the key according to value


#when we want to add another key in dictionary

student.update({"city" : "Mumbai"})