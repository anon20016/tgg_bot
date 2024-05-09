from entity.state import State
from helpers.config import GetParam
from helpers.logger import logger, log_error


class StateManager:
    def __init__(self):
        self.states = dict()
        self.transitions = dict()

    def Load(self):
        if GetParam('user_storage_type') == 'json':
            self.states = JsonLoad()

    def GetState(self, state_id: int):
        if state_id in self.states:
            return self.states[state_id]
        return None

    def WhereCanMove(self, state_id: int, command: str) -> list:
        res = []
        state = self.GetState(state_id)
        if state is None:
            log_error(f"Invalid state {state_id}")
        for neighbour in state.neighbours:
            main_tags = self.GetState(neighbour['id']).tags
            if command in neighbour['tags'] + main_tags:
                res.append(neighbour['id'])
        return res


@logger
def JsonLoad():
    import os
    import json
    directory = "./states/"

    result = dict()
    for file in os.listdir(directory):
        with open(directory + file, encoding='utf-8') as json_data:
            state = State(**json.load(json_data))
            result[state.id] = state
    return result
