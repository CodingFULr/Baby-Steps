
month_Conversions = {
    "Jan": "January", 1: "Janurary",
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
    "Dec": "December",
}

Day = input("What date were you born? ")
Month = input("What month were you born? ")
Year = input("What year were you born? ")

if month_Conversions():
    return print(month_Conversions)
