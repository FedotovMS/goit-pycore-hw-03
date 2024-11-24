from datetime import datetime

def get_days_from_today(date):
  try:
      date = datetime.strptime(date, '%Y-%m-%d').date()
      current_date = datetime.today().date()
      delta = (current_date - date).days
      print(f"{delta} day(s)")
      return delta
  except ValueError:
     raise ValueError("Wrong date format, use YYYY-MM-DD.")

  

get_days_from_today("2024-11-28")
