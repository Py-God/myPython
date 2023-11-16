import datetime

delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
delta.days, delta.seconds, delta.microseconds
(11, 36548, 0)

delta.total_seconds()
986948.0
str(delta)
'11 days, 10:09:08'

dt = datetime.datetime.now()
dt
datetime.datetime(2022, 7, 20, 23, 35, 41, 401100)
thousandDays = datetime.timedelta(days=1000)
dt + thousandDays
datetime.datetime(2025, 4, 15, 23, 35, 41, 401100)

oct21st = datetime.datetime(2015, 10, 21, 16, 29, 0)
aboutThirtyYears = datetime.timedelta(days=365 * 30)
oct21st
datetime.datetime(2015, 10, 21, 16, 29)
oct21st - aboutThirtyYears
datetime.datetime(1985, 10, 28, 16, 29)
oct21st - (2*aboutThirtyYears)
datetime.datetime(1955, 11, 5, 16, 29)
