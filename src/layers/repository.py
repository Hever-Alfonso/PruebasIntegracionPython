
from typing import Optional
from .models import User

class InMemoryUserRepository:
    _data = {
        1: User(1, "Ada", "Lovelace"),
        2: User(2, "Alan", "Turing"),
        3: User(3, "Grace", "Hopper"),
    }

    def find_by_id(self, user_id: int) -> Optional[User]:
        return self._data.get(user_id)
