import time

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')  # Print the timer on the same line
        time.sleep(1)  # Wait for one second
        seconds -= 1

    print("Time's up!")  # Message when the countdown ends

# Example usage
if __name__ == "__main__":
    try:
        total_seconds = int(input("Enter the time in seconds: "))
        countdown_timer(total_seconds)
    except ValueError:
        print("Please enter a valid integer.")