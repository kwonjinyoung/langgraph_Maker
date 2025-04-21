# LangGraph Maker

LangGraph를 이용한 그래프 시각화 도구입니다.

## 설치 방법

필요한 라이브러리를 설치하기 위해 다음 명령어를 실행하세요:

```bash
# Graphviz 개발 라이브러리 설치 (Ubuntu/Debian)
sudo apt-get install -y graphviz graphviz-dev

# 파이썬 패키지 설치
uv add pygraphviz
```

## 사용 방법

### 그래프 생성

다음 명령어로 그래프를 생성할 수 있습니다:

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

### 그래프 시각화

생성된 그래프를 시각화하려면 다음 명령어를 실행하세요:

```bash
python output_yml/makeImage.py
```

이 스크립트는 다음과 같은 기능을 제공합니다:
- ASCII 형식으로 그래프 출력
- Mermaid 코드 형식으로 그래프 출력
- PNG 이미지로 그래프 저장 (output_yml/digital_world_graph.png)

## 주의사항

pygraphviz 설치 시 graphviz 개발 라이브러리가 필요합니다. 설치 오류가 발생할 경우 먼저 시스템에 필요한 개발 라이브러리가 설치되어 있는지 확인하세요.

## 오류 해결

오류 메시지 예시:
```
fatal error: graphviz/cgraph.h: No such file or directory
```

위와 같은 오류가 발생하면 다음 명령어로 graphviz 개발 라이브러리를 설치하세요:
```bash
sudo apt-get install -y graphviz graphviz-dev
```
