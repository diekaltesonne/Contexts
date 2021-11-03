class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(course,prerequisite,used):
            used.add(course) 
            if prerequisites[1] not in used:
                        dfs(prerequisites,prerequisites[1],used)
        used = set()
        used_1 = set()
        ans = dfs(prerequisites[0],used)
        if ans is None:
            return True
