"""Christina Torres, Casey, Collin
Group Project 1
Jump Python Bridge Course
4/15/2022"""

from getpass import getpass

mydict ={"Toy Story" : "Completed",
"Jumanji" : "In Progress",
"The Batman" : "Not Completed",
"Unchartered" : "Completed",
"What Happens in Vegas"  : "Not Completed",
"WALL-E" : "Completed",
"Tangled" : "Completed",
"She's Out of My League" : "Not Completed",
"Marley and Me" : "In Progress",
"Dear John" : "Not Completed"}


"""******************************
UI interface that presents the options the user 
has to choose from
Listing options :
    1: Update
    2: View
    2.1: Extensions
    3: Exit

Redirecting to appropiate function calls
"""
def UIinterface() :

    print("""********************************************************************************
    ********************************************************************************
    ********************************************************************************
    ********************************************************************************
    ********************************************************************************
    ********************************************************************************





    Hello! Welcome to the Tracker system. We will take care of all your movie
    tracking needs. We take the uptmost interest in taking care of your personal information
    so we require a valid account in order to best serve you. If you don't already have an account 
    you can choose to make one on this menu as well. 
    """)
    
    user= None
    while True:
        print("""Please select from the following options: \n1. Login \n2. Create an Account""")
        answer = input("...: ")
        while True:
            if (answer == "1" or answer == "2") : break
            else: answer = input("""Please make a valid selection:
            ...: """)
        if answer == "2" : 
            user = User.CreateAccount()
            

        else: 
            if len(User.users) == 0 : 
                print("""There are no accounts yet. Please create an account.
                """)
                user = User.CreateAccount()
                

        print("Please Login \n")
        while True :
            login = User.Login()
            if login == False : print("""This is not a valid account. Please try again\n""")
            else : break
        
        while True :
            if(isinstance(user, Admin)) :
                print("""Please choose from the following options; 
                1: Update movie progress tracker
                2: View all progress trackers
                3: Edit or remove movie names for all users
                4: Exit""")
                answer = input("...: ")
                while True:
                    if (answer == "1" or answer == "2" or answer =="3" or answer =="4") : break
                    else: answer = input("""Please make a valid selection:
                    ...: """)
                match answer :
                    case "1" : 
                        user.tracker.update_entry()
                        print("Entry successfully updated!")
                    case "2" : user.tracker.view_tracker()
                    case "3" : 
                        user.edit_topic()
                        for user in User.users :
                            new_dict = {}
                            status = list(Tracker.super_movie_dict.values())
                            movies = list(Tracker.super_movie_dict.keys())
                            for i in range(len(status)) :
                                new_dict[movies[i]] = status[i]
                            user.tracker.movie_dict = new_dict

                    case "4" : break

            else :
                print("""Please choose from the following options; 
                1: Update movie progress tracker
                2: View all progress trackers
                3: Exit""")
                answer = input("...: ")
                while True:
                    if (answer == "1" or answer == "2" or answer =="3") : break
                    else: answer = input("""Please make a valid selection:
                    ...: """)
                match answer :
                    case "1" : 
                        user.tracker.update_entry()
                        print("Entry successfully updated!")
                    case "2" : user.tracker.view_tracker()
                    case "3" : break
        print("Would you like to login?")
        answer = input("Y/N...: ")

        while True :
            if (answer == "Y" or answer == "N") : break
            else : answer = input("Please write Y or N: ")
        if answer == 'N' : break
        
    print("""Goodbye!
    ********************************************************************************
    ********************************************************************************
    ********************************************************************************
    ********************************************************************************""")
    
 


"""********************
tracker class that holds lists of (completed), 
(in-progress), (not-yet-completed)

*function update_entry() ->reasign entry to different list

*function view_entry() -> print an entry and it's tracking status
"""
class Tracker():
    super_movie_dict = {}
    def __init__(self):
        self.movie_dict = {}

    def populate_dict(self, dictionary) :
        self.movie_dict = dictionary

    def __str__(self):
        c_list = list(Tracker.super_movie_dict.keys())
        return str(c_list)
    def update_entry(self):
        print(len(Tracker.super_movie_dict))
        count = 1
        print("What movie would you like to change?")
        for movies in Tracker.super_movie_dict.keys() :
            print(f"{count}. {movies}")
            count += 1
        movie = input("\n...: ")

        while True :
            if (movie == "1" or movie == "2" or movie == "3" or movie == "4" or movie == "5" or movie == "6" or movie == "7" or
            movie == "8" or movie == "9" or movie == "10") : break
            else :  movie = input("Please make a selection between 1 and 10: ")
        movie = int(movie)
        movie -=1
        status =input(''' What would you like to change it to? \n 1.Not Completed \n 2. In Progress\n 3. Completed \n...: ''')
        while True :
            if (status == '1' or status == '2' or status == '3') : break
            else : status = input("Please make a selection between 1 and 3: ")
        status = int(status)
        for key in self.movie_dict:
            if key == list(self.movie_dict)[movie]:  # if the movie we want to change is in the dictionary
                if status == 1:
                    self.movie_dict[key] = 'Not Completed'
                elif status == 2:
                    self.movie_dict[key] = 'In Progress'
                elif status == 3:
                    self.movie_dict[key] = 'Completed'
                else:
                    print('Wrong input')
                return
    def view_tracker(self):
        inputs = input('What tracker would you like to view? \n 1. Not Completed \n 2.In Progress \n 3. Completed \n...: ')
        while True :
            if (inputs == '1' or inputs == '2' or inputs == '3') : break
            else : inputs = input("Please make a selection between 1 and 3: ")
        inputs = int(inputs)
        if inputs ==1:
            for key, value in self.movie_dict.items():
                if value == 'Not Completed':
                    print (f'Not Completed: {key}' )
            print('\n')
        elif inputs ==2:
            for key, value in self.movie_dict.items():
                if value == 'In Progress':
                    print (f'In Progress: {key}' )
            print('\n')
        elif inputs ==3:
            for key, value in self.movie_dict.items():
                if value == 'Completed':
                        print (f'Completed: {key}' )
            print('\n')
        else:
            print("That is not a valid input")

