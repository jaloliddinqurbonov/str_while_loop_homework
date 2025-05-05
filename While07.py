def main(s):
    """
    A string of numbers is given. Find how many even digits there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a=0
    l=0
    while True:
        if int(s[a])%2==0:
            l+=1
        a+=1
        if a==len(s):
            break
    return l