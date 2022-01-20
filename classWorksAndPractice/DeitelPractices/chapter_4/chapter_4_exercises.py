def cube(x):
    x **= 3
    return x


print("The cube of 2 is", cube(2))


def mystery_number(x):
    y = 0
    for value in x:
        y += value ** 2
    return y


print("The mystery number is", mystery_number([1, 2, 3, 4, 5]))


def seconds_since_midnight(hour, minutes, seconds):
    # hour_in_seconds = 0
    # minutes_in_seconds = 0
    hour_is_lesser_than_zero = 0 > hour
    minutes_is_lesser_than_zero = 0 > minutes
    seconds_is_lesser_than_zero = 0 > seconds
    hour_is_greater_than_11 = hour > 11
    minute_is_greater_than_59 = minutes > 60
    seconds_is_greater_than_59 = seconds > 60
    hour_in_seconds = hour * 60 * 60
    minutes_in_seconds = minutes * 60
    return hour_in_seconds + minutes_in_seconds + seconds


time = "1:45:32"
print("The number of seconds since", time + " is", seconds_since_midnight(1, 45, 59), "seconds")
