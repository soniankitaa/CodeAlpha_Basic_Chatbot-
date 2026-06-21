import datetime

# Store chat history
chat_history = []

# Store user information
user_name = ""


def save_chat(user, bot):
    chat_history.append(f"You: {user}")
    chat_history.append(f"Bot: {bot}")


def show_help():
    print("\nAvailable Commands:")
    print("- hello")
    print("- how are you")
    print("- what is your name")
    print("- my name is <your name>")
    print("- time")
    print("- date")
    print("- calculator")
    print("- history")
    print("- help")
    print("- bye\n")


def calculator():
    print("\nSimple Calculator")

    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operation (+ - * /): ")
        num2 = float(input("Enter second number: "))

        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            if num2 == 0:
                return "Cannot divide by zero."
            result = num1 / num2
        else:
            return "Invalid operator."

        return f"Result = {result}"

    except ValueError:
        return "Invalid input."


def get_response(user_input):
    global user_name

    message = user_input.lower().strip()

    if message == "hello":
        return f"Hello {user_name if user_name else 'there'}!"

    elif message == "hi":
        return "Hi! How can I help you today?"

    elif message == "how are you":
        return "I am doing great. Thanks for asking."

    elif message == "what is your name":
        return "My name is SmartBot."

    elif message.startswith("my name is"):
        user_name = user_input[11:].strip()

        if user_name:
            return f"Nice to meet you, {user_name}!"
        else:
            return "Please tell me your name properly."

    elif message == "time":
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        return f"Current Time: {current_time}"

    elif message == "date":
        current_date = datetime.datetime.now().strftime("%d-%m-%Y")
        return f"Today's Date: {current_date}"

    elif message == "calculator":
        return calculator()

    elif message == "history":

        if not chat_history:
            return "No chat history available."

        print("\n------ CHAT HISTORY ------")

        for line in chat_history:
            print(line)

        print("--------------------------")

        return "History displayed."

    elif message == "help":
        show_help()
        return "Help menu displayed."

    elif message == "thank you":
        return "You're welcome."

    elif message == "bye":
        return "Goodbye! Have a wonderful day."

    else:
        return (
            "Sorry, I don't understand that. "
            "Type 'help' to see available commands."
        )


def chatbot():
    print("=" * 50)
    print("      SMART RULE-BASED CHATBOT")
    print("      Internship Project")
    print("=" * 50)

    print("\nType 'help' to view commands.")
    print("Type 'bye' to exit.\n")

    total_messages = 0

    while True:

        user_input = input("You: ")

        total_messages += 1

        response = get_response(user_input)

        print("Bot:", response)

        save_chat(user_input, response)

        if user_input.lower().strip() == "bye":
            break

    print("\nSession Summary")
    print("----------------")
    print("Messages Exchanged:", total_messages)
    print("User Name:", user_name if user_name else "Not Provided")
    print("Thank you for using SmartBot!")


# Start Program
chatbot()