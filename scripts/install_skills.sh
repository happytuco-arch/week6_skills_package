#!/usr/bin/env bash
# week6_skills_package — 오픈소스 스킬 5종 설치
#
# 스킬 본체를 이 저장소에 복제해 넣지 않는 이유: 각 저장소의 라이선스를 따르기 위해서다.
# 여기서는 출처와 설치 경로만 관리한다.
#
# 실행: bash scripts/install_skills.sh
set -euo pipefail

DEST="${HOME}/.claude/skills"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

mkdir -p "$DEST"
echo "설치 위치: $DEST"
echo

# ── 1. im-not-ai — 한글 AI 티 제거 (MIT) ────────────────────────────────
echo "[1/5] im-not-ai"
git clone --depth 1 -q https://github.com/epoko77-ai/im-not-ai.git "$TMP/im-not-ai"
for s in humanize-korean humanize humanize-scan humanize-redo; do
  rm -rf "${DEST:?}/${s:?}"
  cp -r "$TMP/im-not-ai/skills/$s" "$DEST/$s"
done
cp "$TMP/im-not-ai/LICENSE" "$DEST/humanize-korean/LICENSE"

# ── 2. hallmark — 디자인 (MIT) ──────────────────────────────────────────
echo "[2/5] hallmark"
git clone --depth 1 -q https://github.com/Nutlope/hallmark.git "$TMP/hallmark"
rm -rf "${DEST:?}/hallmark"
cp -r "$TMP/hallmark/skills/hallmark" "$DEST/hallmark"
cp "$TMP/hallmark/LICENSE" "$DEST/hallmark/LICENSE"

# ── 3. paper-search-pro — 문헌 검색 (Apache-2.0) ────────────────────────
#    저장소 루트가 곧 스킬이다. 받은 상태로 27MB 라서 실행에 쓰지 않는 부분을 덜어 낸다.
echo "[3/5] paper-search-pro"
rm -rf "${DEST:?}/paper-search-pro"
git clone --depth 1 -q https://github.com/O0000-code/paper-search-pro.git "$DEST/paper-search-pro"
rm -rf "${DEST:?}/paper-search-pro/.git" \
       "${DEST:?}/paper-search-pro/docs" \
       "${DEST:?}/paper-search-pro/tests" \
       "${DEST:?}/paper-search-pro/evals"
# 렌더러는 완성본 bundle.html 만 쓴다. src/ 는 그걸 다시 빌드하는 용도.
R="${DEST:?}/paper-search-pro/assets/webartifacts_app/paper-report"
rm -rf "${R:?}/src" "${R:?}/public"
rm -f "${R:?}/pnpm-lock.yaml" "${R:?}/package.json" "${R:?}/index.html" \
      "${R:?}/components.json" "${R:?}/eslint.config.js" "${R:?}/.parcelrc"
# 중국어 전용 모듈 (이 과제에서는 쓰지 않음)
rm -f "${DEST:?}/paper-search-pro/scripts/nssd_helper.py" \
      "${DEST:?}/paper-search-pro/scripts/yiigle_helper.py" \
      "${DEST:?}/paper-search-pro/README.zh.md"

# ── 4. citation-management — 인용·BibTeX (MIT) ──────────────────────────
#    저장소에 스킬이 177개 들어 있다. 하나만 꺼낸다.
echo "[4/5] citation-management"
git clone --depth 1 --filter=blob:none --sparse -q \
  https://github.com/K-Dense-AI/scientific-agent-skills.git "$TMP/sci"
git -C "$TMP/sci" sparse-checkout set skills/citation-management
rm -rf "${DEST:?}/citation-management"
cp -r "$TMP/sci/skills/citation-management" "$DEST/citation-management"
cp "$TMP/sci/LICENSE.md" "$DEST/citation-management/LICENSE.md"

# ── 5. frontend-slides — HTML 슬라이드 (MIT) ────────────────────────────
#    스킬 본체가 plugins/ 아래 깊이 있고, 참조 파일 일부는 저장소 루트에 있다.
echo "[5/5] frontend-slides"
git clone --depth 1 -q https://github.com/zarazhangrui/frontend-slides.git "$TMP/fs"
rm -rf "${DEST:?}/frontend-slides"
cp -r "$TMP/fs/plugins/frontend-slides/skills/frontend-slides" "$DEST/frontend-slides"
cp "$TMP/fs/html-template.md" "$DEST/frontend-slides/html-template.md"
cp "$TMP/fs/LICENSE" "$DEST/frontend-slides/LICENSE"
# 참고: SKILL.md 가 요구하는 viewport-base.css 는 업스트림에 존재하지 않는다.
#       html-template.md 의 스케일 구조로 대체해 썼다.

echo
echo "완료. 설치된 스킬:"
ls -1 "$DEST"
echo
echo "주의 — 새 세션을 열어야 목록에 잡힙니다."
