# makeImage.py 실행 시 문제 해결 가이드

## 일반적인 에러 상황

### 1. NotImplementedError 발생 시

makeImage.py 실행 시 다음과 같은 에러가 발생할 수 있습니다:

```python
def has_cybernetics_core(state: SomeState) -> str:
    print("In condition: has_cybernetics_core")
    raise NotImplementedError("Implement me.")
```

에러 메시지:
```
예외가 발생했습니다. NotImplementedError
Implement me.
  File "/home/petero/langgraph_Maker/output_yml/response_impl.py", line 70, in has_cybernetics_core
    raise NotImplementedError("Implement me.")
  File "/home/petero/langgraph_Maker/output_yml/response_impl.py", line 89, in <module>
    print(compiled_agent.invoke({"foo": "bar"}))
  File "/home/petero/langgraph_Maker/output_yml/makeImage.py", line 2, in <module>
    from response_impl import compiled_agent
NotImplementedError: Implement me.
```

### 해결 방법
해당 함수를 다음과 같이 수정하여 pass 처리합니다:

```python
def has_cybernetics_core(state: SomeState) -> str:
    print("In condition: has_cybernetics_core")
    pass
```

### 2. invoke 관련 에러 발생 시

`print(compiled_agent.invoke({"foo": "bar"}))` 부분에서 에러가 발생하면 해당 라인을 주석 처리하세요.

