class Patrol:
    def __init__(self, patrol_id, area, officers_assigned):
        self.patrol_id = patrol_id
        self.area = area
        self.officers_assigned = officers_assigned

class PatrolRoutePlanner:
    def __init__(self):
        self.patrols_file = "patrols.txt"
        self.routes_file = "routes.txt"
        self.efficiencies_file = "efficiencies.txt"

    def create_patrol(self, patrol_id, area, officers_assigned):
        with open(self.patrols_file, "a") as file:
            file.write(f"{patrol_id},{area},{','.join(officers_assigned)}\n")
        print("Patrol details created successfully.")

    def read_patrol(self, patrol_id):
        updated_officers = []
        updated_area = None
        with open(self.patrols_file, "r") as file:
            for line in file:
                data = line.strip().split(",")
                if data[0] == patrol_id:
                    updated_area = data[1]  # Keep track of the updated area
                    officers = data[2].split(",")
                    updated_officers.extend(officers)  # Keep track of all updated officers
                    print(f"Patrol ID: {data[0]}, Area: {data[1]}, Officers Assigned: {', '.join(officers)}")
                    return updated_area, updated_officers
        print("Patrol ID not found.")
        return updated_area, updated_officers

    def update_patrol(self, patrol_id, new_area, new_officers_assigned):
        updated_lines = []
        with open(self.patrols_file, "r") as file:
            for line in file:
                data = line.strip().split(",")
                if data[0] == patrol_id:
                    line = f"{patrol_id},{new_area},{','.join(new_officers_assigned)}\n"
                updated_lines.append(line)
        
        with open(self.patrols_file, "w") as file:
            file.writelines(updated_lines)
        print("Patrol details updated successfully.")

    def delete_patrol(self, patrol_id):
        with open(self.patrols_file, "r") as file:
            lines = file.readlines()
        with open(self.patrols_file, "w") as file:
            for line in lines:
                data = line.strip().split(",")
                if data[0] != patrol_id:
                    file.write(line)
        print("Patrol deleted successfully.")

    def analyze_patrol_efficiency(self, route_id):
        with open(self.routes_file, "r") as file:
            for line in file:
                data = line.strip().split(",")
                if data[0] == route_id:
                    patrol_ids = data[1:]
                    total_officers = 0
                    total_areas = len(patrol_ids)
                    for patrol_id in patrol_ids:
                        with open(self.patrols_file, "r") as patrol_file:
                            for patrol_line in patrol_file:
                                patrol_data = patrol_line.strip().split(",")
                                if patrol_data[0] == patrol_id:
                                    total_officers += len(patrol_data[2].split(","))
                                    break
                    efficiency = total_officers / total_areas
                    with open(self.efficiencies_file, "a") as eff_file:
                        eff_file.write(f"{route_id},{efficiency}\n")
                    print(f"Patrol efficiency analyzed for Route ID: {route_id}. Efficiency: {efficiency}")
                    return
        print("Route ID not found.")

    def plan_patrol_routes(self, route_id, patrol_ids):
        with open(self.routes_file, "a") as file:
            file.write(f"{route_id},{','.join(patrol_ids)}\n")
        print(f"Patrol routes planned for Route ID: {route_id}")

def main_menu():
    print("\nMain Menu:")
    print("1. Create Patrol Details")
    print("2. Read Patrol Details")
    print("3. Update Patrol Details")
    print("4. Delete Patrol Details")
    print("5. Analyze Patrol Efficiency")
    print("6. Plan Patrol Routes")
    print("7. Exit")

def main():
    patrol_planner = PatrolRoutePlanner()

    while True:
        main_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            patrol_id = input("Enter Patrol ID: ")
            area = input("Enter Patrol Area: ")
            officers_assigned = input("Enter Officers Assigned (space-separated manner): ").split(",")
            patrol_planner.create_patrol(patrol_id, area, officers_assigned)
        elif choice == "2":
            patrol_id = input("Enter Patrol ID to read details: ")
            patrol_planner.read_patrol(patrol_id)
        elif choice == "3":
            patrol_id = input("Enter Patrol ID to update: ")
            new_area = input("Enter new Patrol Area: ")
            new_officers_assigned = input("Enter new Officers Assigned(space-sparated manner): ").split(",")
            patrol_planner.update_patrol(patrol_id, new_area, new_officers_assigned)
        elif choice == "4":
            patrol_id = input("Enter Patrol ID to delete: ")
            patrol_planner.delete_patrol(patrol_id)
        elif choice == "5":
            route_id = input("Enter Route ID to analyze efficiency: ")
            patrol_planner.analyze_patrol_efficiency(route_id)
        elif choice == "6":
            route_id = input("Enter Route ID: ")
            patrol_ids = input("Enter Patrol IDs for Route (comma-separated): ").split(",")
            patrol_planner.plan_patrol_routes(route_id, patrol_ids)
        elif choice == "7":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
