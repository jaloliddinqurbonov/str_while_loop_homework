def main(s):
    """
    A string of numbers is given. Find and return the sum of all odd digits.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a=0
    l=0
    while True:
        if int(s[a])%2==1:
            l+=int(s[a])
        a+=1
        if a==len(s):
            break
    return l
print(main('1313413456898765433245678965342145678654'))