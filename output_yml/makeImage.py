import graphviz
from response_impl import compiled_agent
from langchain_core.runnables.graph import MermaidDrawMethod

# compiled_agent를 이미지로 저장
# 그래프 시각화
graph = compiled_agent.get_graph()
# 이미지 파일로 저장 (PNG 형식) - Pyppeteer 사용
graph.draw_mermaid_png(
    output_file_path="output_yml/digital_world_graph.png",
    draw_method=MermaidDrawMethod.PYPPETEER,
    max_retries=5,
    retry_delay=2.0
)
print("그래프 이미지가 'output_yml/digital_world_graph.png'에 저장되었습니다.")
