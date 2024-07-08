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

# =================== Multiple ===================
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

# ================== Swaping =====================
x=20
y=10
print(x,y)
z=x
x=y
y=z
print(x,y)
# ================== Swaping By Multiplacation and Division ==================
x=int(input("Enter first no"))
y=int(input("Enter Second no"))
print("Before Swap:",x,y)
x=x*y
y=x/y
x=x/y
print("After Swap:",x,y)

# ================== Swaping By Addition and Substraction ==================
x=int(input("Enter first no"))
y=int(input("Enter Second no"))
print("Before Swap:",x,y)
x=x+y
y=x-y
x=x-y
print("After Swap:",x,y)

# ================== Swaping By without using third variable ==================

x=int(input("Enter first no"))
y=int(input("Enter Second no"))
print("Before Swap:",x,y)
x,y=y,x
print("After Swap:",x,y)

# ======================= Armstronng Numbers ====================

n=int(input("Enter first no"))
m,p=n,n
sum=0
count=0
while n>0:
    count=count+1
    n=n//10
print("Count:",count)
while m>0:
    last=m%10
    sum=sum+last**count
    m=m//10
if sum==p:
    print("Armstrong No.")
else:
    print("Not Armtrong No.")

# =========== Palindrom Numbers With The Help Of Slice Method =============

n=input("Enter Number : ")
m=n[::-1]
if n==m:
    print("Palindrom Number")
else:
    print("Not Palindrom Number")

# =========== Palindrom Numbers Without Slice Method =============

n=int(input("Enter Number : "))
sum,x=0,n
while n>0:
    rev=n%10
    sum=sum*10+rev
    n=n//10
print(sum)
print(n)
print(x)
if x==sum:
    print("Palindrom")
else:
    print("Not Palindrom")

# ==================== Pettern ===========================
#(Pettern-1)
# *
# **
# ***
# ****
# *****
 
# Solve:-

n=int(input("Enter Rows"))
i=1
while i<=n:
    print(i*'*'+(n-i)*(' '))
    i=i+1

#(Pettern-2)
# *****
# ****
# ***
# **
# *
# Solve:- 
n=int(input("Enter Rows"))
i=1
while i<=n:
    print((n-i)*(' ')+i*'*')
    i=i+1
# ===========================================
#(Pettern-3)
#      *
#     * * 
#    * * *
#   * * * *
# 
# Solve:-
n=int(input("Enter Rows"))
i=1
while i<=n:
    print((n-i)*(' ')+i*' *')
    i=i+1

# ============================================
#(Pettern-4)
 #       *
  #     ***
  #    *****
  #   *******
  #  *********
# 
# Solve:-

n=int(input("Enter Rows"))
i=1
while i<=n:
    print((n-i)*(' ')+(2*i-1)*'*')
    i=i+1

# =============================================
# (Pettern-5)
# *****
#  ****
#   ***
#    **
#     *
# Solve:-
n=int(input("Enter Rows"))
i=0
while i<=n:
    print(i*" "+(n-i)*"*")
    i=i+1

# ============================================

# (Pettern-6)
# *****
# **** 
# ***  
# **   
# *
# Solve:-
n=int(input("Enter Rows"))
i=0
while i<=n:
    print((n-i)*"*"+i*" ")
    i=i+1

# ================== Fibona Series ======================

# Solve:-
n=int(input("Enter Any No"))
a=0
b=1
print(a,end=',')
print(b,end=',')
i=1
while i<=n-2:
    c=a+b
    a=b
    b=c
    if i<n-2:
        print(c,end=',')
    else:
        print(c)
    i=i+1


# ===================== Function ==========================

def add(x,y,z):
    return x+y+z
p=int(input("enter number"))
q=int(input("enter number"))
r=int(input("enter number"))
      
x=add(10,20,30)
print(x)
n=x+100
print(x)

# ======================= Function ==========================

def add(x,y):
    return x+y,x-y,x*y,x/y,x%y,x//y
p=int(input("enter number"))
q=int(input("enter number"))
# r=int(input("enter number"))
      
a,b,c,d,e,f=add(p,q)
print(a,b,c,d,e,f)