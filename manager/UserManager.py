import json

from entity.user import User
from helpers.config import GetParam
from helpers.logger import logger, log_error


class UserManager:
    def __init__(self):
        self.users = dict()
        self.online = set()

    def Load(self):
        if GetParam('user_storage_type') == 'json':
            self.users = JsonLoad()

    def Move(self, user_id: int, state: int, command: str):
        user = self.users[user_id]
        user.Move(command, state)
        with open(f'users/{user_id}.json', 'w', encoding='utf-8') as f:
            json.dump(user.__dict__, f, ensure_ascii=False)

    def GetStateId(self, user_id: int) -> int:
        if user_id in self.users:
            return self.users[user_id].state
        else:
            log_error(f"Trying to get state from unknown user {user_id}")


@logger
def JsonLoad():
    import os
    import json
    directory = "./users/"

    result = dict()
    for file in os.listdir(directory):
        with open(directory + file, encoding='utf-8') as json_data:
            user = User(**json.load(json_data))
            result[user.user_id] = user
    return result
