'''File for remembering users' birthdays'''
from datetime import date, datetime, timedelta


def get_birthdays_per_week(users):
    '''Function to create a dictionary with usernames and their birthday dates'''
    week_birthdays = {}
    for user in users:
        user_name = user['name'].split()[0]
        birthday = user['birthday']
        today = date.today()
        sunday = 6 - today.weekday()
        date_sunday = today.replace(day=today.day + sunday)
        days = []
        user_names = []

        if birthday < today:
            birthday = birthday.replace(year=today.year + 1)

        weekday_birth = birthday.strftime('%A')

        if not (birthday > today and birthday < today + timedelta(days=7)):
            continue

        for day in range(today.weekday(), date_sunday.weekday() + 1):
            day = (today + timedelta(days=day)).strftime('%A')
            days.append(day)

            if weekday_birth == day:
                if day == 'Saturday' or day == 'Sunday':
                    if 'Monday' in week_birthdays:
                        week_birthdays.get('Monday').append(user_name)
                    else:
                        user_names.append(user_name)
                        week_birthdays.update({'Monday': user_names})
                elif day not in week_birthdays:
                    user_names.append(user_name)
                    week_birthdays.update({day: user_names})
                else:
                    week_birthdays.get(day).append(user_name)

    return week_birthdays


if __name__ == "__main__":
    example_users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(example_users)
    print(result)

    # Print the result
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")