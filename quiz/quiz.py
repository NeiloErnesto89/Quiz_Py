def show_menu():
    print("1. Ask questions")
    print("2. Add a question")
    print("3. Exit game")
    
    option = input("Enter option: ")
    return option
    
def ask_question():
    questions = []
    answers = []
    
    with open("questions.txt", 'r') as file:
        lines = file.read().splitlines()
    
    for i, text in enumerate(lines):
        if i%2 ==0:
            questions.append(text)
        else:
            answers.append(text)
            
    number_of_questions = len(questions)
    questions_and_answers = zip(questions, answers)
    
    score = 0
    
    for question, answer in questions_and_answers: 
        #zip(questions, answers): removed to avoid zip in every for loop
        guess = input(question + "> ")
        if guess == answer:
            score += 1
            print("correct!")
            print(score)
        else:
            print("wrong, loser !!")
            
    print("You got {0} correct out of {1}".format(score, number_of_questions))
            
   #What is Inertia?
   # Inertia is when an object remains at rest or in motion, unless acted upon!    
        
def add_question():
    print("")
    question = input("Enter a question\n> ")
    
    print("")
    print("OK, tell me the answer!")
    answer = input("{0}\n>".format(question))
    
    file = open("questions.txt", "a")
    file.write(question + "\n")
    file.write(answer + "\n")
    file.close()
    
def game_loop():
    while True: #loop forever unless there's a break
        option = show_menu()
        if option == "1":
            ask_question()
            #print("you selected 'Ask questions")
        elif option == "2":
            #print("you selected 'Add a question")
            add_question()
        elif option == "3":
            break
        else:
            print("Invaild option - choose again!")
        print("")
        
game_loop()
            # print("you selected 'Exit game")
            
#print(show_menu())