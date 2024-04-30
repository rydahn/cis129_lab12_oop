# Jesus Ramos
# 04/29/2024
# Lab 12 OOP
"""This program gets pet name, type, and age and displays it as a formatted string representing a pet object"""

class Pet:
    def __init__(self):
        self._name = ""
        self._type = ""
        self._age = 0
    
    def setName(self, name):
        self._name = name
    
    def setType(self, type):
        self._type = type
    
    def setAge(self, age):
        self._age = age
    
    def getName(self):
        return self._name
    
    def getType(self):
        return self._type
    
    def getAge(self):
        return self._age
    
    def __repr__(self):
        return f"Pet(name='{self._name}', type='{self._type}', age={self._age})"

# main module
def main():
    # Declare input variables
    inputName = ""
    inputType = ""
    inputAge = 0

    # create Pet object
    Animal = Pet()

    # Get values for pet
    inputName = input("Enter a pet name: ")
    Animal.setName(inputName)

    inputType = input("Enter a pet type: ")
    Animal.setType(inputType)

    inputAge = int(input("Enter a pet age: "))
    Animal.setAge(inputAge)

    # Print values for pet
    print("The pet name:", Animal.getName())
    print("The pet type:", Animal.getType())
    print("The pet age:", Animal.getAge())

if __name__ == "__main__":
    main()