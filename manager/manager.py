from entity.state import State
from helpers.logger import log_warning, log_error
from manager.StateManager import StateManager
from manager.UserManager import UserManager


class Manager:
    state_manager: StateManager
    user_manager: UserManager

    def __init__(self):
        self.user_manager = UserManager()
        self.user_manager.Load()

        self.state_manager = StateManager()
        self.state_manager.Load()

    def WhereCanMove(self, user_id: int, command: str):
        # Тут можно вставить анализатор текста
        user_state: State = self.state_manager.GetState(self.user_manager.GetStateId(user_id))
        if not user_state:
            log_warning(f"No user with id {user_id} in system")
            return []
        return self.state_manager.WhereCanMove(user_state.id, command)

    def Move(self, user_id: int, state: int, command: str):
        user_state: State = self.state_manager.GetState(self.user_manager.GetStateId(user_id))
        if state not in self.state_manager.WhereCanMove(user_state.id, command):
            log_error(f"Invalid state for {user_id}. Try to move from {user_state.id} to {state}")
        self.user_manager.Move(user_id, state, command)
