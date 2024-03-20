class person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years and I am {self.gender}")

person1 = person("Suleiman", 28, "male")
person1.introduce()