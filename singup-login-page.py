users = {}

try:
    with open('users.txt', 'r') as f:
        for line in f:
            stored_username, stored_password = line.strip().split(',')
            users[stored_username] = stored_password
except FileNotFoundError:
    pass

logged_in = False
#This code allows users to sign up using a username and password.
while not logged_in:
    action = input("Do you want to sign up or log in?").strip().lower()

    if action == 'signup' or action == 'sign up':
        username  = input("Please enter a username:")
        password = input("Please enter a password:")
    
        if username in users:
            print("This username is already being used. Please choose a new one.")
        else:
            users[username] = password

            with open('users.txt', 'a') as f:
                f.write("{},{}\n".format(username, password))
                print("You are signed up!")

#This code allows users to login with the username and password they set.
    elif action == 'login' or action == 'log in':
        attempts = 0

        while attempts < 5 :
            username = input("Please enter your username:")
            password = input("Please enter you password:")
            attempts += 1
            if username not in users or users[username] != password:
                print("Incorrect username or password.")
            else:
                print("You're logged in!")
                logged_in = True
                break
        if attempts >= 5:
            print("Login failed.")
    else:
        print("Invalid input")
