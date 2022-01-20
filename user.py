from redis_om import (Field, HashModel)

class User(HashModel):
    name: str = Field(index=True)
    user_id: str = Field(index=True)
    job_title: str = Field(index=True)