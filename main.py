class Soda:
    def __init__(self, tip=None):
        self.tip = tip

    def show_my_drink(self):
        if self.tip:
            print(f"Газировка и {self.tip}")
        else:
            print("Обычная газировка")


soda = Soda()
soda.show_my_drink()