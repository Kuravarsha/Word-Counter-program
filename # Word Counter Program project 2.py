# Word Counter Program

def count_words(text):
    """
    Function to count the number of words in the given text.
    """
    words = text.split()  # Splitting the text by spaces to get individual words
    return len(words)

def main():
    """
    Main function to handle user input and display the word count.
    """
    # Prompt the user to enter a sentence or paragraph
    user_input = input("Please enter a sentence or paragraph: ").strip()
    
    # Error Handling: Check if the input is empty
    if not user_input:
        print("Error: You entered an empty string. Please provide some text.")
    else:
        # Counting the words
        word_count = count_words(user_input)
        
        # Output Display: Show the word count
        print(f"The number of words in the entered text is: {word_count}")

# Ensuring the main function is called when the script is executed
if __name__ == "__main__":
    main()
