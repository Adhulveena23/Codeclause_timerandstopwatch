import time

def countdown_timer(duration):
    remaining_time = duration
    while remaining_time >= 0:
        minutes, seconds = divmod(remaining_time, 60)
        timer_display = '{:02d}:{:02d}'.format(minutes, seconds)
        print(timer_display, end='\r')
        time.sleep(1)
        remaining_time -= 1

    print("Timer completed!")

# Example usage: Set timer duration to 5 minutes (300 seconds)
timer_duration = 300
countdown_timer(timer_duration)
