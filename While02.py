def main(s):
    """
    A variable of type str is given. Find how many letters it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a=0
    l=0
    while True:
        if s[a].isalpha():
            l+=1
        a+=1
        if a==len(s):
            break
    return l