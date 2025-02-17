import time
import threading

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
        
        self.state = "stationary"
        self.running = False
        self.timer_thread = None

    def start_trip(self):
        """Starts a trip and begins tracking time and cost."""
        print("\nWelcome to the Digital Taximeter!")
        print("The taxi is now ready to start.\n")
        
        # Ask if it's raining
        raining = input("Is it raining? (y/n): ").strip().lower()
        if raining == 'y':
            self.rain_rate_multiplier = self.rain_surcharge
        else:
            self.rain_rate_multiplier = 1  # No surcharge
        
        # Ask if the area is hot or not (rush hour, event, airport)
        area_demand = input("Is the area overdemanded or underdemanded? (o/u): ").strip().lower()
        if area_demand == 'o':
            self.demand_rate_multiplier = self.overdemand_surcharge
        elif area_demand == 'u':
            self.demand_rate_multiplier = self.underdemand_discount
        else:
            self.demand_rate_multiplier = 1

        self.time_seconds = 0
        self.cost = 0
        self.state = "stationary"
        self.running = True

        # Track separately
        self.timer_thread = threading.Thread(target=self.track_time, args=(self.stationary_rate,))
        self.timer_thread.start()

        try:
            while self.running:
                print(f"\nTaxi is currently {self.state}.")
                print(f"Time: {self.format_time(self.time_seconds)} | Cost: €{self.cost:.2f}\n")
                
                print("1. Start moving (m)")
                print("2. Pause (p)")
                print("3. Finish trip (f)")
                print("4. Resume (r, only when paused)\n")
                
                action = input("Choose an option: ").strip().lower()

                if action == 'm' and self.state == "stationary":
                    self.state = "moving"
                    print("\nTaxi is now moving.\n")
                    self.set_rate(self.moving_rate)
                
                elif action == 'p' and self.state != "paused":
                    self.state = "paused"
                    print("\nTaxi is paused.\n")
                    self.set_rate(self.pause_rate)
                
                elif action == 'r' and self.state == "paused":
                    self.state = "moving"
                    print("\nTaxi is now resuming the trip.\n")
                    self.set_rate(self.moving_rate)
                
                elif action == 'f':
                    self.finish_trip()
                    break

                else:
                    print("\nInvalid option. Please choose from the options.\n")
        except KeyboardInterrupt:
            print("\nTrip ended due to an interruption.\n")

    def track_time(self, rate):
        """Track time and calculate the fare while the taxi is in any state."""
        print("\nTracking time... (You can interact with the program now!)\n")
        while self.running:
            time.sleep(1)
            self.time_seconds += 1
            
            adjusted_rate = rate * self.rain_rate_multiplier * self.demand_rate_multiplier
            self.cost = self.time_seconds * adjusted_rate
            print(f"\rTime: {self.format_time(self.time_seconds)} | Cost: €{self.cost:.2f}", end="")

    def set_rate(self, rate):
        """Update the rate used for time tracking."""
        self.current_rate = rate

    def finish_trip(self):
        """End the trip and display total cost."""
        print(f"\n\nTotal time: {self.format_time(self.time_seconds)}")
        print(f"Total fare: €{self.cost:.2f}\n")
        self.running = False
        self.timer_thread.join()

    def format_time(self, seconds):
        """Format seconds into a readable format (minutes:seconds)."""
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{minutes:02d}:{seconds:02d}"

def main():
    taximeter = Taximeter()
    while True:
        print("\nMenu:")
        print("1. Start Trip")
        print("2. Exit\n")
        choice = input("Choose an option: ").strip()
        
        if choice == "1":
            taximeter.start_trip()
        elif choice == "2":
            print("\nGoodbye! See you next time!\n")
            break
        else:
            print("\nInvalid choice, please try again.\n")

if __name__ == "__main__":
    main()