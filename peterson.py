import math

class Peterson:

    flag = [False, False]
    turn = 0

    def lock(self, Thread_ID):
        global flag
        global turn
        flag[Thread_ID] = True
        turn = abs(Thread_ID-1)

        while self.turn == 1 and flag[abs(Thread_ID-1)]: pass

    def unlock(self, Thread_ID):
        global flag
        flag[Thread_ID] = False