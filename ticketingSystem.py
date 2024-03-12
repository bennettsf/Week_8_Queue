import queue
from datetime import datetime
import time
import random

class Ticket:
    def __init__(self, num: int, timeStamp: str):
        self.num = num
        self.timeStamp = timeStamp

ticketQueue = queue.Queue()
ticket_count = 0

while (True):  
    if ticket_count <= 15:
        time.sleep(random.random() * 2)
        now = datetime.now()
        added = Ticket(ticket_count, now.strftime('%H:%M:%S'))
        ticketQueue.put(added)
        print('Added Ticket Number: ' + str(added.num))
        ticket_count += 1
        
    if ticketQueue.qsize() == 0:
        break
    
    time.sleep(1)
    curr: Ticket = ticketQueue.get()
    print('Ticket Number: ' + str(curr.num) + ' | Time: ' + curr.timeStamp)
    
    
    
        