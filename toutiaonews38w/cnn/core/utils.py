import datetime as dt


class Timer:
    def __init__(self):
        self.start_time = None

    def start(self):
        self.start_time = dt.datetime.now()

    def end(self):
        end_time = dt.datetime.now()
        print('Time taken: %s' % (end_time - self.start_time))
