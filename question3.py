""""
input - no of students 
output - number of clasess
size of class - 30 
"""
import math

no_of_students= input('what is the number of students?')

def class_number(no_of_students):
   no_of_classes =  float(no_of_students)/ 30 
   no_of_classes = (math.ceil(no_of_classes))
   print(no_of_classes)
   size_of_class = int(no_of_students)/(no_of_classes)
   print(size_of_class)
   if size_of_class % 1 == 0:
     print(size_of_class)
   else:
      frac,whole = math.modf(size_of_class)
      frac = math.floor(frac *10)
      print(frac)
      round_up = frac / 2 
      print(math.ceil(size_of_class) * round_up)
      round_down = no_of_classes - round_up
      print(math.ceil(size_of_class) * round_down)
   return no_of_classes

number_of_classes = class_number(no_of_students)

print('Proposed Allocation: {}'.format(number_of_classes),'classes')
dict =	{
  "Class 1": ,
}
print(dict)
