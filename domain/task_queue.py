class TaskQueue:
    def __init__(self):
        self.queue = []
        self.running = False

    def add_task(self, task):
        self.queue.append(task)

    async def run_tasks(self):
        if self.running:
            return

        self.running = True

        while self.queue:
            controller = self.queue.pop(0)
            await controller.logic()

        self.running = False
