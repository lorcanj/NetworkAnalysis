class Edge:
    def __init__(self, edge_id: int, start: str, end: str, weight: int = 1, capacity: int = 1):
        self.edge_id = edge_id
        self.start = start
        self.end = end
        self.weight = weight
        self.capacity = capacity

    def __str__(self):
        print(f"Edge starts at {self.start} and ends at {self.end}, with a weight of {self.weight}")
