# week6_skills_package

**과제 1 — Skill Creation.** 같은 선행연구 조사 과제를 스킬 없이(A) 한 번, 오픈소스 스킬
5종을 적용해(B) 한 번 수행하고 그 차이를 기록했다.

- 과제 주제 — 게임 닉네임의 형태·의미 분석 선행연구 조사
- 결과물 — 발표용 `.pptx` 9장 (B는 HTML 버전 추가)
- 분야 — 오노마스틱스(인명학) · 게임 HCI
- 수업 — AI기반콘텐츠창업워크숍2 (2026-10-14)

---

## 요약 — 무엇이 달라졌나

| | A (스킬 없음) | B (스킬 5종) |
|---|---|---|
| 다룬 논문 | 7편 (주어진 목록이 전부) | **18편** |
| 서지정보 확정 | 1/7 | **6/7** |
| DOI 기재 | 0건 | **12건** |
| 슬라이드 구조 | 9장 모두 "제목+글머리표" | 9장이 서로 다른 리듬 |
| 사전 준비 | 없음 | Python + 패키지 5종 |

**가장 큰 성과는 분량이 아니라 교정이다.** A안은 연구 공백으로 "비유럽 언어는 거의
다뤄지지 않았다"를 들었는데, 검색해 보니 스와힐리어·응움보어·중국어·페르시아어 연구가
이미 있었다. **A안대로 발표했다면 틀린 주장을 했을 것이다.**

자세한 내용은 [`COMPARISON.md`](COMPARISON.md)에 있다.

---

## 과제 요건 대조표

| 요건 | 이 레포의 위치 |
|---|---|
| 레포 이름 `week6_skills_package` | ✓ |
| 과제 선정 | 게임 닉네임 형태·의미 분석 선행연구 조사 — 본인 리서치 주제 |
| OpenSource Skill 5개 이상 | [`B_with_skills/skills/`](B_with_skills/skills/) — 5개 저장소, 8개 스킬 폴더 |
| **A** — 코드 | [`A_without_skills/make_ppt.py`](A_without_skills/make_ppt.py) |
| **A** — 프롬프트 (.md) | [`A_without_skills/prompt.md`](A_without_skills/prompt.md) |
| **A** — 결과물 | [`선행연구조사_게임닉네임.pptx`](A_without_skills/선행연구조사_게임닉네임.pptx) — 9장 |
| **B** — 스킬 묶음 | [`B_with_skills/skills/`](B_with_skills/skills/) + [`ATTRIBUTION.md`](B_with_skills/skills/ATTRIBUTION.md) |
| **B** — Scripts | [`B_with_skills/scripts/install_skills.sh`](B_with_skills/scripts/install_skills.sh), [`B_with_skills/make_ppt.py`](B_with_skills/make_ppt.py) |
| **B** — 결과물 | [`선행연구조사_게임닉네임_B.pptx`](B_with_skills/선행연구조사_게임닉네임_B.pptx) — 9장 · [HTML 판](B_with_skills/선행연구조사_게임닉네임_B.html) |
| A/B 비교 | [`COMPARISON.md`](COMPARISON.md) |

---

## 사용한 오픈소스 스킬 5종

전부 GitHub 공개 저장소이며 라이선스가 명확하다. **본체를 이 레포에 담았고**
(`B_with_skills/skills/`), 각 폴더 안에 원저작자의 라이선스 전문이 들어 있다.
출처·수정 내역은 [`ATTRIBUTION.md`](B_with_skills/skills/ATTRIBUTION.md)에 정리했다.

