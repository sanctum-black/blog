# -----------------------
# Import modules
# -----------------------

import re

# -----------------------
# Example 1: A simple string
# -----------------------

# Declare string
mystring = """
Mr. John Smith
Mrs. Catherina Jones
Mr. Kali Smith
Mrs. Jenneth Smith
"""
# Check string
print(mystring)

# Declare pattern
pattern = re.compile(r"^Mrs\. \w+ \w+", re.M)

## Using finditer

# Match & print
matches = pattern.finditer(mystring)
[x for x in matches]

# Match without compiling
matches = re.finditer(r"^Mrs\. \w+ \w+", mystring, re.M)
[x for x in matches]

## Using findall
matches = pattern.findall(mystring)
matches

## Using match
mystring = "Hello World"
pattern = re.compile(r"[A-Za-z]+ [A-Za-z]+")
match = pattern.match(mystring)
print(match)

mystring = """
Mr. John Smith
Mrs. Catherina Jones
Mr. Kali Smith
Mrs. Jenneth Smith
"""

pattern = re.compile(r"^Mrs\. \w+ \w+", re.M)
match = pattern.search(mystring)
print(match)

# -----------------------
# Example 2: Operating on re.Match objects
# -----------------------

# Declare a string
mystring = r"""
John Doe, johndoe@email.com, (123) 456-7890, 123 Main St.
Jane Smith, jane.smith@email.com, (234) 567-8901, 456 Elm St.
Robert Johnson, robert.johnson@email.com, (345) 678-9012, 789 Oak Ave.
Sarah Lee, sarah_lee@email.com, (456) 789-0123, 234 Pine St.
Michael Brown, michael.brown@email.com, (567) 890-1234, 567 Maple Dr.
Lisa Davis, lisa.davis@email.com, (678) 901-2345, 890 Cedar Rd.
David Rodriguez, david.rodriguez@email.com, (789) 012-3456, 1234 Willow Way
Emily Kim, emily.kim@email.com, (890) 123-4567, 5678 Birch Blvd.
James Johnson, james_johnson@email.com, (901) 234-5678, 9012 Pine St.
"""

# Declare a regular expression
pattern = re.compile(r"(?<=\.com\, )\(\d{3}\) \d{3}\-\d{4}\b", re.M)

# Match using finditer()
matches = pattern.finditer(mystring)

# Print matches
for match in matches:
    # Print complete phone numbers
    print(f"Full re.Match object: {match}\n")

    # Print match locations in body of text
    #  (returns tuple)
    print(f"Match Location: {match.span()}\n")

    # Print start and end of each match
    print(f"Start Index: {match.start()} ; End Index: {match.end()}\n")

    # Print length
    print(f"Phone Number Length: {match.end() - match.start()}\n")

    # Print the actual phone number
    print(f"Phone Number: {match.group()}\n")