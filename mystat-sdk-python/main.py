from core import *

token = get_auth("Utemb_aa50","lookism20062007#A")
print(token)
if token:
    m = get_marks(token)
    if m and isinstance(m, list):
        for i in m:
            print(i.get("mark_date"), " ", i.get("mark"))
    else:
        print("Ошибка получения оценок")

    print("Расписание на неделю:")
    week_schedule = get_schedule(token, "week")
    if week_schedule and isinstance(week_schedule, dict):
        for key, lessons in week_schedule.items():
            if lessons:
                first = lessons[0]
                if isinstance(first, dict):
                    print(f"{key}: {first.get('date', 'Нет даты')}")
                else:
                    print(f"{key}: {first}")
            else:
                print(f"{key}: Нет уроков")
    else:
        print("Расписание на неделю не доступно")

    print("Расписание на месяц:")
    month_schedule = get_schedule(token, "month")
    if month_schedule and isinstance(month_schedule, list):
        for lesson in month_schedule:
            print(lesson)
    else:
        print("Расписание на месяц не доступно")
else:
    print("Error!")
