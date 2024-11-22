import re
from datetime import datetime


def format_phone_number(phone: str) -> str:
    """
    Formats the phone number to a standard format.
    :param phone: phone number to format
    :return: formatted phone number
    """
    # Remove all non-digits and blank spaces
    phone = re.sub(r"\D", "", phone)
    phone = re.sub(r"\s+", "", phone)
    # Format the phone number
    return f"{phone[0:3]} {phone[3:6]} {phone[6:]}"


def count_digits(s: str) -> int:
    """
    Counts the number of digits in a string.
    :param s: string to count digits in
    :return: number of digits in the string
    """
    return sum(c.isdigit() for c in s)


def get_ordinal_suffix(day):
    if 11 <= day <= 13:  # Special case for 11th, 12th, 13th
        return "th"
    if day % 10 == 1:  # 1st
        return "st"
    if day % 10 == 2:  # 2nd
        return "nd"
    if day % 10 == 3:  # 3rd
        return "rd"
    return "th"  # All other cases


def format_date(date: datetime.date) -> str:
    """
    Formats the date to a standard format.
    :param date: date to format
    :return: formatted date
    """
    day = date.day
    month = date.strftime("%B")  # Full month name
    year = date.year

    return f"{month} {day}{get_ordinal_suffix(day)}, {year}"
