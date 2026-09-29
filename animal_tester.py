


# POLYMORPHISM:
# All of these objects can be treated as Animals because Pet and
# WildAnimal inherit from Animal.
# The same operation, print(animal), works for every object.

# Dynamic binding:
# When an overridden method is called, Python determines which
# version of the method to execute at runtime based on the
# actual object's type.

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