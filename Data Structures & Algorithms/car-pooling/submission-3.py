class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        curr_cap = 0
        trips.sort(key= lambda x: x[1])
        eap = []
        for num_passenger, start_time, end_time in trips:
            while eap and start_time >= eap[0][0]:
                curr_cap -= heapq.heappop(eap)[1]
                
            curr_cap += num_passenger   
            if curr_cap > capacity:
                return False
            
            heapq.heappush(eap, (end_time, num_passenger))
        
        return True
            
