import time

def countdown_timer(seconds):
    # Loop to countdown every second
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer = f'{mins:02d}:{secs:02d}'
        print(timer, end="\r")  # Print the timer on the same line
        time.sleep(1)  # Wait for one second
        seconds -= 1
    
    print("Time's up!")  # Once the countdown reaches zero

def main():
    print("Welcome to the Countdown Timer!")
    
    # Get the countdown time from the user
    try:
        total_time = int(input("Enter the time in seconds: "))
        
        # Ensure that the time entered is a positive number
        if total_time <= 0:
            print("Please enter a positive number of seconds.")
        else:
            countdown_timer(total_time)
    
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
