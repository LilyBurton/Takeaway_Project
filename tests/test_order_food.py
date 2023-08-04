from lib.menu import Menu
from lib.menu_list import Menu_Entry
from lib.order import Order

def test_ordering_food():
        menu = Menu()
        food_price_1 = Menu_Entry("Burger", 5.00)
        food_price_2 = Menu_Entry("Chips", 2.00)
        food_price_3 = Menu_Entry("Fizzy Drink", 2.00)
        menu.add(food_price_1)
        menu.add(food_price_2)
        menu.add(food_price_3)
        order_food = Order(menu)
        assert order_food.order() == ["Burger", "Chips", "Fizzy Drink"]

def test_prices_adding_together():
        menu = Menu()
        food_price_1 = Menu_Entry("Burger", 5)
        food_price_2 = Menu_Entry("Chips", 2)
        food_price_3 = Menu_Entry("Fizzy Drink", 2)
        menu.add(food_price_1)
        menu.add(food_price_2)
        menu.add(food_price_3)
        assert menu.price_adding_up() == 9