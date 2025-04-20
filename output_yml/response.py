"""This is an automatically generated file. Do not modify it.

This file was generated using `langgraph-gen` version 0.0.6.
To regenerate this file, run `langgraph-gen` with the source `yaml` file as an argument.

Usage:

1. Add the generated file to your project.
2. Create a new agent using the stub.

Below is a sample implementation of the generated stub:

```python
from typing_extensions import TypedDict

from response import DigitalWorldExploration

class SomeState(TypedDict):
    # define your attributes here
    foo: str

# Define stand-alone functions
def start(state: SomeState) -> dict:
    print("In node: start")
    return {
        # Add your state update logic here
    }


def path_choice(state: SomeState) -> dict:
    print("In node: path_choice")
    return {
        # Add your state update logic here
    }


def encounter_guardian(state: SomeState) -> dict:
    print("In node: encounter_guardian")
    return {
        # Add your state update logic here
    }


def puzzle_room(state: SomeState) -> dict:
    print("In node: puzzle_room")
    return {
        # Add your state update logic here
    }


def hidden_path(state: SomeState) -> dict:
    print("In node: hidden_path")
    return {
        # Add your state update logic here
    }


def ai_companion(state: SomeState) -> dict:
    print("In node: ai_companion")
    return {
        # Add your state update logic here
    }


def betrayal_check(state: SomeState) -> dict:
    print("In node: betrayal_check")
    return {
        # Add your state update logic here
    }


def meta_anomaly(state: SomeState) -> dict:
    print("In node: meta_anomaly")
    return {
        # Add your state update logic here
    }


def final_gate(state: SomeState) -> dict:
    print("In node: final_gate")
    return {
        # Add your state update logic here
    }


def end(state: SomeState) -> dict:
    print("In node: end")
    return {
        # Add your state update logic here
    }


def user_input(state: SomeState) -> str:
    print("In condition: user_input")
    raise NotImplementedError("Implement me.")


def puzzle_success(state: SomeState) -> str:
    print("In condition: puzzle_success")
    raise NotImplementedError("Implement me.")


agent = DigitalWorldExploration(
    state_schema=SomeState,
    impl=[
        ("start", start),
        ("path_choice", path_choice),
        ("encounter_guardian", encounter_guardian),
        ("puzzle_room", puzzle_room),
        ("hidden_path", hidden_path),
        ("ai_companion", ai_companion),
        ("betrayal_check", betrayal_check),
        ("meta_anomaly", meta_anomaly),
        ("final_gate", final_gate),
        ("end", end),
        ("user_input", user_input),
        ("puzzle_success", puzzle_success),
    ]
)

compiled_agent = agent.compile()

print(compiled_agent.invoke({"foo": "bar"}))
"""

from typing import Callable, Any, Optional, Type

from langgraph.constants import START, END  # noqa: F401
from langgraph.graph import StateGraph


def DigitalWorldExploration(
    *,
    state_schema: Optional[Type[Any]] = None,
    config_schema: Optional[Type[Any]] = None,
    input: Optional[Type[Any]] = None,
    output: Optional[Type[Any]] = None,
    impl: list[tuple[str, Callable]],
) -> StateGraph:
    """Create the state graph for DigitalWorldExploration."""
    # Declare the state graph
    builder = StateGraph(
        state_schema, config_schema=config_schema, input=input, output=output
    )

    nodes_by_name = {name: imp for name, imp in impl}

    all_names = set(nodes_by_name)

    expected_implementations = {
        "start",
        "path_choice",
        "encounter_guardian",
        "puzzle_room",
        "hidden_path",
        "ai_companion",
        "betrayal_check",
        "meta_anomaly",
        "final_gate",
        "end",
        "user_input",
        "puzzle_success",
    }

    missing_nodes = expected_implementations - all_names
    if missing_nodes:
        raise ValueError(f"Missing implementations for: {missing_nodes}")

    extra_nodes = all_names - expected_implementations

    if extra_nodes:
        raise ValueError(
            f"Extra implementations for: {extra_nodes}. Please regenerate the stub."
        )

    # Add nodes
    builder.add_node("start", nodes_by_name["start"])
    builder.add_node("path_choice", nodes_by_name["path_choice"])
    builder.add_node("encounter_guardian", nodes_by_name["encounter_guardian"])
    builder.add_node("puzzle_room", nodes_by_name["puzzle_room"])
    builder.add_node("hidden_path", nodes_by_name["hidden_path"])
    builder.add_node("ai_companion", nodes_by_name["ai_companion"])
    builder.add_node("betrayal_check", nodes_by_name["betrayal_check"])
    builder.add_node("meta_anomaly", nodes_by_name["meta_anomaly"])
    builder.add_node("final_gate", nodes_by_name["final_gate"])
    builder.add_node("end", nodes_by_name["end"])

    # Add edges
    builder.add_edge(START, "start")
    builder.add_edge("start", "path_choice")
    builder.add_conditional_edges(
        "path_choice",
        nodes_by_name["user_input"],
        [
            "encounter_guardian",
            "hidden_path",
            "puzzle_room",
        ],
    )
    builder.add_edge("encounter_guardian", "puzzle_room")
    builder.add_conditional_edges(
        "puzzle_room",
        nodes_by_name["puzzle_success"],
        [
            "hidden_path",
            "puzzle_room",
        ],
    )
    builder.add_edge("hidden_path", "ai_companion")
    builder.add_edge("ai_companion", "betrayal_check")
    builder.add_edge("betrayal_check", "meta_anomaly")
    builder.add_edge("meta_anomaly", "final_gate")
    builder.add_edge("final_gate", END)
    return builder
