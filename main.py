from datetime import date, datetime


def get_birthdays_per_week(users):
    # Реалізуйте тут домашнє завдання
    week_birthdays = {}
    for user in users:
        user_name = user['name'].split()[0]
        birthday = user['birthday']
        weekday_birth = birthday.strftime('%A')
        # print(user_name, weekday_birth)
        today = date.today()
        sunday = 6 - today.weekday()
        date_sunday = today.replace(day=today.day + sunday)
        print(date_sunday)
        days = []
        names = []
        if birthday < today:
            continue
        for day in range(today.weekday(), date_sunday.weekday() + 1):
            day = today.replace(day = day + 1).strftime('%A')
            # print(date_sunday.weekday())
            days.append(day)
            print(day)
            if weekday_birth == day:
                if day == 'Saturday' or day == 'Sunday':
                    if 'Monday' in week_birthdays:
                        week_birthdays.get('Monday').append(user_name)
                    else:
                        names.append(user_name)
                        week_birthdays.update({'Monday' : names})
                elif day not in week_birthdays:
                    names.append(user_name)  
                    week_birthdays.update({day : names})  
                else:
                    week_birthdays.get(day).append(user_name)
                 
        # print(days)
    
    print(week_birthdays)
    return week_birthdays


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
