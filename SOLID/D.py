# Step 1: Create an ABSTRACTION (interface)

# "High-level code should not depend on low-level code. Both should depend on ABSTRACTIONS (interfaces)."

# "Biror narsaga (klassga) kerak bo'lgan qismlarni (obyektlarni) ichkarida yasamang, balki tashqaridan bering!

class Switchable:
    def turn_on(self):
        pass

    def turn_off(self):
        pass


# Step 2: Low-level classes implement the abstraction
class LightBulb(Switchable):
    def turn_on(self):
        return "Light bulb is ON"

    def turn_off(self):
        return "Light bulb is OFF"


class Fan(Switchable):
    def turn_on(self):
        return "Fan is spinning"

    def turn_off(self):
        return "Fan is stopped"


class AirConditioner(Switchable):
    def turn_on(self):
        return "AC is cooling"

    def turn_off(self):
        return "AC is off"


# Step 3: High-level class depends on ABSTRACTION (not a specific thing)
class Switch:
    def __init__(self, device: Switchable):
        # ✅ GOOD: Switch accepts ANYTHING that is "Switchable"
        self.device = device

    def operate(self):
        self.device.turn_on()


# Step 4: Use it with ANY device!
bulb = LightBulb()
fan = Fan()
ac = AirConditioner()

switch1 = Switch(bulb)  # Controls bulb
switch2 = Switch(fan)  # Controls fan
switch3 = Switch(ac)  # Controls AC

switch1.operate()  # "Light bulb is ON"
switch2.operate()  # "Fan is spinning"
switch3.operate()  # "AC is cooling"