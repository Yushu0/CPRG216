class facility():
    def __init__(self):
        self.txt=[]
        with open("facilities.txt", "r") as file:
            lines=file.readlines()
            for line in lines:
                self.txt.append(line.split("\n")[0])

    def addFacility(self,name):
        self.txt.append(name)


    def displayFacilities(self):
        for name in self.txt:
            print(name)

    def writeListOffacilitiesToFile(self):
        with open("facilities.txt", "w") as file:
            for name in self.txt:
                file.write(name+"\n")

def printwelcome():
    print("Welcome to Alberta Hospital (AH) Managment system Select from the following options, or select 0 to stop: ")
    print("1-   Doctors")
    print("2-   Facilities")
    print("3-   Laboratories")
    print("4-   Patients")

def printMenu():
    print("Facilities Menu:")
    print("1 - Display Facilities list")
    print("2 - Add Facility")
    print("3 - Back to the Main Menu")



if __name__ == "__main__":
    op=facility()
    while True:        
        printwelcome()
        choose = input()
        if choose == "1":
            pass
        elif choose == "2":
            while True:
                printMenu()               
                choose2 = input()
                if choose2 == "1":
                    op.displayFacilities()
                elif choose2 == "2":
                    name = input("Enter Facility name:\n")
                    op.addFacility(name)
                    op.writeListOffacilitiesToFile()
                elif choose2 == "3":
                    break
        elif choose == "3":
            pass
        elif choose == "4":
            pass