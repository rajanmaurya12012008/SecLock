from auth import register, login, update_score
from quiz import take_exam


def main():
    """Main function to run the exam system"""
    while True:
        print("\n===== Exam Portal =====")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Choose option: ")
        
        if choice == "1":
            # Register and get user_id
            result = register()
            user_id, email, password = result
            
            # After registration, ask to take exam
            print("\n--- Registration Successful ---")
            print("User ID:", user_id)
            print("1. Take Exam Now")
            print("2. Go to Main Menu")
            exam_choice = input("Choose option: ")
            
            if exam_choice == "1":
                # Take the exam
                print("Starting exam...")
                score, total = take_exam()
                print(f"\n--- Your Score: {score} / {total} ---")
                
                # Save score in database directly using user_id
                update_score(user_id, score, total)
                print("Score saved successfully!")
            
            # After registration, go back to menu
            
        elif choice == "2":
            print("Logging in...")
            result = login()
            user_id, score, total = result
            print(f"Login result: user_id={user_id}, score={score}, total={total}")
            
            if user_id:
                # Show last saved score
                print(f"\nWelcome! Your last score: {score} / {total}")
                
                # Ask to start exam
                print("\n1. Start Exam")
                print("2. Exit")
                exam_choice = input("Choose option: ")
                print(f"You chose: {exam_choice}")
                
                if exam_choice == "1":
                    # Take the exam
                    print("Starting exam...")
                    new_score, new_total = take_exam()
                    
                    # Update score in database
                    update_score(user_id, new_score, new_total)
                    print(f"\nScore updated! New Score: {new_score} / {new_total}")
                else:
                    print("Exiting...")
            else:
                print("Login failed. Returning to menu.")
            
        elif choice == "3":
            print("Thank you for using Exam Portal. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
