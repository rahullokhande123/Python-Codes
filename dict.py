my_dict=dict()   #Rsse blank dict ban jata h
print(my_dict) 
print(id(my_dict))
print(type(my_dict))
my_dict["Name"]="Rahul"   # Esse dict me object add ho jayega
print(my_dict)

my_dict["Qulification"]="BBA"
print(my_dict)
my_dict["Name"]="Arun"  # Esse Ager Key Same Ho to value update kr dega or pahle se 
                           # es name ki key nhi hoto ye bna dega or value assign kr dega
print(my_dict)
print(id(my_dict))


del my_dict["Name"]  # Esse Key Vlue Delete Ho Jayegi 
print(my_dict)

# print(my_dict["Name"])   # Esme Error Aayega Kyoki "Name" Ko Hm Delete Kr chuke h

my_dict.clear()     # Esse Puri Dict Clear Hojayegi 
print(my_dict)


my_dict["Class"]="12th"
my_dict["College"]="IES College"
print(max(my_dict))
print(len(my_dict))    # Esse Lenghth dega 
print(my_dict)      
                 # Esme max ko vo ascii value ke bases pr present kr raha h 

print(my_dict.keys())  # Esse Total Keys Bta Dega
print(my_dict.values())  # Esse Total Values Bta Dega

print(my_dict.items())   # Esse Key or value ka piar de dega 

print(my_dict.get('Class','Guest'))  # Esse  Hm key ki value le sakte h or default
                                    # me Guest Set Kr Sakte H , Ki Kabhi Ye key dic
                                    # n ho to bhi error n de default value de.
                                           #. Yah Ak Method H

# print(my_dict["key",Guest]) # Es Condition Me Error Throgh Krega 

print(my_dict.pop("Class"))