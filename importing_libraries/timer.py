from time import *

# initialize var for begining time
start_timer = time()

# create struct_time 
struct = localtime(start_timer)

# announce countdown begining from start_timer
print(f"Starting Countdown At: {strftime('%X',struct)}")

# loop init/go down counter
i = 10
while i > -1:
    print(i)
    i -= 1
    sleep(1)

# showing elapsed time 
end_timer = time()

# create rounded number for elapsed time
difference = round(end_timer - start_timer)

# display time taken to execute countdown loop
print('\nRuntime:', difference, 'Seconds')