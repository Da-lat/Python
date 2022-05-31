import random

main = ['Bean burger', 'Sausage', 'No beef burger', 'No chicken burger']
carb = ['Mash', 'Rice', 'Pasta', 'Brown rice']
fibre = ['Beans', 'Spaghetti hoops', 'Mixed veg', 'Peas']

def choose_food(main, carb, fibre):
    main1 = random.choice(main)
    carb1 = random.choice(carb)
    fibre1 = random.choice(fibre)
    return main1, carb1, fibre1


print(choose_food(main, carb, fibre))
