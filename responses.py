import random

"""
This function is responsible for responding to the user's input with a message. 
If the user inputs 'hello' or 'roll', the program will respond with a fixed messages. 
Otherwise, it will respond with an error message notifying the user of an invalid input. 
"""


def get_response(message: str) -> str:
    p_message = message.lower()
    if p_message == 'hello':
        return 'Hello!'

    if p_message == 'roll':  # roll a random number
        return str(random.randint(1, 6))

    if p_message == '!help':
        return 'No one can help you here'

    return 'I didn\'t understand what you wrote. Try typing "!help"'
