class Taximeter:
    def __init__(self):
        self.time_seconds = 0
        self.cost = 0
        self.stationary_rate = 0.02
        self.moving_rate = 0.05
        self.pause_rate = 0.02
        self.rain_surcharge = 1.30
        self.overdemand_surcharge = 1.50
        self.underdemand_discount = 0.80
        self.state = 'stopped'

    def start_trip(self, is_raining, demand_type):
        self.is_raining = is_raining
        self.demand_type = demand_type
        self.time_seconds = 0
        self.cost = 0
        self.state = 'stationary'
        print("Tracking time... (You can interact with the program now!)")

    def calculate_cost(self):
        rate = self.stationary_rate if self.state == 'stationary' else self.moving_rate
        if self.is_raining:
            rate *= self.rain_surcharge
        if self.demand_type == 'o':
            rate *= self.overdemand_surcharge
        elif self.demand_type == 'u':
            rate *= self.underdemand_discount
        self.cost = self.time_seconds * rate / 100
        return self.cost

    def update_time(self, time_increase):
        self.time_seconds += time_increase
        print(f"Time: {self.time_seconds // 60:02}:{self.time_seconds % 60:02} | Cost: €{self.calculate_cost():.2f}")

    def pause_trip(self):
        self.state = 'paused'
        print("Taxi is paused.")

    def resume_trip(self):
        self.state = 'moving'
        print("Taxi is now resuming the trip.")

    def finish_trip(self):
        print(f"Total time: {self.time_seconds // 60:02}:{self.time_seconds % 60:02}")
        print(f"Total fare: €{self.calculate_cost():.2f}")


def main():
    taximeter = Taximeter()
    print("Menu:")
    print("1. Start Trip")
    print("2. Exit")

    choice = input("Choose an option: ").strip()

    if choice == '1':
        print("\nWelcome to the Digital Taximeter!")
        print("The taxi is now ready to start.")

        rain = input("Is it raining? (y/n): ").strip().lower() == 'y'
        demand = input("Is the area overdemanded or underdemanded? (o/u): ").strip().lower()

        taximeter.start_trip(rain, demand)

        while True:
            print(f"\nTaxi is currently {taximeter.state}.")
            taximeter.update_time(10)

            print("\n1. Start moving (m)")
            print("2. Pause (p)")
            print("3. Finish trip (f)")

            action = input("\nChoose an option: ").strip().lower()

            if action == 'm' and taximeter.state == 'stationary':
                taximeter.resume_trip()
            elif action == 'p' and taximeter.state == 'moving':
                taximeter.pause_trip()
            elif action == 'f':
                taximeter.finish_trip()
                break
            else:
                print("Invalid option. Please choose from the options.")

    elif choice == '2':
        print("Goodbye!")
    else:
        print("Invalid option. Please choose again.")


if __name__ == '__main__':
    main()
