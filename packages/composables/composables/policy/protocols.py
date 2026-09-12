from abc import ABC, abstractmethod
from collections.abc import AsyncIterator


class Policy[State, Action](ABC):
    """Stateless policy that holds static configuration.

    Each ``run`` call manages its own state and stateful actions.
    Concurrent calls on the same policy must not interfere with one another.
    Execution state must not be stored on the policy itself.
    """

    @abstractmethod
    async def run(self, observation: State) -> AsyncIterator[Action]:
        """Stream actions from the initial observation."""
        ...
