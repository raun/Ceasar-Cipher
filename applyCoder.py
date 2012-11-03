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
def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    res=''
    for ch in text:
        if ch in string.ascii_lowercase:
            res = res + coder[ch]
        elif ch in string.ascii_uppercase:
            res = res + coder[ch]
        else:
            res = res + ch
    return res
