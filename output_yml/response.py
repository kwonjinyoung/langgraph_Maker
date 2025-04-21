"""This is an automatically generated file. Do not modify it.

This file was generated using `langgraph-gen` version 0.0.6.
To regenerate this file, run `langgraph-gen` with the source `yaml` file as an argument.

Usage:

1. Add the generated file to your project.
2. Create a new agent using the stub.

Below is a sample implementation of the generated stub:

```python
from typing_extensions import TypedDict

from response import TerranTechTree

class SomeState(TypedDict):
    # define your attributes here
    foo: str

# Define stand-alone functions
def CommandCenter(state: SomeState) -> dict:
    print("In node: CommandCenter")
    return {
        # Add your state update logic here
    }


def SupplyDepot(state: SomeState) -> dict:
    print("In node: SupplyDepot")
    return {
        # Add your state update logic here
    }


def Refinery(state: SomeState) -> dict:
    print("In node: Refinery")
    return {
        # Add your state update logic here
    }


def Barracks(state: SomeState) -> dict:
    print("In node: Barracks")
    return {
        # Add your state update logic here
    }


def EngineeringBay(state: SomeState) -> dict:
    print("In node: EngineeringBay")
    return {
        # Add your state update logic here
    }


def Academy(state: SomeState) -> dict:
    print("In node: Academy")
    return {
        # Add your state update logic here
    }


def Factory(state: SomeState) -> dict:
    print("In node: Factory")
    return {
        # Add your state update logic here
    }


def Armory(state: SomeState) -> dict:
    print("In node: Armory")
    return {
        # Add your state update logic here
    }


def Starport(state: SomeState) -> dict:
    print("In node: Starport")
    return {
        # Add your state update logic here
    }


def ScienceFacility(state: SomeState) -> dict:
    print("In node: ScienceFacility")
    return {
        # Add your state update logic here
    }


def FusionCore(state: SomeState) -> dict:
    print("In node: FusionCore")
    return {
        # Add your state update logic here
    }


def GhostAcademy(state: SomeState) -> dict:
    print("In node: GhostAcademy")
    return {
        # Add your state update logic here
    }


def Bunker(state: SomeState) -> dict:
    print("In node: Bunker")
    return {
        # Add your state update logic here
    }


def MissileTurret(state: SomeState) -> dict:
    print("In node: MissileTurret")
    return {
        # Add your state update logic here
    }


def SensorTower(state: SomeState) -> dict:
    print("In node: SensorTower")
    return {
        # Add your state update logic here
    }


def TechLabBarracks(state: SomeState) -> dict:
    print("In node: TechLabBarracks")
    return {
        # Add your state update logic here
    }


def ReactorBarracks(state: SomeState) -> dict:
    print("In node: ReactorBarracks")
    return {
        # Add your state update logic here
    }


def TechLabFactory(state: SomeState) -> dict:
    print("In node: TechLabFactory")
    return {
        # Add your state update logic here
    }


def ReactorFactory(state: SomeState) -> dict:
    print("In node: ReactorFactory")
    return {
        # Add your state update logic here
    }


def TechLabStarport(state: SomeState) -> dict:
    print("In node: TechLabStarport")
    return {
        # Add your state update logic here
    }


def ReactorStarport(state: SomeState) -> dict:
    print("In node: ReactorStarport")
    return {
        # Add your state update logic here
    }


agent = TerranTechTree(
    state_schema=SomeState,
    impl=[
        ("CommandCenter", CommandCenter),
        ("SupplyDepot", SupplyDepot),
        ("Refinery", Refinery),
        ("Barracks", Barracks),
        ("EngineeringBay", EngineeringBay),
        ("Academy", Academy),
        ("Factory", Factory),
        ("Armory", Armory),
        ("Starport", Starport),
        ("ScienceFacility", ScienceFacility),
        ("FusionCore", FusionCore),
        ("GhostAcademy", GhostAcademy),
        ("Bunker", Bunker),
        ("MissileTurret", MissileTurret),
        ("SensorTower", SensorTower),
        ("TechLabBarracks", TechLabBarracks),
        ("ReactorBarracks", ReactorBarracks),
        ("TechLabFactory", TechLabFactory),
        ("ReactorFactory", ReactorFactory),
        ("TechLabStarport", TechLabStarport),
        ("ReactorStarport", ReactorStarport),
    ]
)

compiled_agent = agent.compile()

print(compiled_agent.invoke({"foo": "bar"}))
"""

