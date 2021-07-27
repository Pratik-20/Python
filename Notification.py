import time 
from plyer import notification 
if __name__ == '__main__':
	while True:
		notification.notify(
		title = " Title of Notification ",
		message = "Main part of notification",
		timeout = 20
		)
		time.sleep(40)