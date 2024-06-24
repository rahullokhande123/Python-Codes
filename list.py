# my_list=[10,20,30,'abc',"abc123",'abc',10]
# print(my_list)
# print(my_list[5])
# print(my_list[2:])
# my_list[0]="Rahul"
# print(my_list)

x=10,20,30,40,50,60
print(len(x))
print(max(x))
print(min(x))
print(sum(x))
print(list(x))
# ============== append() =================
my_list=[10,20,30,'abc',"abc123",'abc',10] 
my_list.append("Rahul")
print(my_list)
# ================ extende() ==============
my_list.extend(x)
print(my_list)
# ================ pop() ==================
my_list.pop()
print(my_list)

# =============== remove() ================
my_list.remove('abc123')
print(my_list)

# ================= insert() ==============
my_list.insert(1,"Arun")
print(my_list)

# ================ sort() =================
y=[50,80,48,6,4]
z=["arun","jalaj","chiku","sohan"]
y.sort()
print(y)
z.sort()
print(z)

# ========== sort(reverse=True) ============
z.sort(reverse=True)
print(z)
