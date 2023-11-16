import re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              # area code
    (\s|-|\.)?                      # seperator
    \d{3}                           # first 3 digits
    (\s|-|\.)                       # seperator
    \d{4}                           # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?    # extension    
    )''', re.VERBOSE)

# Explanation of the regex above
# 1 - it should be random 3 digits number or an area code(inside brackets)
# 2 - it should be a whitespace character, a dash or a dot
# 3 - it should be a random 3 digit number
# 4 - same as (2) above 
# 5 - it should be a random 4 digit number 
# 6 - it should be an extension? im not too sure of this one