""" **************
User class
contains username and password as dict element

*
first function
Login() dictionary object
expected return is a bool
*

contains a tracker
"""
class User() :
    users = []

    def __init__(self, login):
        self.login = login
        User.users.append(self)
        User.tracker = Tracker()
        if len(User.users) == 1 : Tracker.super_movie_dict = mydict
        new_dict = Tracker.super_movie_dict.copy()
        User.tracker.populate_dict(new_dict)
       


    "Checks to see if inputed data will return an actual User"
    def Login() :
        username = input("Please enter your username: ")
        password = getpass(prompt='Please enter your password: ')
        for user in User.users :
            if username == user.login.get("username") :
                if password == user.login.get("password") :
                    return True
        
        return False
    
    def CreateAccount():
        answer = input("""Please choose an option:
        1: Create a user account
        2: Create an admin account
        ...: """)
        count = 0
        while count < 2:
            if (answer == "1" or answer == "2") : break
            elif count == 2 : return None
            answer = input("""Please make a valid selection:
            ...: """)
            count += 1


        username = ""
        password = ""

        unique_name_ = False
        while True :
            username = input("Please enter your username: ")  
            unique_name_ = True
            for user in User.users :
                if user.login.get("username") == username :
                    unique_name_ = False 
                    print(f"The username: {username} is already taken")

            if unique_name_ == True : 
                break


        unique_pass = False
        while True :
            password = input("Please enter your password: ")  
            unique_pass = True
            for user in User.users :
                if user.login.get("password") == password :
                    unique_pass = False 
                    print("This password is unavailble.")
                             
            if unique_pass == True : 
                break

        login = {"username" : str(username),
                "password" : str(password)}
        
        if answer == "1":
            new_user = User(login)
            return new_user
        else :
            new_user = Admin(login)
            return new_user



class Admin(User) :
    admin_ctr = 0
    admins = []

    def __init__(self, login):
        super().__init__(login)
        Admin.admins.append(self)
        Admin.admin_ctr += 1
    
    def is_admin(self) :
        for admin in Admin.admins :
            if self == admin :
                return True
        return False

    def edit_topic(self) :
        movies = list(Tracker.super_movie_dict.keys())
        print(movies)
        count = 1
        add_opt = 0
        exit_opt = 0
        for movie in movies :
            print(f"{count}. {movie}")
            count += 1
        print(f"{count}. Add Movie ")
        add_opt = count
        count+= 1
        print(f"{count}. exit")
        exit_opt = count

        option = input("Select a movie to edit: ")
        valid_options = []

        for i in range(count+1) :
            valid_options.append(str(i+1))
        while True : 
            if option in valid_options : break 
            else : option = input(f"Invalid option. Please choose between 1 and {exit_opt}: ")
            option = int(option)
        
        if option == add_opt :
            movie_name = input("Please enter movie name: ")
            status = input("""Is this movie \n1. In Progress \n2. Completed \n3.Not Completed \n...: """)
            valid_choice = ['1', '2', '3']
            while True :   
                if status in valid_choice : break            
                status = input(f"{status} not a valid choice, please choose between 1 and 3 \n...:")
            Tracker.super_movie_dict[str(movie_name)] = str(status)
            print("Movie successfully added!\n")

        else: 
            while True:
                action = input("""Would you like to change or remove this item. 
                Please write edit or remove: """ )
                match action :
                    case "edit" : 
                        new_name = input("What is the new name for this Movie: ")
                        status = Tracker.super_movie_dict[movies[int(option)-1]]
                        Tracker.super_movie_dict.pop(movies[int(option)-1])
                        Tracker.super_movie_dict[str(new_name)] = status
                        print("Movie successfully changed!\n")

                    case "remove" : 
                        Tracker.super_movie_dict.pop(option)
                        print("Movie successfully removed!\n")

                    case _: 
                        print("Invalid option")
                        continue
                break


UIinterface()