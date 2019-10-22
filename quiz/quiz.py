def show_menu():
    print("1. Ask questions")
    print("2. Add a question")
    print("3. Exit game")
    
    option = input("Enter option: ")
    return option
    
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
            print("you selected 'Ask questions")
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