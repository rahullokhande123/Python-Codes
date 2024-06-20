# Slice=============================

my_str="RAHUL"
x=slice(-1,-4,)
print(my_str[x])


# Collection========================
y="Rahul Lokhande"
c="I M RAHULLOKHANDE"


print(c[0:15:2])
print(y[::-1]) # Esse pura revers ho jayega 
print(y[::]) # Esse Puri String As tis print ho jati h
print(y[:4:]) # Esse Jo bhi hm end point denge (n-1) tk print krega.
print(type(y))

my_list=(10,20,"Rahul Lokhande",30,40,"Shubham")
print(my_list[::])
print(my_list[2:5:])
print(my_list[::-1])
print(my_list[-2:-5:-1])
