# x=input("Enter your Name:")
# print(x)
# print(type(x))


# #  By Using TypeCasting ==========================

# y=int(input("enter your age:"))
# print(y)
# print(type(y))


# Collection=(10,20,30,40,50)
# print(ord('A'))
# print(chr(65))
# print(float(5))
# print(complex(5))
# print(list(Collection))

# my_str="Rahul"
# my_str[0]='r' # r given error

# =================================================

my_str2="Rahul"
print(len(my_str2))
print(max(my_str2))
print(min(my_str2))
print(type(my_str2))
print(id(my_str2))
print(ord(max(my_str2)))
print(my_str2.upper())
# print(my_str2.center(40"#"))
x="abc"
print(' '.join(x))
y='123'
print(x.join(y))
print('---'.join(y))

# ============== Split =============

str="Python is a programming language"
print(str.split(" "))
print(str.split(",",2)) # kuch change nhi krega kyoki use , ye symbol nhi mila
print(str.split(":",4)) # kuch change nhi krega kyoki use : ye symbol nhi mila
print(str.split(" ",1)) # frist time space milne pr split krega 2 part me
print(str.split(" ",0))

