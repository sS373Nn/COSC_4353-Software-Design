from dataclasses import replace

def process_airports(airports, sort_key=lambda airport: ()): 
    def convert_name_to_upper(airport):
        return replace(airport, name=airport.name.upper())
        
    return sorted(map(convert_name_to_upper, airports), key=sort_key)
