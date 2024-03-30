class House:
    def __init__(self, area, price):
        self.area = area
        self.price = price
    def _area(self):
        print(f"House area: {self.area}")
    def _price(self):
        print (f"House price without discount: {self.price}")
    def final_price(self, discount):
        final_price = self.price * (100 - discount) / 100
        print(f"Final price: {final_price}")
        return final_price


class Human:

    def_name = 'name'
    def_age = 30

    def __init__(self, name=def_name, age=def_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None

    def get_name(self):
        print(f"Name: {self.name}")

    def get_age(self):
        print(f"Age: {self.age}")

    def get_money(self):
        print(f"Money: {self.__money}")

    def get_house(self):
        print(f"House: {self.__house}")

    def info(self):
        self.get_name()
        self.get_age()
        self.get_money()
        self.get_house()

    @staticmethod
    def def_info():
        print(f'Default name: {Human.def_name}')
        print(f'Default age: {Human.def_age}')

    def __make_deal(self, house, result_cost):
        self.__money -= result_cost
        self.__house = house
        print("Deal completed!")

    def earn_money(self, add_money):
        self.__money += add_money

    def buy_house(self, house, discount):
        result_cost = house.final_price(discount)
        if result_cost > self.__money:
            print("Not enough money")
        else:
            self.__make_deal(house, result_cost)


class SmallHouse(House):
    def_area = 40
    def __init__(self, price):
        super().__init__(SmallHouse.def_area, price)



Human.def_info()
human = Human('Nikolai', 25)
human.info()
smallhouse = SmallHouse(200)
human.buy_house(smallhouse, 10)
human.earn_money(500)
human.buy_house(smallhouse, 10)