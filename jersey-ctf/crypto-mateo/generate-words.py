from datetime import datetime

# Birth dates from the conversation
dates_info = [
    {"name": "Jennifer", "birthday": "09/16/1979"},
    {"name": "Mateo", "birthday": "09/18/2010"},  # Assuming the year based on his current age of 45
    {"name": "Melia", "birthday": "09/18/2011"}   # Assuming the year based on her age of 13 in 2024
]

# Define all possible date formats
date_formats = [
    "%m%d%Y", "%d%m%Y", "%Y%m%d",  # No separator
    "%m-%d-%Y", "%d-%m-%Y", "%Y-%m-%d",  # Dash separator
    "%m/%d/%Y", "%d/%m/%Y", "%Y/%m/%d",  # Slash separator
    "%m%d%y", "%d%m%y", "%y%m%d",  # No separator with two-digit year
    "%m-%d-%y", "%d-%m-%y", "%y-%m-%d",  # Dash separator with two-digit year
    "%m/%d/%y", "%d/%m/%y", "%y/%m/%d",  # Slash separator with two-digit year
]

# Create a wordlist with all possible date format permutations for each date
wordlist = set()
for date_info in dates_info:
    # Parse the date
    birthday = datetime.strptime(date_info["birthday"], "%m/%d/%Y")
    # Generate dates with all formats
    for fmt in date_formats:
        formatted_date = birthday.strftime(fmt)
        wordlist.add(formatted_date)

# Print the wordlist

with open('wordlist.txt', 'w') as f:
    for word in sorted(wordlist):
        f.write(f"{word}\n")
