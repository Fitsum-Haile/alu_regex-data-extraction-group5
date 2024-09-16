mport re

# Define the regular expressions for time and hashtags
time_pattern = r'\b(?:[01][0-9]|2[0-3]):[0-5][0-9]\b|(?:0?[1-9]|1[0-2]):[0-5][0-9] ?(?:AM|PM)\b'
hashtag_pattern = r'#\w+'

# Sample text containing both times and hashtags
text = """
The meeting is at 14:30.
Lunch is at 12:00 PM.
The deadline is 23:59 tonight.
Here are some hashtags: #example, #ThisIsAHashtag, and #Python.
Some more text without hashtags.
"""

# Find all matches for time and hashtags
times = re.findall(time_pattern, text)
hashtags = re.findall(hashtag_pattern, text)

# Print the results
print("Times found:", times)
print("Hashtags found:", hashtags)

