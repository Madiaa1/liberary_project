def main():

    print("Welcom to Mahdia's liberary!")
    print("Lets create your account first!")
    username, password = create_acount()

    print("Please enter your username and password to log into your acount!")
    login(username, password)

    print("Now that you are logged in, we need your email address to send you book of your interest.")
    email = user_email()

    print("Welcom to your account! now you are a member of Mahdia's liberary." 
          "lets view some available options!")
    user_choice = choice()

    questions()
    feedback()

def create_acount():
          username = input("Enter a username to use in your account: ").strip()
          while not username:
              print("Username cannot be empty! Please enter a valid username.")
              username = input("Enter a username to use in your account: ").strip()

          password = input("Enter a password with at least 4 digits: ").strip()
          while len(password) < 4 or not password.isdigit():
           print("Password should have 4 or more numbers! Please try again.")
           password = input("Enter a password: ").strip()

          conf_pass = input("Please Confirm your password: ").strip()
          while password != conf_pass:
               print("Password do not match. try again!")
               conf_pass = input("Enter your password again: ").strip()
               
          print("Your account has been created. Now, lets log in!")
          return username, password

def login(stored_username, stored_password):
    while True:
        username = input("Enter your username: ").strip()
        password = input("Enter your passwrd: ").strip()
        
        if username == stored_username and password == stored_password:
            print("Your are logged in!")
            break
        else:
            print("Invalid username or password! try again.")

def user_email():
    while True:
        email = input("Please enter your email address: ").strip()
        
        if "@" not in email or '.' not in email:
            print("Invalid email format. PLease try again and enter a valid email.")
            continue
        
        conf_email = input("Please confirm your email: ").strip()
        if email == conf_email:
            print("Email accepted and the process succesfully completed.")
            return email
        else:
            print("Email do not match. Please try again.")

def choice():
    available_books = [
        "A Thousand Splendid Suns",
        "And The Mountain Echoed",
        "Forty Rules Of Love", 
        "The Kite Runner",
        "Crime and punishment", 
        "Harry Potter and the Sorcerer's Stone", 
        "Wonder", 
        "Little Women"
    ]
    
    common_books = [
        "Crime and punishment", 
        "Harry Potter and the Sorcerer's Stone", 
        "Wonder", 
        "Little Women",
        "One Hundred Years of Solitude", 
        "Human in search of meaning",
        "Algebra 1",
        "Python for beginners",
        "Algebra 2",
        "English for begginers",
        "English for Advanced level"
    ]

    print("Please choose one of these options: \n1. Viewing Available Books \n2. Searching for a Book")
    while True:
        user_choice = input("Enter your choice: ").strip() 

        if user_choice == "1":
            print("\nHere are some available books:")
            for book in available_books:
                print(f"- {book}")
                
            selected_book = input("Enter the name of the book your want: ").strip()
            if selected_book in available_books:
                print(f"Thanks for chosing {selected_book} book! we will send the book to your email address soon!")
                return user_choice
            else:
                print("The book you entered is not available at the moment. "
                      "Or perhaps you did not write the name correctly. "
                      "Please see the available books again and select one of them.")
                    
        elif user_choice == "2":
            search_query = input("Please enter the name of the most common book you are interested in: ").strip()

            if search_query in common_books:
                print(f"Great choice! we will send the {search_query} book to your email address soon!")
                return user_choice
            else:
                print("The book is not available at the moment. We will try to get it for you next week. in the meantime, try to see the avilable books or search the most common book.")

        else:
            print("Invalid choice! Please enter '1' to view available books or '2' to search for a book.")

def questions():
    fre_as_que = [
        "1. How do I create a liberary account?",
        "2. Is my account free, or do I need to pay for it?",
        "3. What should I do if a book I want is currently unavailable?",
        "4. Can I create an account without an email?",
        "5. How do I log to my liberary account?",
        "6. How can I get a book after a select that?",
        "7. How long can I keep a borrowed book?"
        ]
    
    answers = [
        "1. You can sign up online or visit our liberary in person and provide your details like username, password, and email.",
        "2. Yes, you can create your account free! there is no need to pay for it.",
        "3. You can let us know and we will try to get that for you soon. We will also let you know in your email once we get that.",
        "4. Yes, you can. But after you create your account and logged in, we do need your email in case to send you the book you choose.",
        "5. Once you create your account, go to our liberary website, enter your username and password.",
        "6. Once you select the book of your interest, We will send the book to your email adress soon.",
        "7. The borrowing period is usually 2-4 weeks."
        ]
    
    print("Do you have any questions? (yes/no)")
    while True:
        user_response = input().strip().lower()
        if user_response == "yes":
            print("\nHere is our liberary FAQ: ")
            for question, answer in zip(fre_as_que, answers):
                print(f"\nQ: {question} \nA: {answer}")
            break
            
        elif user_response == "no":
            print("That is great! Let me know if you need help later :)")
            break
        else:
            print("Please answer with 'yes' or 'no'.")

def feedback():
    print("Was it helpful?(yes/no)")
    while True:
        ans = input().strip().lower()
        if ans == 'yes':
            print("Great! thanks for your feedback")
            break
        elif ans == 'no':
            print("Please ask your question")
            ques = input("Enter your question: ")
            print("Thank your for the question. We already sent the answer with its detail in your email 😉")
            break
        else:
            print("Please answer with 'yes' or 'no'")

main()
