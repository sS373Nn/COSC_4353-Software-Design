from src.airport_data import airports
from src.fetch_a_criterion import fetch_criteria, fetch_a_criterion
from src.process_airport import process_airports

def print_selections(selection, criteria):
    print(f"Select a criteria to sort:\n{selection}: Nothing")
    
    for criterion in criteria:
        selection += 1
        print(f"{selection}: {criterion}")

def make_selection():
    while True:
        try:
            selection = int(input("\nPlease select a sorting option:\n"))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    return selection

def determine_sorting(selection, criteria):
    sorting = None
    
    if selection > 0 and selection < len(criteria) + 1:
        print("Proper selection!")
        sorting = fetch_a_criterion(criteria[selection - 1])

    return sorting

def print_sorted_airports(airports):
    for airport in airports:
        print(airport)

def main():
    criteria = fetch_criteria()
    selection = 0

    print_selections(selection, criteria)
    
    selection = make_selection()

    sorting = determine_sorting(selection, criteria)

    if sorting != None:
        print("Sorting...")
        sorted_airports = process_airports(airports, sorting)
    else:
        sorted_airports = process_airports(airports)

    print_sorted_airports(sorted_airports)

    return 0

if __name__ == '__main__':
    main()
