from Date import *


class Event:
    def __init__(self, name, start_hour, end_hour, event_date):
        self._name = name
        self._start_hour = start_hour
        self._end_hour = end_hour
        self._event_date = event_date
        if start_hour < 0 or start_hour > 23:
            raise ValueError("Start hour must be between 0 and 23")
        if end_hour < 0 or end_hour > 23:
            raise ValueError("End hour must be between 0 and 23")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def start_hour(self):
        return self._start_hour

    @start_hour.setter
    def start_hour(self, start_hour):
        self._start_hour = start_hour

    @property
    def end_hour(self):
        return self._end_hour

    @end_hour.setter
    def end_hour(self, end_hour):
        self._end_hour = end_hour

    @property
    def event_date(self):
        return self._event_date

    @event_date.setter
    def event_date(self, event_date):
        self._event_date = event_date

    def __str__(self):
        return "Name of the event: " + str(self._name) + ", " + "Start and End times: " + str(
            self._start_hour) + " to " + str(self._end_hour) + ", Date of the Event: " + str(self._event_date)
