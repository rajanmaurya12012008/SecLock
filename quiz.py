from que import questions

def start_quiz():
    score = 0
    total = len(questions)

    for i, q in enumerate(questions):
        user_answer = int(input(f"Q{i+1}: {q['question']} = "))

        if user_answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! Correct answer is {q['answer']}")

    return score, total


def take_exam():
    """Main function to handle the exam with re-exam option"""
    while True:
        print("\n--- Starting Exam ---")
        score, total = start_quiz()
        
        print(f"\n--- Result ---")
        print(f"Your Score: {score} / {total}")
        percentage = (score / total) * 100 if total > 0 else 0
        print(f"Percentage: {percentage:.2f}%")
        
        # Ask for re-exam
        print("\n1. Re-exam")
        print("2. Exit to main menu")
        
        choice = input("Choose option: ")
        
        if choice != "1":
            break
    
    return score, total
