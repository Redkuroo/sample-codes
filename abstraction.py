from abc import ABC, abstractmethod

# Abstract Base Class (The Blueprint / Contract)
class HoiPoiCapsule(ABC):
    @abstractmethod
    def press_button(self):
        """Every capsule must implement a press_button method."""
        pass

# Concrete Implementation 1: Spaceship Capsule
class SpaceshipCapsule(HoiPoiCapsule):
    def press_button(self):
        # Complex internal logic is hidden from the user
        self.__decompress_spatial_matter()
        self.__ignite_gravity_engine()
        return "🚀 Capsule Corp Spaceship deployed!"

    def __decompress_spatial_matter(self):
        # Hidden background process
        pass

    def __ignite_gravity_engine(self):
        # Hidden background process
        pass

# Concrete Implementation 2: Motorcycle Capsule
class MotorcycleCapsule(HoiPoiCapsule):
    def press_button(self):
        return "🏍️ Capsule Corp Hover-Bike deployed!"

# --- Usage ---
# The user doesn't care HOW matter decompresses; they just press the button.
capsule: HoiPoiCapsule = MotorcycleCapsule()
print(capsule.press_button())  # Output: 🚀 Capsule Corp Spaceship deployed!