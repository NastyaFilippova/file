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

    print(get_cook_list())










