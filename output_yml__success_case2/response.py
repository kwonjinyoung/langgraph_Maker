"""This is an automatically generated file. Do not modify it.

This file was generated using `langgraph-gen` version 0.0.6.
To regenerate this file, run `langgraph-gen` with the source `yaml` file as an argument.

Usage:

1. Add the generated file to your project.
2. Create a new agent using the stub.

Below is a sample implementation of the generated stub:

```python
from typing_extensions import TypedDict

from response import ProtossBuildingUnitActivation

class SomeState(TypedDict):
    # define your attributes here
    foo: str

# Define stand-alone functions
def Nexus(state: SomeState) -> dict:
    print("In node: Nexus")
    return {
        # Add your state update logic here
    }


def Pylon(state: SomeState) -> dict:
    print("In node: Pylon")
    return {
        # Add your state update logic here
    }


def Assimilator(state: SomeState) -> dict:
    print("In node: Assimilator")
    return {
        # Add your state update logic here
    }


def Gateway(state: SomeState) -> dict:
    print("In node: Gateway")
    return {
        # Add your state update logic here
    }


def Cybernetics_Core(state: SomeState) -> dict:
    print("In node: Cybernetics Core")
    return {
        # Add your state update logic here
    }


def Warp_Gate(state: SomeState) -> dict:
    print("In node: Warp Gate")
    return {
        # Add your state update logic here
    }


def Robotics_Facility(state: SomeState) -> dict:
    print("In node: Robotics Facility")
    return {
        # Add your state update logic here
    }


def Robotics_Bay(state: SomeState) -> dict:
    print("In node: Robotics Bay")
    return {
        # Add your state update logic here
    }


def Stargate(state: SomeState) -> dict:
    print("In node: Stargate")
    return {
        # Add your state update logic here
    }


def Fleet_Beacon(state: SomeState) -> dict:
    print("In node: Fleet Beacon")
    return {
        # Add your state update logic here
    }


def Twilight_Council(state: SomeState) -> dict:
    print("In node: Twilight Council")
    return {
        # Add your state update logic here
    }


def Templar_Archives(state: SomeState) -> dict:
    print("In node: Templar Archives")
    return {
        # Add your state update logic here
    }


def Dark_Shrine(state: SomeState) -> dict:
    print("In node: Dark Shrine")
    return {
        # Add your state update logic here
    }


def Zealot(state: SomeState) -> dict:
    print("In node: Zealot")
    return {
        # Add your state update logic here
    }


def Stalker(state: SomeState) -> dict:
    print("In node: Stalker")
    return {
        # Add your state update logic here
    }


def Sentry(state: SomeState) -> dict:
    print("In node: Sentry")
    return {
        # Add your state update logic here
    }


def Adept(state: SomeState) -> dict:
    print("In node: Adept")
    return {
        # Add your state update logic here
    }


def High_Templar(state: SomeState) -> dict:
    print("In node: High Templar")
    return {
        # Add your state update logic here
    }


def Dark_Templar(state: SomeState) -> dict:
    print("In node: Dark Templar")
    return {
        # Add your state update logic here
    }


def Archon(state: SomeState) -> dict:
    print("In node: Archon")
    return {
        # Add your state update logic here
    }


def Immortal(state: SomeState) -> dict:
    print("In node: Immortal")
    return {
        # Add your state update logic here
    }


def Colossus(state: SomeState) -> dict:
    print("In node: Colossus")
    return {
        # Add your state update logic here
    }


def Disruptor(state: SomeState) -> dict:
    print("In node: Disruptor")
    return {
        # Add your state update logic here
    }


def Phoenix(state: SomeState) -> dict:
    print("In node: Phoenix")
    return {
        # Add your state update logic here
    }


def Void_Ray(state: SomeState) -> dict:
    print("In node: Void Ray")
    return {
        # Add your state update logic here
    }


def Oracle(state: SomeState) -> dict:
    print("In node: Oracle")
    return {
        # Add your state update logic here
    }


def Carrier(state: SomeState) -> dict:
    print("In node: Carrier")
    return {
        # Add your state update logic here
    }


def Tempest(state: SomeState) -> dict:
    print("In node: Tempest")
    return {
        # Add your state update logic here
    }


def Mothership(state: SomeState) -> dict:
    print("In node: Mothership")
    return {
        # Add your state update logic here
    }


agent = ProtossBuildingUnitActivation(
    state_schema=SomeState,
    impl=[
        ("Nexus", Nexus),
        ("Pylon", Pylon),
        ("Assimilator", Assimilator),
        ("Gateway", Gateway),
        ("Cybernetics Core", Cybernetics_Core),
        ("Warp Gate", Warp_Gate),
        ("Robotics Facility", Robotics_Facility),
        ("Robotics Bay", Robotics_Bay),
        ("Stargate", Stargate),
        ("Fleet Beacon", Fleet_Beacon),
        ("Twilight Council", Twilight_Council),
        ("Templar Archives", Templar_Archives),
        ("Dark Shrine", Dark_Shrine),
        ("Zealot", Zealot),
        ("Stalker", Stalker),
        ("Sentry", Sentry),
        ("Adept", Adept),
        ("High Templar", High_Templar),
        ("Dark Templar", Dark_Templar),
        ("Archon", Archon),
        ("Immortal", Immortal),
        ("Colossus", Colossus),
        ("Disruptor", Disruptor),
        ("Phoenix", Phoenix),
        ("Void Ray", Void_Ray),
        ("Oracle", Oracle),
        ("Carrier", Carrier),
        ("Tempest", Tempest),
        ("Mothership", Mothership),
    ]
)

compiled_agent = agent.compile()

print(compiled_agent.invoke({"foo": "bar"}))
"""

