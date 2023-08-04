from lib.menu import Menu
from lib.menu_list import Menu_Entry

def test_add_show_list_food_and_prices():
        menu = Menu()
        food_price_1 = Menu_Entry("Burger", 5.00)
        food_price_2 = Menu_Entry("Hot Dog", 4.00)
        food_price_3 = Menu_Entry("Chips", 2.00)
        food_price_4 = Menu_Entry("Fizzy Drink", 2.00)
        food_price_5 = Menu_Entry("Water", 1.00)
        menu.add(food_price_1)
        menu.add(food_price_2)
        menu.add(food_price_3)
        menu.add(food_price_4)
        menu.add(food_price_5)
        assert menu.all() == [food_price_1, food_price_2, food_price_3, food_price_4, food_price_5]