import json


class User:
    user_id: int
    user_name: str
    state: int
    extra: str
    history: list[tuple[str, int]]

    def __init__(self, user_id, user_name='newcomer', state=0, extra='', history=None):
        if history is None:
            history = []
        self.user_id = user_id
        self.user_name = user_name
        self.state = state
        self.extra = extra
        self.history = history

    def __repr__(self):
        return f"User: {self.user_id}; Name: {self.user_name}; State: {self.state}; Extra: {self.extra}"

    def ToJson(self):
        return json.dumps(
            self,
            default=lambda o: o.__dict__,
            sort_keys=True,
            indent=5
        )

    def Move(self, command, state):
        self.history.append((command, state))
        self.state = state
