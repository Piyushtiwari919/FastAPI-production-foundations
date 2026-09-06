from pydantic import BaseModel, field_validator, model_validator, Field
from typing import Self


class Address(BaseModel):
    city: str
    zip_code: int


class UserProfile(BaseModel):
    username: str
    age: int
    password: str = Field(min_length=6)
    repeated_password: str
    address: Address  # Nested BaseModel

    @field_validator("age")
    @classmethod
    def check_valid_age(cls, value: int):
        # 2. Write your business logic
        if value < 18:
            raise ValueError("User must be at least 18 years old.")
        if value > 120:
            raise ValueError("Age exceeds realistic human limits.")

        # 3. You MUST return the value if it passes
        return value

    @model_validator(mode="after")
    def check_for_password_match(self) -> Self:
        if self.password != self.repeated_password:
            raise ValueError("Password do not match")
        return self
