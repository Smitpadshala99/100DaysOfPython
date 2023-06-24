def play_game():
    questions = [
        {
            "question": "Which Indian cricketer has the highest number of international centuries?",
            "options": ["A. Sachin Tendulkar", "B. Virat Kohli", "C. Rahul Dravid", "D. Virender Sehwag"],
            "answer": "A"
        },
        {
            "question": "Who is the host of 'Kaun Banega Crorepati'?",
            "options": ["A. Shah Rukh Khan", "B. Amitabh Bachchan ", "C. Salman Khan", "D. Aamir Khan"],
            "answer": "B"
        },
        {
            "question": "Who is the current Prime Minister of India?",
            "options": ["A. Narendra Modi", "B. Rahul Gandhi", "C. Amit Shah", "D. Arvind Kejriwal"],
            "answer": "A"
        },
        {
            "question": "Best YouTube channel for learning coding?",
            "options": ["A. Jenny's Lectures CS IT", "B. CodeWithHarry", "C. Apna Collage", "D. freecodecamp"],
            "answer": "B"
        }
        # Add more questions here
    ]

    total_questions = len(questions)
    question_index = 0
    prize_money = 0  # Initial prize money

    while question_index < total_questions:
        current_question = questions[question_index]
        print(f"Question {question_index + 1}: {current_question['question']}")
        for option in current_question['options']:
            print(option)
        user_answer = input("Enter your answer (A, B, C, or D): ")

        if user_answer.upper() == current_question['answer']:
            print("Correct answer!")
            question_index += 1
            prize_money = 1000
            prize_money *= 2  # Double the prize money for each correct answer
        else:
            print("Wrong answer!")
            break

    print(f"Congratulations! You answered {question_index} questions correctly.")
    print(f"You are taking home {prize_money}Rs.")

# Start the game
play_game()
