class Menu:

    def __init__(self):
        self._menu = []

    def add(self, entry):
        self._menu.append(entry)

    def all(self):
        return self._menu
    
    def price_adding_up(self):
        total = 0
        for price in self._menu:
            total += price.price_adding_up()
        return total
    
    
    