from typing import Callable, Any, Optional, Type

from langgraph.constants import START, END  # noqa: F401
from langgraph.graph import StateGraph


def TerranTechTree(
    *,
    state_schema: Optional[Type[Any]] = None,
    config_schema: Optional[Type[Any]] = None,
    input: Optional[Type[Any]] = None,
    output: Optional[Type[Any]] = None,
    impl: list[tuple[str, Callable]],
) -> StateGraph:
    """Create the state graph for TerranTechTree."""
    # Declare the state graph
    builder = StateGraph(
        state_schema, config_schema=config_schema, input=input, output=output
    )

    nodes_by_name = {name: imp for name, imp in impl}

    all_names = set(nodes_by_name)

    expected_implementations = {
        "CommandCenter",
        "SupplyDepot",
        "Refinery",
        "Barracks",
        "EngineeringBay",
        "Academy",
        "Factory",
        "Armory",
        "Starport",
        "ScienceFacility",
        "FusionCore",
        "GhostAcademy",
        "Bunker",
        "MissileTurret",
        "SensorTower",
        "TechLabBarracks",
        "ReactorBarracks",
        "TechLabFactory",
        "ReactorFactory",
        "TechLabStarport",
        "ReactorStarport",
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
    builder.add_node("CommandCenter", nodes_by_name["CommandCenter"])
    builder.add_node("SupplyDepot", nodes_by_name["SupplyDepot"])
    builder.add_node("Refinery", nodes_by_name["Refinery"])
    builder.add_node("Barracks", nodes_by_name["Barracks"])
    builder.add_node("EngineeringBay", nodes_by_name["EngineeringBay"])
    builder.add_node("Academy", nodes_by_name["Academy"])
    builder.add_node("Factory", nodes_by_name["Factory"])
    builder.add_node("Armory", nodes_by_name["Armory"])
    builder.add_node("Starport", nodes_by_name["Starport"])
    builder.add_node("ScienceFacility", nodes_by_name["ScienceFacility"])
    builder.add_node("FusionCore", nodes_by_name["FusionCore"])
    builder.add_node("GhostAcademy", nodes_by_name["GhostAcademy"])
    builder.add_node("Bunker", nodes_by_name["Bunker"])
    builder.add_node("MissileTurret", nodes_by_name["MissileTurret"])
    builder.add_node("SensorTower", nodes_by_name["SensorTower"])
    builder.add_node("TechLabBarracks", nodes_by_name["TechLabBarracks"])
    builder.add_node("ReactorBarracks", nodes_by_name["ReactorBarracks"])
    builder.add_node("TechLabFactory", nodes_by_name["TechLabFactory"])
    builder.add_node("ReactorFactory", nodes_by_name["ReactorFactory"])
    builder.add_node("TechLabStarport", nodes_by_name["TechLabStarport"])
    builder.add_node("ReactorStarport", nodes_by_name["ReactorStarport"])

    # Add edges
    builder.add_edge(START, "CommandCenter")
    builder.add_edge("CommandCenter", "SupplyDepot")
    builder.add_edge("CommandCenter", "Refinery")
    builder.add_edge("SupplyDepot", "Barracks")
    builder.add_edge("Barracks", "EngineeringBay")
    builder.add_edge("Barracks", "Academy")
    builder.add_edge("Barracks", "Factory")
    builder.add_edge("Factory", "Armory")
    builder.add_edge("Factory", "Starport")
    builder.add_edge("Starport", "ScienceFacility")
    builder.add_edge("ScienceFacility", "FusionCore")
    builder.add_edge("Barracks", "GhostAcademy")
    builder.add_edge("Barracks", "Bunker")
    builder.add_edge("EngineeringBay", "MissileTurret")
    builder.add_edge("EngineeringBay", "SensorTower")
    builder.add_edge("Barracks", "TechLabBarracks")
    builder.add_edge("Barracks", "ReactorBarracks")
    builder.add_edge("Factory", "TechLabFactory")
    builder.add_edge("Factory", "ReactorFactory")
    builder.add_edge("Starport", "TechLabStarport")
    builder.add_edge("Starport", "ReactorStarport")
    builder.add_edge("FusionCore", END)
    builder.set_entry_point("CommandCenter")
    return builder
