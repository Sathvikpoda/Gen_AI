import random

# Define airlines and locations
airlines = [
    "American Airlines", "Delta Air Lines", "United Airlines", "Southwest Airlines", "Alaska Airlines",
    "JetBlue Airways", "Spirit Airlines", "Frontier Airlines", "Allegiant Air", "Hawaiian Airlines",
    "British Airways", "Lufthansa", "Emirates", "Qatar Airways", "Singapore Airlines",
    "Air France", "KLM", "Cathay Pacific", "Qantas", "Turkish Airlines"
]

locations = [
    "New York", "Los Angeles", "Chicago", "Houston", "Phoenix",
    "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose",
    "Miami", "Atlanta", "Boston", "Seattle", "Denver",
    "Las Vegas", "Orlando", "Washington D.C.", "Toronto", "Vancouver"
]

# Generate random flights
flights = []
for _ in range(200):
    airline = random.choice(airlines)
    source = random.choice(locations)
    destination = random.choice([loc for loc in locations if loc != source])
    flight_number = airline[:2].upper() + str(random.randint(1000, 9999))
    flights.append({"airline": airline, "source": source, "destination": destination, "flight_number": flight_number})

# Create a dictionary to represent distances between cities (randomly generated for this example)
distances = {}
for loc1 in locations:
    for loc2 in locations:
        if loc1 != loc2:
            distances[(loc1, loc2)] = random.randint(500, 5000)

# Function to find flights between source and destination
def find_flights(source, destination):
    # Convert inputs to lowercase for case-insensitive matching
    source = source.lower()
    destination = destination.lower()

    # Convert locations to lowercase for matching
    lower_locations = [loc.lower() for loc in locations]

    if source not in lower_locations or destination not in lower_locations:
        print("Invalid source or destination.")
        return

    # Convert flights data to lowercase for case-insensitive comparison
    direct_flights = [flight for flight in flights if flight['source'].lower() == source and flight['destination'].lower() == destination]

    # Check for direct flights
    if direct_flights:
        print(f"\nDirect flights from {source.title()} to {destination.title()}:")
        for flight in direct_flights:
            print(f"  - {flight['airline']} (Flight Number: {flight['flight_number']})")
    else:
        print(f"\nNo direct flights from {source.title()} to {destination.title()}.")

    # Find connecting flights with 1 stop
    connecting_flights = []
    for stop in lower_locations:
        if stop != source and stop != destination:
            first_leg = [flight for flight in flights if flight['source'].lower() == source and flight['destination'].lower() == stop]
            second_leg = [flight for flight in flights if flight['source'].lower() == stop and flight['destination'].lower() == destination]

            if first_leg and second_leg:
                for leg1 in first_leg:
                    for leg2 in second_leg:
                        connecting_flights.append({
                            'airline1': leg1['airline'],
                            'flight_number1': leg1['flight_number'],
                            'stop': stop,
                            'airline2': leg2['airline'],
                            'flight_number2': leg2['flight_number'],
                            'stops': 1
                        })

    # Display connecting flights with 1 stop
    if connecting_flights:
        print(f"\nConnecting flights from {source.title()} to {destination.title()} with 1 stop:")
        for flight in connecting_flights:
            print(f"  - {flight['airline1']} (Flight Number: {flight['flight_number1']}) from {source.title()} to {flight['stop'].title()}")
            print(f"  - {flight['airline2']} (Flight Number: {flight['flight_number2']}) from {flight['stop'].title()} to {destination.title()}")
    else:
        print(f"\nNo connecting flights with 1 stop from {source.title()} to {destination.title()}.")

# Main function to take user input
def book_flight():
    print("Available locations: ", ", ".join(locations))

    source = input("Enter your source location: ").strip()
    destination = input("Enter your destination: ").strip()

    find_flights(source, destination)

# Start the process
book_flight()
