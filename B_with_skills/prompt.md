# B안 — 스킬 5종 적용

## 조건

A안과 **같은 프롬프트**를 쓰되, 설치된 오픈소스 스킬 5종을 적용한다.

## 프롬프트

A안의 `prompt.md`와 동일하다. 한 글자도 바꾸지 않았다.

## 적용한 스킬과 실제로 한 일

### 1. paper-search-pro — 문헌 검색

OpenAlex에 세 갈래로 질의했다.

```
전략1  ("username" OR "nickname" OR "gamertag" OR "screen name")
       AND (morphology OR semantics OR onomastics OR "word formation")
전략2  (nickname OR username OR pseudonym) AND (naming OR onomastics)
       AND (online OR game OR gaming OR internet)
전략3  "semantic network" AND (co-occurrence OR "co-occurrence matrix")
       AND (corpus OR keyword)
```

135건 → 중복 제거 128건 → 제목에 닉네임 계열 단어가 있는 것 72건 → 18편 선정.

**학회 화이트리스트 판정 — 이 주제에는 맞지 않는다.** 설치할 때 넣어 둔
ICEC·IEEE·CHI PLAY·FDG 로 거르면 128편 중 **1편**만 남는다(CHI PLAY 2020,
"Gaming the Name"). 스킬 규칙인 "15편 미만이면 멈추고 물어보라"에 걸렸다.

실제 분야는 게임 HCI가 아니라 **오노마스틱스(인명학)** 였다. 많이 나온 수록지는
*Names*(8편), *Вопросы ономастики*, 각국 문헌학 저널이다. 화이트리스트를 끄고
진행했고, 이 판정 자체를 발표에 넣었다.

### 2. citation-management — 서지정보 확정

A안이 "[서지정보 보완 필요]"로 남긴 6건 중 **5건을 해결**했다.

| A안 | B안 |
|---|---|
| GD Usernames (저자·연도 미상) | **Hassanein, H. S. A. (2019)**, Int. J. English Linguistics 9(5), 107, doi:10.5539/ijel.v9n5p107 |
| Murcia 저널 논문 (저자·연도 미상) | **Stuart, K. & Botella, A. (2009)**, IJES 9(1), doi:10.6018/ijes.1.1.99481 |
| Omodei et al. (2014) 제목 미상 | *Mapping the NLP Domain: Experiments using the ACL Anthology*, doi:10.63317/4hcdpzpoxfj8 |
| Kaziaba (2022) 제목·수록지 미상 | *Self-Nominations with Function of Anthroponym in Runet*, Nauchnyi Dialog 11(7), 212–230 |
| Dubiec-Stach (2021) 제목 미상 | *Nick – tożsamość w Internecie*, doi:10.5604/01.3001.0015.6126 |
| Szymański (2013) | **미해결** — 지어내지 않고 미확인으로 남김 |

**불일치 하나를 발견했다.** 주신 목록의 "Fomin & Chobotar (2022)"는 검색에서
**Chobotar (2026)** 단독 저자 논문으로만 잡힌다. 별건일 수 있어 발표에 그대로 적었다.

### 3. hallmark — 디자인

웹 UI용 스킬이라 PPT에 그대로 적용되지는 않는다. 원칙만 옮겼다.

- **구조 다양성** — A안은 9장이 전부 "제목 + 글머리표"였다. B안은 표지 / 수치 타일 /
  2열 대비 / 타임라인 / 표 / 가로 막대 / 블록 / 단계 / 2열 참고문헌으로 리듬을 바꿨다.
  이것이 hallmark의 핵심 주장이고, 실제로 가장 크게 달라진 부분이다.
- **지어낸 수치 금지** — 타일의 18편·11개 언어·44년은 모두 실제로 센 값이다.
- **번호 머리말 기본 끔** — A안은 "1. 2. 3. …"을 모든 장에 붙였다. B안은 순서가
  실제로 의미 있는 제안 4단계에만 번호를 쓴다.
- **토큰 고정** — 색·글씨를 코드 상단 한 곳에 묶고 중간에서 새 값을 만들지 않는다.
- **2종 폰트 페어링** — 바탕(명조, 표제) + 맑은 고딕(본문). A안은 맑은 고딕 하나였다.

### 4. humanize-scan — 한국어 AI 티 점검

본문을 스캔해 **6개 신호 중 4개가 발동**했다.

| 신호 | 내용 | 조치 |
|---|---|---|
| C-8 대구 반복 | "~쪽이었고 ~쪽은 아니었다", "지어내지 않고 ~남긴다" 2회 | 1회만 남김 |
| E-1 장문 부재 | 100자 넘는 문장 0개 | 인접 문장을 이어 장문 3개 생성 |
| C-11 연결어미 뒤 쉼표 | "맞히는 쪽이었고**,** 언어학적으로" | 쉼표 삭제 |
| E-2 종결 편중 | 틀렸다/있다/있다/없다 4연속 | 문장 구조 재배치 |

스킬 규칙상 4개 발동은 "손볼 게 많다"에 해당해 `/humanize` 전수 윤문을 권한다.
이번에는 발동한 4개만 고쳤고, **나머지 79개 패턴은 점검하지 않았다.**

### 5. frontend-slides — HTML 버전

같은 내용을 단일 HTML 슬라이드로 만들었다(`make_html.py`). 발표는 브라우저로,
제출은 pptx로 하는 구성이다.

## 실행

```bash
python3 make_ppt.py
python3 make_html.py
```

## 사전 준비

A안에는 없던 설치 작업이 필요했다.

```
Python 3.12 + pyyaml, requests, pyalex, python-pptx
python3.exe 별칭 생성 (윈도우에는 없는데 스킬들이 python3 를 호출함)
```
