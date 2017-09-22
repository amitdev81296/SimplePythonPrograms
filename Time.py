import time, calendar, datetime

print("\n" + str(datetime.datetime.now()))

ticks = time.time()
print("\nNumber of ticks since 12:00am, January 1, 1970 : " + str(ticks))

local_time = time.localtime(time.time())
print("\nLocal Current Time : " + str(local_time))

local_time = time.asctime(time.localtime(time.time()))
print("\nLocal Current Time : " + str(local_time))

cal = calendar.month(2017, 7)
print("\nHere is that calender you ordered : ")
print(cal)