
makeImage.py 실행시 다음과 같은 에러가 나올 수도 있다.


def has_cybernetics_core(state: SomeState) -> str:
    print("In condition: has_cybernetics_core")
    raise NotImplementedError("Implement me.")


예외가 발생했습니다. NotImplementedError
Implement me.
  File "/home/petero/langgraph_Maker/output_yml/response_impl.py", line 70, in has_cybernetics_core
    raise NotImplementedError("Implement me.")
  File "/home/petero/langgraph_Maker/output_yml/response_impl.py", line 89, in <module>
    print(compiled_agent.invoke({"foo": "bar"}))
  File "/home/petero/langgraph_Maker/output_yml/makeImage.py", line 2, in <module>
    from response_impl import compiled_agent
NotImplementedError: Implement me.

그럴 경우 다음과 같이 pass 처리 하면 된다.


def has_cybernetics_core(state: SomeState) -> str:
    print("In condition: has_cybernetics_core")
    pass


-------------------

print(compiled_agent.invoke({"foo": "bar"}))
이 부분에서 에러 발생시 주석 처리

