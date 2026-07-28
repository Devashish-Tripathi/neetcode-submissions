class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n_boats = 0
        people.sort()
        n = len(people)
        i, j = 0, n-1
        done = set()
        while i <= j:
            if people[i] + people[j] <= limit:
                i += 1
                j -= 1
            else:
                j -= 1
            n_boats += 1
        return n_boats