import tkinter as tk
from tkinter import scrolledtext

class Chatbot:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Chatbot")
        
        # Create chat display area
        self.chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled')
        self.chat_display.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        
        # Create input field
        self.input_field = tk.Entry(root, width=50)
        self.input_field.grid(row=1, column=0, padx=10, pady=10)
        
        # Create send button
        self.send_button = tk.Button(root, text="Send", command=self.send_message)
        self.send_button.grid(row=1, column=1, padx=10, pady=10)
        
        # Bind Enter key to send message
        self.root.bind('<Return>', self.send_message)

    def send_message(self, event=None):
        user_input = self.input_field.get().strip().lower()
        if user_input:
            self.display_message("You: " + user_input)
            self.input_field.delete(0, tk.END)
            self.respond_to_message(user_input)
    
    def display_message(self, message):
        self.chat_display.configure(state='normal')
        self.chat_display.insert(tk.END, message + '\n')
        self.chat_display.configure(state='disabled')
        self.chat_display.yview(tk.END)

    def respond_to_message(self, user_input):
        response = self.generate_response(user_input)
        self.display_message("Chatbot: " + response)

    def generate_response(self, user_input):
        # Predefined responses based on user input
        if user_input in ["hi", "hello", "hey"]:
            return "Hello! How can I help you today?"
        elif "how are you" in user_input:
            return "I'm just a program, so I don't have feelings, but thank you for asking!"
        elif "your name" in user_input or "who are you" in user_input:
            return "I am a simple chatbot created by a Python script."
        elif "bye" in user_input or "goodbye" in user_input or "exit" in user_input:
            return "Goodbye! Have a great day!"
        else:
            return "I'm sorry, I don't understand that. Can you rephrase your question?"

# Initialize the Tkinter root window
root = tk.Tk()

# Create and run the chatbot application
chatbot = Chatbot(root)
root.mainloop()
