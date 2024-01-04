import redis


class RedisStorage:
    def __init__(self):
        self.redis = redis.Redis(host='localhost', port=6380, db=0)

    def add_task(self, task):
        task_id = self.redis.incr("task_id")
        task_key = f"task:{task_id}"
        self.redis.hmset(task_key, {
            "title": task.title,
            "description": task.description,
            "priority": task.priority
        })
