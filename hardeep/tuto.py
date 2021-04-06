a =[] 
b =[]
d =[]
for i in range(11):
    b.append(i)

c= list(range(11))

d = [x for x in range(11)]
# ============================================

print(b)
print(c)
print(d) 

a2 = [x*2 for x in b]
print(a2)


print(b[4])
print(len(b))
# print(b[10:11])
print(b[len(b)-1])
print(b[10])
print(b[-1])
