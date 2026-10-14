# A안 — 스킬 미사용 조건

## 조건

설치된 오픈소스 스킬을 하나도 쓰지 않는다. 검색 파이프라인(`paper-search-pro`),
인용 관리(`citation-management`), 디자인 감수(`hallmark`), 슬라이드 생성
(`frontend-slides`), 한글 윤문(`humanize-korean`) 모두 호출하지 않는다.

사람이 평소에 하듯 **프롬프트 한 번 + 생성 코드 한 벌**로 결과물을 만든다.

## 실제로 입력한 프롬프트

```
게임 닉네임 연구로 선행연구 조사 발표 PPT를 만들어줘.

아래가 지도교수님이 주신 선행연구 목록이야.

1. Semantic network 방법론 (키워드 간 상관관계 분석)
- Corpus Linguistics, Network Analysis and Co-occurrence Matrices
  (International Journal of English Studies, Univ. of Murcia)
  : 코퍼스에서 빈도·키워드·연어 분석을 거쳐 동시출현 행렬과 semantic network를 생성하는 절차
- Omodei, Cointet & Poibeau (2014), LREC'14, pp. 2972-2978
  : 언어 패턴과 통계를 혼합한 키워드 추출 및 동시출현 기반 네트워크 구축

2. 닉네임 사용자명의 형태론/통사/의미론 분석
- GD Usernames and Euphemism: A Morphosemantic Analysis
  : 게임 사이트 사용자명의 단어 형성, 철자 변형, 차용, 의미 혁신 분석
- Szymanski (2013): 7,456개 닉네임의 형태론 및 문자 선택 동기
- Dubiec-Stach (2021): 독일어·폴란드어 닉네임의 의미·형태·통사·문자 양식 분류
- Kaziaba (2022): 5,000개 사례의 다층위 분석 (온라인 게임 포함)
- Fomin & Chobotar (2022): 게임 내 닉네임의 작명 동기와 생성 기제

연구 방향은 이거야. 선행연구를 기반으로 현재 연구를 진행시키고, LLM 기반 시스템을
만들어 다국어로 발전시킨 뒤, 작명 동기와 행위를 볼 수 있으면 좋겠어.

수업 발표용이고 10장 안쪽이면 좋겠어. pptx 파일로 줘.
```

## 생성 방법

`make_ppt.py` — python-pptx로 직접 작성. 템플릿·디자인 시스템 없이 기본 레이아웃을 쓴다.

```bash
python3 make_ppt.py
```

## 결과물

`선행연구조사_게임닉네임.pptx` (9장)

## 기록 — 이 조건에서 걸린 문제

B안과 비교할 때 쓰기 위해 작업 중 실제로 발생한 문제를 남긴다.

1. **서지정보가 불완전한 채로 끝났다.** 주신 목록 중 1-1(Murcia 저널 논문)과 2-1(GD
   Usernames)은 저자명과 연도가 없다. 검색 도구를 쓰지 않아 채우지 못했고, 참고문헌
   슬라이드에 "서지정보 보완 필요"로 남겼다.
2. **목록에 없는 논문은 한 편도 추가하지 못했다.** 선행연구 조사는 주어진 목록을
   넘어 분야 전체를 훑어야 공백이 보이는데, 이 조건에서는 7편이 전부다.
3. **인용 서식이 통일되지 않았다.** APA·ACM·IEEE 중 무엇을 쓸지 판단할 근거가 없어
   저자-연도 표기만 임의로 맞췄다.
4. **디자인은 python-pptx 기본값.** 색·글씨체·여백을 직접 정했고, 검수 절차가 없다.
