def format_days_word(days):
    if days % 10 == 1 and days % 100 != 11:
        return "день"
    elif days % 10 in [2, 3, 4] and days % 100 not in [12, 13, 14]:
        return "дні"
    else:
        return "днів"


def convert_seconds_to_time(total_seconds):
    days, remainder = divmod(total_seconds, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)

    hours_str = str(hours).zfill(2)
    minutes_str = str(minutes).zfill(2)
    seconds_str = str(seconds).zfill(2)

    days_word = format_days_word(days)

    return f"{days} {days_word}, {hours_str}:{minutes_str}:{seconds_str}"

test_cases = [
    0, 224930, 466289, 950400, 1209600,
    1900800, 8639999, 22493, 7948799
]

if __name__ == "__main__":
    print("--- Seconds to Time Converter Test Results ---")
    for case in test_cases:
        result = convert_seconds_to_time(case)
        print(f"{case} -> {result}")