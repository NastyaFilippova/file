with open('recipes.txt', 'r', encoding='utf-8') as file:
    def get_cook_list():
        cook_book = {}
        for cook in file:
            cook_name = cook.strip()
            product_count = int(file.readline().strip())

            products_list = []
            for products in range(product_count):
                product = file.readline().split('[]')
                for elements in product:
                    element = elements.split('|')
                    products_dict = {'ingredient_name': element[0], 'quantity': element[1], 'measure': element[2].rstrip()}
                    products_list.append(products_dict)
            file.readline()

            cook_book[cook_name] = products_list
        return cook_book

    # print(get_cook_list())

    def get_shop_list_by_dishes(dishes, person_count):
        cook_book = get_cook_list()
        shop_list_by_dishes = {}
        for dish in dishes:
            dish_recipe = cook_book.get(dish)
            # print(dish_recipe)
            for recipes in dish_recipe:
                # print(recipes)
                # person_count_quantity = int(recipes['quantity']) * int(person_count)
                shop_list_by_dishes[recipes['ingredient_name']] = {'measure': recipes['measure'], 'quantity': int(recipes['quantity']) * int(person_count)}
        return shop_list_by_dishes
    
    print(get_shop_list_by_dishes(['Омлет', 'Запеченный картофель'], '2'))














