
# quizes with object (or dictionary) format
quizes = {

    '1. How many provinces are there in Iran?' : {20: False, 31: True, 10: False, 5: False},
    '2. Which animal is recognized as the symbol of China?' : {'Panda': True, 'Lion': False, 'Wolf': False, 'Kiwi': False},
    '3. Which season is known for its heat and longer days?' : {'Spring': False, 'Summer': True, 'Autumn': False, 'Winter': False},
    '4. Which color is known as the color of the sky during the day?' : {'Red': False, 'Blue': True, 'Green': False, 'Yellow': False},
    '5. Which substance plays a role in forming human skin?' : {'Calcium': False, 'Protein': True, 'Iron': False, 'Vitamin': False},
    '6. Which continent is the largest in the world?' : {'Asia': True, 'Africa': False, 'America': False, 'Europe': False},
    '7. Which substance plays a role in forming blood?' : {'Iron': True, 'Calcium': False, 'Protein': False, 'Vitamin': False},
    '8. Which planet in the solar system has rings?' : {'Earth': False, 'Mars': False, 'Neptune': False, 'Uranus': True},
    '9. Which city is recognized as the capital of Italy?' : {'Rome': True, 'Milan': False, 'Venice': False, 'Florence': False},
    '10. Which language is recognized as the international scientific language?' : {'English': True, 'French': False, 'Spanish': False, 'Chinese': False},

}





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

            # the_option for making difference between the above option and this option in the loop
            for the_option, is_correct in quizes[quiz].items():

                if option == the_option:
                    answers[quiz] = [option, is_correct]
                    break





    for key, value in quizes[quiz].items():
        
        if value:
            print('--- The true option is ' + str(key) + ' ---')
            break




# with keyword: opens the file and automatically closes the file when the process ends
# as keyword: adding name to the file that is opened to work with
with open('quizResults.txt', 'a') as file:

    file.write(f'\n ==== {name}, here are your answers: ==== \n')

    # writing the results
    for quiz, answer in answers.items():
        
        file.write(
            f'\n{quiz} - Your answer: {answer[0]} (is_correct: {answer[1]})\n'
        )