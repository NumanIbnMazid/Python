# Key Value Pairs, Key must be unique

monthConversion = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

print(monthConversion["Nov"])

# get will set a default value if not found
print(monthConversion.get("Luv", "Not a valid Key"))

