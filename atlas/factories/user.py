from dataclasses import dataclass
from uuid import uuid4


@dataclass(frozen=True)
class UserData:
    name: str
    email: str


def user_factory(name: str = "Atlas User") -> UserData:
    token = uuid4().hex[:10]
    return UserData(name=name, email=f"atlas-{token}@example.test")
