def reverse_string(s):
    rev=" "
    for char in s:
        rev=char+rev
    print("rev",rev)
print(reverse_string("hello"))