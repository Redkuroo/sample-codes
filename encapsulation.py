#----------------------------------------------------Encapsulation--------------------------------------
class Goku:
    def __init__(self, name, initial_ki):
        self.name = name
        # Private variables (cannot be modified directly from outside)
        self.__ki = initial_ki
        self.__max_ki = 10000

    # Public Getter: Controlled read access
    def get_ki(self):
        return self.__ki

def get_max_ki(self):
        return self.__max_ki

    # Public Setter Method: Controlled write access with validation
    def take_damage(self, damage):
        self.__ki = max(0, self.__ki - damage)
        return f"{self.name} took {damage} damage! Remaining Ki: {self.__ki}"

    def charge_ki(self, amount):
        if amount <= 0:
            return "Invalid charge amount!"
        self.__ki = min(self.__max_ki, self.__ki + amount)
        return f"{self.name} charged Ki! Current Ki: {self.__ki}"
# main2.py (Another developer using your class)
#from goku import Goku
# --- Usage ---
goku = Goku("Goku", 5000)

# Direct access fails or is blocked:
 print(goku.__ki) # Raises AttributeError

# Access via controlled public methods:
#print(goku.take_damage(1500))  # Output: Goku took 1500 damage! Remaining Ki: 3500
#print(goku.charge_ki(2000))   # Output: Goku charged Ki! Current Ki: 5500