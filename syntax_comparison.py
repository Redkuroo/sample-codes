Class & Constructor (__init__ vs. Constructor Method)
In Python, the constructor is always named __init__. In Java, the constructor must have the exact same name as the class.

#Python
class Saiyan:
    # Constructor
    def __init__(self, name: str, power_level: int):
        self.name = name            # Public property
        self.power_level = power_level

#Java
        public class Saiyan {
   # 1. Declare instance variables with types
    public String name;
    public int powerLevel;

   #2. Constructor (matches class name exactly)
    public Saiyan(String name, int powerLevel) {
        this.name = name;           # 'this' in Java equals 'self' in Python
        this.powerLevel = powerLevel;
    }
}





Encapsulation (Private Attributes & Getters/Setters)
Python uses double underscores (__) for private variables. Java uses explicit access keywords (private, public, protected).

#Python

class Goku:
    def __init__(self, initial_ki: int):
        self.__ki = initial_ki  # Private attribute

    # Getter
    def get_ki(self) -> int:
        return self.__ki

    # Setter with validation
    def take_damage(self, damage: int):
        self.__ki = max(0, self.__ki - damage)

#Java

public class Goku {
    private int ki; # Explicitly declared private

    public Goku(int initialKi) {
        this.ki = initialKi;
    }

   # Public Getter
    public int getKi() {
        return this.ki;
    }

    # Public Setter with validation
    public void takeDamage(int damage) {
        this.ki = Math.max(0, this.ki - damage);
    }
}





Inheritance & super() Call
Python puts the parent class name in parentheses Class Child(Parent):. Java uses the extends keyword. Both use super() to trigger the parent constructor.


#Python
class HalfSaiyan(Saiyan):
    def __init__(self, name: str, power_level: int, human_parent: str):
        # Call parent constructor
        super().__init__(name, power_level)
        self.human_parent = human_parent

#Java
public class HalfSaiyan extends Saiyan {
    public String humanParent;

    public HalfSaiyan(String name, int powerLevel, String humanParent) {
       # Call parent constructor (must be the first line inside Java constructor)
        super(name, powerLevel);
        this.humanParent = humanParent;
    }
}



Abstraction (Abstract Classes vs. Interfaces)
Python uses the abc library (ABC and @abstractmethod). Java uses either the abstract keyword or dedicated interface types.

#Python
from abc import ABC, abstractmethod

# Abstract Class
class HoiPoiCapsule(ABC):
    @abstractmethod
    def press_button(self) -> str:
        pass

class SpaceshipCapsule(HoiPoiCapsule):
    def press_button(self) -> str:
        return "🚀 Spaceship deployed!"

#Java (using an Interface):
# Interface (Contract)
public interface HoiPoiCapsule {
    String pressButton(); # Abstract method (no body)
}

# Class implementing the contract
public class SpaceshipCapsule implements HoiPoiCapsule {
    @Override
    public String pressButton() {
        return "🚀 Spaceship deployed!";
    }
}

Polymorphism (Method Overriding)
Both languages allow child classes to override a parent method. Java uses the @Override annotation to explicitly check method signatures at compile time.

#Python
class ZFighter:
    def attack(self) -> str:
        return "Base attack!"

class Goku(ZFighter):
    def attack(self) -> str:
        return "💥 Kamehameha!"

# Usage
fighters: list[ZFighter] = [Goku(), ZFighter()]
for f in fighters:
    print(f.attack())

#Java
import java.util.List;

public class ZFighter {
    public String attack() {
        return "Base attack!";
    }
}

public class Goku extends ZFighter {
    @Override # Expresses intent to override parent method
    public String attack() {
        return "💥 Kamehameha!";
    }
}

# Usage in Main method
public class Main {
    public static void main(String[] args) {
        List<ZFighter> roster = List.of(new Goku(), new ZFighter());
        for (ZFighter f : roster) {
            System.out.println(f.attack());
        }
    }
}