def get_reply(user_input):
    message = user_input.lower().strip()

    if message == "hello" or message == "hi":
        return "Hi!"
    elif message == "how are you":
        return "I'm fine, thanks!"
    elif message == "what is your name":
        return "I'm a simple Python chatbot."
    elif message == "bye":
        return "Goodbye!"
    else:
        return "Sorry, I don't understand that."

def start_chat():
    print("Chatbot is ready! Type 'bye' to exit.\n")

    while True:
        user_message = input("You: ")
        reply = get_reply(user_message)
        print("Bot:", reply)

        if user_message.lower().strip() == "bye":
            break

start_chat()