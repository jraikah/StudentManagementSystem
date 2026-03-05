
def student_management_system():
    students = {} # Using a dictionary for faster ID lookups

    while True:
        print("\n" + "="*30)
        print(" STUDENT MANAGEMENT SYSTEM ")
        print("="*30)
        print("1. Add Student Information")
        print("2. Update Student Information")
        print("3. Remove a Student")
        print("4. Add Student (Quick Add)")
        print("5. List All Students")
        print("6. Fees Structure")
        print("7. Exit")
        
        choice = input("\nSelect an option (1-7): ")

        # 1. Add Student Information (Detailed)
        if choice == '1':
            s_id = input("Enter Student ID: ")
            name = input("Enter Full Name: ")
            course = input("Enter Course: ")
            balance = float(input("Enter Initial Tuition Balance: "))
            students[s_id] = {"name": name, "course": course, "balance": balance}
            print(f"\nRecord for {name} created successfully!")

        # 2. Update Student Information
        elif choice == '2':
            s_id = input("Enter Student ID to update: ")
            if s_id in students:
                print("Leave blank to keep current value.")
                new_name = input(f"New Name ({students[s_id]['name']}): ")
                new_course = input(f"New Course ({students[s_id]['course']}): ")
                
                if new_name: students[s_id]['name'] = new_name
                if new_course: students[s_id]['course'] = new_course
                print("Information updated.")
            else:
                print("Error: Student ID not found.")

        # 3. Remove a Student
        elif choice == '4' or choice == '3': # Handling both "Remove" and "Add" logic per your list
            if choice == '3':
                s_id = input("Enter Student ID to remove: ")
                if s_id in students:
                    removed = students.pop(s_id)
                    print(f"Student {removed['name']} has been removed.")
                else:
                    print("Error: Student ID not found.")
            
            # 4. Add Student (Quick Add/Repeat functionality)
            else:
                s_id = input("Enter ID: ")
                name = input("Enter Name: ")
                students[s_id] = {"name": name, "course": "General", "balance": 0.0}
                print("Student added.")

        # 5. List All Students
        elif choice == '5':
            if not students:
                print("\nNo records found.")
            else:
                print(f"\n{'ID':<10} {'Name':<20} {'Course':<15} {'Balance':<10}")
                print("-" * 55)
                for s_id, info in students.items():
                    print(f"{s_id:<10} {info['name']:<20} {info['course']:<15} ${info['balance']:<10.2f}")

        # 6. Fees Structure
        elif choice == '6':
            print("\n--- OFFICIAL FEES STRUCTURE ---")
            print("1. Engineering: $5,000 / Semester")
            print("2. Computer Science: $4,500 / Semester")
            print("3. Business Administration: $3,800 / Semester")
            print("4. Arts & Humanities: $3,000 / Semester")
            print("-" * 30)

        # 7. Exit
        elif choice == '7':
            print("Closing system. Have a great day!")
            break

        else:
            print("Invalid input. Please choose 1-7.")

if __name__ == "__main__":
    student_management_system()