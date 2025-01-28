import random

class Student:
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("Type a name.")
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} is from house {self.house}"
    
    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        patronus = input("Patronus: ")
        return cls(name, house, patronus)

    @property
    def house(self):
        return self._house
    
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House")
        self._house = house

    def charm(self):
        match self.patronus:
            case "Stag":
                return "🦌"
            case "Otter":
                return "🦦"
            case "Jack Russell terrier":
                return "🐶"
            case _:
                return "🪄"

def main():
    student = Student.get()
    print("Expecto patronum!")
    print(student.charm())

# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     patronus = input("Patronus: ")
#     return Student(name, house, patronus)
     

if __name__ == "__main__":
    main()

class Hat:
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(cls, name):
        print(f"{name} is in {random.choice(cls.houses)}")

Hat.sort("Harry")