import string
def buildCoder(shift):
    mapper={}
    for ch in string.ascii_lowercase:
        if (ord(ch)+shift)>ord('z'):
            mapper[ch]=chr(ord(ch)+shift-ord('z')+ord('a')-1)
        else:
            mapper[ch]=chr(ord(ch)+shift)
    for ch in string.ascii_uppercase:
        if (ord(ch)+shift)>ord('Z'):
            mapper[ch]=chr(ord(ch)+shift-ord('Z')+ord('A')-1)
        else:
            mapper[ch]=chr(ord(ch)+shift)
    return mapper
