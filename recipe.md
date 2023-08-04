As a customer
So that I can check if I want to order something
I would like to see a list of dishes with prices.

As a customer
So that I can order the meal I want
I would like to be able to select some number of several available dishes.

As a customer
So that I can verify that my order is correct
I would like to see an itemised receipt with a grand total.

class Menu:

    self._menu = []

    def add(self, entry):
        menu.append(list(entry))

    def all():
        return self._menu

    Test!

    def test_add_show_list_food_and_prices():
        menu = Menu()
        food_price_1 = Menu_Entry("Burger", "£5.00")
        food_price_2 = Menu_Entry("Hot Dog", "£4.00")
        food_price_3 = Menu_Entry("Chips", "£2.00")
        food_price_4 = Menu_Entry("Fizzy Drink", "£2.00")
        food_price_5 = Menu_Entry("Water", "£1.00")
        assert menu.all() == [[food_price_1], [food_price_2], [food_price_3], [food_price_4], [food_price_5]]


    



        