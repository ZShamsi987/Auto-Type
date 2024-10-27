import pyautogui
import time

def human_typing(text, wpm):
    # Calculate the delay between each word based on WPM
    words_per_second = wpm / 60
    delay_between_words = 1 / words_per_second

    # Split the text into words
    words = text.split()

    # Simulate typing
    for word in words:
        pyautogui.typewrite(word + ' ')
        time.sleep(delay_between_words)  # Wait before typing the next word

# Function to read text from a .txt file
def read_text_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    return text

# Example usage
if __name__ == "__main__":
    file_path = "/Users/zafirshamsi/Downloads/biz org full essay q1.txt"  # Replace with the path to your .txt file
    typing_speed_wpm = 1500  # Change this to your desired WPM

    text_to_type = read_text_file(file_path)
    print("Starting in 5 seconds. Make sure to click on the text area where you want to type.")
    time.sleep(5)  # Wait for 5 seconds to allow you to focus the input area
    human_typing(text_to_type, typing_speed_wpm)
