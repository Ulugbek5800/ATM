class Card:
    password = 1111
    balance = 0

    def __init__(self, bank: str, number: int, expiry: str):
        self.bank = bank
        self.number = number
        self.expiry = expiry

    def show_card_info(self):
        return f"""
bank: {self.bank}
number: {self.number}
expiry date: {self.expiry}
balance: {self.balance}"""

    def change_password(self):
        checkPassword = int(input("Enter your current password: "))
        if checkPassword == self.password:
            self.password = int(input("Enter new password: "))
        else:
            print("Password is wrong.")

    def show_balance(self):
        return self.balance

    def add_money(self, money):
        self.balance += money
        print("Balance:", self.balance)

    def take_money(self, money):
        if self.balance >= money:
            self.balance -= money
        else:
            print("You dont have enought money.")
        print("Balance:", self.balance)


class User:
    cash = 1000

    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
        self.cards = list()

    def show_info(self):
        return f"{self.firstName} {self.lastName}"

    def add_card(self, newCard: Card):
        self.cards.append(newCard)


class ATM(Card):
    bankName = "Asaka"

    def __init__(self, curUser: User):
        self.curUser = curUser

    def show_user_info(self):
        print(self.curUser.show_info())
        print()
        print("Cards: ")
        if self.curUser.cards != []:
            print([i.number for i in self.curUser.cards])
            print("\n".join([i.show_card_info() for i in self.curUser.cards]))
        else:
            print("empty...")

    def takeMoney(self, money):
        super().take_money(money)

    def addMoney(self, money):
        if self.curUser.cash >= money:
            self.curUser.cash -= money
            super().add_money(money)
        else:
            print("You dont have enough cash.")


c1 = Card("Asaka", 860012345, "02/25")

u1 = User("Ulugbek", "Suleymonov")
u1.add_card(c1)

a1 = ATM(u1)
a1.show_user_info()
