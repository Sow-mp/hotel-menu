def gen_iter():
    n=1
    print("this is printed first")

    yield n

    n=n+1
    print("this is printed second: ")

    yield n
for i in gen_iter():
    print(i)
#a=gen_iter()
#next(a)
#print(next(a))
#print(next(a))
