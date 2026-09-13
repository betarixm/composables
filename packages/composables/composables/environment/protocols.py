from abc import ABC, abstractmethod
from types import TracebackType

from .types import Terminated, Truncated


class EnvironmentSession[State, Action, Reward, Context](ABC):
    """Stateful interaction with session resources scoped to ``async with``."""

    @abstractmethod
    async def step(
        self, action: Action
    ) -> tuple[State, Reward, Terminated, Truncated, Context]:
        """Apply an action and return the next state, reward, end flags, and context."""
        ...

    @abstractmethod
    async def __aenter__(self) -> State:
        """Acquire session resources and return the initial state."""
        ...

    @abstractmethod
    async def __aexit__(
        self,
        exception_type: type[BaseException] | None,
        exception: BaseException | None,
        traceback: TracebackType | None,
    ) -> bool | None:
        """Release session resources; return true to suppress an exception."""
        ...


class Environment[State, Action, Reward, Context](ABC):
    """Stateless factory for independent environment sessions."""

    @abstractmethod
    async def session(self) -> EnvironmentSession[State, Action, Reward, Context]:
        """Asynchronously create a session to be entered with ``async with``.

        Use ``async with await environment.session() as initial_state:``.
        """
        ...
