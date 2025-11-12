from animal import Animal
from dog import Dog

if __name__ == "__main__":

    # kitty is an instance of the Animal class
    kitty = Animal("kitty", "feline")
    fido = Dog("Fido", "Canine", "Bulldog")

    print (kitty)
    kitty.speak()

    print (fido)
    fido.speak()

    # Print out all the animals
    print("\nAll traked animals:")
    for animal in Animal.all_animals:
        print(f"  - {animal}")


# List Animal.all_animals
# object animal