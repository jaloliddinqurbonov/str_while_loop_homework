def main(s):
    """
    A variable of type str is given. Find how many punctuations it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a=0
    l=0
    while True:
        if s[a].isalpha() or s[a].isdecimal():
            l+=1
        a+=1
        if a==len(s):
            break
    return len(s)-l

print(main("nasefnwein4i3i4r3i5t45iuninf34iu34infij,..,.,"))