def chatbot_response(user_input):
    user_input = user_input.lower()

    if user_input == "hello":
        return "Hi! Nice to meet you 😊"
    
    elif user_input == "how are you":
        return "I'm fine, thanks! How about you?"
    
    elif user_input == "what is your name":
        return "I'm a simple rule-based chatbot 🤖"
    
    elif user_input == "who created you":
        return "I was created by a Python programmer 😉"
    
    elif user_input == "help":
        return "You can try: hello, how are you, time, date, joke, bye"
    
    elif user_input == "time":
        return "Sorry, I can't show real time yet ⏰"
    
    elif user_input == "date":
        return "Sorry, I can't show today's date yet 📅"
    
    elif user_input == "joke":
        return "Why do programmers love Python? Because it's easy to understand 😄"
    
    elif user_input == "thank you":
        return "You're welcome! 😊"
    
    elif user_input == "bye":
        return "Goodbye! Have a great day 👋"
    
    else:
        return "Sorry, I don't understand that. Type 'help' for options."


# Main loop
print("🤖 Chatbot Started! (type 'bye' to exit)")

while True:
    user = input("You: ")
    reply = chatbot_response(user)
    print("Bot:", reply)

    if user.lower() == "bye":
        break
