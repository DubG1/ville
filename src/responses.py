import random

def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == "/rand":
        return str(random.randint(0, 10))
    
    if p_message == "/help":
        return "`/rand` returns a random number between 0 and 10"
    
    return "Uknown command, try `/help` for a list of commands."