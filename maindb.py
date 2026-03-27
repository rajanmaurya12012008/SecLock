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
            res = register()
            uid, email, pw = res
            
            print()
            print("--- Registration Successful ---")
            print("User ID:", uid)
            print("1. Take Exam Now")
            print("2. Go to Main Menu")
            ex_ch = input("Choose option: ")
            
            if ex_ch == "1":
                print("Starting exam...")
                sc, tot = take_exam()
                print(f"\n--- Your Score: {sc} / {tot} ---")
                
                # Save score
                update_score(uid, sc, tot)
                print("✓ Score saved!")
            
            print()
            
        elif choice == "2":
            print("Logging in...")
            res = login()
            uid, sc, tot = res
            
            if uid:
                print(f"\nWelcome! Your last score: {sc} / {tot}")
                
                print("\n1. Start Exam")
                print("2. Exit")
                ex_ch = input("Choose option: ")
                
                if ex_ch == "1":
                    print("Starting exam...")
                    new_sc, new_tot = take_exam()
                    
                    # Update score
                    update_score(uid, new_sc, new_tot)
                    print(f"\n✓ Score updated! New Score: {new_sc} / {new_tot}")
                else:
                    print("Exiting...")
            else:
                print("Login failed.")
            
            print()
            
        elif choice == "3":
            print("Thank you! Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()