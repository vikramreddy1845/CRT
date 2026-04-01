'''# creating a list
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
#creating a set
s = {10,20,30,40,50}    
print(s)
s = set([10,20,30,40,50])
print(s)
#accessing elements of a set
s = {10,20,30,40,50}
for i in s:
    print(i)
#adding elements to a set
s = {10,20,30,40,50}
s.add(60)
print(s)
#removing elements from a set
s = {10,20,30,40,50}
s.remove(40)
print(s)
#set operations
s1 = set([10,20,30,40,50])
s2 = set([40,50,60,70,80])
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))



#tuples
t = (10,20,30,40,50)
print(t)
t1 = tuple([10,20,30,40,50])
print(t1)
print(t[0])
print(t[-1])
print(t + t1)
print(tuple([t, t1]))
print(t*3)
del t1      #Error as tuples are immutable
print(t1)
'''

# Dictionaries
d = {'name': 'John', 'age': 30, 'city': 'New York'}
print(d)
d1 = dict(name='John', age=30, city='New York')
print(d1)
print(d['name'])
d['age'] = 31
print(d)
print(d1.get('name'))
print(d1.values())
print(d1.get('age'))