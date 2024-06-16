from datetime import datetime

class Schedule:
    def __init__(self):
        self.events = {}

    def add_event(self, event_name, event_date):
        if event_date in self.events:
            self.events[event_date].append(event_name)
        else:
            self.events[event_date] = [event_name]

    def view_events(self):
        for date in sorted(self.events.keys()):
            formatted_date = date.strftime("%Y-%m-%d %H:%M")
            print(f"{formatted_date}: {', '.join(self.events[date])}")

    def remove_event(self, event_name, event_date):
        if event_date in self.events and event_name in self.events[event_date]:
            self.events[event_date].remove(event_name)
            if not self.events[event_date]:
                del self.events[event_date]
        else:
            print(f"Event '{event_name}' not found")