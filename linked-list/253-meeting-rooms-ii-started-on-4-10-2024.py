class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        times = defaultdict(int)
        highest = 0
        # first pass to add to hashmap
        for i in intervals:
            start = i[0]
            end = i[1]
            while start < end:
                times[start] += 1
                start += 1
        # second pass to get max count at any point in hashmap
        for t in times:
            highest = max(highest, times[t])
        return highest
