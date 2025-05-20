# LangGraph Maker

LangGraph 설계 도구를 Azure OpenAI와 연동하여 사용할 수 있는 프로젝트입니다.

## 개요

이 프로젝트는 사용자의 요구사항을 분석하여 LangGraph 멀티 에이전트 시스템을 설계하고, 설계된 아키텍처를 YAML 형식으로 문서화하여 실제 코드를 생성합니다.

## 설치 방법

```bash
# 저장소 클론
git clone [repository-url]
cd langgraph_Maker

# 가상환경 생성 및 활성화
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 필요한 패키지 설치
pip install -r requirements.txt
```

## 환경 변수 설정

`.env` 파일을 생성하고 다음과 같이 환경 변수를 설정합니다:

```
# Azure OpenAI API 설정
AZURE_OPENAI_API_KEY=your_api_key_here
AZURE_OPENAI_ENDPOINT=https://your-resource-name.openai.azure.com
AZURE_OPENAI_API_VERSION=2024-07-01-preview
AZURE_OPENAI_DEPLOYMENT=gpt-4o
```

## 사용 방법

1. Azure OpenAI 설정: Azure OpenAI 서비스에서 API 키와 엔드포인트를 발급받아 환경 변수에 설정합니다.
2. 실행: `python main.py` 명령어로 실행합니다.
3. 프롬프트 입력: 구현하려는 LangGraph 시스템의 요구사항을 입력합니다.
4. 결과 확인: `output_yml` 디렉토리에 생성된 결과물을 확인합니다.
   - `thinking.md`: 요구사항 분석 및 설계 과정
   - `response.yml`: LangGraph YAML 설계서
   - 생성된 Python 구현 파일들

## 예시

```bash
python main.py
# 기본 예제를 사용하거나 자신의 시나리오 입력
```

## 구조 설명

- `main.py`: 메인 실행 파일
- `prompt.py`: 시스템 프롬프트 및 YAML 형식 정의
- `output_yml/`: 생성된 결과물 디렉토리
  - `thinking.md`: 요구사항 분석 및 설계 과정
  - `response.yml`: LangGraph YAML 설계서
  - `response.py`: LangGraph 골격 코드
  - `response_impl.py`: 구현해야 할 코드 템플릿
  - `makeImage.py`: 그래프 이미지 생성 스크립트

## 요구사항

- Python 3.10 이상
- Azure OpenAI API 접근 권한
- `langchain`, `langgraph` 및 기타 필요 라이브러리 (requirements.txt 참조)

## 참고 사항

- 이 프로젝트를 사용하려면 Azure OpenAI에 대한 액세스 권한이 필요합니다.
- 생성된 코드는 기본 골격만 제공하며, 실제 구현을 위해서는 추가 개발이 필요합니다.
