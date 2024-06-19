#print("-----------------Bytes---------------")
my_data = [10,20,25,32,35]
x = bytes(my_data)
print(type(x))
print(x)
 
# 'bytes' object does not support item assignment
# x[0]=100
# print(x)

print("-----------------bytearray---------------")
my_data = [10,20,25,32,35]
x = bytearray(my_data)
print(type(x))
print(x)

# 'bytearray' object supports item assignment
x[0]=100
print(x)


