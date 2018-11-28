def open_cook_book():
    cook_book = {}
    with open('cook_book.txt', encoding='UTF8') as f:
        for line in f:
            dish = line.strip()
            quantity_ingredients = f.readline().strip()
            ingredient_list = []
            ingredient_dish = {}
            for i in range(int(quantity_ingredients)):
                ingredient = f.readline().strip().split(' | ')
                ingredient_dish['ingredient_name'] = ingredient[0]
                ingredient_dish['quantity'] = ingredient[1]
                ingredient_dish['measure'] = ingredient[2]
                ingredient_list.append(ingredient_dish.copy())
                cook_book[dish] = ingredient_list
            f.readline()
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    cook_book = open_cook_book()
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            ingredient_dish = ingredient
            if ingredient_dish['ingredient_name'] not in shop_list:
                shop_list[ingredient_dish['ingredient_name']] = {'measure' : ingredient_dish['measure'], 'quantity' : int(ingredient_dish['quantity']) * person_count}
            else:
                shop_list[ingredient_dish['ingredient_name']]['quantity'] += int(ingredient_dish['quantity']) * person_count
    print(shop_list)


get_shop_list_by_dishes(['Фахитос', 'Омлет'], 4)
