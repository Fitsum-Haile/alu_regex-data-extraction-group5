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

emails = re.findall(r'[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', sample_text)
print ("Email adresses:")
for email in emails:
    print (emails)

# 2. Extracting URLs


# 3. Extracting Phone Numbers (various formats)


# 4. Extracting Time in 12-hour or 24-hour format


# 5. Extracting Hashtags


# 6. Extracting Credit Card Numbers


# 7. Extracting HTML Tags


#regex to match HTML tags
html_tag_pattern = r'<[^>]+>'

#extracting all HTML tags using re.findall
html_tags = re.findall(html_tag_pattern, sample_text)

#outputting the extracted tags
print("Extracted HTML Tags:", html_tags)


# 8. Extracting Currency Amounts
