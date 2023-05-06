# -----------------------
# Import modules
# -----------------------
import re

# -----------------------
# Clean database
# -----------------------

# Define a multi-line RegEx expression
pattern = re.compile(
    r"^(?P<first_name>\w+)(?:\.? )(?P<last_name>\w+)"
    r"(?P<suffix> Jr\.|Sr\.)?(\.?)(?:[\%\$\{\}]{1,3} )?"
    r"(?P<email_address>(?P<email_name>\w+)(?P<email_second_name>\.\w+)?"
    r"(?P<email_third_name>\.\w+)?\@(?P<email_domain>hotmail|gmail|aol|outlook|yahoo|protonmail)(?:\.com))?"
    r"(?:[\%\$\{\}]{1,3} )?(?P<phone>\(\d{3}\) \d{3}\-\d{4})?(?:[\%\$\{\}]{1,3} )"
    r"(?P<address>\d+ (?:\w+ ?){1,}\.?)(?:[\%\$\{\}]{1,3} )?"
    r"(?P<ip_address>(([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])\.){3}([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5]))$",
    re.M
)

# Read database
rdir = "src/inputs/advanced_set.txt"

with open(rdir, 'r') as file:
    database = file.read()
    matches = pattern.finditer(database)

for match in matches:
    print(f'NAME: {match.group("first_name")}, {match.group("last_name")}')
    print(f'EMAIL ADDRESS: {match.group("email_address")}')
    print(f'IP ADDRESS: {match.group("ip_address")}')
    print('')