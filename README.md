#Data Extraction Script

This Python script extracts various types of data from a text file using regular expressions. It handles extracting emails, URLs, phone numbers, times, hashtags, credit card numbers, HTML tags, and currency amounts.

#Features

Extract Email Addresses: Identifies email addresses in the text.
Extract URLs: Finds and extracts web addresses (http and https).
Extract Phone Numbers: Detects phone numbers in various formats (e.g., 123-456-7890, (123) 456-7890).
Extract Time: Recognizes times in both 12-hour and 24-hour formats.
Extract Hashtags: Identifies hashtags (e.g., #example) from social media-like text.
Extract Credit Card Numbers: Extracts credit card numbers that match standard patterns.
Extract HTML Tags: Finds and extracts HTML tags from the text.
Extract Currency Amounts: Recognizes currency values like $100.00, £50, etc.

#Installation

-Clone the repository.
-Ensure Python is installed on your system.
No additional external dependencies are required as the script uses Python's built-in re module.

#Usage

Place your text file (e.g., sample_text.txt) in the same directory as the script.

#Run the script:

python script.py
The script will extract and display the data based on the patterns listed above.


#Requirements

-Python 3.x
-re module (part of Python’s standard library)

