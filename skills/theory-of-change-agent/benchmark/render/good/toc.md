# 변화이론 (Theory of Change) — 니카라과 ICT 활용 교육역량 강화사업

## 1. 변화이론 도식

**사회문제 → 활동 (Activities) → 산출물 (Outputs) → 성과 (Outcomes) · 지표 → 영향 (Impact)**

```mermaid
%%{init: {"flowchart": {"defaultRenderer": "elk"}, "theme": "base", "themeVariables": {"fontSize": "16px", "lineColor": "#888", "primaryTextColor": "#000", "clusterBkg": "transparent", "clusterBorder": "#90a4ae", "edgeLabelBackground": "#ffffff"}}}%%
flowchart LR
  classDef act fill:#fff3e0,stroke:#ffb74d,color:#000;
  classDef out fill:#e8f5e9,stroke:#81c784,color:#000;
  classDef outcome fill:#e3f2fd,stroke:#64b5f6,color:#000;
  classDef ind fill:#f5f5f5,stroke:#bdbdbd,color:#000;
  classDef impact fill:#ede7f6,stroke:#9575cd,color:#000;
  act_1["연수 프로그램 개발 지원"]:::act --> op_1["개발된 연수프로그램"]:::out
  subgraph oc_g1 [" "]
    direction TB
    oc_1["ICT 활용 교육역량 강화"]:::outcome
    ind_oc_1_1("수료자 중 ICT 활용교육 선도교사 자격증 취득률"):::ind
    oc_1 -.-> ind_oc_1_1
  end
  op_1 --> oc_1
  oc_1 --> imp_1["영향: 자격있는 교사 공급 증대"]:::impact
```

```
사회문제 → [활동 1.1 연수 프로그램 개발] → [산출물 1.1 개발된 연수프로그램] → (성과 1 ICT 활용 교육역량 강화 ↑) → 영향: 자격있는 교사 공급 증대
                                                                              └ 지표: [1-1 수료자 중 ICT 활용교육 선도교사 자격증 취득률]
```
