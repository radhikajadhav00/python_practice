import time

input("Press Enter to start stopwatch")
start = time.time()

input("Press Enter to stop stopwatch")
end = time.time()

print("Time elapsed:", round(end - start, 2), "seconds")
