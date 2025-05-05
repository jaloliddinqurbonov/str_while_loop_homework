def main(s):
    """
    A string of numbers is given. Find the sum of all the digits and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a=0
    l=0
    while True:
        l+=int(s[a])
        a+=1
        if a==len(s):
            break
    return l