x=(10,20,40,50,80,100)
print(len(x))
print(max(x))
print(min(x))
print(sum(x))
print(x)

# Inbuild Method==================
print(x.count(10))
print(x.index(80))
y = list(x)
y.append(200)
print(list(y))

a=[10,20,30]
a.append([40,50,60])
a.remove([40,50,60])
print(a)

# =====================================

r=("Rahul","Arun","Yashi",60,40,"#","/+")
s=list(r)
s.append(500)
print(s)
print(s.index("Yashi"))
