from tortoise.contrib.pydantic import pydantic_model_creater

from src.database.models import Users

UserInsSchema = pydantic_model_creater(
    Users, name="UserIn", exclude_readonly=True
)
UserOutSchema = pydantic_model_creater(
    Users, name="UserOut", exclude=["password", "created_at", "modified_at"]
)
UserDatabaseSchema = pydantic_model_creater(
    Users, name="User", exclude=["created_at", "modified_at"]
)