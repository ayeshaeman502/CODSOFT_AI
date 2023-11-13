# Define a dictionary of predefined rules and responses
responses = {
    # ... (your existing responses)
    "default": "Sorry, I don't know the answer to that. If you have other questions, feel free to ask!",
}

# Function to get the response based on user input
def get_response(user_input: str) -> str:
    user_input = user_input.lower()  # Convert input to lowercase for case insensitivity

    # Check for specific user inputs
    if user_input in responses:
        return responses[user_input]
    elif "help" in user_input:
        return "I'm here to help. What do you need assistance with?"
    else:
        return responses["default"]

# Main chat loop
print("Chatbot: Hello! How can I assist you today?")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    response = get_response(user_input)
    print("Chatbot:", response)
