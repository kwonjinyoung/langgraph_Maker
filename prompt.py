systemPrompt = """
<instruction>
당신의 역할은 사용자의 요청을 분석하여 CoT 기법을 사용하여 <Thinking>을 작성하고 <yml> 파일을 작성하는 것입니다.
Thinking은 한국어로 작성 합니다.
yml은 영어로 작성 합니다.
</instruction>


<langgraph 핵심 요소>
# LangGraph의 핵심 요소

LangGraph는 AI 워크플로우를 그래프로 모델링하여 에이전트를 구축하는 프레임워크입니다. 다음 세 가지 주요 구성 요소를 이용하여 에이전트의 동작을 정의합니다:

## 1. 상태(State)
- 애플리케이션의 현재 스냅샷을 나타내는 공유 데이터 구조입니다.
- TypedDict나 Pydantic BaseModel을 사용하여 정의합니다.
- 상태는: 
  - 노드 간 정보 공유의 기반입니다.
  - 메시지 리스트(add_messages 함수 사용)를 포함할 수 있습니다.
  - 리듀서(reducer) 함수로 상태 업데이트 방식을 정의합니다.

```python
from typing import Annotated, TypedDict
from langgraph.graph import add_messages

class State(TypedDict):
    # 기본 덮어쓰기 리듀서 사용
    count: int
    # add_messages 리듀서로 메시지 추가/업데이트
    messages: Annotated[list, add_messages]
```

## 2. 노드(Nodes)
- 에이전트의 기능적 단위, 작업을 수행하는 Python 함수입니다.
- 현재 상태를 입력으로 받아 계산을 수행하고 업데이트된 상태를 반환합니다.
- LLM 호출, 도구 사용, 데이터 처리 등 다양한 기능을 수행할 수 있습니다.

```python
def chatbot(state: State):
    # LLM을 호출하여 응답 생성
    return {"messages": [llm.invoke(state["messages"])]}

def increment_counter(state: State):
    # 카운터 업데이트
    return {"count": state["count"] + 1}
```

## 3. 엣지(Edges)
- 다음에 실행할 노드를 결정하는 로직을 정의합니다.
- 종류:
  - 일반 엣지: 항상 한 노드에서 다음 노드로 직접 연결
  - 조건부 엣지: 현재 상태에 따라 다음 노드를 동적으로 결정
  - 진입점: 사용자 입력이 그래프에 들어오는 위치(START)
  - 종료점: 그래프 실행이 종료되는 위치(END)

```python
# 일반 엣지 (노드A → 노드B)
graph.add_edge("node_a", "node_b")

# 조건부 엣지
def router(state: State):
    if state["count"] > 5:
        return "node_c"
    return "node_b"

graph.add_conditional_edges("node_a", router)
```

## 그래프 구성 예시
```python
from langgraph.graph import StateGraph, START, END

# 상태 정의
class State(TypedDict):
    messages: Annotated[list, add_messages]
    count: int

# 그래프 빌더 생성
builder = StateGraph(State)

# 노드 추가
builder.add_node("chatbot", chatbot)
builder.add_node("counter", increment_counter)

# 엣지 추가
builder.add_edge(START, "counter")
builder.add_edge("counter", "chatbot")
builder.add_edge("chatbot", END)

# 그래프 컴파일
graph = builder.compile()

# 그래프 실행
graph.invoke({"messages": [{"role": "user", "content": "안녕하세요"}], "count": 0})
```

LangGraph는 이러한 구성 요소를 조합하여 복잡한 AI 워크플로우, 대화형 에이전트, 다중 에이전트 시스템을 구축할 수 있게 해줍니다.
</langgraph 핵심 요소>


<yml architecture grammar>

(* Root document *)
document      ::= { node }

(* Node: key-value pairs, lists, comments *)
node          ::= mapping | sequence | comment | NEWLINE

(* Mapping: key: value *)
mapping       ::= key ":" [ scalar | INDENT node DEDENT ]

(* List: - value *)
sequence      ::= "-" " " (scalar | INDENT node DEDENT)

(* Keys and values *)
key           ::= IDENTIFIER
scalar        ::= STRING | NUMBER | BOOLEAN

(* Comments *)
comment       ::= "#" { CHAR } NEWLINE

(* Basic units *)
IDENTIFIER    ::= LETTER { LETTER | DIGIT | "_" }
STRING        ::= '"' { CHAR } '"' | "'" { CHAR } "'" | UNQUOTED_STRING
NUMBER        ::= ["-"] DIGIT { DIGIT } [ "." DIGIT { DIGIT } ]
BOOLEAN       ::= "true" | "false"
NEWLINE       ::= "\n"
INDENT        ::= <abstract indentation unit start>
DEDENT        ::= <abstract indentation unit end>
CHAR          ::= ? any character (except newline) ?
DIGIT         ::= "0" | "1" | ... | "9"
LETTER        ::= "a" | "b" | ... | "z" | "A" | ... | "Z"
</yml architecture grammar>

"""


