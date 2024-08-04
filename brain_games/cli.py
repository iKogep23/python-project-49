import prompt


def welcome_user():
    '''Greeting and returning the username.'''
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name
