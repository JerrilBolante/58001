class Person:

  def __init__(self, std, pre, mid, fin):
    self.__std = std
    self.__pre = pre
    self.__mid = mid
    self.__fin = fin
    self.__gradeavg = round (self.Grade(), 2)
  def display(self):
    print("The Student named", self.__std, "has a term grade of",self.__gradeavg)
  def Grade(self):
    gradeavg=(self.__pre + self.__mid + self.__fin)/3
    return gradeavg

class Std1(Person):
  pass
class Std2(Person):
  pass
class Std3(Person):
  pass



std1 = Std1("student1", 95, 76, 94)
std1.display()
std1 = Std2("student2", 65, 65, 80)
std1.display()
std1 = Std3("student3", 90, 94, 98)
std1.display()
