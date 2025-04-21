"""This is an automatically generated file. Do not modify it.

This file was generated using `langgraph-gen` version 0.0.6.
To regenerate this file, run `langgraph-gen` with the source `yaml` file as an argument.

Usage:

1. Add the generated file to your project.
2. Create a new agent using the stub.

Below is a sample implementation of the generated stub:

```python
from typing_extensions import TypedDict

from response import WebServiceUserFlow

class SomeState(TypedDict):
    # define your attributes here
    foo: str

# Define stand-alone functions
def GuestHomepage(state: SomeState) -> dict:
    print("In node: GuestHomepage")
    return {
        # Add your state update logic here
    }


def SignupForm(state: SomeState) -> dict:
    print("In node: SignupForm")
    return {
        # Add your state update logic here
    }


def LoginForm(state: SomeState) -> dict:
    print("In node: LoginForm")
    return {
        # Add your state update logic here
    }


def AuthenticatedUser(state: SomeState) -> dict:
    print("In node: AuthenticatedUser")
    return {
        # Add your state update logic here
    }


def ViewBoard(state: SomeState) -> dict:
    print("In node: ViewBoard")
    return {
        # Add your state update logic here
    }


def ReadPost(state: SomeState) -> dict:
    print("In node: ReadPost")
    return {
        # Add your state update logic here
    }


def WritePost(state: SomeState) -> dict:
    print("In node: WritePost")
    return {
        # Add your state update logic here
    }


def EditPost(state: SomeState) -> dict:
    print("In node: EditPost")
    return {
        # Add your state update logic here
    }


def CommentPost(state: SomeState) -> dict:
    print("In node: CommentPost")
    return {
        # Add your state update logic here
    }


def UserSettings(state: SomeState) -> dict:
    print("In node: UserSettings")
    return {
        # Add your state update logic here
    }


def Logout(state: SomeState) -> dict:
    print("In node: Logout")
    return {
        # Add your state update logic here
    }


def AdminPanel(state: SomeState) -> dict:
    print("In node: AdminPanel")
    return {
        # Add your state update logic here
    }


def ModerateContent(state: SomeState) -> dict:
    print("In node: ModerateContent")
    return {
        # Add your state update logic here
    }


agent = WebServiceUserFlow(
    state_schema=SomeState,
    impl=[
        ("GuestHomepage", GuestHomepage),
        ("SignupForm", SignupForm),
        ("LoginForm", LoginForm),
        ("AuthenticatedUser", AuthenticatedUser),
        ("ViewBoard", ViewBoard),
        ("ReadPost", ReadPost),
        ("WritePost", WritePost),
        ("EditPost", EditPost),
        ("CommentPost", CommentPost),
        ("UserSettings", UserSettings),
        ("Logout", Logout),
        ("AdminPanel", AdminPanel),
        ("ModerateContent", ModerateContent),
    ]
)

compiled_agent = agent.compile()

print(compiled_agent.invoke({"foo": "bar"}))
"""

from typing import Callable, Any, Optional, Type

from langgraph.constants import START, END  # noqa: F401
from langgraph.graph import StateGraph


def WebServiceUserFlow(
    *,
    state_schema: Optional[Type[Any]] = None,
    config_schema: Optional[Type[Any]] = None,
    input: Optional[Type[Any]] = None,
    output: Optional[Type[Any]] = None,
    impl: list[tuple[str, Callable]],
) -> StateGraph:
    """Create the state graph for WebServiceUserFlow."""
    # Declare the state graph
    builder = StateGraph(
        state_schema, config_schema=config_schema, input=input, output=output
    )

    nodes_by_name = {name: imp for name, imp in impl}

    all_names = set(nodes_by_name)

    expected_implementations = {
        "GuestHomepage",
        "SignupForm",
        "LoginForm",
        "AuthenticatedUser",
        "ViewBoard",
        "ReadPost",
        "WritePost",
        "EditPost",
        "CommentPost",
        "UserSettings",
        "Logout",
        "AdminPanel",
        "ModerateContent",
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
    builder.add_node("GuestHomepage", nodes_by_name["GuestHomepage"])
    builder.add_node("SignupForm", nodes_by_name["SignupForm"])
    builder.add_node("LoginForm", nodes_by_name["LoginForm"])
    builder.add_node("AuthenticatedUser", nodes_by_name["AuthenticatedUser"])
    builder.add_node("ViewBoard", nodes_by_name["ViewBoard"])
    builder.add_node("ReadPost", nodes_by_name["ReadPost"])
    builder.add_node("WritePost", nodes_by_name["WritePost"])
    builder.add_node("EditPost", nodes_by_name["EditPost"])
    builder.add_node("CommentPost", nodes_by_name["CommentPost"])
    builder.add_node("UserSettings", nodes_by_name["UserSettings"])
    builder.add_node("Logout", nodes_by_name["Logout"])
    builder.add_node("AdminPanel", nodes_by_name["AdminPanel"])
    builder.add_node("ModerateContent", nodes_by_name["ModerateContent"])

    # Add edges
    builder.add_edge(START, "GuestHomepage")
    builder.add_edge("GuestHomepage", "SignupForm")
    builder.add_edge("GuestHomepage", "LoginForm")
    builder.add_edge("SignupForm", "AuthenticatedUser")
    builder.add_edge("LoginForm", "AuthenticatedUser")
    builder.add_edge("AuthenticatedUser", "ViewBoard")
    builder.add_edge("ViewBoard", "ReadPost")
    builder.add_edge("ViewBoard", "WritePost")
    builder.add_edge("ReadPost", "EditPost")
    builder.add_edge("ReadPost", "CommentPost")
    builder.add_edge("AuthenticatedUser", "UserSettings")
    builder.add_edge("AuthenticatedUser", "Logout")
    builder.add_edge("AuthenticatedUser", "AdminPanel")
    builder.add_edge("AdminPanel", "ModerateContent")
    builder.add_edge("Logout", END)
    builder.set_entry_point("GuestHomepage")
    return builder
