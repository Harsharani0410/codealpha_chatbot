def get_response(user_input):
    """Return a predefined reply based on simple keyword matching."""
    text = user_input.lower().strip()

    if text in ("hello", "hi", "hey"):
        return "Hi! How can I help you today?"
    elif "how are you" in text:
        return "I'm fine, thanks! How about you?"
    elif "your name" in text:
        return "I'm ChatBot, a simple rule-based assistant."
    elif "help" in text:
        return "I can chat about basic things. Try saying hello, asking how I am, or saying bye."
    elif "thank" in text:
        return "You're welcome!"
    elif text in ("bye", "goodbye", "exit", "quit"):
        return "Goodbye! Have a great day."
    else:
        return "Sorry, I didn't understand that. Could you rephrase?"

def chat():
    print("ChatBot: Hi! I'm a simple rule-based chatbot. Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print("ChatBot:", response)

        if user_input.lower().strip() in ("bye", "goodbye", "exit", "quit"):
            break

if __name__ == "__main__":
    chat()
