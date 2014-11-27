def anagram(a,b):
    if (len(a) == len(b)):
       return sorted(list(a.upper())) == sorted(list(b.upper()))
    else:
       return False
print anagram("heart", "barth")
