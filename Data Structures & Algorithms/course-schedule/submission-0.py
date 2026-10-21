from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        def fill_graph(a,b): # something like this to add stuff
            graph[a].append(b)
            indegree[b] += 1 
        graph = {}
        for i in range(numCourses):
            graph[i] = []
        
        queue = deque()
        indegree = [0] * numCourses # where we are going to store the number of arrows pointing to a node

        for a, b in prerequisites: 
            fill_graph(a,b)
        
        for i in range(len(indegree)): 
            if indegree[i] == 0:
                queue.append(i)
        
            # if b does not have any requirements add it to queue
        print(indegree)
        while queue:
            curr = queue.popleft() 
            # and rebove all of its things that its conncected to
            for edge in graph[curr]:
                indegree[edge] -= 1
                if indegree[edge] == 0:
                    queue.append(edge)
        print(queue)
        print(indegree)
        print(graph)
        if sum(indegree) == 0:
            return True
        else:
            return False