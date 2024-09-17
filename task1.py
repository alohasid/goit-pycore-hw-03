from datetime import datetime

def get_days_from_today(date: str) -> int:
    try:
        converted_date = datetime.strptime(date, "%Y-%m-%d")
        current_date = datetime.today()

        return abs((current_date - converted_date).days) # I needed this abs to get a positive value, because the difference in days can be negative
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")

delta = get_days_from_today("2021-10-09") # 1075 17.09.2024
# with_exception = get_days_from_today("2021.10.10") # ValueError Incorrect data format, should be YYYY-MM-DD
print(delta)