key=['name','age','salary']
values=['sow',21,22000]
res=dict([('name','sow'),('age',21),('salary',20000)])
print(res)
str="123456'' "
str="123456"
str="abcABC123"
print(str.isalnum())
str='just!jj'
print(str.isalpha())
str=u"1234561"
print(str.isdecimal())
str="he$1234561"
print(str.isascii())
str = " \n"
result=str.isspace()
print("Are all the characters of the string spaces?", result)
str="class"
str="my_variable"
str="  _hi  "
print(str.isidentifier())
print(str.rstrip())
str="hello\nworld"
str="hello world"
print(str.isprintable())

