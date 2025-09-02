class Device:
    """Base class for all smart devices"""
    def __init__(self, name):
        self.name = name
        self.status = False  # OFF by default

    def turn_on(self):
        self.status = True
        print(f"{self.name} is now ON.")

    def turn_off(self):
        self.status = False
        print(f"{self.name} is now OFF.")

    def get_status(self):
        return f"{self.name} status: {'ON' if self.status else 'OFF'}"


class Light(Device):
    """Smart light that can change brightness"""
    def __init__(self, name, brightness=50):
        super().__init__(name)
        self.brightness = brightness

    def set_brightness(self, value):
        if 0 <= value <= 100:
            self.brightness = value
            print(f"{self.name} brightness set to {self.brightness}%.")
        else:
            print("Brightness must be between 0 and 100.")

    def get_status(self):
        return f"{self.name}: {'ON' if self.status else 'OFF'}, Brightness {self.brightness}%"


class Thermostat(Device):
    """Smart thermostat to control temperature"""
    def __init__(self, name, temperature=22):
        super().__init__(name)
        self.temperature = temperature

    def set_temperature(self, value):
        self.temperature = value
        print(f"{self.name} temperature set to {self.temperature}°C.")

    def get_status(self):
        return f"{self.name}: {'ON' if self.status else 'OFF'}, Temperature {self.temperature}°C"


class SmartHome:
    """Smart home system managing multiple devices"""
    def __init__(self):
        self.devices = []

    def add_device(self, device):
        self.devices.append(device)
        print(f"{device.name} added to Smart Home.")

    def show_all_status(self):
        for device in self.devices:
            print(device.get_status())


# --- Usage Example ---
home = SmartHome()

light1 = Light("Living Room Light")
light2 = Light("Bedroom Light", brightness=70)
thermo = Thermostat("Hall Thermostat", temperature=24)

home.add_device(light1)
home.add_device(light2)
home.add_device(thermo)

light1.turn_on()
light1.set_brightness(80)

thermo.turn_on()
thermo.set_temperature(20)

print("\n--- Current Smart Home Status ---")
home.show_all_status()
