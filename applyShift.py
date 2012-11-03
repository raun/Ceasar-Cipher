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
def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    return applyCoder(text,buildCoder(shift))
