def main(s):
    """
    A variable of type str is given. Find and return how many consonant letters there are.
    Args:
        s: str
        consonant: other than vowels(a, e, i, o, u)
    Returns:
        int: return answer
    """
    d=s.lower()
    a=0
    g=0
    l=['a','e','o','i','u']
    while True:
        if d[a] in l:
            g+=1
        a+=1
        if a==len(d):
            break
    return g
print(main('afajfnaburgfyiuefhakhjauyagryle'))