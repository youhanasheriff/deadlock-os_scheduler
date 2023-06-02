class Process(object):

    last_scheduled_time = 0

    def __init__(self, id, arrival_time, burst_time):
        self.id = id
        self.arrival_time = arrival_time
        self.burst_time = burst_time

    def __repr__(self):
        return ('[id %d : arrival_time %d,  burst_time %d]' %
                (self.id, self.arrival_time, self.burst_time))
