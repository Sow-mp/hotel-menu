set1={"hello",1,22,"hi",123}
print(set1)
set1.add(12)
print(set1)
set1.update(["welcome",'145'])
print(set1)
set={1,"sow","hello"}
print(set1.union(set))
print(set1 | set)
print(set1.intersection(set))
print(set1 & set)
print(set1-set)
print(set1.difference(set))
print(set1.symmetric_difference(set))

set1={"hello",1,22,"hi",123,1,2}
print(set1)
print(set1.pop())
print(set1)
print(set1.remove("hello"))
print(set1)
for i in set1:
    print(i)

res=list(set1)
for index,item in enumerate(res):
    print("index:",index,"item:",item)