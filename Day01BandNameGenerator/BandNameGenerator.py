
print("Welcome to the Band Name Generator App!")
city_name = input("What is the city you grew up? ")
pet_name = input(f"What is your pet name? ")
def band_name_generator(city, pet):
    band_name = f"Your band name: {city} {pet}".title()
    return band_name
band_name = band_name_generator(city_name, pet_name)
print(band_name)

