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
    while(1):
        user_response = input("Enter your choice: ")
        try:
            user_response = int(user_response)
            return str(user_response)
        except:
            0

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
    print(f"That's {round((correct_answers/max_questions)*100, 2)}%!")

# Main function
def main():
    filename = "questions.json"
    print("Select question set:")
    print("(1) OS ChatGPT generated questions")
    # print("(2) ChatGPT generated questions set 2")
    # print("(3) Weekly questions from NTULearn")
    # print("(4) Critical thinking generated questions")
    choice = int(input())
    if choice == 1:
        filename = "OSMCQ1.json"
    # elif choice == 2:
    #     filename = "generated_questions2.json"
    # elif choice == 3:
    #     filename = "weekly_questions.json"
    # elif choice == 4:
    #     filename = "critical_thinking_gq.json"
        
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
