class Activity:
    def __init__(self, id, name, duration_minutes, activity_type):
        self.id = id
        self.name = name
        self.duration_minutes = duration_minutes
        self.activity_type = activity_type

class AdvancedActivity(Activity):
    def __init__(self, id, name, duration_minutes, activity_type, intensity):
        super().__init__(id, name, duration_minutes, activity_type)
        self.intensity = intensity