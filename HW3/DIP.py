from abc import ABC, abstractmethod


# Определение модуля высокого уровня (абстракция)

class SwitchableDevice(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


# Реализация низкоуровневых модулей

class LightBulb(SwitchableDevice):
    def turn_on(self):
        print("Light bulb is on")

    def turn_off(self):
        print("Light bulb is off")


class Fan(SwitchableDevice):
    def turn_on(self):
        print("Fan is on")

    def turn_off(self):
        print("Fan is off")


# Модуль высокого уровня

class Switch:
    def __init__(self, device: SwitchableDevice):
        self.device = device

    def turn_on(self):
        self.device.turn_on()

    def turn_off(self):
        self.device.turn_off()


if __name__ == '__main__':
    light_bulb = LightBulb()
    fan = Fan()

    switch1 = Switch(light_bulb)
    switch1.turn_on()
    switch1.turn_off()

    switch2 = Switch(fan)
    switch2.turn_on()
    switch2.turn_off()
