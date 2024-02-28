
# using property decorator

class Rabbit:
    """
    -   @property is equivalent to @age.getter
    -   @age.getter overwrites @property

    @age.getter
    def age(self):
        pass
    """

    @property
    def age(self):
        if not hasattr(self, "Age"):
            self.Age = None
        return self.Age


    @age.setter
    def age(self, value):
        self.Age = value

    @age.deleter
    def age(self):
        del self.Age

rabbit = Rabbit()
print(rabbit.age)

rabbit.age = 14
print(rabbit.age)

del rabbit.age
print(rabbit.age)

print("\n ******** Another Way ******* \n")

# using property keyword

class Rabbit1:

    def get_age(self):
        if not hasattr(self, "Age"):
            self.Age = None
        return self.Age

    def set_age(self, val):
        self.Age = val

    def del_age(self):
        del self.Age

    age = property(get_age, set_age, del_age)


rabbit = Rabbit1()
print(rabbit.age)

rabbit.age = 14
print(rabbit.age)

del rabbit.age
print(rabbit.age)

