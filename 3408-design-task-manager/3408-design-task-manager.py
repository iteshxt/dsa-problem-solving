import heapq

class TaskManager:
    def __init__(self, tasks: list[list[int]]):
        self.task_map: dict[int, tuple[int, int]] = {}
        self.heap: list[tuple[int, int, int]] = []
        for userId, taskId, priority in tasks:
            self.add(userId, taskId, priority)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.task_map[taskId] = (userId, priority)
        heapq.heappush(self.heap, (-priority, -taskId, taskId))

    def edit(self, taskId: int, newPriority: int) -> None:
        userId, _ = self.task_map[taskId]
        self.task_map[taskId] = (userId, newPriority)
        heapq.heappush(self.heap, (-newPriority, -taskId, taskId))

    def rmv(self, taskId: int) -> None:
        if taskId in self.task_map:
            del self.task_map[taskId]

    def execTop(self) -> int:
        while self.heap:
            negPriority, negTaskId, taskId = heapq.heappop(self.heap)
            if taskId in self.task_map and self.task_map[taskId][1] == -negPriority:
                return self.task_map.pop(taskId)[0]
        return -1
