def any_lowercase(s):
     for c in s:
          if c.islower():
               return True
     return False
print(any_lowercase("CAT"))