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
    time.sleep(8)  # Wait for the search results to appear
    pyautogui.hotkey("ctrl", "w")  # Close the opened tab
    time.sleep(2)  # Wait for the tab to be closed


search_items = [
    "Stack Overflow",
    "GitHub",
    "TechCrunch",
    "Wired",
    "Hacker News",
    "Ars Technica",
    "The Verge",
    "Mashable",
    "Engadget",
    "TechRadar",
    "Codecademy",
    "FreeCodeCamp",
    "GeeksforGeeks",
    "Hackaday",
    "SitePoint",
    "Smashing Magazine",
    "CodeProject",
    "Tuts+",
    "TechTarget",
    "TechRepublic",
    "InfoWorld",
    "CNET",
    "DZone",
    "CodePen",
    "Bitbucket",
    "Dribbble",
    "Product Hunt",
    "TechGig",
    "HackerRank",
    "LeetCode",
]


# Shuffle the search items in place
random.shuffle(search_items)

for item in search_items:
    print(f"Searching for: {item}")
    search_windows(item)


print(f"Congratulations! You've earned MS rewards.")
