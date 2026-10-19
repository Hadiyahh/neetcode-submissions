class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #intervals.sort(key=lambda interval:interval.start)
        intervals.sort()
        stack = []
        stack.append(intervals[0])
        
        for i in range(1, len(intervals)):
            if stack[-1][1] >= intervals[i][0]: # if the first session end time is greater then the 2nd session start time
                if stack[-1][1] < intervals[i][1]: # first end greater then 2nd end
                    stack[-1][1] = intervals[i][1]
            else:    
                stack.append(intervals[i])
        
        
        return stack
