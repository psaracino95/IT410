favorite_movie = {
    "title": "Kung Pow",
    "rating": "PG-13",
    "director": "Steve Oedekerk",
    "year_released": 2002,
    "genre": "Action Comedy",
    "runtime_minutes": 81
}

product = {
    "item_number": 101,
    "product_name": "Wireless Mouse",
    "price": 25.00
}

# Increase price by 30%
product["price"] *= 1.30

print(f"The price of the {product['product_name']} has been increased by 30%.")

#Looping through the movie dictionary
for key, value in favorite_movie.items():
    print(f"{key}: {value}")


dictionary_list = [
    {"word": "Python", "definition": "A high-level programming language."},
    {"word": "Dictionary", "definition": "A collection of key-value pairs."},
    {"word": "Loop", "definition": "A way to repeat a block of code multiple times."}
]

for item in dictionary_list:
    print(f"Word: {item['word']}")
    print(f"Definition: {item['definition']}\n")

#This adds the list of actors to the dictionary

favorite_movie["actors"] = ["Steve Oedekerk", "Hui Lou Chen", "Elliot Page", "Fei Lung"]

for actor in favorite_movie["actors"]:
    print(actor)
