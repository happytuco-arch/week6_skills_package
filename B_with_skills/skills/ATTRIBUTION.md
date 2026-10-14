# 스킬 묶음 — 출처·라이선스·변경 사항

이 폴더의 스킬은 전부 **제3자가 만든 오픈소스**다. 과제 요건(“B: 스킬 묶음”)에 따라
본체를 그대로 담았으며, 각 스킬 폴더 안에 원저작자의 라이선스 전문이 들어 있다.

| 폴더 | 출처 | 라이선스 | 원저작자 |
|---|---|---|---|
| `humanize-korean`, `humanize`, `humanize-scan`, `humanize-redo` | [epoko77-ai/im-not-ai](https://github.com/epoko77-ai/im-not-ai) | MIT | epoko77-ai |
| `hallmark` | [Nutlope/hallmark](https://github.com/Nutlope/hallmark) | MIT | Hallmark contributors |
| `paper-search-pro` | [O0000-code/paper-search-pro](https://github.com/O0000-code/paper-search-pro) | Apache-2.0 | Bo |
| `citation-management` | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | MIT | K-Dense Inc. |
| `frontend-slides` | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | MIT | Zara Zhang |

---

## 원본에서 바꾼 것

Apache-2.0 §4(b)는 수정한 파일에 그 사실을 밝히도록 요구한다. MIT 쪽도 같은 원칙을 따라
적어 둔다. **아래 외에는 원본 그대로다.**

### `paper-search-pro` — 수정함

내려받은 상태로 27MB였고, 이 과제에 쓰지 않는 부분이 대부분이었다. 8.5MB로 줄였다.

**지운 것**

| 대상 | 이유 |
|---|---|
| `docs/` (설명서 사이트 6.9MB + 스크린샷 3.2MB) | 실행에 쓰이지 않음 |
| `assets/webartifacts_app/paper-report/src/` 와 빌드 설정 | 완성본 `bundle.html` 만 쓰면 됨 |
| `tests/`, `evals/`, `pytest.ini` | 실행에 쓰이지 않음 |
| `scripts/nssd_helper.py`, `scripts/yiigle_helper.py` | 중국어 전용 소스 (이 과제에서 미사용) |
| `references/search_export/syntax_cards/{cnki,sinomed,wanfang}.md`, `chinese_methodology.md`, `README.zh.md` | 위와 같음 |

**고친 것**

- `SKILL.md` — 설명(description)을 한국어 기준으로 다시 썼다. 원본에는 중국어 트리거가
  길게 들어 있어 다른 스킬 호출을 방해했다.
- `SKILL.md` STEP 1·2·4 — 중국어 언어 공간 판정과 NSSD/yiigle 경로를 들어냈다.
- `SKILL.md` STEP 5 — 학회 화이트리스트로 거르는 단계를 넣었다.
- `SKILL.md` 참조 표 — `venue_whitelist.md` 항목을 추가했다.

**새로 만든 것**

- `references/venue_whitelist.md` — ICEC·IEEE·CHI PLAY·FDG 네 학회의 이름 변형,
  거르는 순서, 범위를 넓혀야 할 때의 판단 기준.

> **이 수정이 과제 결과에 영향을 준 지점.** 화이트리스트로 거르면 검색 결과 128편 중
> 1편만 남았다. 이 주제가 게임 HCI가 아니라 오노마스틱스 분야였기 때문이다.
> 결국 화이트리스트를 끄고 진행했고, 그 판정 자체를 발표 자료에 넣었다.
> 자세한 내용은 [`../../COMPARISON.md`](../../COMPARISON.md)에 있다.

### `frontend-slides` — 파일 한 개 보탬

`SKILL.md`가 “전문을 포함하라”고 지시하는 `viewport-base.css`가 **업스트림 저장소에 없다.**
대신 저장소 루트에 있던 `html-template.md`를 스킬 폴더 안으로 복사해 그 스케일 구조를 썼다.
원본 파일은 하나도 고치지 않았다.

### 나머지 세 묶음 — 원본 그대로

`im-not-ai`(humanize 계열), `hallmark`, `citation-management`는 한 글자도 바꾸지 않았다.
`citation-management`는 원 저장소의 스킬 177개 중 한 개만 꺼내 온 것이다.

---

## 다시 받으려면

이 폴더를 지우고 [`../scripts/install_skills.sh`](../scripts/install_skills.sh)를 실행하면
원본 저장소에서 같은 구성으로 내려받는다. 다만 `paper-search-pro`의 `venue_whitelist.md`와
`SKILL.md` 수정분은 이 폴더에만 있다.
