from datetime import datetime, timedelta

def get_upcoming_birthdays(users):

  today = datetime.today().date()
  end_date = today + timedelta(days=7)
  upcoming_birthdays = []

  for user in users:
        #переводимо у формат datetime
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        
       #отимуємо дату ДН в цьому році
        birthday_this_year = birthday.replace(year=today.year)
        #ДН пройшов? Беремо наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday.replace(year=today.year + 1)
        
        #ДН в межах наступних 7днів?
        if today <= birthday_this_year <= end_date:
            # Перевіряємо, чи ДН припадає на вихідний
            if birthday_this_year.weekday() in (5, 6):  # Субота (5) або неділя (6)
                # Робимо перенос на наступний понеділок
                congratulation_date = birthday_this_year + timedelta(days=(7 - birthday_this_year.weekday()))
            else:
                congratulation_date = birthday_this_year

            # Додаємо до результатів
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

  return upcoming_birthdays


users = [
    {"name": "John Doe", "birthday": "1985.11.27"},
    {"name": "Jane Smith", "birthday": "1990.11.24"},
    {"name": "Kate Smith", "birthday": "1990.01.24"}

]
upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)