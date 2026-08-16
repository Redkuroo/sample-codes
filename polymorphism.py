# Base Class
class ZFighter:
    def attack(self):
        raise NotImplementedError("Subclasses must implement attack()")

# Polymorphic Classes
class Goku(ZFighter):
    def attack(self):
        return "Goku fires a Kamehameha! 💥"

class Vegeta(ZFighter):
    def attack(self):
        return "Vegeta launches a Final Flash! ⚡"

class Krillin(ZFighter):
    def attack(self):
        return "Krillin throws a Destructo Disc! 🟡"

# Polymorphism in Action
roster: list[ZFighter] = [Goku(), Vegeta(), Krillin()]

# Calling the exact same method on different objects triggers distinct behaviors
for fighter in roster:
    print(fighter.attack())

# Output:
# Goku fires a Kamehameha! 💥
# Vegeta launches a Final Flash! ⚡
# Krillin throws a Destructo Disc! 🟡