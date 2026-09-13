import asyncio
from collections.abc import AsyncGenerator, AsyncIterator
from contextlib import aclosing

from composables.agent.protocols import Agent
from composables.policy.protocols import Policy


class CountingPolicy(Policy[int, str]):
    async def run(self, observation: int) -> AsyncIterator[str]:
        for count in range(observation):
            yield str(count)


class ObservationAgent(Agent[int, str]):
    async def interact(self, observation: int) -> AsyncGenerator[str, int]:
        updated_observation = yield str(observation)
        yield str(updated_observation)


def test_policy_streams_actions_without_awaiting_run() -> None:
    async def collect_actions(policy: Policy[int, str]) -> list[str]:
        return [action async for action in policy.run(3)]

    assert asyncio.run(collect_actions(CountingPolicy())) == ["0", "1", "2"]


def test_agent_accepts_observations_without_awaiting_interact() -> None:
    async def exchange_observations(agent: Agent[int, str]) -> tuple[str, str]:
        async with aclosing(agent.interact(3)) as interaction:
            initial_action = await anext(interaction)
            updated_action = await interaction.asend(7)
            return initial_action, updated_action

    assert asyncio.run(exchange_observations(ObservationAgent())) == ("3", "7")
