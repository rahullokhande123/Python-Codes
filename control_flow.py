# age=int(input("Enter Your Age :"))
# if age>18:
#     print("YOU ARE VALIDE FOR VOTING")
# else:
#     print("You are not eligible for votting")
    
# print("Thank You For Visiting")


a=range(10)
print(a)
print(list(a))
print(tuple(a))
print(set(a))
# Even No. in - way
b=range(-2,-11,-2)
# odd No. in -way
c=range(-1,-11,-2)
# Positive odd No.
d=range(2,11,2)
print(list(b))
print(list(c))
print(list(d))
# ============ for Loop ==================

my_list=[]
for i in range(2,11,2):
    x=i**2
    my_list.append(x)
print(my_list)

# ========================================

my_str=input("Enter Your Name : ")
total_char=0
Vowel=0
Consonent=0
for i in my_str:
    total_char=total_char+1
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        Vowel=Vowel+1
    else:
        Consonent=Consonent+1
    
print(total_char)
print(Vowel)
print(Consonent)

# ============= While Loop =============

n=int (input("Enter no."))
i=1
sum=0
while i<=n:
     if i==n:
         print(i,end="=")
     else:
         print(i,end="+")
         sum=sum+i
     i=i+1
print(sum)
# ==============Even No================

n=int (input("Enter no."))
i=1
sum=0
while i<=n:
     if i%2==0:
         print(i,end=",") 
     i=i+1
# ============ Factorial =================

n=int (input("Enter no."))
i=1
multi=1
while i<=n:
     multi=multi*n
     if i<n:
         print(n,end="x")
          
     else:
         print(n,end="=")
         
     n=n-1
print(multi)

# =============== Multiple ==============
n=int (input("Enter no."))
i=1
multi=1
while i<=n:
     multi=multi*i
     if i==n:
         print(i,end="=") 
     else:
         print(i,end="x")
         
     i=i+1
print(multi)