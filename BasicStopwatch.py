import time

input("Press Enter to start the stopwatch...")
start = time.time()

input("Press Enter to stop...")
end = time.time()

elapsed = end - start
minutes = int(elapsed // 60)
seconds = round(elapsed % 60, 2)

print(f"Time: {minutes} minutes {seconds} seconds")
