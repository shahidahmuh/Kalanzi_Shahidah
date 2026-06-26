import csv
import json
import logging
import os

#LOGGING
logging.basicConfig(
    filename="student_system.log",
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)

#CUSTOM EXCEPTION
class StudentNotFoundError(Exception):
    #when a student cannot be found.
    pass

CSV_FILE = "students.csv"
JSON_FILE = "students.json"

#CREATE FILES 
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Registration Number", "Name"])

if not os.path.exists(JSON_FILE):
    with open(JSON_FILE, "w") as file:
        json.dump({}, file, indent=4)

#LOAD JSON
def load_json():
    with open(JSON_FILE, "r")as file:
        return json.load(file)
    
#SAVE JSON
def save_json(data):
    with open(JSON_FILE, "w") as file:
        json.dump(data, file, indent=4)

#ADD STUDENT
def add_student():
    try:
        reg = input("Registration Number: ")
        name = input("Student Name: ")
        address = input("Address: ")
        contact = input("Contact: ")
        program = input("Prgram: ")

        #save to a CSV 
        with open(CSV_FILE, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([reg, name])

        #Save to JSON
        students = load_json()

        students[reg] = {
            "name": name,
            "address": address,
            "contact": contact,
            "program": program
        }

        save_json(students)
        print("Student added successfully!!")
        logging.info(f"Added student {reg}")
        
    except Exception as e:
        logging.error(e)
        print("Error adding student.")
    finally:
        print()

#VIEW STUDENTS
def view_students():

    try:
        with open(CSV_FILE, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
        
        logging.info("Viewed students.")

    except Exception as e:
        logging.error(e)
    finally:
        print()

#SEARCH
def search_student():
    try:
        reg = input("Enter registration number: ")
        students = load_json()

        if reg not in students:
            raise StudentNotFoundError("Student not found.")
        print()
        print("Student Details")
        print("Registration: ", reg)

        for key, value in students[reg].items():
            print(key.capitalize(), ":", value)
        logging.info(f"Searched {reg}")

    except StudentNotFoundError as e:
        print(e)
        logging.error(e)
    finally:
        print()

#UPDATE
def update_student():
    try:
        reg = input("Registration Number: ")

        students = load_json()

        if reg not in students:
            raise StudentNotFoundError("Student does not exist.")
        
        students[reg]["address"] = input("New Address: ")
        students[reg]["contact"] = input("New Contact: ")
        students[reg]["program"] = input("New Program: ")

        save_json(students)
        print("Student updated successfully.")

        logging.info(f"Updated {reg}")

    except StudentNotFoundError as e:
        print(e)

        logging.error(e)
    finally:
        print()

#DELETE
def delete_student():

    try:
        reg = input("Registration Number: ")
        students = load_json()

        if reg not in students:
            raise StudentNotFoundError("Student not found.")
        
        del students[reg]
        save_json(students)

        #update csv

        rows = []
        with open(CSV_FILE, "r") as file:
            reader = csv.reader(file)

            for row in reader:
                if len(row) > 0 and row[0] != reg:
                    rows.append(row)
        with open(CSV_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        print("Student deleted successfully.")

        logging.info(f"Deleted {reg}")
    except StudentNotFoundError as e:
        print(e)
        logging.error(e)
    finally:
        print()

#MENU
while True:
    print("STUDENT MANAGEMENT SYSTEM")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        add_student()
    elif choice  == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print('GoodBye!!!')
        logging.info("Program exited")
        break
    else:
        print("INVALID CHOICE.")
        logging.warning("Invalid menu choice.")





