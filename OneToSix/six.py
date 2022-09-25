
def createList():
   myList = []
   return myList

def fillList(myList):
    try:
        number = int(input("Please enter a price, 0 to end: "))
        while number != 0:
            myList.append(number)
            number = int(input("Please enter a price, 0 to end: "))

    except:
        print("That's not a number")
        pass


def printList(myList):
        print(' + '.join(map(str, myList)), end = ' = \n')
        print("Total cost : ", sum(myList))
        #print("Highest price : ", max(myList))
        #print("Lowest price : ", min(myList))

def main():
    myList = createList()
    fillList(myList)
    printList(myList)

main()

