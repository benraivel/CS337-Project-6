import numpy as np

class Bakery:

    def __init__(self, thread_count):
        '''
        create choosing and tickets list
        '''
        
        self.choosing = np.empty(thread_count, dtype=bool)
        self.tickets = np.empty(thread_count, dtype=int)


    def lock(self, thread_ID):
        '''
        
        '''
        # thread wants a ticket
        self.choosing[thread_ID] == True

        # give ticket
        self.tickets[thread_ID] = np.max(self.tickets) + 1
