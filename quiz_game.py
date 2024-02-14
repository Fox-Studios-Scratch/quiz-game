# quiz_game.py

# Define a list of questions. Each question is a dictionary with the question, options, and the correct answer.
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["London", "Paris", "Berlin", "Rome"],
        "correct_answer": "Paris"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["William Shakespeare", "Jane Austen", "Charles Dickens", "Leo Tolstoy"],
        "correct_answer": "William Shakespeare"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["Jupiter", "Mars", "Venus", "Saturn"],
        "correct_answer": "Jupiter"
    },
    {
        "question": "What is the capital of Japan?",
        "options": ["Beijing", "Seoul", "Tokyo", "Bangkok"],
        "correct_answer": "Tokyo"
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": ["Pablo Picasso", "Leonardo da Vinci", "Vincent van Gogh", "Michelangelo"],
        "correct_answer": "Leonardo da Vinci"
    }
]

# Define a function to display questions and get user input
def display_question(question):
    print(question["question"])
    for i, option in enumerate(question["options"], 1):
        print(f"{i}. {option}")
    user_answer = input("Enter your answer (1-4): ")
    return user_answer

# Define a function to check the user's answer
def check_answer(question, user_answer):
    return question["options"][int(user_answer) - 1] == question["correct_answer"]

# Define a function to run the quiz
def run_quiz():
    score = 0
    for question in questions:
        user_answer = display_question(question)
        if check_answer(question, user_answer):
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
            print(f"The correct answer is: {question['correct_answer']}")
    print(f"Your final score is: {score}/{len(questions)}")

# Call the run_quiz function to start the game
run_quiz()