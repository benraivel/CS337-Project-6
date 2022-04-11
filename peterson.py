# Ben Raivel
# CS337

# implements a spinlock using peterson's synchronization solution

class Peterson:

    def __init__(self):
        '''
        create instance variables for flag, turn
        '''
        self.flag = [False, False]
        self.turn = 0

    def lock(self, Thread_ID):
        '''
        acquire a lock for Thread_ID
        '''
        other_thread = abs(Thread_ID-1)
        self.flag[Thread_ID] = True
        self.turn = other_thread

        while self.turn == other_thread and self.flag[other_thread]: pass

    def unlock(self, Thread_ID):
        '''
        release lock held by Thread_ID
        '''
        self.flag[Thread_ID] = False