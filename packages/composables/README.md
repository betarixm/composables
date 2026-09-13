# 🧩 composables

> **Familiar patterns. Beautiful types. Better code.**
>
> Your next abstraction might already have a name.

**Zero runtime dependencies.** Every notion uses only the Python standard
library.

A growing catalog of **notions**: recurring patterns expressed through precise
Python types. Give your code a shared vocabulary that makes intent easier to
read, implementations easier to compose, and changes easier to check.

| Notion | The pattern |
| --- | --- |
| [Agent](#agent) | An ongoing exchange of observations and actions. |
| [Policy](#policy) | A stream of actions from an initial observation. |
| [Environment](#environment) | A factory, a live session, a typed transition. |
| [Configurable](#configurable) | Construction from a typed configuration. |

## Agent

**Give every interaction a clear contract.**

`Agent[State, Action]` names both sides of an interaction. Yield actions,
receive new observations through `asend`, and let the types describe the
exchange before anyone reads the implementation.

```text
interact(observation: State) → AsyncGenerator[Action, State]
```

The agent holds static configuration. Each call owns its interaction state
and actions; concurrent calls on the same agent must remain independent.

[Explore the Agent notion →][agent]

## Policy

**Turn an intention into a typed stream of actions.**

`Policy[State, Action]` gives action generation a reusable shape. Start with
an observation and produce an asynchronous action stream, with the input
and output types visible at the boundary.

```text
run(observation: State) → AsyncIterator[Action]
```

The policy holds static configuration. Each run owns its execution state
and actions; concurrent runs on the same policy must remain independent.

[Explore the Policy notion →][policy]

## Environment

**Make the world your code acts on explicit.**

`Environment[State, Action, Reward, Context]` pairs a reusable factory with
`EnvironmentSession[State, Action, Reward, Context]`. The types name what
an action changes, what it earns, and what comes back with the result.

```text
session() → EnvironmentSession[State, Action, Reward, Context]
await step(action: Action) → tuple[State, Reward, Terminated, Truncated, Context]
```

The environment is stateless. Each session owns its interaction state and
uses `async with` to scope resource acquisition and cleanup. Await each
`session.step(action)` call to obtain its transition result.

Two distinct boolean types give episode endings their own meaning:

| Type | What it tells you |
| --- | --- |
| `Terminated` | The episode reached a terminal state. |
| `Truncated` | An external limit ended the episode. |

[Explore the Environment notion →][environment] · [Episode types][endings]

## Configurable

**Give construction the same clarity as behavior.**

`Configurable[Configuration]` binds a component to a configuration type you
choose. Its factory accepts that type and returns `Self`, preserving the
concrete subclass in the type contract.

```text
from_configuration(configuration: Configuration) → Self
```

A shared construction pattern makes configuration requirements visible
across implementations.

[Explore the Configurable notion →][configurable]

[agent]: composables/agent/protocols.py
[policy]: composables/policy/protocols.py
[environment]: composables/environment/protocols.py
[endings]: composables/environment/types.py
[configurable]: composables/configurable/protocols.py
