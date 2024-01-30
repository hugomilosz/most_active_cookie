#!/usr/bin/env python
import argparse
from collections import Counter
from datetime import datetime


def get_most_active_cookie(filename, date_str):
    date = datetime.strptime(date_str, '%Y-%m-%d').date()

    with open(filename, 'r') as file:
        lines = file.readlines()

    cookies = []

    # Iterate through each line of the file
    for line in lines:
        cookie, timestamp = line.strip().split(',')
        timestamp_date = datetime.fromisoformat(timestamp).date()

        # Append to cookies list if the date matches
        if timestamp_date == date:
            cookies.append(cookie)
        # If the cookie date is before the requested date, break the loop (cookies sorted in reverse order of dates)
        elif timestamp_date < date:
            break

    if cookies:
        # Get cookies with the maximum count
        cookie_counts = Counter(cookies)
        most_active_cookies = [cookie for cookie, count in cookie_counts.items() if count == max(cookie_counts.values())]
        return most_active_cookies

    return None


if __name__ == "__main__":
    # CLI parsing - includes argument prompts for user
    parser = argparse.ArgumentParser(description='Find the most active cookie for a specific day.')
    parser.add_argument('-f', '--filename', help='Path to the cookie log file', required=True)
    parser.add_argument('-d', '--date', help='Date in the format YYYY-MM-DD', required=True)
    args = parser.parse_args()

    # Get the most active cookie for a specific date and print to terminal
    most_active_cookies = get_most_active_cookie(args.filename, args.date)
    if not most_active_cookies:
        print("No cookies found for the provided date")
    else:
        for cookie in most_active_cookies:
            print(cookie)
