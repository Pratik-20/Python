import time
from datetime import datetime
from datetime import date


today = date.today()
print("Today's date:", today)
h=datetime.fromtimestamp(time.time())
print(h)
