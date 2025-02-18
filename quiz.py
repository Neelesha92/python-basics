import random;
print('Ready to test your IQ? Lets get started.')

quiz_questions = [

     { 
        "question":"What is the capital of France?",
        "options": ["A) Berlin ", "B) Madrid", "C) Paris", "D) Rome"],
        "Answer": "C"
    },
    { "question":"Which programming language is known as the 'Mother of All Languages'",
       "options": ["A) python ", "B) C", "C) Java", "D) Javascript"],
       "Answer": "B"
    },
    { "question":"What is the chemical symbol for water?",
       "options": ["A) O2 ", "B) CO2", "C)H2 ", "D) H20"],
       "Answer": "D"
    }]

random.shuffle(quiz_questions)

score = 0

for i, q in enumerate(quiz_questions):
    print(f"your question is:",q["question"])
    for option in q["options"]:
        print(option)
    
    answer= input("Enter your answer A.B.C or D: ").strip().upper()

    if answer == q["Answer"]:
        print("Correct answer!!")
        score= score +1
    else:
        print(f"Incorrect Answer. The correct ans was: ",q["Answer"])

print("your total score is: ", score)

