import time
from plyer import notification

def drink_water_reminder():
    while True:
        # Display the notification
        notification.notify(
            title="Drink Water Reminder",
            message="Remember to drink water now!",
            timeout=3  # Notification will stay on screen for 10 seconds
        )
        
        # Wait for an hour before reminding again
        time.sleep(5)  # 1 hour = 3600 seconds
        print("notification after 5 second")

if __name__ == "__main__":
    drink_water_reminder()
