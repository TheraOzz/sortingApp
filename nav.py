from strategy import *
from sort import *
from product import *
from menu import *


# STARTING MENU
def startingMenu():
    while True:
        menuOption = input(Menu.startingMenu())
        match menuOption:
            case "my"|"1":
                myTshirtMenu()
            case "random"|"2":
                randomTshirtsMenu()
            case "exit"|"0":
                break
            case _:
                print(Colors.WARNING + ">> wrong input try again" + Colors.ENDC)

# MY T-SHIRT LIST IN GLOBAL SCOPE
myTshirtList = []

# MY T-SHIRT MENU
def myTshirtMenu():
    while True:
        myTshirtOption = input(Menu.myTshirtMenu())
        match myTshirtOption:
            case "create"|"1":
                createMyTshirt(myTshirtList)
                print(Colors.OKGREEN + "OK MY T-SHIRT IS CREATED!" + Colors.ENDC)
            case "read"|"2":
                readTshirts(myTshirtList)
            case "payment"|"3":
                paymentMethod(myTshirtList)
            case "exit"|"0":
                break
            case _:
                print(Colors.WARNING + ">> wrong input try again" + Colors.ENDC)

# RANDOM T-SHIRTS MENU
def randomTshirtsMenu():
    randomTshirtList = []
    while True:
        randomTshirtOption = input(Menu.randomTshirtMenu())
        match randomTshirtOption:
            case "create"|"1":
                createRandomTshirts(randomTshirtList)
                print(Colors.OKGREEN + "OK RANDOM T-SHIRTS ARE CREATED!" + Colors.ENDC)
            case "sort"|"2":
                sortMenu(randomTshirtList)
            case "payment"|"3":
                paymentMethod(randomTshirtList)
            case "exit"|"0":
                break
            case _:
                print(Colors.WARNING + ">> wrong input try again" + Colors.ENDC)

# SORTING MENU & READ LIST
def sortMenu(randomTshirtList):
    while True:
        sortOption = input(Menu.sortMenu())
        match sortOption:
            case "quick"|"1":
                while True:
                    try:
                        quickOption = int(input(Menu.quickMenu()))
                        ascend_descend = int(input(Menu.ascending_descendingMenu()))
                    except ValueError:
                        print(Colors.WARNING + ">> wrong input try again" + Colors.ENDC)
                        continue
                    if quickOption >= 1 and quickOption <=3 and ascend_descend >= 1 and ascend_descend <= 2:
                        break
                    else:
                        print(Colors.WARNING + ">> wrong input try again" + Colors.ENDC)
                quickSort(0, len(randomTshirtList)-1, randomTshirtList, quickOption)
                if ascend_descend == 2:
                    randomTshirtList.reverse()
                
                print(Colors.OKGREEN + "OK LIST IS SORTED!" + Colors.ENDC)
            case "bubble"|"2":
                while True:
                    try:
                        bubbleOption = int(input(Menu.bubbleMenu()))
                        ascend_descend = int(input(Menu.ascending_descendingMenu()))
                    except ValueError:
                        print(Colors.WARNING + ">> wrong input try again" + Colors.ENDC)
                        continue
                    if bubbleOption >= 1 and bubbleOption <=3 and ascend_descend >= 1 and ascend_descend <= 2:
                        break
                    else:
                        print(Colors.WARNING + ">> wrong input try again" + Colors.ENDC)
                bubbleSort(randomTshirtList, bubbleOption)
                if ascend_descend == 2:
                    randomTshirtList.reverse()
                print(Colors.OKGREEN + "OK LIST IS SORTED!" + Colors.ENDC)
            case "bucket"|"3":
                while True:
                    try:
                        bucketOption = int(input(Menu.bucketMenu()))
                        ascend_descend = int(input(Menu.ascending_descendingMenu()))
                    except ValueError:
                        print(Colors.WARNING + ">> wrong input try again" + Colors.ENDC)
                        continue
                    if bucketOption >= 1 and bucketOption <=3 and ascend_descend >= 1 and ascend_descend <= 2:
                        break
                    else:
                        print(Colors.WARNING + ">> wrong input try again" + Colors.ENDC)
                bucketSort(randomTshirtList, bucketOption)
                if ascend_descend == 2:
                    randomTshirtList.reverse()
                print(Colors.OKGREEN + "OK LIST IS SORTED!" + Colors.ENDC)
            case "multi"|"4":
                while True:
                    try:
                        ascend_descend = int(input(Menu.ascending_descendingMenu()))
                    except ValueError:
                        print(Colors.WARNING + ">> wrong input try again" + Colors.ENDC)
                        continue
                    if ascend_descend >= 1 and ascend_descend <= 2:
                        break
                    else:
                        print(Colors.WARNING + ">> wrong input try again" + Colors.ENDC)
                bubbleSort(randomTshirtList, 3)
                bubbleSort(randomTshirtList, 2)
                bubbleSort(randomTshirtList, 1)
                if ascend_descend == 2:
                    randomTshirtList.reverse()
                print(Colors.OKGREEN + "OK LIST IS SORTED!" + Colors.ENDC)
            case "read"|"5":
                readTshirts(randomTshirtList)
            case "exit"|"0":
                break
            case _:
                print(Colors.WARNING + ">> wrong input try again" + Colors.ENDC)

