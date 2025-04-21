주어진 정보를 바탕으로, 프로토스의 건물과 유닛 활성 조건을 LangGraph의 그래프 모델로 변환하기 위해서는 각 건물과 유닛을 노드로 정의하고, 그들 간의 활성화 조건과 종속 관계를 엣지로 연결해야 합니다.

먼저 상태를 정의하고, 각 노드가 상태를 어떻게 변화시키는지 고려합니다. 예를 들어, `Nexus`는 기본적으로 게임 시작 시 제공되므로 `START`에서 바로 연결될 수 있습니다. `Pylon`은 모든 건물의 전제 조건이므로, `Nexus`에서 `Pylon`으로의 엣지를 추가합니다.

유닛 생산 건물과 관련해서는, `Gateway`는 `Zealot`을 즉시 생산할 수 있는 조건을 가집니다. 따라서 `Gateway` 노드는 `Zealot` 생산을 위한 엣지를 가집니다. `Cybernetics Core`가 지어지면 `Stalker`, `Sentry`, `Adept`를 생산할 수 있게 되므로, `Gateway`에서 `Cybernetics Core`로, 그리고 `Cybernetics Core`에서 해당 유닛들로의 엣지를 추가합니다.

`Robotics Facility`와 `Stargate`는 각각 `Observer`, `Warp Prism`, `Immortal` 및 `Phoenix`, `Void Ray`, `Oracle` 생산을 위한 조건을 제공합니다. `Robotics Bay`와 `Fleet Beacon`은 상위 유닛인 `Colossus`, `Disruptor`, `Carrier`, `Tempest`, `Mothership`의 생산 조건을 제공하므로 이들 간의 관계를 엣지로 연결해야 합니다.

이제 이 조건들을 바탕으로 YML 파일을 작성합니다.