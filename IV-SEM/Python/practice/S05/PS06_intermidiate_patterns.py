'''li = [1,2,3,4,5]
res = []
for i in li:
    res.append(i**2)
print(res)

li = [1,2,3,4,5]
res = []
for i in li:
    if i%2 == 0:
        res.append(i)
print(res)


li = ['a','b','c']
res = ''
for i in li:
    res = res + i + " "
print(res) 
print("^".join(li)) 


 
print("--------------------------------")
for i in range(n,0,-1):
    print(" " * (n-i) + "* " * i)
    

n = int(input())
for i in range(1,n):
    print(" " * (n-i) + "* " * i)
for i in range(n,0,-1):
    print(" " * (n-i) + "* " * i)


n = int(input())
for i in range(1,n+1):
    print(" " *(n-i) + " ".join([str(j) for j in range(1,i+1)]))
'''

n = int(input())
for i in range(1,n+1):
    print("* ")
    
