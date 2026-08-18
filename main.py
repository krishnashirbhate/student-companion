#started from making differentt functions here , i am defing a fuction for calculating the grade 
def calculate_grade():
    """Takes marks for 5 subjects and prints total, percentage, and grade."""
    print("\n---  Student Grade Calculator ---")



    #the try statement is used to run code that might cause an error, and if an error occurs,
    #control is passed to an except block instead of crashing the program.
    # i have used this this ststement for the two times as i am defining the two functions.

    try:
        # Step 1: Get marks from user
        maths = float(input("Enter marks for Mathematics (out of 100): "))
        physics = float(input("Enter marks for Physics (out of 100): "))
        chemistry = float(input("Enter marks for Chemistry (out of 100): "))
        programming = float(input("Enter marks for Programming (out of 100): "))
        english = float(input("Enter marks for English (out of 100): "))

        marks = [maths, physics, chemistry, programming, english]

        # Step 2: Check marks are valid (0-100)

        if any(m < 0 or m > 100 for m in marks):
            print(" Invalid input! Marks should be between 0 and 100.")
            return

        # Step 3: Calculate total and percentage
        total = sum(marks)
        percentage = (total / 500) * 100

        # Step 4: Decide grade based on percentage
        if percentage >= 90:
            grade = "A+"
        elif percentage >= 80:
            grade = "A"
        elif percentage >= 70:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        elif percentage >= 40:
            grade = "D"
        else:
            grade = "F (Fail)"

        # Step 5: Show results , using /n for making it on another line
        print("\n--- RESULTS ---")
        print(f"Total Marks : {total:.2f} / 500")
        print(f"Percentage  : {percentage:.2f}%")
        print(f"Final Grade : {grade}")

        # Python raises a ValueError, and the except block runs instead of crashing.

    except ValueError:
        print(" Invalid input! Please enter numerical values for marks.")


        # defining secnd fuction here.


def calculate_attendance():
    # i have taken 75 percent rule a/c to my college 
    """Takes total and attended lectures, checks exam eligibility criteria (75%)."""
    print("\n--- Attendance Tracker ---")
    try:
        # Step 1: Get lecture counts
        total_lectures = int(input("Enter tootal lectures conducted: "))
        attended_lectures = int(input("Enter total lectures attended: "))

        # Step 2: Validate input
        if total_lectures <= 0 or attended_lectures < 0 or attended_lectures > total_lectures:
            print(" Invalid input! Check total and attended lecture numbers.")
            return

        # Step 3: Calculate attendance percentage y simple maths calculation using aithmatic operators 
        attendance_pct = (attended_lectures / total_lectures) * 100

        # Step 4: Showing  results
        print("\n--- RESULTS ---")
        print(f"Attendance Percentage: {attendance_pct:.2f}%")

        if attendance_pct >= 75.0:
            print("Status:  Eligible for Exams")
        else:
            print("Status: Shortage of Attendance (< 75%) and ur not eligible for the examination ")

    except ValueError:
        print(" Invalid input! Please enter whole numbers.")


def main():
    """Shows the menu and runs the chosen feature in a loop."""
    while True:
        print("\n=================================")
        print("       STUDENT COMPANION      ")
        print("=================================")
        print("1. Grade Calculator")
        print("2. Attendance Tracker")
        print("3. Exit Application")

        choice = input("\nSelect an option (1-3): ").strip()
        #fuction call steps happen here

        if choice == '1':
            calculate_grade()
        elif choice == '2':
            calculate_attendance()
        elif choice == '3':
            print("\nThank you for using Student Companion. Good luck with your studies!")
            break
        else:
            print("\n Invalid choice! Please select 1, 2, or 3.")

            #here it use for makint it work in the loop

if __name__ == "__main__":
    main()