# creating a list
a = [10,20,30,40,50]
print(a)
b = list([10,20,312])
print(b)
# accessing elements of a list
a = [10,20,30,40,50]
print(a[0])
print(a[-1])
# creating list with repeated elements
a = [10,20,30,40,40]
print(a*2)
#addding elements to a list
a = [10,20,30,40,50]
a.append(100)
print(a)
a.insert(1, 50)
print(a)
#removing elements from a list
a = [10,20,30,40,50]
a.remove(40)
print(a)
a.pop()
print(a)
#slicing a list
a = [10,20,30,40,50]
print(a[0:])
print(a[2:])