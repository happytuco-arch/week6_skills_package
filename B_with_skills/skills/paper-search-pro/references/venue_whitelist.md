# 학회 화이트리스트 (ICEC · IEEE · CHI PLAY · FDG)

이 설치본의 기본 검색 범위입니다. 게임·엔터테인먼트 컴퓨팅 선행연구를 찾기 위한 것이며,
사용자가 범위를 바꾸라고 하면 그 지시가 우선합니다.

## 네 곳이 무엇인지

| 약칭 | 정식 명칭 | 발행처 | 성격 |
|---|---|---|---|
| **ICEC** | IFIP International Conference on Entertainment Computing | Springer LNCS | 엔터테인먼트 컴퓨팅 전반. 유럽·아시아 중심 |
| **IEEE** | IEEE 산하 학회·저널 (아래 참고) | IEEE | 범위가 넓어 따로 좁혀야 함 |
| **CHI PLAY** | ACM SIGCHI Annual Symposium on Computer-Human Interaction in Play | ACM | 게임 HCI·플레이어 경험의 중심 학회 |
| **FDG** | ACM/IEEE International Conference on the Foundations of Digital Games | ACM | 게임 디자인·AI·연구방법론 |

**IEEE는 그대로 쓰면 안 됩니다.** IEEE 전체는 수십만 편이라 화이트리스트 역할을 못 합니다.
게임·HCI 맥락에서는 아래로 좁히세요.

- IEEE Transactions on Games (ToG) — 2018년 이전 명칭: *IEEE Transactions on Computational Intelligence and AI in Games* (TCIAIG)
- IEEE Conference on Games (CoG) — 2019년 이전 명칭: *IEEE Conference on Computational Intelligence and Games* (CIG)
- IEEE VR / ISMAR — VR·AR 게임 주제일 때만

사용자가 "IEEE"라고만 말했다면 위 세 묶음으로 해석하고, **한 줄로 그렇게 했다고 알리세요.**

## 이름 맞추기

OpenAlex의 `venue` · `host_venue` · `display_name`에 들어오는 표기가 제각각입니다.
아래 변형을 모두 같은 학회로 봅니다. 대소문자는 무시하고, 부분 일치로 판정합니다.

```
ICEC       : "Entertainment Computing", "ICEC", "IFIP ... Entertainment Computing"
             ※ 저널 "Entertainment Computing"(Elsevier)과 혼동 주의 — 아래 참고
CHI PLAY   : "CHI PLAY", "Computer-Human Interaction in Play", "CHI Play"
FDG        : "Foundations of Digital Games", "FDG"
IEEE ToG   : "Transactions on Games", "Computational Intelligence and AI in Games", "TCIAIG"
IEEE CoG   : "Conference on Games", "Computational Intelligence and Games", "CIG"
```

**ICEC는 함정이 하나 있습니다.** Elsevier의 저널 *Entertainment Computing*과 학회
*ICEC*는 이름이 거의 같지만 다른 것입니다. 둘 다 유효한 선행연구이므로 **버리지 말고,
표에서 `ICEC(학회)` / `Entertainment Computing(저널)`로 구분해 표기**하세요.

## 거르는 순서

STEP 5에서 합친 직후, 분류(STEP 6) 전에 거릅니다. 버릴 논문을 분류하는 것이 가장 비쌉니다.

1. `kg.json`은 전체 후보로 그대로 둡니다 (되돌아갈 수 있어야 합니다).
2. 각 항목의 venue 필드를 위 변형 목록과 맞춰 `kg_venue.json`으로 추립니다.
3. **숫자를 보고합니다** — "전체 180편 중 23편이 네 학회 소속입니다."

## 범위를 넓혀야 할 때

**남은 논문이 15편 미만이면 멈추고 물어보세요.** 선행연구 정리는 20~40편은 있어야
연구 흐름과 공백이 보입니다. 억지로 적은 수로 표를 만들면 "이 분야에 연구가 없다"는
잘못된 결론이 나옵니다.

넓힐 때는 이 순서를 권합니다 — 가까운 것부터입니다.

1. **DiGRA** (Digital Games Research Association) — 게임학 쪽 핵심인데 네 곳에 안 들어감
2. **CHI 본회의 · CSCW** — 게임 논문이 상당수 실림
3. **저널** — *Entertainment Computing*(Elsevier), *Games and Culture*, *Simulation & Gaming*
4. **arXiv cs.HC** — 최신 연구, 단 동료심사 전임을 표에 명시

넓힌 뒤에는 **어디까지 넓혔는지 보고서에 적으세요.** 범위가 곧 방법론이라, 적지 않으면
나중에 재현할 수 없습니다.

## 화이트리스트를 끄는 경우

사용자가 "전체에서 찾아줘", "학회 상관없이" 같은 말을 하면 거르지 않습니다.
그때도 **최종 표에는 학회명 칸을 남겨** 두세요 — 어느 논문이 네 학회 것인지는
여전히 유용한 정보입니다.
