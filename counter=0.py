counter=0 

def increase():
    global counter
    for in range(1000000):
        counter +=1

def decrease():
    global counter 
    for in range(1000000):
        counter -=1 


thread1= threading.Thread(target=increase_counter)
thread2= threading.Thread(target=dectease_counter)
