pizza_prefs = [{'name': 'sandeep', 'toppings': 'Mushrooms', 'Pizza_type': 'round'},
{'name': 'Lelan', 'toppings': ['Mushrooms'],'Pizza_type': 'round'},
{'name': 'Kyle', 'toppings': ['Mushrooms', 'Pepperoni'],'Pizza_type': 'Square'},
{'name': 'Dan', 'toppings': ['Mushrooms','Olives', 'Garlic'],'Pizza_type': 'Square'}]

# pizza_prefs['name'] = "sandeep"
# pizza_prefs['toppings']="Mushrooms"


for person in pizza_prefs:

        mushrooms_found = False

        if type(person['toppings']) is str:
                if(person['toppings'])=="Mushrooms":
                        mushrooms_found= True
        elif type(person['toppings']) is list:
                if("Mushrooms" in person['toppings']):
                        mushrooms_found=True

        if mushrooms_found:
                pizza_prefs.remove(person)


print(pizza_prefs)

