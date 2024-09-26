#!/usr/bin/env python3
"""
Daily Quote Generator

This script selects a random quote for the day and prints it. Optional: The same quote should be generated for a given day.

Your task:
1. Complete the get_quote_of_the_day() function
2. Set up a cron job to run this script daily at 8:00 AM and append the output to a file

Hint: Look up `random.choice()` to select a random item from a list. You can use the `date` module to get the current date and set a seed for the random number generator.
"""

import random
from datetime import date


quotes = [
    # Create a list of quotes here
    "When I saw you I fell in love, and you smiled because you knew",
    "Anyone can be a God or a devil. All it takes is for people to believe it",
    "You either die a hero or you live long enough to see yourself become the villain",
    "Life can only be understood backwards but it must be lived forwards",
    "Time doesn't heal anything, it just teaches us how to live with the pain",
    "In the end, we will remember not the words of our enemies, but the silence of our friends"
]

def get_quote_of_the_day(quotes):
    todays_quote = None

    # Your code here
    todays_quote = random.choice(quotes)
    return todays_quote

if __name__ == "__main__":
    print(get_quote_of_the_day(quotes))

# Cron job (add this to your crontab):
# [minute] [hour] [day-of-month] [month] [day-of-week]
# 0 8 * * * /usr/bin/python3 /path/to/quote_generator.py >> /path/to/daily_quote.txt