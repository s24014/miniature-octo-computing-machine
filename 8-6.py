from datetime import datetime
now = datetime.today()
print(now)             #　現在年月日時分秒マイクロ秒
print(now.year)        #　現在年
print(now.month)       #　現在月
print(now.day)         #　現在日
print(now.hour)        #　現在時
print(now.minute)      #　現在分
print(now.second)      #　現在秒
print(now.microsecond) #　現在マイクロ病
dum_day = datetime(2024, 8, 13, hour= 14, minute=57, second= 57, microsecond=0)
print(dum_day)

from datetime import datetime
t_str = '2028015120130'
dt = datetime.strptime(t_str, "%Y%m%d%H%M%S")
print(dt)
dt2 = dt.strftime("%Y%m%d%H%M%S")
print(dt2)

import datetime
t_delta = datetime.timedelta(days=1)
dt = detetime.strptime("21/11/06 16:30", "%d%m/%y %H:%M")
dt + t_delta
