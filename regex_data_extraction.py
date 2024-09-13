import re

# Sample string generated, containing different data types
sample_text = '''
    Contact us at info@example.com or support@company.co.uk.
    Visit our website: https://www.example.com or http://subdomain.example.org/page.
    Call us at (123) 456-7890, 123-456-7890, or 123.456.7890.
    Credit card details: 1234 5678 9012 3456 or 1234-5678-9012-3456.
    The event starts at 14:30 (24-hour format) and ends at 2:30 PM (12-hour format).
    Tags: <div class="container"> <p>Paragraph</p> <img src="image.jpg" alt="description">
    Trending: #SoftwareEngineering #ThisIsAHashtag
    Prices: $19.99, $1,234.56
'''

# 1. Extracting Email Addresses


# 2. Extracting URLs

import re

def extract_urls(text):
    # Regular expression pattern for URLs
    url_regex = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'
    
    # Find all matches in the given text
    urls = re.findall(url_regex, text)
    
    return urls

# Example usage
example_text = """
    Visit https://www.example.com for more info.
    You can also check out http://subdomain.example.org/page.
    Invalid URL: htt://invalid.com should not be captured.
"""

# Call the function and print the result
extracted_urls = extract_urls(example_text)
print("Extracted URLs:", extracted_urls)


# 3. Extracting Phone Numbers (various formats)


# 4. Extracting Time in 12-hour or 24-hour format


# 5. Extracting Hashtags


# 6. Extracting Credit Card Numbers
print()
# Regular expression pattern for credit card numbers
cc_regex = r'\b\d{4}(?:[-\s])?\d{4}(?:[-\s])?\d{4}(?:[-\s])?\d{4}\b'

# Find all matches in the given text
credit_card_numbers = re.findall(cc_regex, sample_text)

print("Extracted Credit card numbers:", credit_card_numbers)
print()

# 7. Extracting HTML Tags


#regex to match HTML tags
html_tag_pattern = r'<[^>]+>'

#extracting all HTML tags using re.findall
html_tags = re.findall(html_tag_pattern, sample_text)

#outputting the extracted tags
print("Extracted HTML Tags:", html_tags)


# 8. Extracting Currency Amounts
