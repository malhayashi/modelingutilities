import numpy as np 
import random as pr
import datetime as dt 
import copy
import sys
import os
from math import *

class Agent(object):
    def __init__(self):
        pass

class Model(object):
    def __init__(self):

        ### Initialize event dictionary
        self.events = {
            'dummy event': 0,

        }

        ### Calculate initial event rates
        self.events['dummy event'] = 1

        self.totalRate = np.sum(self.events.values())

    def run(self):
        pass

    def draw_event_time(self):
        ### Draw time of next event
        return np.random.exponential(scale=1/float(self.totalRate))
    
    def draw_event(self):
        ### Determine which event occurs
        r = np.random.random()
        s = 0.0
        for event, rate in self.events.iteritems():
            s += rate/float(self.totalRate)
            if r < s:
                return event
        return event

    def dummy_event(self):
        pass

    def update_event_rates(self):
        pass

    def resolve(self,event):
        dispatch = {
            'dummy event': self.dummy_event,

        }
        dispatch[event]()


