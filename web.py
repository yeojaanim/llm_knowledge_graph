import streamlit as st
import json
import requests
import os
from streamlit_agraph import agraph, Node, Edge, Config, TripleStore
from chat import auto_knowledge_graph

st.title("😊 Knowledge Graph Generater")

st.markdown("### 문장의 구조도 설명")

user_text = st.text_area(label = "분석할 문장을 입력하세요. (10~5000자)",
                         value= """지도 학습이란 레이블(Label) 이라는 정답과 함께 학습하는 것을 말한다. 자
연어 처리는 대부분 지도 학습에 속한다. 레이블이라는 말 이외에도 y, 실제값 등으로 부르
기도 한다. 간단히 말해 선생님이 문제를 내고 그 다음 바로 정답까지 같이 알려주는 방식의 학습 방법
이다. 여러 문제와 답을 같이 학습함으로 미지의 문제에 대한 올바른 답을 예측하고자 하는 방법이
다. 지도학습을 위한 데이터로는 문제와 함께 그 정답까지 같이 알고 잇는 데이터가 선택된
다.""", height=200)

res = None
with st.form("summarize_form", clear_on_submit=True):
    submitted = st.form_submit_button("구조도 생성하기")
    if submitted:
        with st.spinner("지식 그래프 생성 중... 잠시만 기다려주세요...⌛"):
            result = auto_knowledge_graph(user_text)
            res = result

if res:
    nodes = []
    edges = []
    dupliacation = []
    for item in result:
        if item[0] in dupliacation:
            pass
        else:
            nodes.append(Node(id=item[0], label=item[0], size=10))
            dupliacation.append(item[0])

        if item[1] in dupliacation:
            pass
        else:
            nodes.append(Node(id=item[1], label=item[1], size=10))
            dupliacation.append(item[1])

        if item[2] in dupliacation:
            pass
        else:
            nodes.append(Node(id=item[2], label=item[2], size=10))
            dupliacation.append(item[2])

        edges.append(Edge(source=item[0], target=item[1], type="curve_smooth"))
        edges.append(Edge(source=item[1], target=item[2], type="curve_smooth"))

    config = Config(width=750,
                    height=950,
                    directed=True,
                    physics=True,
                    nodeHighlightBehavior=True,
                    highlightColor="#F7A7A6",
                    collapsible=True,
                    hierarchical=False,
                    node={"labelProperty":"label"}
                    )
    
    return_value = agraph(nodes=nodes, edges=edges, config=config)