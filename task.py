from redis_om import (Field, JsonModel, EmbeddedJsonModel)
from typing import List

class TaskAssignee(EmbeddedJsonModel):
    user_id: str = Field(index=True)

class Task(JsonModel):
    name: str = Field(index=True)
    task_id: str = Field(index=True)
    status: str = Field(index=True)
    description: str = Field(index=True, full_text_search=True)
    assigned_to: List[TaskAssignee]