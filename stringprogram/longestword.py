
def longest_word(s):
    words=s.split()
    longest=" "
    for word in words:
        if len(word)>len(longest):
            longest=word
    return longest

print(longest_word("pyhton programming"))

def longest_word(s):
    words=s.split()
    long=" "
    for word in words:
        if len(word)>len(long):
            long=word
    return long

print(longest_word("pyhton hi"))