print("Welcome to the Elementary Chatbot!")
print("You can start chatting. Type 'bye' to exit.")

while True:
    user_input = input("You: ")

    if user_input.lower() == "bye":
        print("Chatbot: Goodbye! Have a nice day.")
        break
    elif user_input.lower() in ["hi", "hello"]:
        print("Chatbot: Hello! How can I help you?")
    elif user_input.lower() == "how are you":
        print("Chatbot: I am fine, but I'm just a chatbot and I don't have feelings.")
    else:
        print("Chatbot: Please enter a valid input.")
        