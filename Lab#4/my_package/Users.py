def user_input(text):
    with open('users_input.txt', 'w', encoding = 'utf-8') as file:
        file.write(text)