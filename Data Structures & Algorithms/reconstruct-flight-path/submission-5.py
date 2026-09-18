class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        n = len(tickets)
        dct = {fro: deque([]) for fro, to in tickets}
        tickets.sort()
        for fro, to in tickets:
            dct[fro].append(to)

        iti = []

        def dfs(curr):
            while curr in dct and dct[curr]:
                nbr = dct[curr].popleft()
                dfs(nbr)
            iti.append(curr)


        dfs('JFK')
        return iti[::-1]
