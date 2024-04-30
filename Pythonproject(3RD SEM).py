class Patrol:
    def __init__(self, patrol_id, area, officers_assigned):
        self.patrol_id = patrol_id
        self.area = area
        self.officers_assigned = officers_assigned

class PatrolRoutePlanner:
    def __init__(self):
        self.patrols = {}
        self.routes = {}
        self.efficiencies = {}

    def create_patrol(self):
        patrol_id = input("Enter Patrol ID: ")
        area = input("Enter Patrol Area: ")
        officers_assigned = input("Enter Officers Assigned (comma-separated): ").split(",")
        self.patrols[patrol_id] = Patrol(patrol_id, area, officers_assigned)
        print("Patrol details created successfully.")

    def read_patrol(self, patrol_id):
        if patrol_id in self.patrols:
            patrol = self.patrols[patrol_id]
            print(f"Patrol ID: {patrol.patrol_id}, Area: {patrol.area}, Officers Assigned: {', '.join(patrol.officers_assigned)}")
        else:
            print("Patrol ID not found.")

    def update_patrol(self, patrol_id):
        if patrol_id in self.patrols:
            print("Enter new details for the patrol:")
            area = input("Enter Patrol Area: ")
            officers_assigned = input("Enter Officers Assigned (comma-separated): ").split(",")
            self.patrols[patrol_id].area = area
            self.patrols[patrol_id].officers_assigned = officers_assigned
            print("Patrol details updated successfully.")
        else:
            print("Patrol ID not found.")

    def delete_patrol(self, patrol_id):
        if patrol_id in self.patrols:
            del self.patrols[patrol_id]
            print("Patrol deleted successfully.")
        else:
            print("Patrol ID not found.")

    def plan_patrol_routes(self, route_id):
        patrol_ids = input("Enter Patrol IDs for Route (comma-separated): ").split(",")
        self.routes[route_id] = patrol_ids
        print(f"Patrol routes planned for Route ID: {route_id}")

    def analyze_patrol_efficiency(self, efficiency_id):
        route_id = input("Enter Route ID to analyze efficiency: ")
        if route_id in self.routes:
            patrol_ids = self.routes[route_id]
            total_officers = sum(len(self.patrols[patrol_id].officers_assigned) for patrol_id in patrol_ids)
            total_areas = len(patrol_ids)
            efficiency = total_officers / total_areas
            self.efficiencies[efficiency_id] = efficiency
            print(f"Patrol efficiency analyzed for Efficiency ID: {efficiency_id}. Efficiency: {efficiency}")
        else:
            print("Route ID not found.")

    def read_efficiency(self, efficiency_id):
        if efficiency_id in self.efficiencies:
            print(f"Efficiency ID: {efficiency_id}, Efficiency: {self.efficiencies[efficiency_id]}")
        else:
            print("Efficiency ID not found.")

def main_menu():
    print("\nMain Menu:")
    print("1. Create Patrol Details")
    print("2. Plan Patrol Routes")
    print("3. Analyze Patrol Efficiency")
    print("4. Read Patrol Details")
    print("5. Update Patrol Details")
    print("6. Delete Patrol Details")
    print("7. Exit")

def main():
    patrol_planner = PatrolRoutePlanner()

    while True:
        main_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            patrol_planner.create_patrol()
        elif choice == "2":
            route_id = input("Enter Route ID: ")
            patrol_planner.plan_patrol_routes(route_id)
        elif choice == "3":
            efficiency_id = input("Enter Efficiency ID: ")
            patrol_planner.analyze_patrol_efficiency(efficiency_id)
        elif choice == "4":
            patrol_id = input("Enter Patrol ID to read details: ")
            patrol_planner.read_patrol(patrol_id)
        elif choice == "5":
            patrol_id = input("Enter Patrol ID to update details: ")
            patrol_planner.update_patrol(patrol_id)
        elif choice == "6":
            patrol_id = input("Enter Patrol ID to delete: ")
            patrol_planner.delete_patrol(patrol_id)
        elif choice == "7":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
