# Hospital Patient Management System

## 1. Project Overview

The **Hospital Patient Management System** is a beginner-friendly Python
console application designed to manage basic hospital patient records.

The application allows the user to:

-   Add a new patient
-   View all patient records
-   Search for a patient using Patient ID
-   Delete a patient record
-   Exit the application

This project is suitable as a **BTech CSE Health Informatics**
mini-project because it demonstrates basic programming concepts in a
healthcare-related context.

------------------------------------------------------------------------

## 2. Technologies Used

-   **Programming Language:** Python 3
-   **Interface:** Command-line / Terminal
-   **Data Storage:** Python list and dictionaries
-   **External Libraries:** None

The project uses only Python's built-in features, so no third-party
packages are required.

------------------------------------------------------------------------

## 3. Project Structure

The project should have the following structure:

``` text
Hospital-Patient-Management/
│
├── README.md
└── hospital_patient_management.py
```

-   `README.md` --- Project documentation and setup instructions.
-   `hospital_patient_management.py` --- Main Python program.

------------------------------------------------------------------------

## 4. Prerequisites

Before running the project, make sure Python 3 is installed on your
computer.

### Check whether Python is installed

Open **Command Prompt / PowerShell / Terminal** and run:

``` bash
python --version
```

If that does not work on Windows, try:

``` bash
py --version
```

You should see a Python 3 version, for example:

``` text
Python 3.x.x
```

If Python is not installed, download Python 3 from the official Python
website and install it.

During Windows installation, enable the option:

``` text
Add Python to PATH
```

------------------------------------------------------------------------

## 5. Set Up the Project

### Step 1: Create the project folder

Create a folder named:

``` text
Hospital-Patient-Management
```

Place the following files inside it:

``` text
Hospital-Patient-Management/
├── README.md
└── hospital_patient_management.py
```

### Step 2: Add the Python code

Save the Hospital Patient Management System code in:

``` text
hospital_patient_management.py
```

Make sure the file extension is `.py` and not `.txt`.

------------------------------------------------------------------------

## 6. Environment Setup

A virtual environment is optional because this project does not use
external packages. However, using one is a good development practice.

### Windows

Open Command Prompt or PowerShell inside the project folder and run:

``` bash
python -m venv venv
```

Activate the environment:

**Command Prompt:**

``` bash
venv\Scripts\activate
```

**PowerShell:**

``` powershell
venv\Scripts\Activate.ps1
```

### macOS / Linux

Create the virtual environment:

``` bash
python3 -m venv venv
```

Activate it:

``` bash
source venv/bin/activate
```

------------------------------------------------------------------------

## 7. Dependency Installation

This project has **no external dependencies**.

Therefore, there is no `pip install` command required.

If a virtual environment was created, Python's standard library is
already available inside it.

You can verify Python and pip with:

``` bash
python --version
pip --version
```

------------------------------------------------------------------------

## 8. Configuration

No configuration file, API key, database server, or environment
variables are required.

The current version stores patient records temporarily in memory using a
Python list.

### Important

Patient records are **not permanently saved**. When the program is
closed, the records entered during that session are lost.

------------------------------------------------------------------------

## 9. Running the Project

Open a terminal in the project directory.

### Windows

Run:

``` bash
python hospital_patient_management.py
```

If your system uses the `py` command:

``` bash
py hospital_patient_management.py
```

### macOS / Linux

Run:

``` bash
python3 hospital_patient_management.py
```

------------------------------------------------------------------------

## 10. Using the Application

After starting the program, the following menu will appear:

``` text
==============================
 HOSPITAL PATIENT MANAGEMENT
==============================
1. Add Patient
2. View All Patients
3. Search Patient
4. Delete Patient
5. Exit

Enter your choice:
```

### Option 1 --- Add Patient

Select:

``` text
1
```

The program will ask for:

-   Patient ID
-   Patient Name
-   Age
-   Gender
-   Disease/Condition
-   Doctor Name

Example:

