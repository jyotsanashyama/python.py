a = "Hello World"
print(a[1])
b = "Jyotsana"
print(b[5])
print(b[4:8])#here, index 4 is included and index 8 is excluded...print upto index 7 only
print(b[-5]) #negative index starts from back
print("Length of b = ",len(b))

c = "Eat Sleep Code Repeat"
if "leep" not in c:# if "leep in c: print("Yes")---- it will print yes
    print("Yes")
else:
    print("No")

#Slicing of Array    
print(c[4:20])
print(c[:])#will print from start to end
print(c[2:])#print from 2 upto last
print(c[:7])#print from start to index 6 [Remember last 7 is excluded]

print(a[-5:-2])
