class Menu:
    """class for project menus"""
    def startingMenu():
        return (Colors.HEADER + "\n>> STARTING MENU" + 
                Colors.OKBLUE + "\n1. My T-Shirt\
                                 \n2. Random T-Shirts" +
                  Colors.FAIL + "\n0. exit \n" + Colors.ENDC)

    def myTshirtMenu():
        return (Colors.HEADER + "\n>> MY T-SHIRTS" +  
                Colors.OKCYAN + "\n1. Create my T-Shirt\
                                 \n2. Read my T-Shirts\
                                 \n3. Payment Methods" +
                Colors.OKBLUE + "\n0. back to starting menu \n" + Colors.ENDC)

    def randomTshirtMenu():
        return (Colors.HEADER + "\n>> RANDOM T-SHIRTS" +  
                Colors.OKCYAN + "\n1. Create random T-Shirts\
                                 \n2. Sort /Read random T-Shirts\
                                 \n3. Payment Methods" +
                Colors.OKBLUE + "\n0. back to starting menu \n" + Colors.ENDC)

    def colorMenu():
        return (Colors.BOLD + "\n>> PICK A COLOR" +  
                Colors.ENDC + "\n1. Red\
                                \n2. Orange\
                                \n3. Yellow\
                                \n4. Green\
                                \n5. Blue\
                                \n6. Indigo\
                                \n7. Violet \n")

    def sizeMenu():
        return (Colors.BOLD + "\n>> PICK A SIZE" +  
                Colors.ENDC + "\n1. XS\
                                \n2. S\
                                \n3. M\
                                \n4. L\
                                \n5. XL\
                                \n6. XXL\
                                \n7. XXXL \n")

    def fabricMenu():
        return (Colors.BOLD + "\n>> PICK A FABRIC" +  
                Colors.ENDC + "\n1. WOOL\
                                \n2. COTTON\
                                \n3. POLYESTER\
                                \n4. RAYON\
                                \n5. LINEN\
                                \n6. CASHMERE\
                                \n7. SILK \n")

    def sortMenu():
        return (Colors.HEADER + "\n>> SORTING MENU & READ LIST" +  
                Colors.OKCYAN + "\n1. Quick Sort\
                                 \n2. Bubble Sort\
                                 \n3. Bucket Sort\
                                 \n4. Multi Sort\
                                 \n5. Read /View List" +
                Colors.OKBLUE + "\n0. back to random t-shirts menu \n" + Colors.ENDC)

    def quickMenu():
        return (Colors.BOLD + "\n>> QUICK SORT" +  
                Colors.ENDC + "\n1. by Color\
                                \n2. by Size\
                                \n3. by Fabric \n")

    def bubbleMenu():
        return (Colors.BOLD + "\n>> BUBBLE SORT" +  
                Colors.ENDC + "\n1. by Color\
                                \n2. by Size\
                                \n3. by Fabric \n")

    def bucketMenu():
        return (Colors.BOLD + "\n>> BUCKET SORT" +  
                Colors.ENDC + "\n1. by Color\
                                \n2. by Size\
                                \n3. by Fabric \n")


    def ascending_descendingMenu():
        return (Colors.BOLD + "\n>> TYPE OF SORTING" +  
                Colors.ENDC + "\n1. by Ascending\
                                \n2. by Descending \n")
        

    def paymentMenu():
        return (Colors.HEADER + "\n>> CHOOSE PAYMENT METHOD" +  
                Colors.OKCYAN + "\n1. Credit /Debit cards\
                                 \n2. Money /Bank transfer\
                                 \n3. Cash" +
                Colors.WARNING + "\n0. cancel payment \n" + Colors.ENDC)


class Colors:
    """class for colored text"""
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
