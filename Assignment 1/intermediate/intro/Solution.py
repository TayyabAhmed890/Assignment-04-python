# Planetary Weight Calculator

# Dictionary containing gravity factors for each planet relative to Earth
gravity_factors = {
    "Mercury": 0.376,
    "Venus": 0.889,
    "Mars": 0.378,
    "Jupiter": 2.36,
    "Saturn": 1.081,
    "Uranus": 0.815,
    "Neptune": 1.14
}

# Ask user for their weight on Earth
earth_weight = float(input("Enter a weight on Earth: "))

# Ask user for a planet name
planet = input("Enter a planet (e.g., Mars, Jupiter): ")

# Check if the planet is valid
if planet in gravity_factors:
    # Calculate equivalent weight
    planetary_weight = earth_weight * gravity_factors[planet]
    # Print rounded result
    print(f"The equivalent weight on {planet}: {round(planetary_weight, 2)}")
else:
    print("Invalid planet name. Please enter a valid planet with the first letter capitalized.")
