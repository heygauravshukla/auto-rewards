# Script for grinding ms rewards at level 2.
import pyautogui
import time
import random


def search_windows(query):
    pyautogui.hotkey("win", "s")
    time.sleep(2)  # Wait for the search bar to appear
    pyautogui.write(query)
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(15)  # Wait for the search results to appear
    pyautogui.hotkey("ctrl", "w")  # Close the opened tab
    time.sleep(2)  # Wait for the tab to be closed


search_items = [
    "leetcode",
    "w3schools",
    "programiz",
    "javatpoint",
    "takeuforward",
    "geeksforgeeks",
    "tutorialspoint",
    "bing homepage quiz",
    "online c++ formatter",
    "coding ninjas studio",
    # Add more search items here
]

# Shuffle the search items in place
random.shuffle(search_items)

for item in search_items:
    print(f"Searching for: {item}")
    search_windows(item)


print(f"Congratulations! You've earned MS rewards.")
