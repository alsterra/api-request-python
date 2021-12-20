from datetime import datetime

user_input = input("Enter your goal with a deadline separated by colon\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

dl_date = datetime.strptime(deadline, "%d.%m.%Y")
today_date = datetime.today()
# calculate how many days from now till deadline
time_range = dl_date - today_date

days_till = time_range.days
hours_till = int(time_range.total_seconds() / 60 / 60)
print(f"Hello, time remaining for your goal: {goal} is {days_till} days, "
      f"or {hours_till} hours")