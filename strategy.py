from abc import ABC, abstractmethod
from product import *
from menu import *

class Strategy(ABC):
    @abstractmethod
    def doPayment(self, price):
        pass

class Card(Strategy):
    def doPayment(self, price):
        price -= 5/100*price
        return price

class Transfer(Strategy):
    def doPayment(self, price):
        price += 5/100*price
        return price

class Cash(Strategy):
    def doPayment(self, price):
        return price

class Context:
    def __init__(self,strategy):
        self.strategy = strategy
    
    def executeStrategy(self,price):
        return self.strategy.doPayment(price)


# function for payment method using strategy
def paymentMethod(myTshirtList):
    while True:
        paymentOption = input(Menu.paymentMenu())
        match paymentOption:
            case "card"|"1":
                for tshirt in myTshirtList:
                    context = Context(Card())
                    print(f"color: {tshirt.color}, size: {tshirt.size}, fabric: {tshirt.fabric}, final price by using Credit /Debit card: " + "{:.2f}".format(context.executeStrategy(tshirt.price)) + "€")
                break
            case "transfer"|"2":
                for tshirt in myTshirtList:
                    context = Context(Transfer())
                    print(f"color: {tshirt.color}, size: {tshirt.size}, fabric: {tshirt.fabric}, final price by using Money /Bank transfer: " + "{:.2f}".format(context.executeStrategy(tshirt.price)) + "€")
                break
            case "cash"|"3":
                for tshirt in myTshirtList:
                    context = Context(Cash())
                    print(f"color: {tshirt.color}, size: {tshirt.size}, fabric: {tshirt.fabric}, final price by using Cash: " + "{:.2f}".format(context.executeStrategy(tshirt.price)) + "€")
                break
            case "back"|"0":
                break
            case _:
                print(Colors.WARNING + ">> wrong input try again" + Colors.ENDC)