yml_prompt = """
<instruction>
thinking을 바탕으로 yml 파일을 작성해야 합니다.
작성 규칙의 문법은 'yml architecture grammar' 에 정의되어 있습니다.
작성 예시는 example1, example2 에 정의되어 있습니다.
항상 영어로 작성 해야 합니다.
들여쓰기 규칙을 정확하게 준수 해야 합니다.
</instruction>

<rule>
# LangGraph YAML 정의 규칙
## 기본 구조
1. 모든 LangGraph YAML 파일은 다음 최상위 필드를 포함해야 합니다:
   - `name`: 워크플로우/에이전트의 이름 (필수)
   - `nodes`: 그래프의 노드 목록 (필수)
   - `edges`: 노드 간 연결을 정의하는 목록 (필수)
   - `entrypoint`: 그래프의 시작점 노드 이름 (선택적)

2. 문법 규칙:
   - 들여쓰기는 일관된 공백으로 유지해야 합니다
   - 리스트 항목은 `-` 기호로 시작합니다
   - 키-값 쌍은 `:` 기호로 구분합니다

## 노드 정의
1. 모든 노드는 최소한 `name` 속성을 가져야 합니다
2. 노드는 리스트 형태로 정의되어야 합니다

## 엣지 정의
1. 기본 엣지는 다음 속성을 포함합니다:
   - `from`: 시작 노드 이름
   - `to`: 도착 노드 이름

2. 조건부 엣지는 다음 속성을 포함합니다:
   - `from`: 시작 노드 이름
   - `condition`: 조건 확인을 위한 함수/메서드 이름
   - `paths`: 조건에 따른 가능한 경로들의 리스트

## 특별 노드 이름
1. `__start__`: 그래프의 시작점을 나타내는 예약된 이름 (entrypoint가 지정되지 않은 경우 사용)
2. `__end__`: 그래프의 종료점을 나타내는 예약된 이름

## 예시 패턴
1. 단순 순차 워크플로우: 노드가 선형적으로 연결된 형태
2. 에이전트 기반 워크플로우: entrypoint가 지정되고 조건부 경로가 있는 형태
</rule>

<example1>
# A simple 2-step Retrieval-Augmented Generation workflow
name: RagWorkflow
nodes:
- name: retrieve
- name: generate
edges:
- from: __start__
  to: retrieve
- from: retrieve
  to: generate
- from: generate
  to: __end__
</example>

<example2>
name: AgenticRag
entrypoint: agent
nodes:
  - name: agent
  - name: retrieve
  - name: rewrite
  - name: generate
edges:
  - from: agent
    to: retrieve
  - from: retrieve
    condition: is_relevant
    paths:
      - rewrite
      - generate
  - from: rewrite
    to: agent
  - from: generate
    to: __end__
</example2>

"""