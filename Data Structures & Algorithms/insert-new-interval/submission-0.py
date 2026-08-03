class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        answer = []
        idx = 0
        n = len(intervals)
        while idx < n and intervals[idx][1] < newInterval[0]:
            answer.append(intervals[idx])
            idx += 1
        while idx < n and intervals[idx][0] <= newInterval[1]:
            newInterval = [min(intervals[idx][0], newInterval[0]), max(intervals[idx][1], newInterval[1])]
            idx += 1
        answer.append(newInterval)
        answer += intervals[idx:]

        return answer
