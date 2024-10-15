import nltk
from nltk.chat.util import Chat

# Download required NLTK data
nltk.download('punkt')

# Define chatbot pairs (patterns and responses)
pairs = [
    ["hi", "hello there! how can i help you?"],
    ["what is your name", "my name is chatbot"],
    ["how are you", "i'm doing well, thanks for asking! how are you?"],
    ["what is the weather like", "the weather is sunny today"],
    ["what is the capital of india", "the capital of india is new delhi"],
    ["who is the prime minister of india", "the prime minister of india is narendra modi"],
    ["thanks", "you're welcome!"],
    ["goodbye", "goodbye! have a nice day!"]
]

# Create a chatbot object
chatbot = Chat(pairs)

# Start the conversation
print("Welcome to Chatbot!")
print("Type 'quit' to exit.")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        print("Chatbot: Goodbye!")
        break
    response = chatbot.respond(user_input)
    print("Chatbot:", response)