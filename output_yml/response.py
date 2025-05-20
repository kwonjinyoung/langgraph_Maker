"""This is an automatically generated file. Do not modify it.

This file was generated using `langgraph-gen` version 0.0.6.
To regenerate this file, run `langgraph-gen` with the source `yaml` file as an argument.

Usage:

1. Add the generated file to your project.
2. Create a new agent using the stub.

Below is a sample implementation of the generated stub:

```python
from typing_extensions import TypedDict

from response import PermissionInfoRetrieval

class SomeState(TypedDict):
    # define your attributes here
    foo: str

# Define stand-alone functions
def check_vectorstore(state: SomeState) -> dict:
    print("In node: check_vectorstore")
    return {
        # Add your state update logic here
    }


def process_vectorstore_result(state: SomeState) -> dict:
    print("In node: process_vectorstore_result")
    return {
        # Add your state update logic here
    }


def extract_keywords(state: SomeState) -> dict:
    print("In node: extract_keywords")
    return {
        # Add your state update logic here
    }


def search_confluence(state: SomeState) -> dict:
    print("In node: search_confluence")
    return {
        # Add your state update logic here
    }


def analyze_confluence_result(state: SomeState) -> dict:
    print("In node: analyze_confluence_result")
    return {
        # Add your state update logic here
    }


def generate_rag_response(state: SomeState) -> dict:
    print("In node: generate_rag_response")
    return {
        # Add your state update logic here
    }


def retry_with_alternate_keywords(state: SomeState) -> dict:
    print("In node: retry_with_alternate_keywords")
    return {
        # Add your state update logic here
    }


def is_sufficient(state: SomeState) -> str:
    print("In condition: is_sufficient")
    raise NotImplementedError("Implement me.")


def is_sufficient(state: SomeState) -> str:
    print("In condition: is_sufficient")
    raise NotImplementedError("Implement me.")


def retry_limit_exceeded(state: SomeState) -> str:
    print("In condition: retry_limit_exceeded")
    raise NotImplementedError("Implement me.")


agent = PermissionInfoRetrieval(
    state_schema=SomeState,
    impl=[
        ("check_vectorstore", check_vectorstore),
        ("process_vectorstore_result", process_vectorstore_result),
        ("extract_keywords", extract_keywords),
        ("search_confluence", search_confluence),
        ("analyze_confluence_result", analyze_confluence_result),
        ("generate_rag_response", generate_rag_response),
        ("retry_with_alternate_keywords", retry_with_alternate_keywords),
        ("is_sufficient", is_sufficient),
        ("is_sufficient", is_sufficient),
        ("retry_limit_exceeded", retry_limit_exceeded),
    ]
)

compiled_agent = agent.compile()

print(compiled_agent.invoke({"foo": "bar"}))
"""

from typing import Callable, Any, Optional, Type

from langgraph.constants import START, END  # noqa: F401
from langgraph.graph import StateGraph


def PermissionInfoRetrieval(
    *,
    state_schema: Optional[Type[Any]] = None,
    config_schema: Optional[Type[Any]] = None,
    input: Optional[Type[Any]] = None,
    output: Optional[Type[Any]] = None,
    impl: list[tuple[str, Callable]],
) -> StateGraph:
    """Create the state graph for PermissionInfoRetrieval."""
    # Declare the state graph
    builder = StateGraph(
        state_schema, config_schema=config_schema, input=input, output=output
    )

    nodes_by_name = {name: imp for name, imp in impl}

    all_names = set(nodes_by_name)

    expected_implementations = {
        "check_vectorstore",
        "process_vectorstore_result",
        "extract_keywords",
        "search_confluence",
        "analyze_confluence_result",
        "generate_rag_response",
        "retry_with_alternate_keywords",
        "is_sufficient",
        "is_sufficient",
        "retry_limit_exceeded",
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
    builder.add_node("check_vectorstore", nodes_by_name["check_vectorstore"])
    builder.add_node("process_vectorstore_result", nodes_by_name["process_vectorstore_result"])
    builder.add_node("extract_keywords", nodes_by_name["extract_keywords"])
    builder.add_node("search_confluence", nodes_by_name["search_confluence"])
    builder.add_node("analyze_confluence_result", nodes_by_name["analyze_confluence_result"])
    builder.add_node("generate_rag_response", nodes_by_name["generate_rag_response"])
    builder.add_node("retry_with_alternate_keywords", nodes_by_name["retry_with_alternate_keywords"])

    # Add edges
    builder.add_edge(START, "check_vectorstore")
    builder.add_edge("check_vectorstore", "process_vectorstore_result")
    builder.add_conditional_edges(
        "process_vectorstore_result",
        nodes_by_name["is_sufficient"],
        [
            "generate_rag_response",
            "extract_keywords",
        ],
    )
    builder.add_edge("extract_keywords", "search_confluence")
    builder.add_edge("search_confluence", "analyze_confluence_result")
    builder.add_conditional_edges(
        "analyze_confluence_result",
        nodes_by_name["is_sufficient"],
        [
            "generate_rag_response",
            "retry_with_alternate_keywords",
        ],
    )
    builder.add_conditional_edges(
        "retry_with_alternate_keywords",
        nodes_by_name["retry_limit_exceeded"],
        [
            "search_confluence",
            END,
        ],
    )
    builder.add_edge("generate_rag_response", END)
    return builder
