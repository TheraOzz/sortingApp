from menu import *

# class for parent class Product
class Product:
    @staticmethod
    def colorSet():
        return {
                "RED": (0, 5.0),
                "ORANGE": (1, 5.1),
                "YELLOW": (2, 5.2),
                "GREEN": (3, 5.3),
                "BLUE": (4, 5.4),
                "INDIGO": (5, 5.5),
                "VIOLET": (6, 5.6)
                }

    @staticmethod
    def sizeSet():
        return {
                "XS": (0, 6.0),
                "S": (1, 6.1),
                "M": (2, 6.2),
                "L": (3, 6.3),
                "XL": (4, 6.4),
                "XXL": (5, 6.5),
                "XXXL": (6, 6.6)
                }

    @staticmethod
    def fabricSet():
        return {
                "WOOL": (0, 7.0),
                "COTTON": (1, 7.1),
                "POLYESTER": (2, 7.2),
                "RAYON": (3, 7.3),
                "LINEN": (4, 7.4),
                "CASHMERE": (5, 7.5),
                "SILK": (6, 7.6)
                }

# class for child class T-shirt
class Tshirt(Product):
    def __init__(self, color, size, fabric):
        self.color = color
        self.size = size
        self.fabric = fabric
        self.colors = Product.colorSet()
        self.sizes = Product.sizeSet()
        self.fabrics = Product.fabricSet()
        self.price = self.attributePrice(self.color) + self.attributePrice(self.size) + self.attributePrice(self.fabric)

    def attributePrice(self, attribute):
        if attribute == self.color:
            for k, v in self.colors.items():
                if k in self.color:
                    return v[1]
        elif attribute == self.size:
            for k, v in self.sizes.items():
                if k in self.size:
                    return v[1]
        elif attribute == self.fabric:
            for k, v in self.fabrics.items():
                if k in self.fabric:
                    return v[1]

    def sortBy(self, option):
        if option == 1:
            for k, v in self.colors.items():
                if k == self.color:
                    return v[0]
        elif option == 2:
            for k, v in self.sizes.items():
                if k == self.size:
                    return v[0]
        elif option == 3:
            for k, v in self.fabrics.items():
                if k == self.fabric:
                    return v[0]

    def __str__(self):
        return f"color: {self.color}, size: {self.size}, fabric: {self.fabric}, current price: " + "{:.2f}".format(self.price) + "€"


def createMyTshirt(myTshirtList):
    """function that creates my T-shirt objects"""
    newColor = colorPick()
    newSize = sizePick()
    newFabric = fabricPick()
    newTshirt = Tshirt(newColor, newSize, newFabric)
    myTshirtList.append(newTshirt)
    return myTshirtList


def createRandomTshirts(randomTshirtList):
    """function that creates random T-shirts objects"""
    while True:
        try:
            userNum = int(input("Type a number of random T-Shirts you would like to produce (max 343 combinations) \n"))
            break
        except ValueError:
            print(Colors.WARNING + ">> wrong input try again" + Colors.ENDC)
    counter = 0
    for color in Product.colorSet().keys():
        for size in Product.sizeSet().keys():
            for fabric in Product.fabricSet().keys():
                randomTshirt=Tshirt(color, size, fabric)
                randomTshirtList.append(randomTshirt)
                counter += 1
                if counter == userNum:
                    break
            if counter == userNum:
                break
        if counter == userNum:
            break


def colorPick():
    """function for color pick"""
    while True:
        colorOption = input(Menu.colorMenu())
        match colorOption:
            case "red"|"1":
                color = "RED"
                break
            case "orange"|"2":
                color = "ORANGE"
                break
            case "yellow"|"3":
                color = "YELLOW"
                break
            case "green"|"4":
                color = "GREEN"
                break
            case "blue"|"5":
                color = "BLUE"
                break
            case "indigo"|"6":
                color = "INDIGO"
                break
            case "violet"|"7":
                color = "VIOLET"
                break
            case _:
                print(Colors.WARNING + ">> wrong input try again" + Colors.ENDC)
    print(Colors.OKGREEN + "color added!" + Colors.ENDC)
    return color

def sizePick():
    """function for size pick"""
    while True:
        sizeOption = input(Menu.sizeMenu())
        match sizeOption:
            case "xs"|"1":
                size = "XS"
                break
            case "s"|"2":
                size = "S"
                break
            case "m"|"3":
                size = "M"
                break
            case "l"|"4":
                size = "L"
                break
            case "xl"|"5":
                size = "XL"
                break
            case "xxl"|"6":
                size = "XXL"
                break
            case "xxxl"|"7":
                size = "XXXL"
                break
            case _:
                print(Colors.WARNING + ">> wrong input try again" + Colors.ENDC)
    print(Colors.OKGREEN + "size added!" + Colors.ENDC)
    return size

def fabricPick():
    """function for fabric pick"""
    while True:
        fabricOption = input(Menu.fabricMenu())
        match fabricOption:
            case "wool"|"1":
                fabric = "WOOL"
                break
            case "cotton"|"2":
                fabric = "COTTON"
                break
            case "polyester"|"3":
                fabric = "POLYESTER"
                break
            case "rayon"|"4":
                fabric = "RAYON"
                break
            case "linen"|"5":
                fabric = "LINEN"
                break
            case "cashmere"|"6":
                fabric = "CASHMERE"
                break
            case "silk"|"7":
                fabric = "SILK"
                break
            case _:
                print(Colors.WARNING + ">> wrong input try again" + Colors.ENDC)
    print(Colors.OKGREEN + "fabric added!" + Colors.ENDC)
    return fabric
