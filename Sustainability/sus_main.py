"""
MCQ python script generated from ChatGPT 3.5
Prompt: 
    Write a python script that allows users to test themselves some MCQ questions, with data stored in a json format. 
    Give an example of a json format that will make it compatible with this script

JSON questions and answers generated from ChatGPT 4.0
Prompt:
    Imagine you are the teacher teaching this course. With the following course slides, generate 20 MCQ questions and answers based on the course slides, 
    with the data loaded into a json format. here's an example:

    [
        {
            "question": "What is the capital of France?",
            "options": ["Paris", "London", "Rome", "Berlin"],
            "answer": "1"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["Venus", "Mars", "Jupiter", "Saturn"],
            "answer": "2"
        },
        {
            "question": "Who wrote 'To Kill a Mockingbird'?",
            "options": ["Mark Twain", "Harper Lee", "J.K. Rowling", "Ernest Hemingway"],
            "answer": "2"
        }
    ]

    questions must not be repeated
"""

import json
import random
import time

# Function to load MCQs from JSON file
def load_mcqs(filename):
    with open(filename, 'r') as file:
        mcqs_data = json.load(file)
    return mcqs_data

# Function to display MCQ and get user's response
def display_mcq(mcq, counter):
    print('\n'+f"Q{counter+1}. "+mcq['question'])
    for i, option in enumerate(mcq['options'], start=1):
        print(f"{i}. {option}")
    user_response = input("Enter your choice: ")
    return user_response

# Function to evaluate user's responses
def evaluate_responses(mcqs_data, max_questions):
    counter = 0
    correct_answers = 0
    for mcq in mcqs_data:
        user_response = display_mcq(mcq, counter)
        if user_response == mcq['answer']:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"Wrong! The correct answer is: {mcq['answer']}")
        counter+=1
        if(counter==max_questions): break
    print(f"\nYou answered {correct_answers} out of {max_questions} questions correctly.")

# Main function
def main():
    filename = "questions.json"
    print("Select question set:\n(1) ChatGPT generated questions\n(2) ChatGPT generated questions set 2\n(3) Weekly questions from NTULearn\n(4) Critical thinking generated questions")
    choice = int(input())
    if choice == 1:
        filename = "generated_questions.json"
    elif choice == 2:
        filename = "generated_questions2.json"
    elif choice == 3:
        filename = "weekly_questions.json"
    elif choice == 4:
        filename = "critical_thinking_gq.json"
        
    mcqs_data = load_mcqs(filename)
    
    if mcqs_data:
        random.shuffle(mcqs_data)  # Shuffle the questions
        print(f"How many questions would you like to try? There is a total of {len(mcqs_data)} questions. Type -1 to select all questions")
        questions = int(input())
        questions = len(mcqs_data) if questions == -1 else questions
        
        start_time = time.time()  # Record the start time
        evaluate_responses(mcqs_data, questions)
        end_time = time.time()  # Record the end time
        execution_time = end_time - start_time  # Calculate the execution time
        execution_time_minutes = int(execution_time // 60)  # Minutes
        execution_time_seconds = execution_time % 60  # Seconds remaining
        print(f"You took {execution_time_minutes}min {round(execution_time_seconds)}s")
        
    else:
        print("No valid data found in the JSON file.")

if __name__ == "__main__":
    main()
