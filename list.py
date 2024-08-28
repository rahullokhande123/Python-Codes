# # my_list=[10,20,30,'abc',"abc123",'abc',10]
# # print(my_list)
# # print(my_list[5])
# # print(my_list[2:])
# # my_list[0]="Rahul"
# # print(my_list)

# x=10,20,30,40,50,60
# print(len(x))
# print(max(x))
# print(min(x))
# print(sum(x))
# print(list(x))
# # ============== append() =================
# my_list=[10,20,30,'abc',"abc123",'abc',10] 
# my_list.append("Rahul")
# print(my_list)
# # ================ extende() ==============
# my_list.extend(x)
# print(my_list)
# # ================ pop() ==================
# my_list.pop()
# print(my_list)

# # =============== remove() ================
# my_list.remove('abc123')
# print(my_list)

# # ================= insert() ==============
# my_list.insert(1,"Arun")
# print(my_list)

# # ================ sort() =================
# y=[50,80,48,6,4]
# z=["arun","jalaj","chiku","sohan"]
# y.sort()
# print(y)
# z.sort()
# print(z)

# # ========== sort(reverse=True) ============
# z.sort(reverse=True)
# print(z)

# # ========== Q1 Capital First Letter ===========

# lis = ["we","are","here","to","revise","python"]

# for i in range(0,len(lis)):
#     lis[i]=lis[i].capitalize()
# print(lis)

# # # ========== Capital All Letters ===========

# lis = ["we","are","here","to","revise","python"]

# for i in range(0,len(lis)):
#     lis[i]=lis[i].upper()
# print(lis)

# # # ========== Capital All Letters ===========

# lis = ["we","are","here","to","revise","python"]

# for i in range(0,len(lis)):
#     lis[i]=lis[i][0].upper() + lis[i][1:]
# print(lis)

# # ============== Q2 Palindrom ===============
# # WAP to create a new list with the help of list 
# # lis such that it contain only palindrome string which has a length more then 2.

# lis=["ababa","nitin","we","new","ww","a","aaaa"]
# lis1=[]
# for i in lis:
#     if i==i[::-1] and len(i)>2:
#         lis1.append(i)
# print(lis1)

# # Seconde Way :-
# # for i in range(len(lis)):
# #     if lis[i]==lis[i][::-1] and len (lis[i])>2:
# #         lis1.append(lis[i])
# # print(lis1)

# ===================== Find Max Marks ========================

name= ["ajay","aman","akash","sonam","radha"]
address=["bhopal","ujjain","bhopal","ratlam","agra"]
st_marks= [45,56,35,56,12]
mx=max(st_marks)
count=st_marks.count(mx)
# print(count)
index=-1
for i in range(count):
    index=st_marks.index(mx,index+1)
    print("Student Name:",name[index])
    print("Student Address:",address[index])
    print("Student Marks:",st_marks[index])

# WAP to create following list at runtime and placed them all in single list.(list of list)
# ==================== Create List Of List ====================

record=int(input("How Many Student Do You Want ???"))
st_details=[[],[],[]]
for i in range(record):
    name=input("Enter Name")
    address=input("Enter Address")
    marks=int(input("Enter Marks"))
    st_details[0].append(name)
    st_details[1].append(address)
    st_details[2].append(marks)
print(st_details)

