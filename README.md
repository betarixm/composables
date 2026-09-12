<!-- markdownlint-disable -->

<div align="center">

<br />

<p><strong>GOOD PATTERNS DESERVE BEAUTIFUL TYPES.</strong></p>

<h1>🧩 composables</h1>

<p><strong>Familiar patterns. Beautiful types. Better code.</strong></p>

<p>
The patterns you reach for every day, expressed through precise Python types.<br />
Turn familiar ideas into clear contracts and code worth building on.
</p>

<p><strong>Zero runtime dependencies.</strong> Built entirely on the Python standard library.</p>

<p>
  <a href="packages/composables/pyproject.toml"><img src="https://img.shields.io/badge/Python-3.12%2B-3776AB?style=for-the-badge&amp;logo=python&amp;logoColor=white" alt="Python 3.12 or newer" /></a>
  <a href="packages/composables/pyproject.toml"><img src="https://img.shields.io/badge/Runtime_dependencies-0-0EA5E9?style=for-the-badge" alt="Zero runtime dependencies" /></a>
  <a href="packages/composables/composables/py.typed"><img src="https://img.shields.io/badge/Typing-PEP%20561-8B5CF6?style=for-the-badge" alt="PEP 561 typing support" /></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-10B981?style=for-the-badge" alt="MIT license" /></a>
  <a href="https://github.com/betarixm/composables/issues"><img src="https://img.shields.io/badge/Stage-Early-FF6B35?style=for-the-badge" alt="Early development" /></a>
</p>

<p>
  <a href="packages/composables/README.md"><strong>Explore the notions →</strong></a>
  &nbsp; · &nbsp;
  <a href="https://github.com/betarixm/composables/issues"><strong>Shape what comes next ↗</strong></a>
  &nbsp; · &nbsp;
  <a href="https://github.com/betarixm/composables/releases"><strong>Follow releases</strong></a>
</p>

<br />

</div>

---

## Your best patterns deserve better types.

Configuration factories. Action streams. Interactive agents. Stateful sessions. You reach for these patterns whenever you build something new.

**composables** gives them names and beautiful type definitions. We call them **notions**: recurring patterns expressed as small, precise contracts. Use them to make intent easier to read, implementations easier to compose, and changes easier to check.

The current package contains abstract base classes and domain types. You bring the behavior; the notions give your code a shared vocabulary.

<table>
<tr>
<td width="33%" valign="top">
<h3>🧩 Name the pattern</h3>
<p>Give recurring ideas a recognizable shape. Agents, policies, environments, and configuration factories become concepts your code can speak.</p>
</td>
<td width="33%" valign="top">
<h3>⇄ Let the types explain</h3>
<p>Generic parameters make inputs, outputs, and relationships explicit. See what a component accepts and produces before reading its implementation.</p>
</td>
<td width="33%" valign="top">
<h3>⌁ Raise the quality</h3>
<p>Implement against shared contracts. Help readers follow intent, type checkers catch mismatches, and future changes preserve the boundaries you chose.</p>
</td>
</tr>
</table>

## A small vocabulary. More expressive code.

Choose the notion that fits your pattern. Give its type parameters meaning in your domain.

```mermaid
flowchart LR
    agent["Agent<br/>Observations ↔ Actions"] --> implementation
    policy["Policy<br/>Observation → Action stream"] --> implementation
    environment["Environment<br/>Actions → Typed transitions"] --> implementation
    configurable["Configurable<br/>Configuration → Self"] --> implementation
    implementation["Your implementation<br/>Explicit contracts"] --> code
    code["Code you can<br/>read · compose · evolve"]

    classDef notion fill:#312e81,stroke:#a5b4fc,color:#ffffff,stroke-width:2px
    classDef outcome fill:#064e3b,stroke:#6ee7b7,color:#ffffff,stroke-width:2px
    class agent,policy,environment,configurable notion
    class implementation,code outcome
```

The types describe what goes in, what comes out, and how the pieces relate. Each notion also defines its behavioral contract, including execution state ownership and session lifetimes where relevant.

**Choose your pieces:** [Agent](packages/composables/composables/agent/protocols.py) · [Policy](packages/composables/composables/policy/protocols.py) · [Environment & sessions](packages/composables/composables/environment/protocols.py) · [Configurable](packages/composables/composables/configurable/protocols.py)

[Find your next notion in the catalog →](packages/composables/README.md)

## Get close to the code.

Use Python 3.12+ and the `uv` version pinned in [pyproject.toml](pyproject.toml).

```bash
git clone https://github.com/betarixm/composables.git
cd composables
uv sync --locked
```

Open the [catalog](packages/composables/README.md), recognize a pattern you use, and bring its type contract into your code.

<details>
<summary><strong>Working on the notions? Run the checks.</strong></summary>

```bash
uv run ruff format --check .
uv run ruff check .
uv run pyright
uv run pytest
uv build --package composables --no-sources
```

</details>

---

<div align="center">

<h2>You're early. Help define the vocabulary.</h2>

<p>
The API is still taking shape. Your use case can help define what comes next.<br />
Bring a pattern you keep writing. Help give it the type definition it deserves.
</p>

<p>
<strong>Star the repository to follow along. Open an issue to help steer it.</strong>
</p>

<p>
  <a href="https://github.com/betarixm/composables"><strong>☆ Follow the project</strong></a>
  &nbsp; · &nbsp;
  <a href="https://github.com/betarixm/composables/issues"><strong>Bring your use case →</strong></a>
</p>

<sub>Composable primitives for Python · <a href="LICENSE">MIT licensed</a></sub>

<br />

</div>
