import pyautogui
import time
import random


# Function to search for a query in Windows search
def search_windows(query):
    pyautogui.hotkey("win", "s")  # Press Windows key + S to open search
    time.sleep(2)  # Wait for the search bar to appear
    pyautogui.write(query)  # Type the query
    time.sleep(1)  # Wait for the search to start
    pyautogui.press("enter")  # Press Enter to initiate the search
    time.sleep(8)  # Wait for the search results to appear
    pyautogui.hotkey("ctrl", "w")  # Close the opened tab
    time.sleep(2)  # Wait for the tab to be closed


# List of items to search for
search_items = [
    "Stack Overflow",
    "GitHub",
    "TechCrunch",
    "Hacker News",
    "Codecademy",
    "FreeCodeCamp",
    "GeeksforGeeks",
    "Dribbble",
    "CodePen",
    "HackerRank",
]

# Shuffle the search items randomly
random.shuffle(search_items)

# Loop through each item and search for it
for item in search_items:
    print(f"Searching for: {item}")
    search_windows(item)

# Message indicating completion
print("Congratulations! You've earned MS rewards.")
