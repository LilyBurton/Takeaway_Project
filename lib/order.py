class Order():

    def __init__(self, menu):
        self._menu = menu

    def order(self):
        order = []
        for food in self._menu.all():
            meal = food.food
            order.append(meal)
        return order