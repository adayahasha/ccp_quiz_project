from flashcards_data_set import services_dict
import random
from flashcards_merged_dicts import ccp_exam_questions_answers
import time


class FlashCards:
    """constructor method that takes no arguments"""
    def __init__(self):
        # creating 4 instance attributes
        self.ccp_exam_questions = list(ccp_exam_questions_answers.items())
        # converting ccp dictionary into a nested list to be called by index
        self.correct_answers = 0
        self.incorrect_answers = 0
        self.incorrect_questions = []
        # creating an empty list to store all incorrect answers

    def start_quiz(self):
        # creating an instance method that takes no arguments
        total_questions = len(self.ccp_exam_questions)
        # instance variable that equals length of nested list
        asked_questions = set()
        # instance variable creating an empty set (unordered objects) for variable
        start_time = time.time()
        # instance variable calling time module and .time function

        while len(asked_questions) < total_questions:
            # while loop for length of variable set less than length of nested list
            ccp_exam_question = random.choice(self.ccp_exam_questions)
            # creating a random choice order for questions to ask
            if ccp_exam_question[0] not in asked_questions:
                # condition to verify question asked is not repeated
                asked_questions.add(ccp_exam_question[0])
                # adding question to empty set once asked
                question = ccp_exam_question[1].title()
                # question is index 1 of nested dict list
                answer = ccp_exam_question[0]
                # answer is index 0 of nested dict list

                # get 3 random choices from the dictionary keys
                choices = random.sample(list(services_dict.keys()), k=3)
                # add the correct answer to the choices
                choices.append(answer)
                # shuffle the choices
                random.shuffle(choices)

                questions_remaining = total_questions - len(asked_questions)
                # subtracting total questions from questions asked
                print(f"Question {len(asked_questions)}/{total_questions} "
                      f"(Total: {total_questions}, Remaining: {questions_remaining})")
                print(f"Quiz Results: {self.correct_answers} correct, {self.incorrect_answers} incorrect")
                print(f"{question}")
                # printing f-strings of class attributes and instance variables
                for i, choice in enumerate(choices):
                    # iterating over choices variable
                    # printing numbered choices with first word to each letter uppercase
                    print(f"{i + 1}. {choice.title()}")
                    # asking user to input answer choice
                user_answer = input()

                try:
                    # convert the user answer to an integer and subtract 1 to get the index of the choice
                    choice_index = int(user_answer) - 1
                    user_answer = choices[choice_index]
                    # condition for user input error
                except (ValueError, IndexError):
                    pass
                # conditions to display correct and incorrect answer after user input
                if user_answer.lower() == answer.lower():
                    print("Correct answer!")
                    self.correct_answers += 1
                else:
                    print(f"Wrong answer. The Correct answer is: {answer}.")
                    self.incorrect_answers += 1
                    self.incorrect_questions.append(ccp_exam_question)

        end_time = time.time()
        time_taken = (end_time - start_time) / 60
        # displaying time taken in minutes
        grade = (self.correct_answers / total_questions) * 100
        # converting correct and incorrect into a grade diving by 100
        print(f"Quiz Results: {self.correct_answers} correct, {self.incorrect_answers} incorrect")
        print(f"Grade: {grade:.2f}%")
        # specifies that the value should be formatted as a floating-point number with 2 decimal places
        print(f"Time taken to Complete the Quiz: {time_taken:.2f} minutes")

        if self.incorrect_questions:
            # condition for any incorrect answers
            print("\n\nQuestions Needing Review:")
            for question in self.incorrect_questions:
                print(f"{question[1].title()}: {question[0]}")

    def help_menu(self):
        # instance method with no arguments
        while True:
            # while loop for opening and help menu
            print("\nWelcome to the Flash Cards Help Menu!")
            print("What would you like to do?")
            print("1. Start Quiz")
            print("2. Review Service Categories")
            print("3. Exit")
            user_choice = input()
            # conditions for user input to start quiz, review, or exit
            if user_choice == "1":
                self.start_quiz()
            elif user_choice == "2":
                print("\nServices Categories:")
                for category, services in services_dict.items():
                    print(f" {category.title()} ".center(55, '-'))
                    for service in services:
                        print(f"** {service.title()}")
                    print('\n')
            elif user_choice == "3":
                break
            else:
                print("Invalid choice. Please try again.")


