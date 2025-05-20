import os
from openai import AzureOpenAI
from pydantic import BaseModel, Field
from typing import List, Optional
from prompt import systemPrompt, yml_prompt

# Azure OpenAI API 환경 변수 설정
api_key = os.environ.get("AZURE_OPENAI_API_KEY")
api_endpoint = os.environ.get("AZURE_OPENAI_ENDPOINT")
api_version = os.environ.get("AZURE_OPENAI_API_VERSION", "2024-07-01-preview")
deployment_name = os.environ.get("AZURE_OPENAI_DEPLOYMENT", "gpt-4o")

# 환경 변수 유효성 검사
if not api_key:
    raise ValueError("AZURE_OPENAI_API_KEY 환경변수가 설정되지 않았습니다.")
if not api_endpoint:
    raise ValueError("AZURE_OPENAI_ENDPOINT 환경변수가 설정되지 않았습니다.")

# Azure OpenAI 클라이언트 초기화
client = AzureOpenAI(
    api_key=api_key,
    api_version=api_version,
    azure_endpoint=api_endpoint
)

# Pydantic 모델 정의
class MakeYml(BaseModel):
    """웹 검색 결과를 나타내는 모델"""
    thinking: str = Field(description="CoT 기법을 사용하여 사용자의 요청을 분석하고 langgraph 아키텍처 설계를 위한 thinking을 작성해야 합니다.")
    yml: str = Field(description=yml_prompt)

def generate_structured_response(prompt: str, model: str = deployment_name):
    try:
        # Beta API를 사용하여 구조화된 출력 생성
        response = client.beta.chat.completions.parse(
            model=model,
            messages=[
                {"role": "system", "content": systemPrompt},
                {"role": "user", "content": prompt}
            ],
            response_format=MakeYml,
            temperature=0.7,
            max_tokens=1500
        )
        return response.choices[0].message.parsed
    except Exception as e:
        print(f"오류가 발생했습니다: {str(e)}")
        return None

# 사용 예제
if __name__ == "__main__":
    # 기본 예제 시나리오 
    default_query = """
    사용자 질문에 응답하는 정보 검색 및 답변 생성 시스템을 설계해 주세요.

    시스템 요구사항:
    1. 사용자는 특정 '권한' 획득 방법과 같은 정보를 찾고 있습니다.
    2. 먼저 기존 vectorstore에서 관련 정보를 검색합니다.
    3. 검색된 정보가 충분하면 Azure OpenAI GPT를 사용하여 RAG 방식으로 답변을 생성합니다.
    4. 검색된 정보가 불충분하면 Confluence에서 정보를 검색합니다.
       - 검색을 위한 키워드를 몇 개 추출합니다.
       - Confluence에서 검색을 수행합니다.
       - 상위 2개 페이지를 읽고 내용을 분석합니다.
    5. Confluence 검색 결과가 충분하면 해당 정보로 답변을 생성합니다.
    6. 여전히 정보가 부족하면 다른 키워드로 추가 검색을 수행합니다.
    7. 총 검색 시도는 최대 3회로 제한합니다.
    
    각 단계마다 명확한 판단 기준과 데이터 흐름을 포함한 LangGraph 멀티 에이전트 시스템을 설계해 주세요.
    """

    # 사용자 입력 여부 확인
    use_custom_input = input("자신의 시나리오를 입력하시겠습니까? (y/n): ").strip().lower()
    
    if use_custom_input == 'y':
        print("\n시나리오를 입력하세요 (입력 완료 후 빈 줄에서 Ctrl+D 또는 Ctrl+Z(Windows)를 입력하세요):")
        user_input_lines = []
        
        try:
            while True:
                line = input()
                user_input_lines.append(line)
        except (EOFError, KeyboardInterrupt):
            pass
        
        query = "\n".join(user_input_lines)
        if not query.strip():
            print("입력이 비어있어 기본 예제를 사용합니다.")
            query = default_query
    else:
        print("기본 예제를 사용합니다.")
        query = default_query

    # 응답 생성 및 파일 처리
    response = generate_structured_response(query)
    if response:
        print("\n===== 생성 결과 =====")
        # 디렉토리 확인 및 생성
        if not os.path.exists("output_yml"):
            os.makedirs("output_yml")
            
        # 파일 저장
        with open("output_yml/thinking.md", "w") as f:
            f.write(response.thinking)
        with open("output_yml/response.yml", "w") as f:
            f.write(response.yml)
            
        # 시스템 명령어로 'uv run langgraph-gen output_yml/response.yml' 실행
        print("LangGraph 코드 생성 중...")
        os.system('uv run langgraph-gen output_yml/response.yml')
        
        print("\n그래프 이미지를 생성하려면 다음 명령어를 실행하세요:")
        print("python output_yml/makeImage.py")
    else:
        print("결과를 생성하지 못했습니다.")
