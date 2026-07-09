"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        startTimes = sorted([x.start for x in intervals])
        endTimes = sorted([x.end for x in intervals])
        s, e, count = 0, 0, 0
        ans = 0
        while s < len(startTimes):
            if startTimes[s] < endTimes[e]:
                # these meetings begin before the first meeting that ends
                count += 1
                s += 1
            else:
            # a meeting has ended, so to next meet and decrease the current meets
                e += 1
                count -= 1
            
            ans = max(ans, count)
        
        return ans