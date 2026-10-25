<h1 align="center"> Green-Leaf-Logistics-Staff-Shift-and-Overtime-Tracker</h1>
<h1 align="centre"> _README_ <h1> 
Green Leaf Logistics is a small delivery company operating across Brunei. As the company has  grown, its HR and Payroll teams are struggling to manage staff shift records and weekly pay  calculations. Currently, staff hours are tracked on paper timesheets, causing missing entries and  calculation errors.



## Prerequisites
Download Python3.14 on your pc

# How to run Python IDLE Installation & Execution Guide

Follow these step-by-step instructions to install Python, open the program in IDLE, and run the Green Leaf Logistics tracker.

---

## Step 1: Download & Install Python (with IDLE)

IDLE is included by default with the official Python installer.

1. **Go to the Official Website:** Open your web browser and visit [python.org/downloads](https://python.org).
2. **Download the Installer:** Click the **Download Python 3.x** button (choose the latest stable version available for Windows or macOS).
3. **Run the Installer:** Double-click the downloaded setup file.
4. **Crucial Installation Settings:**
   * **Windows:** Make sure to check the box at the bottom that says **"Add python.exe to PATH"** before clicking **Install Now**.
   * **macOS:** Follow the standard onscreen prompts to finish the package installation.

---

## Step 2: Save Your Program File

1. Create a dedicated folder on your computer named `GreenLeafTracker`.
2. Save your code inside that folder as a Python script file named **`tracker.py`**.

---

## Step 3: Open and Run Code in Python IDLE

Instead of using the Command Prompt or Terminal, you can run the application entirely within Python's graphical interface:

### 1. Open the File in IDLE
* **Windows:** Right-click your `tracker.py` file, hover over **Open with**, and select **IDLE (Python 3.x)**. Alternatively, search for "IDLE" in your Start Menu, open it, click **File > Open**, and select your script.
* **macOS:** Open your **Applications** folder, click the **Python 3.x** folder, and double-click **IDLE**. Once open, go to the top menu and select **File > Open** to open your `tracker.py` script.

### 2. View the Code Window
A new window will open displaying your Python source code code (showing your variables like `standardRate = 25.00` and functions like `calculatePay`).

### 3. Run the Script
* Look at the top menu bar of the IDLE code window and click **Run**.
* Click **Run Module** from the dropdown menu (or simply press the **F5** key on your keyboard).

### 4. Interact with the System
A separate **Python Shell** window will pop up automatically. The Green Leaf Logistics text menu will print on the screen, allowing you to type options `1` through `6` to operate the system.

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
 Member Name                                       | Roll number       | Main components Built
-------------------------------------------------- | ------------------| -------------
Nur Syarifah Syahirah Binti Asmady                 | B20250183         | Enhancement Option B,                                                         |                   |input validation
Dk Nur Majdina Safwanah Bte Pg Shahrin             | B20250183         | Menu,staff record view
Nur Amirah Rashidah Binti Abdullah Mohammad Azlan  | B20250304         | Payroll Calculation
Nur Iwani Taqiah binti Haji Abdul Taif             | B20250214         | ReadMe Markdown, Sort

## Checklist
Core requirements:
- [x] Menu-driven (Add / View current / View summary / Search / Spotlight / Exit)
- [x] Input validation (rejects negative hours, hours over 80, empty names, and non-numeric inputs)
- [x] View current staff records (raw, unsorted in entry order with standard/overtime status)
- [x] Payroll calculation with overtime rule (1.5x beyond 40 hrs: $25.00 standard / $37.50 overtime)
- [x] Manually coded sort (nested loop bubble sort shifting names, hours, and pay synchronously)
- [x] Formatted summary output (total staff, total payroll cost, average hours, and descending
      hours ranking)

Enhancement Task:
Enhancement Task (if attempted):

- [ ] Not attempted
- [x] Search by Name
   - [ ] Option A: Delivery Bonus Calculator
   - [x] Option B: Highest/Lowest Earner Spotlight
   - [ ] Option C: Team Average Compari
