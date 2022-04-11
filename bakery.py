import numpy as np

class Bakery:

    def __init__(self, thread_count):
        '''
        create choosing and tickets list
        '''
        self.n_threads = thread_count
        self.choosing = np.empty(thread_count, dtype=bool)
        self.tickets = np.zeros(thread_count)


    def lock(self, thread_ID):
        '''
        
        '''
        # thread wants a ticket
        self.choosing[thread_ID] = True

        # give ticket
        self.tickets[thread_ID] = np.max(self.tickets) + 1

        # got ticket
        self.choosing[thread_ID] = False

        for i in range(self.n_threads):

            while self.choosing[i]: pass
            
            while (self.tickets[i] != 0) and ((self.tickets[i] < self.tickets[thread_ID]) or ((self.tickets[i] == self.tickets[thread_ID]) and (i<thread_ID))): pass


    def unlock(self, thread_ID):

        self.tickets[thread_ID] = 0
        #print('unlocked!')