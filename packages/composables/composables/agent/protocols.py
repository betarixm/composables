from abc import ABC, abstractmethod
from collections.abc import AsyncGenerator


class Agent[State, Action](ABC):
    """Stateless agent that holds static configuration.

    Each ``interact`` call manages its own state and stateful actions.
    Concurrent calls on the same agent must not interfere with one another.
    Interaction state must not be stored on the agent itself.
    """

    @abstractmethod
    async def interact(self, observation: State) -> AsyncGenerator[Action, State]:
        """Yield actions and receive updated observations through ``asend``."""
        ...
