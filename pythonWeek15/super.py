class Sports:
    def __init__(self, name):
         # Initialize a Sports object with a given name.
        self._name = name

    @property
    def sports_name(self):
        # Get the name of the sport.
        return self._name

    @sports_name.setter
    def sports_name(self, value):
        # Set the name of the sport.
        self._name = value

    def practice(self):
        # Simulate practicing for a generic sport.
        print("Doing Sports practice")


class LandSports(Sports):
    def __init__(self, name, field):
        # Initialize a LandSports object with a name and a playing field.
        super().__init__(name)
        self._field = field

    @property
    def landsports_field(self):
        # Get the playing field for the land-based sport.
        return self._field

    def practice(self):
         # Simulate practicing for a land-based sport.
        print("Doing Land Sports practice")


class WaterSports(Sports):
    def __init__(self, name, activity):
         # Initialize a WaterSports object with a name and an activity description.
        super().__init__(name)
        self._activity = activity

    @property
    def watersports_activity(self):
        # Get the activity description for the water-based sport.
        return self._activity

    def practice(self):
        # Simulate practicing for a water-based sport.
        print("Doing Water Sports practice")

# Example of usage
if __name__ == "__main__":
    # Creating a new LandSports object
    baseball = LandSports("baseball", "baseball field")
    print(baseball.sports_name)
    print(baseball.landsports_field)
    print(baseball.practice()) # Call the overridden practice method for LandSports

    water_skiing = WaterSports("Water Skiing", "Strap on your skis and fly across the water")
    print(water_skiing.sports_name)
    print(water_skiing.watersports_activity)
    print(water_skiing.practice()) # Call the overridden practice method for WaterSports

    sports = Sports("Softball")
    print(sports.sports_name)
    print(sports.practice())