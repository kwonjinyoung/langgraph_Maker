import os
from openai import OpenAI
from pydantic import BaseModel, Field
from typing import List, Optional
from prompt import systemPrompt, yml_prompt

# OpenAI API 키 설정
api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY 환경변수가 설정되지 않았습니다.")

# OpenAI 클라이언트 초기화
client = OpenAI(api_key=api_key)


# Pydantic 모델 정의
class MakeYml(BaseModel):
    """웹 검색 결과를 나타내는 모델"""
    thinking: str = Field(description="CoT 기법을 사용하여 사용자의 요청을 분석하고 langgraph 작성을 위한 yml 작성에 대해 계획을 세워야 합니다.")
    yml: str = Field(description=yml_prompt)

def generate_structured_response(prompt: str, model: str = "gpt-4o"):
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
    프로토스: 건물 및 유닛 활성 조건 요약
    1. 기초 건물 계층
    Nexus (넥서스)
    프로토스의 본진 건물로, 자원 수집과 기본 유닛(Probe)의 생산이 가능하다. 게임 시작 시 제공되며, 모든 건물의 건설은 넥서스에서 생산되는 Probe에 의해 수행된다.

    Pylon (파일런)
    프로토스의 에너지 원으로, 건물과 유닛은 Pylon의 전력장 안에 있어야 활성화된다. 어떤 건물이든 건설하려면 해당 위치가 파일런의 범위 안이어야 한다.

    Assimilator (어시밀레이터)
    가스를 채취하기 위한 구조물로, 베스핀 가이저 위에 건설되며, 넥서스를 통해 생성된 Probe가 채광 작업을 수행한다.

    2. 생산 건물과 유닛 조건
    Gateway (게이트웨이)
    기본적인 전투 유닛 생산 건물로, Zealot 생산이 즉시 가능하다.
    Cybernetics Core가 지어진 후에는 Stalker, Sentry, Adept 생산이 가능하며,
    Twilight Council과 Robotics Facility 등의 기술 건물과 연계해 Archon 같은 상위 유닛 조합도 가능하다.
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
