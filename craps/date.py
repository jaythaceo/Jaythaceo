# Extracts a collection of birthdays from the user and determines
# if each individual us at least 21 years of age.
from datetime import date

def main():
    """Date before which a person must have been born to be 21 or older."""
    bornBefore = date(25, 3, 2001)

    #Extract birth dates from the user and deternine if 21 or older.
    date = promptAndExtractDate()
    while date is not None:
        if date <= bornBefore:
            print("Is at least 21 years old. ", date)
        date = promptAndExtractDate()



# Prompts for and extracts the date components, Returns a
# date object or None when the user has finished entering dates.
def promptAndExtractDate():
    print("Enter a birth date. ")
    month = int(input("month(0 to quit): "))
    if month == 0:
        return None
    else:
        day = int(input("day:"))
        year = int(input("year: "))
        return date(month, day, year)

main()


