# Dictionary to store exams using exam ID as the key
exams = {}

# Function to add a new exam to the dictionary
def add_exam():
    exam_id = input("Enter unique exam ID: ")
    
    # Check if the ID already exists
    if exam_id in exams:
        print("Exam ID already exists. Try again.")
        return
    
    # Collect exam details from the user
    name = input("Enter exam name: ")
    date = input("Enter exam date (YYYY-MM-DD): ")
    time = input("Enter exam time (e.g. 10:00 AM): ")
    room = input("Enter exam room: ")
    
    # Store the exam details in the dictionary
    exams[exam_id] = {"name": name, "date": date, "time": time, "room": room}
    print("Exam added successfully!\n")

# Function to view all scheduled exams
def view_exams():
    # If there are no exams, notify the user
    if not exams:
        print("No exams scheduled yet.\n")
        return

    print("\n--- All Scheduled Exams ---")
    
    # Loop through and display each exam
    for exam_id, details in exams.items():
        print(f"ID: {exam_id}")
        print(f"  Name : {details['name']}")
        print(f"  Date : {details['date']}")
        print(f"  Time : {details['time']}")
        print(f"  Room : {details['room']}\n")

# Function to edit an existing exam
def edit_exam():
    exam_id = input("Enter the exam ID to edit: ")
    
    # Check if the exam exists
    if exam_id not in exams:
        print("Exam ID not found.\n")
        return

    print("Leave a field empty to keep it unchanged.")
    
    # Get new values (if any) from the user
    name = input("Enter new exam name: ")
    date = input("Enter new exam date (YYYY-MM-DD): ")
    time = input("Enter new exam time: ")
    room = input("Enter new exam room: ")

    # Update only the fields that were changed
    if name:
        exams[exam_id]["name"] = name
    if date:
        exams[exam_id]["date"] = date
    if time:
        exams[exam_id]["time"] = time
    if room:
        exams[exam_id]["room"] = room

    print("Exam updated successfully!\n")

# Function to delete an exam from the dictionary
def delete_exam():
    exam_id = input("Enter the exam ID to delete: ")
    
    # Delete the exam if it exists
    if exam_id in exams:
        del exams[exam_id]
        print("Exam deleted successfully.\n")
    else:
        print("Exam ID not found.\n")

# Main menu to interact with the user
def main_menu():
    while True:
        # Display menu options
        print("===== Exam Scheduler Menu =====")
        print("1. Add a new exam")
        print("2. View all exams")
        print("3. Edit an exam")
        print("4. Delete an exam")
        print("5. Exit")
        
        # Get user's choice
        choice = input("Select an option (1-5): ")

        # Call the corresponding function based on choice
        if choice == '1':
            add_exam()
        elif choice == '2':
            view_exams()
        elif choice == '3':
            edit_exam()
        elif choice == '4':
            delete_exam()
        elif choice == '5':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid option. Please try again.\n")

# Start the program by calling the main menu
main_menu()