| # | 스킬 | ★ | 라이선스 | 역할 |
|---|---|---:|---|---|
| 1 | [epoko77-ai/im-not-ai](https://github.com/epoko77-ai/im-not-ai) | 5,984 | MIT | 한글 AI 티 제거 (`humanize-korean`, `humanize-scan`) |
| 2 | [Nutlope/hallmark](https://github.com/Nutlope/hallmark) | 30,048 | MIT | 디자인 — 구조 다양성, 토큰 고정 |
| 3 | [O0000-code/paper-search-pro](https://github.com/O0000-code/paper-search-pro) | 194 | Apache-2.0 | 문헌 검색 (OpenAlex·S2·CrossRef·PubMed·arXiv) |
| 4 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | 48,967 | MIT | 인용·BibTeX (`citation-management` 하나만 사용) |
| 5 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | 30,489 | MIT | HTML 슬라이드 |

---

## 폴더 구성

```
week6_skills_package/
├── README.md                     이 파일
├── COMPARISON.md                 A/B 비교 기록
├── A_without_skills/             ← A: 코드 · 프롬프트 · 결과물
│   ├── prompt.md                 조건 + 실제 입력한 프롬프트 + 겪은 문제
│   ├── make_ppt.py               생성 코드
│   └── 선행연구조사_게임닉네임.pptx        ← 결과물 (9장)
└── B_with_skills/                ← B: 스킬 묶음 · Scripts · 결과물
    ├── prompt.md                 같은 프롬프트 + 스킬별로 실제 한 일
    ├── make_ppt.py               생성 코드
    ├── 선행연구조사_게임닉네임_B.pptx      ← 결과물 (9장)
    ├── 선행연구조사_게임닉네임_B.html      ← 같은 내용의 HTML 판
    ├── scripts/
    │   └── install_skills.sh     원본 저장소에서 스킬 5종 다시 받기
    ├── skills/                   ← 스킬 묶음 (11MB)
    │   ├── ATTRIBUTION.md         출처·라이선스·수정 내역
    │   ├── humanize-korean/  humanize/  humanize-scan/  humanize-redo/
    │   ├── hallmark/
    │   ├── paper-search-pro/
    │   ├── citation-management/
    │   └── frontend-slides/
    └── paper-search-results/     검색 원자료 (질의·응답·중복 제거 결과)
```

`paper-search-results/`를 남겨 둔 것은 검색 과정을 재현할 수 있게 하기 위해서다.
어떤 질의로 몇 편이 나왔고 무엇을 걸렀는지가 거기 있다.

---

## 설치와 실행

사전 요건 — Python 3.9 이상.

```bash
pip install pyyaml requests pyalex python-pptx
```

**윈도우 주의.** 스킬들이 `python3` 명령을 호출하는데 윈도우에는 그 이름이 없다.
`python.exe`를 복사해 `python3.exe`를 만들어 두어야 한다.

스킬을 쓰려면 묶음을 개인 스킬 폴더로 옮긴다.

```bash
cp -r B_with_skills/skills/* ~/.claude/skills/
```

원본 저장소에서 새로 받고 싶으면 이쪽을 쓴다. 다만 `paper-search-pro`의
`venue_whitelist.md`와 `SKILL.md` 수정분은 이 레포에만 있다.

```bash
bash B_with_skills/scripts/install_skills.sh
```

어느 쪽이든 **새 세션**을 열어야 스킬 목록에 잡힌다.

발표 자료를 다시 만들려면:

```bash
python3 A_without_skills/make_ppt.py
```

```bash
python3 B_with_skills/make_ppt.py
```

HTML 판은 `B_with_skills/`의 `.html` 파일을 브라우저로 열면 된다. 의존성이 없다.
← → 또는 Space로 넘기고, F로 전체화면, 숫자 키로 해당 장 이동.

---

## 스킬을 쓰면서 걸린 것

좋은 점만 적으면 비교가 아니다. 실제로 막힌 것을 적는다.

**1. 스킬의 설정이 틀렸다.** 설치할 때 넣은 학회 화이트리스트(ICEC·IEEE·CHI PLAY·FDG)로
거르면 128편 중 **1편**만 남았다. 이 주제는 게임 HCI가 아니라 오노마스틱스 분야였고,
주로 나오는 곳은 *Names* 저널이었다. 화이트리스트를 끌지 말지는 사람이 정했다.
**스킬을 쓴다고 판단이 면제되지 않는다.**

**2. 요구한 API 키가 실제로는 필요 없었다.** `paper-search-pro`는 OpenAlex 키가 없으면
중단하라고 되어 있지만 키 없이도 응답이 왔다. 문서를 그대로 따랐다면 시작조차 못 했다.

**3. 스킬 파일이 빠져 있었다.** `frontend-slides`의 `SKILL.md`는 `viewport-base.css`를
"반드시 전문을 포함하라"고 하는데 **업스트림 저장소에 그 파일이 없다.**
`html-template.md`의 스케일 구조로 대체했다.

**4. 용량이 컸다.** `paper-search-pro`는 내려받은 상태로 27MB였다. 중국어 데이터베이스
모듈·문서·테스트·렌더러 소스를 덜어 8.5MB로 줄여 쓰고 있다.

**5. hallmark는 PPT용이 아니다.** 웹 UI 전용이라 원칙(구조 다양성·지어낸 수치 금지·
번호 남용 금지·폰트 2종 페어링)만 옮겨 적용했다.

---

## 정직성에 관하여

지어낸 것이 없도록 신경 썼다.

- **Szymański (2013)** — DOI와 수록지를 끝내 확인하지 못해 미확인으로 남겼다.
- **Fomin & Chobotar (2022)** — 주신 목록의 이 항목이 검색에서는 **Chobotar (2026)**
  단독 저자로만 잡힌다. 별건일 수 있어 추측으로 메우지 않고 그대로 적었다.
- 발표 자료의 모든 수치(18편·11개 언어·44년·피인용 수)는 실제로 센 값이다.
