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
#     query = """사용자는 AI로 구성된 여러 에이전트들과 함께 미지의 디지털 세계를 탐험한다. AI는 상황에 따라 조언을 주거나, 사용자를 대신해 상호작용하거나, 다른 AI 에이전트와 협력/갈등을 벌일 수도 있다. 이 세계는 절차적으로 생성되며, 여러 경로가 존재하고, 한 번의 선택이 전체 흐름을 바꾼다.

# 🧠 핵심 컨셉 요약

# 요소	설명
# 노드 수	10개 (분기/루프/탈출 포함)
# 상태	위치, 에너지, 동료 신뢰도, 진행 단계, 메타 태그
# 분기	조건부 분기 (if-else), 확률적 분기, 사용자 입력 기반 분기
# 특별 처리	루프백 (탐색 실패 → 재도전), 병렬 흐름 (동료 분기)
# 노드 목록 (10개)

# 노드 ID	이름	역할
# start	탐험 시작	기본 상태 초기화, 분기 결정 시작
# path_choice	분기점 결정	사용자 입력 기반 경로 분기 (왼쪽/오른쪽/직진)
# encounter_guardian	AI 수호자 만남	문제 해결 or 전투 → 상태 변화
# puzzle_room	퍼즐 방	퍼즐 성공 여부에 따라 분기 (루프 포함)
# hidden_path	숨겨진 경로	특정 조건 만족 시만 진입 가능
# ai_companion	동료 AI 합류	병렬 흐름 발생 (동료 상태 분기됨)
# betrayal_check	동료 신뢰도 판단	동료가 배신 or 충성 분기
# meta_anomaly	메타 이벤트	세계의 구조 변경, 루트 변경
# final_gate	마지막 관문	조건 만족 여부 판단 (열쇠 보유 등)
# end	탐험 종료	성공/실패 마무리 및 상태 출력
# 계획
# 상태 정의: State 모델 (현재 위치, 동료 신뢰도, 아이템 등)

# 노드 정의: LangGraph @node로 각 노드 정의

# 조건 분기 처리: if/match와 LangGraph의 edges 사용

# 순환 흐름 처리: puzzle_room 실패 시 다시 도전 (루프)

# 병렬 흐름 처리: ai_companion 이후 betrayal_check와 본 경로 분리

# meta_anomaly에서 전체 상태에 영향을 주는 분기 설계

# 마지막 조건 확인 및 종료 처리
    
#     """

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

    query = """
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

Warp Gate (워프게이트)
Gateway를 업그레이드하여 변환 가능한 형태. Cybernetics Core 이후 연구가 가능하며, 유닛을 즉시 원하는 위치에 소환할 수 있는 능력을 가진다.

Robotics Facility (로보틱스 시설)
기술 유닛 생산 건물로, 건설 즉시 Observer, Warp Prism, Immortal을 생산할 수 있다.
Robotics Bay가 건설되면 Colossus와 Disruptor 생산이 가능해진다.

Stargate (스타게이트)
공중 유닛을 생산하는 건물로, 기본적으로 Phoenix, Void Ray, Oracle을 생산할 수 있다.
Fleet Beacon이 건설되면 Carrier, Tempest, Mothership 등 최종 유닛이 해금된다.

3. 기술 및 지원 건물
Cybernetics Core (사이버네틱스 코어)
Gateway 유닛 업그레이드와 고급 유닛 해금에 필수.
이 건물이 있어야 Gateway에서 Stalker, Sentry, Adept 등 다양한 유닛을 생산 가능.

Twilight Council (황혼회관)
고급 지상 유닛 업그레이드를 위한 전제조건.
이 건물 이후 Dark Shrine 또는 Templar Archives를 건설할 수 있으며,
각각 Dark Templar, High Templar 생성의 필수 조건이 된다.

Templar Archives (템플러 기록관)
Twilight Council 이후 지을 수 있으며, High Templar 유닛을 생산할 수 있다.
High Templar는 Archon으로 융합될 수 있다.

Dark Shrine (암흑 성소)
Twilight Council이 선행되어야 하며, Dark Templar 유닛 생산의 필수 건물이다.

Robotics Bay (로보틱스 지원소)
Robotics Facility와 연계되며, Colossus 및 Disruptor 생산 조건이 된다.

Fleet Beacon (함대 신호소)
Stargate 이후 건설할 수 있으며, Carrier, Tempest, Mothership 등의 생산과 업그레이드를 해금한다.

4. 최종 유닛 및 특수 활성 조건 요약

유닛	요구 조건
Zealot	Gateway
Stalker	Gateway + Cybernetics Core
Sentry	Gateway + Cybernetics Core
Adept	Gateway + Cybernetics Core
High Templar	Templar Archives
Dark Templar	Dark Shrine
Archon	High Templar 2기 또는 Dark Templar 2기 융합
Immortal	Robotics Facility
Colossus	Robotics Facility + Robotics Bay
Disruptor	Robotics Facility + Robotics Bay
Phoenix	Stargate
Void Ray	Stargate
Oracle	Stargate
Carrier	Stargate + Fleet Beacon
Tempest	Stargate + Fleet Beacon
Mothership	Fleet Beacon + Nexus (소환은 단 1기만 가능)
    """

    query = """
    hello print and how are you? and end
    """

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
