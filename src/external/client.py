
import httpx
from typing import Optional, Dict, Any

class UserClient:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")

    def fetch_user(self, user_id: int) -> Optional[Dict[str, Any]]:
        url = f"{self.base_url}/users/{user_id}"
        r = httpx.get(url, headers={"Accept": "application/json"}, timeout=5.0)
        if r.status_code == 200:
            data = r.json()
            if "first" not in data or "last" not in data:
                return None
            return data
        return None
