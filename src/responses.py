import random

def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == "/rand":
        return (str(random.randint(1, 10)) + ' hea auf spammen')
    
    if p_message == "/help":
        return "`/rand` returns a random number between 0 and 10" + "\n" + "`/leetify <steamlink>` searches for the entered user's Leetify profile and returns a link to it" + "\n" + "more coming soon..."
    
    if "/leetify" in p_message:
        steamid = p_message.split(" ")[1]
        steamid = steamid.split("/")[4]
        return "Leetify profile: https://leetify.com/app/profile/" + steamid
    
    return "Unknown command, try `/help` for a list of commands."