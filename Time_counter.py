import time
def countdown(t):
  while t>0:
     print(t)
     t = t - 1
     time.sleep(1)
  print("time's up")
  
print("how many seconds to count down? enter an integer .")
seconds = input()
while not seconds.isdigit():
        print("That wasn't an integer number! please Enter an integer")
        seconds =input()
seconds = int(seconds)
countdown(seconds)
    
