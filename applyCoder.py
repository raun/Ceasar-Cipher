import string
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
