print("🤖 Welcome to My Python Chatbot!")
print("Type 'bye' to exit.")

while True:
    message = input("You: ").lower().strip()

    if message == "bye":
        print("Bot: Goodbye! Keep learning Python!")
        break

    elif "hello" in message or "hi" in message:
        print("Bot: Hello! How can I help you?")

    elif "your name" in message:
        print("Bot: I am Python Buddy!")

    elif "how are you" in message:
        print("Bot: I am fine! Thank you.")

    elif "python" in message:
        print("Bot: Python is a beginner-friendly programming language.")

    else:
        print("Bot: Sorry, I don't know that yet.")
