class CountSquares:

    def __init__(self):
        self.struct = dict()

    def add(self, point: List[int]) -> None:
        self.struct[tuple(point)] = self.struct.get(tuple(point), 0)+1

    def count(self, point: List[int]) -> int:
        query = tuple(point)
        count = 0
        for point in self.struct.keys():
            if abs(query[0]-point[0]) == abs(query[1]-point[1]) and abs(query[1]-point[1]) != 0:
                # diagonal can be formed
                A = (point[0], query[1])
                B = (query[0], point[1])
                if A in self.struct.keys() and B in self.struct.keys():
                    count += self.struct[A]*self.struct[B]*self.struct[point]
        
        return count

