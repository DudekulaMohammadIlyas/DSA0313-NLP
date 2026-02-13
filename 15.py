# Represent: TEMPERATURE

# temperature value in Celsius
temperature_celsius = 25

# print temperature in room
print(f"The temperature in the room is {temperature_celsius} degree Celsius.")

# Word representation
word = "temperature"

# Canonical form (standard form)
canonical_form = word.capitalize()

print(f"The canonical form of {word} is {canonical_form}")

# Convert Celsius to Fahrenheit
temperature_fahrenheit = (temperature_celsius * 9/5) + 32
print(f"{temperature_celsius} degree Celsius is equivalent to {temperature_fahrenheit} degree Fahrenheit")


# Function to analyze temperature
def analyze_temperature(temp):
    if temp < 0:
        return "It is freezing!"
    elif 0 <= temp < 20:
        return "It is cool!"
    else:
        return "It is warm!"

# Analyze temperature
analysis = analyze_temperature(temperature_celsius)

print(f"The temperature of {temperature_celsius} degree Celsius: {analysis}")