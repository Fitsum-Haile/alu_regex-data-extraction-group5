import re

# Function to load sample text from a file
def load_sample_text(filename):
    with open(filename, 'r') as file:
        return file.read()

# 1. Extracting Email Addresses

# 2. Extracting URLs

# 3. Extracting Phone Numbers (various formats)

# 4. Extracting Time in 12-hour or 24-hour format

# 5. Extracting Hashtags

# 6. Extracting Credit Card Numbers

# 7. Extracting HTML Tags
def extract_html_tags(text):
    html_tag_pattern = r'</?[a-zA-Z][a-zA-Z0-9\-]*(\s+[a-zA-Z\-]+(\s*=\s*(".*?"|\'.*?\'|[^\s>]+))?)*\s*/?>'
    return re.findall(html_tag_pattern, text)

# 8. Extracting Currency Amounts

# Main function to load the text and run the extractions
def main():
    # Load the sample text from the file
    sample_text = load_sample_text('sample_text.txt')

    # Extract and print different types of data
    print()
    print("------------------------------------------------------------")
    print("Extracted information")
    print("------------------------------------------------------------")
    print()
    print("Extracted Email Addresses:", extract_emails(sample_text))
    print()
    print("Extracted URLs:", extract_urls(sample_text))
    print()
    print("Extracted Phone Numbers:", extract_phone_numbers(sample_text))
    print()
    print("Extracted Times:", extract_times(sample_text))
    print()
    print("Extracted Hashtags:", extract_hashtags(sample_text))
    print()
    print("Extracted Credit Card Numbers:", extract_credit_cards(sample_text))
    print()
    print("Extracted HTML Tags:", extract_html_tags(sample_text))
    print()
    print("Extracted Currency Amounts:", extract_currency_amounts(sample_text))
    print()

if __name__ == '__main__':
    main()
