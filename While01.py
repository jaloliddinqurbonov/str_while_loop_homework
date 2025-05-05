def main(s):
    """
    A variable of type str is given. Find how many digits it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a=0
    l=0
    while True:
        if s[a].isdecimal():
            l+=1
        a+=1
        if a==len(s):
            break
    return l
print(main("salom123"))