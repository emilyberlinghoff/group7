
## ------- import packages -------
import networkx as nx
import dimod,math
# TODO:  Import your sampler
from dwave.system import LeapHybridSampler
# TODO:  Import your Traveling Salesperson QUBO generator
from dwave_networkx import traveling_salesman_qubo

def get_qubo(G, lagrange, n,start_time,end_time):
    """Returns a dictionary representing a QUBO"""
    
    # TODO:  Add QUBO construction here
    Q = traveling_salesman_qubo(G, lagrange=lagrange)

    # Add constraints for visiting supply stations first and demand station last
    for node in G.nodes:
        if 'supply' in G.nodes[node]:
            Q[(node, 0), (node, 0)] += lagrange
        elif 'demand' in G.nodes[node]:
            Q[(node, n-1), (node, n-1)] += lagrange

    offset = 2 * n * lagrange

    return Q, offset


def get_sampler():
    """Returns a sampler"""

    # TODO: Enter your sampler here
    sampler=LeapHybridSampler()


    return sampler


## ------- Main program -------
if __name__ == "__main__":
    
    Demand = 15
    Amount_supply = 5
    lagrange = 4000
    G = nx.Graph()
    G.add_weighted_edges_from([
        (0, 1, 5),
        (0, 2, 4),
        (1, 0, 5),
        (2, 0, 4),
        (1, 2, 3),
        (1, 3, 12),
        (2, 1, 3),
        (3, 1, 12),
        (2, 3, 4),
        (3, 2, 4)
    ])
    # Add supply and demand data to the graph
    G.nodes[1]['supply'] = 10  # Supply station with 10 bikes
    G.nodes[2]['supply'] = 5   # Supply station with 5 bikes
    G.nodes[3]['demand'] = 15  # Demand station needing 15 bikes
    n = len(G)

    Q, offset = get_qubo(G, lagrange, n,0,n-1)
    sampler = get_sampler()
    bqm = dimod.BinaryQuadraticModel.from_qubo(Q, offset=offset)
  
    
    response = sampler.sample(bqm, label="Training - TSP")

    start = None
    sample = response.first.sample
    cost = response.first.energy
    route = [None] * n

    print(sample)

    for (city, time), val in sample.items():
        if val and 0 <= time < n:
            route[time] = city

    if start is not None and route[0] != start:
        # rotate to put the start in front
        idx = route.index(start)
        route = route[-idx:] + route[:-idx]

    if None not in route:
        print(route)
        print(cost)

#database that holds station ids and live bike counts
bike_counts = {
    '7030': 2,  # Example of a station below the floor
    '7012': 18,  # Example of a station above the ceiling
    '7025': 10,
    '7040': 5,
    '7050': 15,
    '7060': 3,
    '7070': 1,  # Another station below the floor
    '7080': 20,  # Another station above the ceiling
}

def check_thresholds_and_select_stations(bike_counts):
    # Check for any station breaking the floor or ceiling thresholds
    threshold_broken = any(count < 3 or count > 17 for count in bike_counts.values())

    if threshold_broken:
        # Calculate how many bikes each station needs to balance all stations
        total_bikes = sum(bike_counts.values())
        num_stations = len(bike_counts)
        target_count = total_bikes // num_stations
        station_needs = {station_id: target_count - count for station_id, count in bike_counts.items()}
        return True, station_needs
    else:
        return False, {}

def refill(station_needs):
    print(station_needs)

# def main():
#     threshold_broken, station_needs = check_thresholds_and_select_stations(bike_counts)

#     if threshold_broken:
#         refill(station_needs)
