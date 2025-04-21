"""This is an automatically generated file. Do not modify it.

This file was generated using `langgraph-gen` version 0.0.6.
To regenerate this file, run `langgraph-gen` with the source `yaml` file as an argument.

Usage:

1. Add the generated file to your project.
2. Create a new agent using the stub.

Below is a sample implementation of the generated stub:

```python
from typing_extensions import TypedDict

from response import ProtossBuildingWorkflow

class SomeState(TypedDict):
    # define your attributes here
    foo: str

# Define stand-alone functions
def nexus(state: SomeState) -> dict:
    print("In node: nexus")
    return {
        # Add your state update logic here
    }


def pylon(state: SomeState) -> dict:
    print("In node: pylon")
    return {
        # Add your state update logic here
    }


def assimilator(state: SomeState) -> dict:
    print("In node: assimilator")
    return {
        # Add your state update logic here
    }


def gateway(state: SomeState) -> dict:
    print("In node: gateway")
    return {
        # Add your state update logic here
    }


def cybernetics_core(state: SomeState) -> dict:
    print("In node: cybernetics_core")
    return {
        # Add your state update logic here
    }


def twilight_council(state: SomeState) -> dict:
    print("In node: twilight_council")
    return {
        # Add your state update logic here
    }


def robotics_facility(state: SomeState) -> dict:
    print("In node: robotics_facility")
    return {
        # Add your state update logic here
    }


def has_cybernetics_core(state: SomeState) -> str:
    print("In condition: has_cybernetics_core")
    raise NotImplementedError("Implement me.")


agent = ProtossBuildingWorkflow(
    state_schema=SomeState,
    impl=[
        ("nexus", nexus),
        ("pylon", pylon),
        ("assimilator", assimilator),
        ("gateway", gateway),
        ("cybernetics_core", cybernetics_core),
        ("twilight_council", twilight_council),
        ("robotics_facility", robotics_facility),
        ("has_cybernetics_core", has_cybernetics_core),
    ]
)

compiled_agent = agent.compile()

print(compiled_agent.invoke({"foo": "bar"}))
"""

from typing import Callable, Any, Optional, Type

from langgraph.constants import START, END  # noqa: F401
from langgraph.graph import StateGraph


def ProtossBuildingWorkflow(
    *,
    state_schema: Optional[Type[Any]] = None,
    config_schema: Optional[Type[Any]] = None,
    input: Optional[Type[Any]] = None,
    output: Optional[Type[Any]] = None,
    impl: list[tuple[str, Callable]],
) -> StateGraph:
    """Create the state graph for ProtossBuildingWorkflow."""
    # Declare the state graph
    builder = StateGraph(
        state_schema, config_schema=config_schema, input=input, output=output
    )

    nodes_by_name = {name: imp for name, imp in impl}

    all_names = set(nodes_by_name)

    expected_implementations = {
        "nexus",
        "pylon",
        "assimilator",
        "gateway",
        "cybernetics_core",
        "twilight_council",
        "robotics_facility",
        "has_cybernetics_core",
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
    builder.add_node("nexus", nodes_by_name["nexus"])
    builder.add_node("pylon", nodes_by_name["pylon"])
    builder.add_node("assimilator", nodes_by_name["assimilator"])
    builder.add_node("gateway", nodes_by_name["gateway"])
    builder.add_node("cybernetics_core", nodes_by_name["cybernetics_core"])
    builder.add_node("twilight_council", nodes_by_name["twilight_council"])
    builder.add_node("robotics_facility", nodes_by_name["robotics_facility"])

    # Add edges
    builder.add_edge(START, "nexus")
    builder.add_edge("nexus", "pylon")
    builder.add_edge("pylon", "assimilator")
    builder.add_edge("assimilator", "gateway")
    builder.add_conditional_edges(
        "gateway",
        nodes_by_name["has_cybernetics_core"],
        [
            "cybernetics_core",
            "twilight_council",
        ],
    )
    builder.add_edge("cybernetics_core", "robotics_facility")
    builder.add_edge("twilight_council", END)
    builder.add_edge("robotics_facility", END)
    return builder
