
flights = {
    "Islamabad": [("Lahore", 40), ("Karachi", 90)],
    "Lahore": [("Karachi", 50), ("Peshawar", 30)],
    "Karachi": [("Quetta", 60)],
    "Peshawar": [("Quetta", 70)],
    "Quetta": [],
}


def ucs_cheapest_route(graph, start, goal):
    queue = [(0, [start])]
    visited = []
    explored_count = 0

    while queue:
        queue.sort(key=lambda item: item[0])
        cost, path = queue.pop(0)

        city = path[-1]

        if city in visited:
            continue

        visited.append(city)
        explored_count += 1

        print("Exploring route:", path, "| Cost:", cost)

        if city == goal:
            return path, cost, explored_count

        for next_city, ticket_price in graph.get(city, []):
            if next_city not in visited:
                queue.append(
                    (cost + ticket_price, path + [next_city])
                )

    return None, None, explored_count


route, total_cost, explored_count = ucs_cheapest_route(
    flights, "Islamabad", "Quetta"
)

if route:
    print("Cheapest route:", route)
    print("Total ticket cost:", total_cost)
else:
    print("No route found")
