<h1 align="center"> Green-Leaf-Logistics-Staff-Shift-and-Overtime-Tracker</h1>

Green Leaf Logistics is a small delivery company operating across Brunei. As the company has  grown, its HR and Payroll teams are struggling to manage staff shift records and weekly pay  calculations. Currently, staff hours are tracked on paper timesheets, causing missing entries and  calculation errors.

## Prerequisites
Download Python3.14 on your pc


## How to run the program

### Step 1: Select an Action
Enter the number corresponding to your desired task and press `Enter`:
* `1` - Add staff records
* `2` - View staff records
* `3` - View payroll summary and ranking
* `4` - Exit

### Step 2: Data Input Guide
When selecting option **1 (Add staff records)**, the program will prompt you sequentially for employee details. 
* **Required Inputs:** You will be prompted to enter the Employee Name, Regular Hours Worked, and Overtime Hours Worked.
* **Continuous Entry:** The program will loop to allow multiple entries. Type `end` when you are finished inputting all staff information to return to the main menu.

### Step 3: Closing the Application
Always choose option **4** from the main menu to properly stop the terminal execution loop and safely exit the code.
 keep entering to add more staff and type end when all staff information are entered

## Group info
 Member Name                                       | Roll number       | Program Area
-------------------------------------------------- | ------------------| -------------
Nur Syarifah Syahirah Binti Asmady                 | B20250183         | Bachelor of Business (Honours) Major in Marketing Information Systems
Dk Nur Majdina Safwanah Bte Pg Shahrin             | B20250183         | Bachelor of Business (Honours) Major in Marketing Information Systems
Nur Amirah Rashidah Binti Abdullah Mohammad Azlan  | B20250304         | Bachelor of Business (Honours) Major in Marketing Information Systems
Nur Iwani Taqiah binti Haji Abdul Taif             | B20250214         | Bachelor of Business (Honours) Major in Marketing Information Systems


## Team Roles Table
Member Name   | Role
------------- | -------------
Dina          | role
Mira          | role
Syar          | role
Iwani         | role

## Checklist
Menu-driven (Add / View current / View summary / Search / Spotlight / Exit)

- [x] Input validation (rejects negative hours, hours over 80, empty names, and non-numeric inputs)
- [x] View current staff records (raw, unsorted in entry order with standard/overtime status)
- [x] Payroll calculation with overtime rule (1.5x beyond 40 hrs: $25.00 standard / $37.50 overtime)
- [x] Manually coded sort (nested loop bubble sort shifting names, hours, and pay synchronously)
- [x] Formatted summary output (total staff, total payroll cost, average hours, and descending hours ranking)
