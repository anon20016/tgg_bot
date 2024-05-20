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

    def GetStateUrl(self, state_id: int):
        if state_id in self.states:
            return self.states[state_id].url
        return None

    def WhereCanMove(self, state_id: int, command: str) -> set:
        res = set()
        state = self.GetState(state_id)
        if state is None:
            log_error(f"Invalid state {state_id}")
        for neighbour in state.neighbours:
            neighbour_state_id = neighbour['id']
            tags = []
            for tag in neighbour['tags']:
                tags += tag['tags']
            main_tags = self.GetState(neighbour_state_id).tags
            for tag in tags + main_tags:
                if tag in command:
                    res.add(neighbour_state_id)
        return res


@logger
def JsonLoad():
    import os
    import json
    directory = "./states/"
    result = dict()

    with open(directory + '0.json', encoding='utf-8') as json_data:
        state = State(**json.load(json_data))
        result[state.id] = state

    for file in os.listdir(directory):
        if file == '0.json':
            pass
        with open(directory + file, encoding='utf-8') as json_data:
            state = State(**json.load(json_data))
            result[state.id] = state
            result[0].neighbours.append({'id': state.id, 'tags': []})
    return result
