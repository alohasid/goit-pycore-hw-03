from datetime import datetime, timedelta
from typing import List, Dict

def get_upcoming_birthdays(users: List[Dict[str, str]]) -> List[Dict[str, str]]:
    current_date = datetime.today().date()
    date_format = "%Y.%m.%d"
    results = []

    for user in users:
        try:
            birthday = datetime.strptime(user['birthday'], date_format).date()
            
            birthday_this_year = birthday.replace(year=current_date.year)

            if birthday_this_year < current_date:
                birthday_this_year = birthday_this_year.replace(year=current_date.year + 1)

            delta_days = (birthday_this_year - current_date).days

            if 0 <= delta_days <= 7:
                if birthday_this_year.weekday() == 5:
                    birthday_this_year += timedelta(days=2)
                elif birthday_this_year.weekday() == 6:
                    birthday_this_year += timedelta(days=1)

                results.append({
                    "name": user['name'], 
                    "congratulation_date": birthday_this_year.strftime(date_format)
                })

        except ValueError:
            raise ValueError("Incorrect data format, should be YYYY.MM.DD")

    return results

users = [
    {"name": "John Doe", "birthday": "1985.09.21"},
    {"name": "Jane Smith", "birthday": "1990.09.22"},
]

# users_with_exceptions = [
#     {"name": "John Doe", "birthday": "1985-09-21"},
#     {"name": "Jane Smith", "birthday": "1990-09-22"},
# ]

# upcoming_birthdays_with_exception = get_upcoming_birthdays(users_with_exceptions)

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
