
import datetime

# quizes with object (or dictionary) format
quizes = {
    
    '1. What will be the output of the following code snippet?\n\nx = [i**2 for i in range(5)]\nprint(x)': {'[0, 1, 4, 9, 16]': True, '[1, 4, 9, 16, 25]': False, '[0, 1, 2, 3, 4]': False, '[1, 2, 3, 4, 5]': False},
    '2. Which of the following is a mutable data type in Python?': {'list': True, 'tuple': False, 'str': False, 'int': False},
    '3. What is the output of the following code?\n\nprint("Hello {0}, your balance is {1:9.3f}".format("Adam", 230.2346))': {'Hello Adam, your balance is   230.235': True, 'Hello Adam, your balance is 230.2346': False, 'Hello Adam, your balance is 230.2350': False, 'Hello Adam, your balance is 230.23': False},
    '4. Which keyword is used to create a loop in Python?': {'for': True, 'loop': False, 'iterate': False, 'repeat': False},
    '5. What will be the output of the following code snippet?\n\nx = lambda a, b : a * b\nprint(x(5, 6))': {30: True, 11: False, 56: False, 1: False},
    '6. Which of the following is used to handle exceptions in Python?': {'try-except': True, 'if-else': False, 'for-while': False, 'do-while': False},
    '7. What is the output of the following code?\n\nprint(list(map(lambda x: x*2, [1, 2, 3, 4])))': {'[2, 4, 6, 8]': True, '[1, 4, 9, 16]': False, '[2, 3, 4, 5]': False, '[1, 2, 3, 4]': False},
    '8. Which of the following is a correct way to open a file for reading in Python?': {'open("file.txt", "r")': True, 'open("file.txt", "w")': False, 'open("file.txt", "rw")': False, 'open("file.txt", "a")': False},
    '9. What will be the output of the following code snippet?\n\nx = [1, 2, 3]\ny = x\nx.append(4)\nprint(y)': {'[1, 2, 3, 4]': True, '[1, 2, 3]': False, '[4, 1, 2, 3]': False, '[1, 2, 3, 4, 4]': False},
    '10. Which of the following is a correct way to create a set in Python?': {'{1, 2, 3}': True, '[1, 2, 3]': False, '(1, 2, 3)': False, '{1: 2, 3: 4}': False},
}


user_score = 0




name = input('Enter your name: ')

answers = {}




for quiz in quizes.keys():



    # Print quizes with thier options
    print('\n', '===' ,quiz)

    for index, option in enumerate(quizes[quiz].keys()):
        print('\n', str(index + 1) + ')', option)


    # ** Tutorial: list.index() or enumerate() function?
    
    # list1 = ['a', 'b', 'c']
    # print(list1.index('a'))

    # print(list(quizes[quiz].keys()).index(31))




    # Validate
    user_answer = input('\nEnter your answer by option numbers: ')

    while not user_answer.isdigit() or int(user_answer) not in range(1, 4 + 1):
        user_answer = input('Invalid!!! try again: ')




    # get the users option
    for index, option in enumerate(quizes[quiz].keys()):

        if int(user_answer) == index + 1:

            # the_option is for making difference between the above option and this option in the loop
            for the_option, is_correct in quizes[quiz].items():

                if option == the_option:
                    answers[quiz] = [option, is_correct]
                    if is_correct:
                        user_score += 10
                    break





    for key, value in quizes[quiz].items():
        
        if value:
            print('--- The true option is ' + str(key) + ' ---')
            break




print('\n ==== the results file has been created ==== \n')




# with keyword: opens the file and automatically closes the file when the process ends
# as keyword: adding name to the file that is opened to work with
with open('quizResults.txt', 'a') as file:

    file.write(f'\n ==== {name}, here are your answers and final score ({datetime.datetime.now()}) ==== \n')

    # writing the results
    for quiz, answer in answers.items():
        
        file.write(
            f'\n{quiz}\n--- Your answer: {answer[0]} => {answer[1]}\n'
        )

    file.write(f'\n ==== final score: {user_score}/100 \n')