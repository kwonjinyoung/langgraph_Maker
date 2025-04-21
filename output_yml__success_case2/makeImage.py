import graphviz
from response_impl import compiled_agent
import os
from IPython.display import Image, display


def save_langgraph_diagram(graph, filename="graph.png", display_ascii=False, display_mermaid=False):
    """
    LangGraph 그래프 객체를 이미지로 저장하고, 선택적으로 ASCII 및 Mermaid 코드 형식으로 출력합니다.

    Parameters:
    - graph: LangGraph의 StateGraph 또는 CompiledGraph 객체
    - filename: 저장할 이미지 파일 이름 (기본값: 'graph.png')
    - display_ascii: ASCII 형식으로 그래프를 출력할지 여부 (기본값: False)
    - display_mermaid: Mermaid 코드 형식으로 그래프를 출력할지 여부 (기본값: False)
    """
    # 그래프 객체 가져오기
    graph_obj = graph.get_graph()
    
    # ASCII 형식으로 그래프 출력
    if display_ascii:
        print("ASCII 형식의 그래프:")
        graph_obj.print_ascii()  # 또는 print(graph_obj.draw_ascii())를 사용할 수 있습니다

    # Mermaid 코드 형식으로 그래프 출력
    if display_mermaid:
        mermaid_code = graph_obj.draw_mermaid()
        print("Mermaid 코드 형식의 그래프:")
        print(mermaid_code)
    
    try:
        # PNG 형식으로 그래프 렌더링 및 저장
        import tempfile
        from langchain_core.runnables.graph import CurveStyle, MermaidDrawMethod
        
        # Graphviz를 사용하여 PNG 생성 시도
        try:
            # print("graphviz를 사용하여 PNG 생성 시도중...")
            png_bytes = graph_obj.draw_png()
            with open(filename, "wb") as f:
                f.write(png_bytes)
            print(f"그래프 이미지가 '{filename}'로 저장되었습니다. (GraphViz 사용)")
        except (ImportError, AttributeError) as e:
            print(f"GraphViz를 사용한 이미지 생성 실패: {e}")
            print("Mermaid를 사용하여 이미지 생성을 시도합니다.")
            
            try:
                # 대체 방법으로 Mermaid 시도 (simplify_mermaid 추가 옵션 시도)
                png_bytes = graph_obj.draw_mermaid_png(
                    curve_style=CurveStyle.LINEAR, 
                    draw_method=MermaidDrawMethod.API,
                    max_retries=5,
                    retry_delay=2.0
                )
                with open(filename, "wb") as f:
                    f.write(png_bytes)
                print(f"그래프 이미지가 '{filename}'로 저장되었습니다. (Mermaid API 사용)")
            except Exception as e2:
                print(f"Mermaid API를 사용한 이미지 생성 실패: {e2}")
                print("직접 Mermaid 코드를 저장합니다.")
                
                # 마지막 방법: Mermaid 코드를 직접 저장
                mermaid_code = graph_obj.draw_mermaid()
                mermaid_file = os.path.splitext(filename)[0] + ".mmd"
                with open(mermaid_file, "w", encoding="utf-8") as f:
                    f.write(mermaid_code)
                print(f"Mermaid 코드가 '{mermaid_file}'로 저장되었습니다.")
                print("https://mermaid.live 에서 이 파일을 열어 시각화할 수 있습니다.")
                
    except Exception as e:
        print(f"그래프 이미지 생성 중 오류가 발생했습니다: {e}")
        print("ASCII 또는 Mermaid 출력을 활용하세요.")


# compiled_agent.invoke() 호출 없이 그래프만 그립니다
save_langgraph_diagram(compiled_agent, filename="output_yml/digital_world_graph.png", display_ascii=True, display_mermaid=True)

print("그래프 시각화가 완료되었습니다.")
