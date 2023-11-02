#2.1
my_str = 'woord'
def is_isogram():
    for i in my_str:
     if my_str.count(i) >1:
         return False
     else:
          return True