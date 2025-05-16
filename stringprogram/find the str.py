str = "sowmya"
index = str.find('o')  # Returns the index of first occurrence of 'o'

if index != -1:
    print(f"'o' is found at index {index}")
else:
    print("'o' is not found in the string")


str = "sowmya"

for i in range(len(str)):
    if str[i] == 'o':
        print(f"'o' is found at index {i}")
        break

str = "sowmya"