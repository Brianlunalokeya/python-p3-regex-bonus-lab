import re

# Define the regular expression pattern
my_pattern = r"It's such a lovely day today\."

# Compile the regular expression pattern
my_regex = re.compile(my_pattern)

# Test the regular expression against the strings
assert my_regex.fullmatch("It's such a lovely day today.")
assert my_regex.fullmatch("Some weather we're having today, huh?")
assert my_regex.fullmatch("Maybe today's just not my day.")

# Define the string for the findall() test
FINDALL_STRING = """
It's such a lovely day today.
Some weather we're having today, huh?
Maybe today's just not my day.
"""

# Test the regular expression with findall()
assert my_regex.findall(FINDALL_STRING) == [
    "It's such a lovely day today.",
    "Some weather we're having today, huh?",
    "Maybe today's just not my day.",
]