from typing import Callable, Any, Optional, Type

from langgraph.constants import START, END  # noqa: F401
from langgraph.graph import StateGraph


def ProtossBuildingUnitActivation(
    *,
    state_schema: Optional[Type[Any]] = None,
    config_schema: Optional[Type[Any]] = None,
    input: Optional[Type[Any]] = None,
    output: Optional[Type[Any]] = None,
    impl: list[tuple[str, Callable]],
) -> StateGraph:
    """Create the state graph for ProtossBuildingUnitActivation."""
    # Declare the state graph
    builder = StateGraph(
        state_schema, config_schema=config_schema, input=input, output=output
    )

    nodes_by_name = {name: imp for name, imp in impl}

    all_names = set(nodes_by_name)

    expected_implementations = {
        "Nexus",
        "Pylon",
        "Assimilator",
        "Gateway",
        "Cybernetics_Core",
        "Warp_Gate",
        "Robotics_Facility",
        "Robotics_Bay",
        "Stargate",
        "Fleet_Beacon",
        "Twilight_Council",
        "Templar_Archives",
        "Dark_Shrine",
        "Zealot",
        "Stalker",
        "Sentry",
        "Adept",
        "High_Templar",
        "Dark_Templar",
        "Archon",
        "Immortal",
        "Colossus",
        "Disruptor",
        "Phoenix",
        "Void_Ray",
        "Oracle",
        "Carrier",
        "Tempest",
        "Mothership",
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
    builder.add_node("Nexus", nodes_by_name["Nexus"])
    builder.add_node("Pylon", nodes_by_name["Pylon"])
    builder.add_node("Assimilator", nodes_by_name["Assimilator"])
    builder.add_node("Gateway", nodes_by_name["Gateway"])
    builder.add_node("Cybernetics Core", nodes_by_name["Cybernetics_Core"])
    builder.add_node("Warp Gate", nodes_by_name["Warp_Gate"])
    builder.add_node("Robotics Facility", nodes_by_name["Robotics_Facility"])
    builder.add_node("Robotics Bay", nodes_by_name["Robotics_Bay"])
    builder.add_node("Stargate", nodes_by_name["Stargate"])
    builder.add_node("Fleet Beacon", nodes_by_name["Fleet_Beacon"])
    builder.add_node("Twilight Council", nodes_by_name["Twilight_Council"])
    builder.add_node("Templar Archives", nodes_by_name["Templar_Archives"])
    builder.add_node("Dark Shrine", nodes_by_name["Dark_Shrine"])
    builder.add_node("Zealot", nodes_by_name["Zealot"])
    builder.add_node("Stalker", nodes_by_name["Stalker"])
    builder.add_node("Sentry", nodes_by_name["Sentry"])
    builder.add_node("Adept", nodes_by_name["Adept"])
    builder.add_node("High Templar", nodes_by_name["High_Templar"])
    builder.add_node("Dark Templar", nodes_by_name["Dark_Templar"])
    builder.add_node("Archon", nodes_by_name["Archon"])
    builder.add_node("Immortal", nodes_by_name["Immortal"])
    builder.add_node("Colossus", nodes_by_name["Colossus"])
    builder.add_node("Disruptor", nodes_by_name["Disruptor"])
    builder.add_node("Phoenix", nodes_by_name["Phoenix"])
    builder.add_node("Void Ray", nodes_by_name["Void_Ray"])
    builder.add_node("Oracle", nodes_by_name["Oracle"])
    builder.add_node("Carrier", nodes_by_name["Carrier"])
    builder.add_node("Tempest", nodes_by_name["Tempest"])
    builder.add_node("Mothership", nodes_by_name["Mothership"])

    # Add edges
    builder.add_edge(START, "Nexus")
    builder.add_edge("Nexus", "Pylon")
    builder.add_edge("Pylon", "Gateway")
    builder.add_edge("Gateway", "Zealot")
    builder.add_edge("Gateway", "Cybernetics Core")
    builder.add_edge("Cybernetics Core", "Stalker")
    builder.add_edge("Cybernetics Core", "Sentry")
    builder.add_edge("Cybernetics Core", "Adept")
    builder.add_edge("Gateway", "Warp Gate")
    builder.add_edge("Warp Gate", "Zealot")
    builder.add_edge("Robotics Facility", "Immortal")
    builder.add_edge("Robotics Facility", "Robotics Bay")
    builder.add_edge("Robotics Bay", "Colossus")
    builder.add_edge("Robotics Bay", "Disruptor")
    builder.add_edge("Stargate", "Phoenix")
    builder.add_edge("Stargate", "Void Ray")
    builder.add_edge("Stargate", "Oracle")
    builder.add_edge("Stargate", "Fleet Beacon")
    builder.add_edge("Fleet Beacon", "Carrier")
    builder.add_edge("Fleet Beacon", "Tempest")
    builder.add_edge("Fleet Beacon", "Mothership")
    builder.add_edge("Twilight Council", "Templar Archives")
    builder.add_edge("Twilight Council", "Dark Shrine")
    builder.add_edge("Templar Archives", "High Templar")
    builder.add_edge("Dark Shrine", "Dark Templar")
    builder.add_edge("High Templar", "Archon")
    builder.add_edge("Dark Templar", "Archon")
    builder.add_edge("Archon", END)
    return builder
