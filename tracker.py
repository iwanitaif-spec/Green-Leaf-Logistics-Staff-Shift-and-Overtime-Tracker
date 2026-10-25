
standardRate = 25.00
overtimeRate = 37.50
maxWeeklyHours = 80
maxStaff = 100


def calculatePay(hours):
    if hours <= 40:
        pay = hours * standardRate
    else:
        pay = (40 * standardRate) + ((hours - 40) * overtimeRate)

    return (pay)


def addStaff(staffNames, staffHours, staffPay, staffCounter):
    name = input("\nEnter staff name (or 'end' to finish): ")

    while name != "end" and staffCounter < maxStaff:

        if name == "":
            print("Error: Staff name cannot be empty.")
            name = input("\nEnter staff name (or 'end' to finish): ")
            continue

        hoursText = input("Enter hours worked: ")

        validHours = 0

        while validHours == 0:
            digitCount = 0
            dotCount = 0
            validHours = 1

            for character in hoursText:
                if character >= "0" and character <= "9":
                    digitCount = digitCount + 1
                    continue

                elif character == ".":
                    dotCount = dotCount + 1
                    continue

                else:
                    validHours = 0
                    break

            if digitCount == 0 or dotCount > 1:
                validHours = 0

            if validHours == 1:
                hours = float(hoursText)

                if hours <= 0 or hours > maxWeeklyHours:
                    validHours = 0

            if validHours == 0:
                print("Invalid hours. Enter a number greater than 0 and not more than 80.")
                hoursText = input("\nEnter hours worked: ")

        hours = float(hoursText)
        pay = calculatePay(hours)

        staffNames[staffCounter] = name
        staffHours[staffCounter] = hours
        staffPay[staffCounter] = pay

        staffCounter = staffCounter + 1

        print("Staff record added successfully.")

        if staffCounter == maxStaff:
            print("Maximum number of staff records reached.")
            break

        name = input("\nEnter staff name (or 'end' to finish): ")

    return (staffCounter)


def viewStaff(staffNames, staffHours, staffPay, staffCounter):
    if staffCounter == 0:
        print("No staff records available.")
    else:
        print("\nCURRENT STAFF RECORDS (in entry order)")
        print("----------------------------------------")

        for a in range(staffCounter):
            print("Name:", staffNames[a])
            print("Hours worked:", staffHours[a])
            print("Pay: $", format(staffPay[a], ".2f"))

            if staffHours[a] <= 40:
                print("Status: Standard hours")
            else:
                print("Status: Overtime")

            print("----------------------------------------")


def sortStaffByHours(rankedNames, rankedHours, rankedPay, staffCounter):
    for a in range(staffCounter - 1):
        for position in range(staffCounter - 1 - a):

            if rankedHours[position] < rankedHours[position + 1]:

                temporary = rankedNames[position]
                rankedNames[position] = rankedNames[position + 1]
                rankedNames[position + 1] = temporary

                temporary = rankedHours[position]
                rankedHours[position] = rankedHours[position + 1]
                rankedHours[position + 1] = temporary

                temporary = rankedPay[position]
                rankedPay[position] = rankedPay[position + 1]
                rankedPay[position + 1] = temporary


def viewSummary(staffNames, staffHours, staffPay, staffCounter):
    if staffCounter == 0:
        print("No staff records available.")
    else:
        totalPayroll = 0
        totalHours = 0

        for a in range(staffCounter):
            totalPayroll = totalPayroll + staffPay[a]
            totalHours = totalHours + staffHours[a]

        averageHours = totalHours / staffCounter

        rankedNames = [""] * maxStaff
        rankedHours = [0] * maxStaff
        rankedPay = [0] * maxStaff

        for a in range(staffCounter):
            rankedNames[a] = staffNames[a]
            rankedHours[a] = staffHours[a]
            rankedPay[a] = staffPay[a]

        sortStaffByHours(rankedNames, rankedHours, rankedPay, staffCounter)

        print("\nWEEKLY SUMMARY")
        print("----------------------------------------")
        print("Total staff recorded:", staffCounter)
        print("Total payroll cost: $", format(totalPayroll, ".2f"))
        print("Average hours worked:", format(averageHours, ".2f"))

        print("\nHOURS RANKING (Highest to Lowest)")
        print("----------------------------------------")

        for a in range(staffCounter):
            print("Rank:", a + 1)
            print("Name:", rankedNames[a])
            print("Hours worked:", rankedHours[a])
            print("Pay: $", format(rankedPay[a], ".2f"))
            print("----------------------------------------")


def searchStaff(staffNames, staffHours, staffPay, staffCounter):
    if staffCounter == 0:
        print("No staff records available.")
    else:
        name = input("\nEnter staff name to search: ")
        found = 0

        while found == 0 and name != "end":
            for a in range(staffCounter):
                if staffNames[a] == name:
                    print("\nStaff member found!")
                    print("Name:", staffNames[a])
                    print("Hours worked:", staffHours[a])
                    print("Pay: $", format(staffPay[a], ".2f"))
                    found = 1
                    break

            if found == 0:
                print("Staff member not found.")
                name = input("Enter staff name to search again (or 'end' to return to menu): ")

        if name == "end":
            print("Returning to main menu.")


def earnerSpotlight(staffNames, staffPay, staffCounter):
    if staffCounter == 0:
        print("No staff records available.")
    else:
        highestPay = staffPay[0]
        lowestPay = staffPay[0]

        for a in range(1, staffCounter):
            if staffPay[a] > highestPay:
                highestPay = staffPay[a]

            if staffPay[a] < lowestPay:
                lowestPay = staffPay[a]

        print("\nHIGHEST AND LOWEST EARNER SPOTLIGHT")
        print("----------------------------------------")

        print("Highest earner(s):")
        for a in range(staffCounter):
            if staffPay[a] == highestPay:
                print("Name:", staffNames[a])
                print("Pay: $", format(staffPay[a], ".2f"))

        print("----------------------------------------")
        print("Lowest earner(s):")
        for a in range(staffCounter):
            if staffPay[a] == lowestPay:
                print("Name:", staffNames[a])
                print("Pay: $", format(staffPay[a], ".2f"))

        print("----------------------------------------")


staffNames = [""] * maxStaff
staffHours = [0] * maxStaff
staffPay = [0] * maxStaff

staffCounter = 0
choice = ""

while choice != "6":
    print("\nGREEN LEAF LOGISTICS")
    print("1. Add staff records")
    print("2. View staff records")
    print("3. View payroll summary and ranking")
    print("4. Search staff by name")
    print("5. Highest/lowest earner spotlight")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        staffCounter = addStaff(
            staffNames, staffHours, staffPay, staffCounter
        )

    elif choice == "2":
        viewStaff(staffNames, staffHours, staffPay, staffCounter)

    elif choice == "3":
        viewSummary(staffNames, staffHours, staffPay, staffCounter)

    elif choice == "4":
        searchStaff(staffNames, staffHours, staffPay, staffCounter)

    elif choice == "5":
        earnerSpotlight(staffNames, staffPay, staffCounter)

    elif choice == "6":
        print("Thank you for using Green Leaf Logistics.")

    else:
        print("Invalid choice. Please enter 1, 2, 3, 4, 5 or 6.")

