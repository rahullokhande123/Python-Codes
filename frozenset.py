my_list=[2,4,6,8,6,10,12]
my_tuple=(1,3,5.6,5,10,)
my_set={2,4,3,5,2,6,}
my_dict={"name":"Rahul", "college":"IES College", "year":2024}

a=frozenset(my_list)
b=frozenset(my_tuple)
c=frozenset(my_dict)
d=frozenset(my_set)
print(a)
print(b)
print(c)
print(d)
print(len(a))
print(max(a))
print(min(a))
print(sum(a))
print(frozenset(a))
# ==========================================

a.union()
print(a)
b.difference()
print(b)
c.intersection()
print(c)

# =========================================

import sys
import keyword



my_list2=[50,4,80,96]
my_tuple2=(78,96,45,10,60)
my_set2={10,85,96,41,20}
l_size= sys.getsizeof(my_list2)
t_size= sys.getsizeof(my_tuple2)
s_size= sys.getsizeof(my_set2)
print(l_size)
print(t_size)
print(s_size)

list=keyword.kwlist
print(list)
