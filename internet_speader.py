data_mb = float(input("Enter data size (MB): "))
time_sec = float(input("Enter time taken (seconds): "))

speed = data_mb / time_sec
print("Internet speed:", round(speed, 2), "MB/s")
