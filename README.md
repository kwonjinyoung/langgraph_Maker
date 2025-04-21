# LangGraph Maker

LangGraph를 이용한 그래프 시각화 도구입니다.

## 소개

LangGraph Maker는 자연어로 설명된 시나리오나 상황을 LangGraph 기반의 워크플로우로 변환하는 도구입니다. 이 도구는 다음과 같은 기능을 제공합니다:

- 자연어 설명을 YAML 형식의 그래프 정의로 변환
- Chain-of-Thought 기법을 활용한 사고 과정 시각화
- LangGraph 코드 자동 생성
- 생성된 그래프의 시각화 (ASCII, Mermaid, PNG)

## 설치 방법

### 필수 요구사항

- Python 3.10 이상
- OpenAI API 키 (환경 변수로 설정)
- Graphviz (시각화에 필요)

### 환경 설정

```bash
# OpenAI API 키 설정
export OPENAI_API_KEY=your_api_key_here

# Graphviz 개발 라이브러리 설치 (Ubuntu/Debian)
sudo apt-get install -y graphviz graphviz-dev

# 파이썬 패키지 설치
uv add grandalf graphviz langgraph langgraph-gen nest-asyncio openai pydot pygraphviz pyppeteer
```

## 사용 방법

### 1. 그래프 생성

자연어 설명을 LangGraph YAML로 변환하고 Python 코드를 생성합니다:

```bash
uv run python main.py
```

실행 결과:
```
===== 생성 결과 =====
✅ Successfully generated files:
📄 Stub file:           output_yml/response.py
🔧 Implementation file:  output_yml/response_impl.py
```

### 2. 그래프 시각화

생성된 그래프를 시각화하려면 다음 명령어를 실행하세요:

```bash
python output_yml/makeImage.py
```

이 스크립트는 다음과 같은 기능을 제공합니다:
- ASCII 형식으로 그래프 출력
- Mermaid 코드 형식으로 그래프 출력
- PNG 이미지로 그래프 저장 (`output_yml/digital_world_graph.png`)

### 3. 커스텀 시나리오 사용

`main.py` 파일에서 `query` 변수를 수정하여 원하는 시나리오를 제공할 수 있습니다. 이 시나리오는 LangGraph 형태로 변환됩니다.

## 주요 파일 구조

```
langgraph-maker/
├── main.py              # 메인 실행 파일
├── prompt.py            # 프롬프트 및 시스템 메시지 정의
├── output_yml/
│   ├── response.yml     # 생성된 YAML 정의
│   ├── response.py      # 생성된 스텁 파일
│   ├── response_impl.py # 생성된 구현 파일
│   ├── thinking.md      # CoT 추론 결과
│   ├── makeImage.py     # 그래프 시각화 도구
│   └── digital_world_graph.png # 생성된 그래프 이미지
└── pyproject.toml       # 프로젝트 의존성 정의
```

## 주의사항

- pygraphviz 설치 시 graphviz 개발 라이브러리가 필요합니다. 설치 오류가 발생할 경우 먼저 시스템에 필요한 개발 라이브러리가 설치되어 있는지 확인하세요.
- OpenAI API 키는 환경변수로 제공해야 합니다. API 키가 없으면 프로그램이 실행되지 않습니다.
- 복잡한 그래프를 생성할 경우 OpenAI API 호출에 더 많은 토큰이 사용될 수 있습니다.

## 오류 해결

오류 메시지 예시:
```
fatal error: graphviz/cgraph.h: No such file or directory
```

위와 같은 오류가 발생하면 다음 명령어로 graphviz 개발 라이브러리를 설치하세요:
```bash
sudo apt-get install -y graphviz graphviz-dev
```

## 라이센스

이 프로젝트는 MIT 라이센스 하에 배포됩니다.
