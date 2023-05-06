# -----------------------
# Import modules
# -----------------------
import re

# -----------------------
# Clean database
# -----------------------

# Define a multi-line RegEx expression
pattern = re.compile(
    r"^(?P<first_name>[A-Za-z]+)(?:\.? )(?P<last_name>[A-Za-z]+\.?)"
    r"(?P<suffix> Jr\.|Sr\.)?(?:[\%\$\{\}]{1,} )?"
    r"(?P<email_address>(?P<email_name>[\w\-\.\_]+)\@"
    r"(?P<email_domain>hotmail|gmail|aol|outlook|yahoo|protonmail)(?:\.com))?(?:[\%\$\{\}]{1,} )?"
    r"(?P<phone>\(\d{3}\) \d{3}\-\d{4})?(?:[\%\$\{\}]{1,} )"
    r"(?P<address>\d+ (?:\w+ ?){1,}\.?)(?:[\%\$\{\}]{1,} )?"
    r"(?P<ip_address>(([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])\.){3}([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5]))$",
    re.M
)

# Read database
rdir = "src/inputs/advanced_set.txt"

with open(rdir, 'r') as file:
    database = file.read()
    matches = pattern.finditer(database)

# Print required captured groups
for match in matches:
    print(f'NAME: {match.group("first_name")}, {match.group("last_name")}')
    print(f'EMAIL ADDRESS: {match.group("email_address")}')
    print(f'PHONE NO.: {match.group("phone")}')
    print(f'IP ADDRESS: {match.group("ip_address")}')
    print('')