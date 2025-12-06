import time

seconds = int(input("Enter time in seconds: "))

for i in range(seconds, 0, -1):
    mins, secs = divmod(i, 60)
    print(f"{mins:02d}:{secs:02d}", end="\r")
    time.sleep(1)

print("Time's up!")
