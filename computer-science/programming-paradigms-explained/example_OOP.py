# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 19:31:58 2023
@author: Pablo Aguirre
GitHub: https://github.com/pabloagn
Website: https://pabloagn.com
Contact: https://pabloagn.com/contact
Part of Blog Article: programming-paradigms-explained
"""

# Abstracting a family of 4
class Family():
    def __init__(self, family_name):
        self.family_name = family_name
        
    def getFamilyName(self):
        return self.family_name
    
    def introduceFamily(self):
        print(f"Hi, we're the {self.family_name}'s.\n")

class Parent(Family):
    def __init__(self, name, age, family_name):
        super().__init__(family_name)
        self.name = name
        self.age = age
        
    def getName(self):
        return self.name
    
    def introduceParent(self):
        print(f"Hi, my name is {self.name} {self.getFamilyName()}. I'm {self.age} years old\n")

class Child(Parent):
    def __init__(self, name, age, family_name, parent1, parent2):
        super().__init__(name, age, family_name)
        self.name = name
        self.age = age
        self.parents = [parent1, parent2]
        
    def introduceChild(self):
        print(f"Sup!, my name is {self.name} {self.family_name}. I'm {self.age} years old.")
        print(f"My parents are {self.parents[0].getName()} and {self.parents[1].getName()}.\n")
    
# Create a family instance
family = Family("Johnson")

# Create 2 parents
parent_1 = Parent("Elena", "29", family.getFamilyName())
parent_2 = Parent("Paul", "32", family.getFamilyName())

# Create 2 children
child_1 = Child("Emma", "13", family.getFamilyName(), parent_1, parent_2)
child_2 = Child("Rowan", "12", family.getFamilyName(), parent_1, parent_2)

# Introduce family
family.introduceFamily()

# Introduce parents
parent_1.introduceParent()
parent_2.introduceParent()

# Introduce children
child_1.introduceChild()
child_2.introduceChild()