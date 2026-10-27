from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = []
        # graph = [[] for _ in range(numCourses)]
        for _ in range(numCourses):
            graph.append([])
        # i want the graph to loop like
        # 0 : 2 
        # coursr : how many things are requored on it
# graph = [
#     [],  # Course 0
#     [],  # Course 1
#     [],  # Course 2
#     [],  # Course 3
#     []   # Course 4
# ]
        indegrees = [0] * numCourses

        queue = deque() 

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegrees[course] += 1
        for index in range(len(indegrees)):
            if indegrees[index] == 0:
                queue.append(index)
        completed = 0
        while queue:
            current = queue.popleft()
            
            for i in graph[current]:
                indegrees[i] -= 1
                if indegrees[i] == 0:
                    queue.append(i)
        if sum(indegrees) == 0:
            return True
        else:
            return False