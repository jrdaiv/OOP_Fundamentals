class Event:
        def __init__(self, name, date):
            self.name = name
            self.date = date
            self.participants = 0
        def add_participants(self):
              self.participants += 1
        def get_participant(self):
              return self.participants

event = Event('Wedding', '7-23-26')
event.add_participants()
print(event.get_participant())