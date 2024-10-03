from datetime import datetime, timedelta


def generate_dates(schedule):
    all_dates = []
    for start_date, end_date in schedule:
        current_date = start_date
        while current_date <= end_date:
            all_dates.append(current_date)
            current_date += timedelta(days=1)
    return all_dates


def show_dates(schedule):
    all_dates = generate_dates(schedule)

    for date in all_dates:
        print(date)


if __name__ == '__main__':
    schedule = [
        (datetime(2020, 1, 1), datetime(2020, 1, 7)),
        (datetime(2020, 1, 15), datetime(2020, 2, 7))
    ]

    show_dates(schedule)
