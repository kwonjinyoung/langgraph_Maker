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
    query = """사용자는 AI로 구성된 여러 에이전트들과 함께 미지의 디지털 세계를 탐험한다. AI는 상황에 따라 조언을 주거나, 사용자를 대신해 상호작용하거나, 다른 AI 에이전트와 협력/갈등을 벌일 수도 있다. 이 세계는 절차적으로 생성되며, 여러 경로가 존재하고, 한 번의 선택이 전체 흐름을 바꾼다.

🧠 핵심 컨셉 요약

요소	설명
노드 수	10개 (분기/루프/탈출 포함)
상태	위치, 에너지, 동료 신뢰도, 진행 단계, 메타 태그
분기	조건부 분기 (if-else), 확률적 분기, 사용자 입력 기반 분기
특별 처리	루프백 (탐색 실패 → 재도전), 병렬 흐름 (동료 분기)
노드 목록 (10개)

노드 ID	이름	역할
start	탐험 시작	기본 상태 초기화, 분기 결정 시작
path_choice	분기점 결정	사용자 입력 기반 경로 분기 (왼쪽/오른쪽/직진)
encounter_guardian	AI 수호자 만남	문제 해결 or 전투 → 상태 변화
puzzle_room	퍼즐 방	퍼즐 성공 여부에 따라 분기 (루프 포함)
hidden_path	숨겨진 경로	특정 조건 만족 시만 진입 가능
ai_companion	동료 AI 합류	병렬 흐름 발생 (동료 상태 분기됨)
betrayal_check	동료 신뢰도 판단	동료가 배신 or 충성 분기
meta_anomaly	메타 이벤트	세계의 구조 변경, 루트 변경
final_gate	마지막 관문	조건 만족 여부 판단 (열쇠 보유 등)
end	탐험 종료	성공/실패 마무리 및 상태 출력
계획
상태 정의: State 모델 (현재 위치, 동료 신뢰도, 아이템 등)

노드 정의: LangGraph @node로 각 노드 정의

조건 분기 처리: if/match와 LangGraph의 edges 사용

순환 흐름 처리: puzzle_room 실패 시 다시 도전 (루프)

병렬 흐름 처리: ai_companion 이후 betrayal_check와 본 경로 분리

meta_anomaly에서 전체 상태에 영향을 주는 분기 설계

마지막 조건 확인 및 종료 처리
    
    """

#     query = """
# 시나리오: AI 외교 시뮬레이션 – "대사관의 그림자"
# 사용자는 AI 대사로서 가상 세계의 외교 위기를 해결해야 한다. 각 노드는 외교적 사건 또는 선택지를 나타내며, 결과는 장기적으로 영향을 미친다. 상대국, 협상 전략, 대내외 여론, 타임라인 등이 상태로 존재하며, 다중 병렬 분기와 비가역 상태가 혼재되어 있다.

# 🎭 핵심 컨셉 요약

# 요소	설명
# 노드 수	10개 (상태 병합, 분기, 시간 제약, 루프 포함)
# 상태	외교 관계도, 내부 여론, 자원, 진행 단계, 신뢰도
# 분기	전략 선택, 상대국 반응, 랜덤 이벤트, 누적 신뢰 기반
# 특별 처리	시간 기반 분기 (데드라인), 병렬 외교 루트, 다중 종료점
# 노드 목록 (10개)

# 노드 ID	이름	역할
# start_briefing	사전 브리핑	초기 상태 로딩, 목표 설정
# initial_contact	첫 접촉	전략 선택: 공격적/수동적/정보 수집
# gather_intel	정보 수집	선택적, 상태 업데이트 (루프 가능)
# public_opinion	여론 체크	외교 전략에 따라 반응 다름
# event_interrupt	이벤트 발생	비정규 이벤트 삽입 (갈등 유발 가능)
# trade_negotiation	무역 협상	신뢰도 기반 분기 (병렬 루트 생성)
# internal_pressure	내부 압력	타임아웃 루트, 상태 리셋 유도
# alliance_offer	동맹 제안	다른 AI 대사와 협상 (결정적 분기)
# emergency_summit	긴급 회담	모든 루트 병합, 최종 판단
# resolution	해결 or 붕괴	성공/실패 마무리, 상세 상태 보고
# 🧠 시나리오적 특징
# 루프: gather_intel → 정보 부족 시 재수행

# 병렬 분기: trade_negotiation / internal_pressure → 독립적 상태 영향

# 조건 루트: alliance_offer → 선택에 따라 'emergency_summit' 흐름 자체 변경

# 이벤트 삽입: event_interrupt는 모든 흐름 중간에 삽입 가능 (LangGraph의 동적 트리거 개념으로 연습)

# 시간 기반 조건: 특정 노드는 state["time"]이 특정 값 이상일 때만 진입 허용

# 병합: emergency_summit은 여러 루트를 병합해 하나의 상태 판단


# """

    response = generate_structured_response(query)
    if response:
        print("\n===== 생성 결과 =====")
        #write file. think = thinking.md, yml = response.yml
        with open("output_yml/thinking.md", "w") as f:
            f.write(response.thinking)
        with open("output_yml/response.yml", "w") as f:
            f.write(response.yml)
            
        # 시스템 명령어로 'uv rn langgraph-gen output_yml/response.yml' 실행
        os.system('uv run langgraph-gen output_yml/response.yml')
    else:
        print("검색 결과를 가져오지 못했습니다.")
