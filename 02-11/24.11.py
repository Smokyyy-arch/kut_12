class Temperature:


    ABSOLUTE_ZERO_C = -273.15

    def __init__(self, temperature_celsius: float):

        if temperature_celsius < self.ABSOLUTE_ZERO_C:
            raise ValueError("Температура не може бути нижчою за абсолютний нуль!")
        self.temperature_celsius = temperature_celsius

    def to_fahrenheit(self) -> float:

        return self.temperature_celsius * 9 / 5 + 32

    @classmethod
    def from_fahrenheit(cls, temperature_fahrenheit: float):

        temperature_celsius = (temperature_fahrenheit - 32) * 5 / 9
        return cls(temperature_celsius)

    def __repr__(self):

        return f"Temperature({self.temperature_celsius:.2f}°C)"



try:
    temp_c = Temperature(-50)
    print(temp_c)
    print(temp_c.to_fahrenheit())

    temp_f = Temperature.from_fahrenheit(32)
    print(temp_f)  # Temperature(0.00°C)
except ValueError as e:
    print(e)