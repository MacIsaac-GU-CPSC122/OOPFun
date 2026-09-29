class Animal:
    """
    Base class for an animal
    """

    # class attribute
    # shared as a common value that all instances can access
    DEFAULT_SPECIES = "default species"
    DEFAULT_AGE = 0

    # instance method
    def __init__(self, species:str = DEFAULT_SPECIES, age:int = DEFAULT_AGE) -> None:
        # instance attributes
        # each instance get its own value/copy
        self._species = species
        self._age = age

    def __str__(self) -> str:
        return f"a {self._age}-year old {self._species}"

    def age_increase(self):
        """
        increments the animal age by 1
        """
        self._age += 1

class Pet(Animal):
    """
    Pet class, inherits from Animal
    """
    def __init__(self, name:str, species:str = Animal.DEFAULT_SPECIES, age:int = Animal.DEFAULT_AGE) -> None:
        super().__init__(species, age)
        self._name = name

    # Method overriding
    # Pet provides its own version of the __str__ method inherited from Animal.
    def __str__(self) -> str:
        str_rep = super().__str__()
        str_rep += f" named {self._name}"
        return str_rep

class WildAnimal(Animal):
    """
    WildAnimal class, inherits from Animal
    """
    def __init__(self, ferocious_noise:str = "...", species:str = Animal.DEFAULT_SPECIES, age:int = Animal.DEFAULT_AGE) -> None:
        super().__init__(species, age)
        self._ferocious_noise = ferocious_noise

    def __str__(self) -> str:
        str_rep = super().__str__()
        str_rep += f" that goes {self._ferocious_noise}"
        return str_rep

a1 = Animal()
a2 = Animal("dog", 7)
print(a1)
print(a2)
print(Animal.DEFAULT_SPECIES)

p1 = Pet("mac")
print(p1)
p2 = Pet("remi", "cat", 1)
print(p2)

w1 = WildAnimal()
w2 = WildAnimal("ROARRR", "tiger", 7)
w1.age_increase()
print(w1)
print(w2)


animals: list[Animal] = [
    p1,
    p2,
    w1,
    w2,
    a1,
    a2
]
print("LOOP")
for animal in animals:
    print(animal)

# POLYMORPHISM:
# All of these objects can be treated as Animals because Pet and WildAnimal inherit from Animal.
# The same operation, print(animal), works for every object.
# Dynamic binding:
# When an overridden method is called, Python determines which version of the method to execute at runtime based on the actual object's type.

# Inheritance allows us to treat a Pet as an Animal.
# Overriding gives Pet its own behavior.
# Dynamic binding chooses that behavior at runtime.
# Polymorphism lets the same code work with all of those different objects.





# TODO:Animal Tester Tasks
#
# 1. Create a list called animals that contains:
#    - at least one Animal object
#    - at least two Pet objects
#    - at least two WildAnimal objects
#
# 2. Loop through the animals list and print each animal.
#    - Notice that the same print statement works for Animal, Pet,
#      and WildAnimal objects.
#    - Which __str__() method is called for each object?
#
# 3. Loop through the animals list and call age_increase() on
#    every animal.
#    - age_increase() is defined in Animal.
#    - Pet and WildAnimal inherit this method from Animal.
#
# 4. Loop through the animals list again and print each animal.
#    - Verify that each animal's age increased by 1.
#
# 5. Add a make_noise() method to the Animal class.
#    - Have it return a generic string such as "..."
#
# 6. Override make_noise() in the WildAnimal class.
#    - Have WildAnimal return its _ferocious_noise.
#
# 8. Loop through the animals list and call make_noise()
#    on every animal.
#
# 9. Think about the following:
#    - The loop calls animal.make_noise() the same way every time.
#    - Why can different objects produce different results?
#    - How is this an example of method overriding?
#    - How is this an example of dynamic binding?
#    - How is this an example of polymorphism?