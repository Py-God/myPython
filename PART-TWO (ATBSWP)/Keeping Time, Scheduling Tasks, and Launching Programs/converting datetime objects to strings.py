import datetime

oct21st = datetime.datetime(2015, 10, 21, 16, 29, 0)
oct21st.strftime('%Y/%m/%d %H:%M:%S')
'2015/10/21 16:29:00'
oct21st.strftime('%I:%M:%p')
'04:29:PM'
oct21st.strftime("%B of '%y")
"October of '15"
