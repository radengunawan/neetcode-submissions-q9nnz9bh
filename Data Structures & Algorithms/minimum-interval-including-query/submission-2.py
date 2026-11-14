class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        events = []
        # Create events for intervals
        for idx, (start, end) in enumerate(intervals):
            events.append((start, 0, end - start + 1, idx))
            events.append((end, 2, end - start + 1, idx))

        # Create events for queries
        for i, q in enumerate(queries):
            events.append((q, 1, i))

        # Sort by time and type (end before query)
        events.sort(key=lambda x: (x[0], x[1]))

        # Min heap storing [size, index]
        sizes = []
        ans = [-1] * len(queries)
        inactive = [False] * len(intervals)

        for time, type, *rest in events:
            if type == 0:  # Interval start
                interval_size, idx = rest
                heapq.heappush(sizes, (interval_size, idx))
            elif type == 2: #Interval end
                idx = rest[1]
                inactive[idx] = True
            else: # Query
                query_idx = rest[0]
                while sizes and inactive[sizes[0][1]]:
                    heapq.heappop(sizes)
                if sizes:
                    ans[query_idx] = sizes[0][0]

        return ans