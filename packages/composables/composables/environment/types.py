from typing import NewType

# The episode ended by reaching a terminal state.
Terminated = NewType("Terminated", bool)
# The episode ended due to an external limit, such as a time budget.
Truncated = NewType("Truncated", bool)
