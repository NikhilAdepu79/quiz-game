import json

def load_questions():
    with open("questions.json", "r") as file:
        return json.load(file)

def run_quiz(questions):
    score = 0
    for i, q in enumerate(questions):
        print(f"\nQuestion {i+1}: {q['question']}")
        for j, option in enumerate(q['options']):
            print(f"{j+1}. {option}")
        try:
            answer = int(input("Your answer (1-4): "))
            if q['options'][answer - 1].lower() == q['answer'].lower():
                print("✅ Correct!")
                score += 1
            else:
                print(f"❌ Wrong! Correct answer: {q['answer']}")
        except:
            print("⚠️ Invalid input! Skipping question.")
    print(f"\n🎯 Final Score: {score}/{len(questions)}")

if __name__ == "__main__":
    quiz_data = load_questions()
    run_quiz(quiz_data)
