class Solution:
    def numOfMinutes(self, n, headID, manager, informTime):
        adjacency = {}
        max_time_elapsed = 0
        def dfs(employee, time_elapsed):
            nonlocal max_time_elapsed
            if employee not in adjacency:
                return
            reports = adjacency[employee]
            time_elapsed += informTime[employee]
            max_time_elapsed = max(max_time_elapsed, time_elapsed)
            for report in reports:
                dfs(report, time_elapsed)
        for employee, manager in enumerate(manager):
            if manager not in adjacency:
                adjacency[manager] = set()
            adjacency[manager].add(employee)
        dfs(headID, 0)
        return max_time_elapsed

        