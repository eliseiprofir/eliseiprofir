def switch_meridian(meridian: str) -> str:
    return "PM" if meridian == "AM" else "AM"


def parse_time(time: str) -> tuple:
    time_parts, meridian = time.split(" ")
    hour, minute = map(int, time_parts.split(":"))
    return hour, minute, meridian


def add_minutes(hour: int, minute: int, add_minute: int) -> tuple[int, int]:
    minute += add_minute
    while minute >= 60:
        hour += 1
        minute -= 60
    return hour, minute


def add_hours(hour: int, add_hour: int, meridian: str) -> tuple[int, str, int]:
    hour += add_hour
    add_days = 0
    while hour >= 12:
        hour -= 12
        meridian = switch_meridian(meridian)
        if meridian == "AM":
            add_days += 1
    if hour == 0:
        hour = 12
    return hour, meridian, add_days


def calculate_day(day: str, add_days: int) -> str:
    days = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
    if day:
        day_index = days.index(day.capitalize())
        new_day_index = (day_index + add_days) % 7
        return days[new_day_index]
    return ""


def format_time(hour: int, minute: int, meridian: str, day: str, add_days: int) -> str:
    time_str = f'{hour}:{str(minute).zfill(2)} {meridian}'
    if day:
        if add_days == 0:
            return f'{time_str}, {day}'
        elif add_days == 1:
            return f'{time_str}, {day} (next day)'
        else:
            return f'{time_str}, {day} ({add_days} days later)'
    else:
        if add_days == 1:
            return f'{time_str} (next day)'
        elif add_days > 1:
            return f'{time_str} ({add_days} days later)'
    return time_str


def add_time(start: str, duration: str, day: str = '') -> str:
    if duration == "0:00":
        return start

    start_hour: int
    start_minute: int
    meridian: str
    duration_hour: int
    duration_minute: int
    finish_hour: int
    finish_minute: int
    meridian: str
    add_days: int

    start_hour, start_minute, meridian = parse_time(start)
    duration_hour, duration_minute = map(int, duration.split(":"))
    finish_hour, finish_minute = add_minutes(start_hour, start_minute, duration_minute)
    finish_hour, meridian, add_days = add_hours(finish_hour, duration_hour, meridian)
    new_day = calculate_day(day, add_days)

    return format_time(hour=finish_hour, minute=finish_minute, meridian=meridian, day=new_day, add_days=add_days)


print(add_time('3:00 PM', '3:10'))  # Returns: 6:10 PM
print(add_time('11:30 AM', '2:32', 'Monday'))  # Returns: 2:02 PM, Monday
print(add_time('11:43 AM', '00:20'))  # Returns: 12:03 PM
print(add_time('10:10 PM', '3:30'))  # Returns: 1:40 AM (next day)
print(add_time('11:43 PM', '24:20', 'tueSday'))  # Returns: 12:03 AM, Thursday (2 days later)
print(add_time('6:30 PM', '205:12'))  # Returns: 7:42 AM (9 days later)
print(add_time('3:30 PM', '2:12'))  # Returns: 5:42 PM
print(add_time('11:55 AM', '3:12'))  # Returns: 3:07 PM
print(add_time('2:59 AM', '24:00'))  # Returns: 2:59 AM (next day)
print(add_time('11:59 PM', '24:05'))  # Returns: 12:04 AM (2 days later)
print(add_time('8:16 PM', '466:02'))  # Returns: 6:18 AM (20 days later)
print(add_time('3:30 PM', '2:12', 'Monday'))  # Returns: 5:42 PM, Monday
print(add_time('2:59 AM', '24:00', 'saturDay'))  # Returns: 2:59 AM, Sunday (next day)
print(add_time('11:59 PM', '24:05', 'Wednesday'))  # Returns: 12:04 AM, Friday (2 days later)
print(add_time('8:16 PM', '466:02', 'tuesday'))  # Returns: 6:18 AM, Monday (20 days later)
