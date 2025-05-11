class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenhiet(c):
        return (c * 5/9) + 32
    
celsius = 26
fahrenhiet = TemperatureConverter.celsius_to_fahrenhiet(celsius)
print(f"{celsius} \u00B0C is equal to {fahrenhiet} \u00B0F")