``` text
Enter Patient ID: P101
Enter Patient Name: Rahul
Enter Age: 25
Enter Gender: Male
Enter Disease/Condition: Fever
Enter Doctor Name: Dr. Sharma
```

The patient record will then be added to the current session.

### Option 2 --- View All Patients

Select:

``` text
2
```

The program displays all patient records currently stored in memory.

### Option 3 --- Search Patient

Select:

``` text
3
```

Enter the Patient ID.

For example:

``` text
Enter Patient ID: P101
```

If the ID exists, the patient's details will be displayed.

### Option 4 --- Delete Patient

Select:

``` text
4
```

Enter the Patient ID of the record that should be removed.

### Option 5 --- Exit

Select:

``` text
5
```

The application will close.

------------------------------------------------------------------------

## 11. Example Workflow

A typical session can be:

``` text
1. Add Patient
   ↓
2. View All Patients
   ↓
3. Search Patient
   ↓
4. Delete Patient
   ↓
5. Exit
```

------------------------------------------------------------------------

## 12. Features

### Patient Registration

Stores basic patient information such as ID, name, age, gender,
condition, and doctor.

### Patient Record Viewing

Displays all patients currently registered during the session.

### Patient Search

Searches for a patient using their unique Patient ID.

### Patient Deletion

Removes an existing patient record using Patient ID.

### Menu-Driven Interface

Provides a simple and easy-to-use command-line menu.

------------------------------------------------------------------------

## 13. Concepts Demonstrated

This project demonstrates several fundamental Python concepts:

-   Variables
-   User input
-   Data types
-   Lists
-   Dictionaries
-   Functions
-   `if-elif-else` statements
-   `for` loops
-   `while` loops
-   Searching
-   Adding and removing list elements
-   Menu-driven programming

------------------------------------------------------------------------

## 14. Limitations

The current version is intentionally simple and has some limitations:

1.  Patient data is stored only in memory.
2.  Data is lost when the program terminates.
3.  There is no login or authentication system.
4.  There is no permanent database.
5.  There is no graphical user interface.
6.  The application is intended for educational purposes and is not
    suitable for handling real patient data.

------------------------------------------------------------------------

## 15. Possible Future Improvements

The project can be expanded by adding:

-   SQLite or MySQL database integration
-   Permanent patient record storage
-   Patient appointment management
-   Doctor management
-   Hospital billing
-   Prescription records
-   Patient medical history
-   Tkinter graphical user interface
-   Login and role-based access
-   Data validation
-   Report generation
-   CSV/PDF export
-   Dashboard and statistics

These improvements could turn the basic project into a more complete
**Health Information Management System**.

------------------------------------------------------------------------

## 16. Privacy and Security Note

This project is intended for **academic and demonstration purposes
only**.

Do not enter real patients' personally identifiable information, medical
information, or other sensitive healthcare data into this application.

A real healthcare information system would require appropriate security,
authentication, authorization, encryption, auditing, backups, and
compliance with applicable healthcare and data-protection requirements.

------------------------------------------------------------------------

## 17. Troubleshooting

### Error: `python is not recognized`

Python may not be installed or may not be added to the system PATH.

Try:

``` bash
py --version
```

If that also fails, install Python 3 and ensure that Python is added to
PATH.

### Error: `can't open file`

Make sure the terminal is opened inside the project folder and that the
filename is exactly:

``` text
hospital_patient_management.py
```

You can check the files in the current directory with:

**Windows:**

``` bash
dir
```

**macOS / Linux:**

``` bash
ls
```

### Program closes immediately

Run the program from a terminal instead of double-clicking the `.py`
file:

``` bash
python hospital_patient_management.py
```

------------------------------------------------------------------------

## 18. Project Purpose

The purpose of this project is to demonstrate how basic Python
programming can be applied to a simple healthcare information-management
problem.

It provides a foundation for developing more advanced Health Informatics
applications involving databases, data analysis, healthcare workflows,
and secure patient information management.

------------------------------------------------------------------------

## 19. Author

**Project:** Hospital Patient Management System\
**Course:** BTech CSE -- Health Informatics\
**Language:** Python
