"""This is an automatically generated file. Do not modify it.

This file was generated using `langgraph-gen` version 0.0.6.
To regenerate this file, run `langgraph-gen` with the source `yaml` file as an argument.

Usage:

1. Add the generated file to your project.
2. Create a new agent using the stub.

Below is a sample implementation of the generated stub:

```python
from typing_extensions import TypedDict

from response import EmbassyShadow

class SomeState(TypedDict):
    # define your attributes here
    foo: str

# Define stand-alone functions
def start_briefing(state: SomeState) -> dict:
    print("In node: start_briefing")
    return {
        # Add your state update logic here
    }


def initial_contact(state: SomeState) -> dict:
    print("In node: initial_contact")
    return {
        # Add your state update logic here
    }


def gather_intel(state: SomeState) -> dict:
    print("In node: gather_intel")
    return {
        # Add your state update logic here
    }


def public_opinion(state: SomeState) -> dict:
    print("In node: public_opinion")
    return {
        # Add your state update logic here
    }


def event_interrupt(state: SomeState) -> dict:
    print("In node: event_interrupt")
    return {
        # Add your state update logic here
    }


def trade_negotiation(state: SomeState) -> dict:
    print("In node: trade_negotiation")
    return {
        # Add your state update logic here
    }


def internal_pressure(state: SomeState) -> dict:
    print("In node: internal_pressure")
    return {
        # Add your state update logic here
    }


def alliance_offer(state: SomeState) -> dict:
    print("In node: alliance_offer")
    return {
        # Add your state update logic here
    }


def emergency_summit(state: SomeState) -> dict:
    print("In node: emergency_summit")
    return {
        # Add your state update logic here
    }


def resolution(state: SomeState) -> dict:
    print("In node: resolution")
    return {
        # Add your state update logic here
    }


def select_strategy(state: SomeState) -> str:
    print("In condition: select_strategy")
    raise NotImplementedError("Implement me.")


def trust_level(state: SomeState) -> str:
    print("In condition: trust_level")
    raise NotImplementedError("Implement me.")


agent = EmbassyShadow(
    state_schema=SomeState,
    impl=[
        ("start_briefing", start_briefing),
        ("initial_contact", initial_contact),
        ("gather_intel", gather_intel),
        ("public_opinion", public_opinion),
        ("event_interrupt", event_interrupt),
        ("trade_negotiation", trade_negotiation),
        ("internal_pressure", internal_pressure),
        ("alliance_offer", alliance_offer),
        ("emergency_summit", emergency_summit),
        ("resolution", resolution),
        ("select_strategy", select_strategy),
        ("trust_level", trust_level),
    ]
)

compiled_agent = agent.compile()

print(compiled_agent.invoke({"foo": "bar"}))
"""

from typing import Callable, Any, Optional, Type

from langgraph.constants import START, END  # noqa: F401
from langgraph.graph import StateGraph


def EmbassyShadow(
    *,
    state_schema: Optional[Type[Any]] = None,
    config_schema: Optional[Type[Any]] = None,
    input: Optional[Type[Any]] = None,
    output: Optional[Type[Any]] = None,
    impl: list[tuple[str, Callable]],
) -> StateGraph:
    """Create the state graph for EmbassyShadow."""
    # Declare the state graph
    builder = StateGraph(
        state_schema, config_schema=config_schema, input=input, output=output
    )

    nodes_by_name = {name: imp for name, imp in impl}

    all_names = set(nodes_by_name)

    expected_implementations = {
        "start_briefing",
        "initial_contact",
        "gather_intel",
        "public_opinion",
        "event_interrupt",
        "trade_negotiation",
        "internal_pressure",
        "alliance_offer",
        "emergency_summit",
        "resolution",
        "select_strategy",
        "trust_level",
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
    builder.add_node("start_briefing", nodes_by_name["start_briefing"])
    builder.add_node("initial_contact", nodes_by_name["initial_contact"])
    builder.add_node("gather_intel", nodes_by_name["gather_intel"])
    builder.add_node("public_opinion", nodes_by_name["public_opinion"])
    builder.add_node("event_interrupt", nodes_by_name["event_interrupt"])
    builder.add_node("trade_negotiation", nodes_by_name["trade_negotiation"])
    builder.add_node("internal_pressure", nodes_by_name["internal_pressure"])
    builder.add_node("alliance_offer", nodes_by_name["alliance_offer"])
    builder.add_node("emergency_summit", nodes_by_name["emergency_summit"])
    builder.add_node("resolution", nodes_by_name["resolution"])

    # Add edges
    builder.add_edge(START, "start_briefing")
    builder.add_edge("start_briefing", "initial_contact")
    builder.add_conditional_edges(
        "initial_contact",
        nodes_by_name["select_strategy"],
        [
            "gather_intel",
            "public_opinion",
        ],
    )
    builder.add_edge("gather_intel", "gather_intel")
    builder.add_edge("gather_intel", "public_opinion")
    builder.add_edge("public_opinion", "event_interrupt")
    builder.add_edge("event_interrupt", "trade_negotiation")
    builder.add_conditional_edges(
        "trade_negotiation",
        nodes_by_name["trust_level"],
        [
            "emergency_summit",
            "internal_pressure",
        ],
    )
    builder.add_edge("internal_pressure", "emergency_summit")
    builder.add_edge("alliance_offer", "emergency_summit")
    builder.add_edge("emergency_summit", "resolution")
    builder.set_entry_point("start_briefing")
    return builder
