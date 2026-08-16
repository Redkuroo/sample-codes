# Parent Class (Superclass)
class Saiyan:
    def __init__(self, name, base_power):
        self.name = name
        self.base_power = base_power
        self.has_tail = True

    def charge_ki(self):
        return f"{self.name} powers up! Power level rises above {self.base_power}!"

# Child Class (Subclass inheriting from Saiyan)
class HalfSaiyan(Saiyan):
    def __init__(self, name, base_power, human_parent):
        # Call the parent class constructor
        super().__init__(name, base_power)
                
        self.human_parent = human_parent
        self.hidden_potential = True

    def unlock_rage(self):
        self.base_power *= 10
        return f"{self.name}'s hybrid rage unlocks! New power: {self.base_power}!"

# Usage
gohan = HalfSaiyan("Gohan", 5000, human_parent="Chi-Chi")

# Inherited from Saiyan
print(gohan.charge_ki())      # "Gohan powers up! Power level rises above 5000!"

# Unique to HalfSaiyan
print(gohan.unlock_rage())   # "Gohan's hybrid rage unlocks! New power: 50000!"