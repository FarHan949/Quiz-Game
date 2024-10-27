quiz = {
    "What is capital of Bangladesh" : "Dhaka",
    "What is 2 + 2 ?"  : "4",
    "What is the color of crow" : "black",
    "What is the name of the nearest galaxy?" : "andromeda",
    "what the name of our galaxy" : "milky way",
}

score = 0

for question , answer in quiz.items():
    user_answer = input(f"{question}  ? ").lower()
    if user_answer ==  answer.lower():
        print("correct")
        score += 1
    else:
        print(f"wrong answer , correct answer is {answer}")

print(f"Your final score is {score}/{len(quiz)}.")


