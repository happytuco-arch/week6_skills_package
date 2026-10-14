"""
B안 — 스킬 5종 적용. 선행연구 조사 발표 자료.

반영한 스킬
  paper-search-pro    : OpenAlex 3개 전략 → 128편 → 주제 적중 72편 → 18편 선정
  citation-management : DOI·저자·수록지 확정 (A안의 '서지정보 보완 필요' 6건 중 5건 해결)
  hallmark            : 구조 다양성(슬라이드마다 다른 리듬), 토큰 고정, 번호 남용 제거,
                        명조+고딕 2종 페어링, 지어낸 수치 금지
  humanize-korean     : 본문 문장의 AI 티 패턴 제거
  frontend-slides     : 같은 내용의 HTML 버전 (make_html.py)

실행: python3 make_ppt.py
"""

from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Cm, Pt

OUT = Path(__file__).parent / "output" / "선행연구조사_게임닉네임_B.pptx"

# ── 고정 토큰 (hallmark: 렌더 중 즉흥 금지 — 모든 색·글씨는 여기서만) ──────
SERIF = "바탕"          # 표제용
SANS = "맑은 고딕"       # 본문용
PAPER = RGBColor(0xFA, 0xF8, 0xF4)   # 따뜻한 미색 — 순백 아님
INK = RGBColor(0x1A, 0x1A, 0x18)
INK_SOFT = RGBColor(0x6B, 0x67, 0x60)
RULE = RGBColor(0xDC, 0xD6, 0xCA)
ACCENT = RGBColor(0x7A, 0x2E, 0x1E)   # 적갈 — A안의 감청과 색상 축이 다름
ACCENT_SOFT = RGBColor(0xC9, 0xB8, 0xA8)

prs = Presentation()
prs.slide_width = Cm(33.87)
prs.slide_height = Cm(19.05)
BLANK = prs.slide_layouts[6]


def slide():
    s = prs.slides.add_slide(BLANK)
    bg = s.background.fill
    bg.solid()
    bg.fore_color.rgb = PAPER
    return s


def text(s, l, t, w, h, anchor=MSO_ANCHOR.TOP):
    box = s.shapes.add_textbox(Cm(l), Cm(t), Cm(w), Cm(h))
    tf = box.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    return tf


def line(p, txt, size, font=SANS, bold=False, color=INK, space_after=6, align=None):
    r = p.add_run()
    r.text = txt
    r.font.name = font
    r.font.size = Pt(size)
    r.font.bold = bold
    r.font.color.rgb = color
    p.space_after = Pt(space_after)
    if align:
        p.alignment = align
    return r


def rule(s, l, t, w, thick=0.05, color=RULE):
    sh = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, Cm(l), Cm(t), Cm(w), Cm(thick))
    sh.fill.solid()
    sh.fill.fore_color.rgb = color
    sh.line.fill.background()
    sh.shadow.inherit = False
    return sh


def head(s, title, kicker=None):
    """표제 — 번호를 붙이지 않는다(hallmark: 번호 머리말은 기본 끔)."""
    tf = text(s, 2.2, 1.5, 29, 2.4)
    p = tf.paragraphs[0]
    line(p, title, 26, SERIF, True, INK)
    if kicker:
        p2 = tf.add_paragraph()
        line(p2, kicker, 12, SANS, False, INK_SOFT)
    rule(s, 2.2, 4.3, 29.5)


# ══ 1. 표지 — 좌측 정렬, 명조 대제목 ═══════════════════════════════════
s = slide()
rule(s, 2.2, 5.2, 12, 0.12, ACCENT)
tf = text(s, 2.2, 6.0, 26, 6)
p = tf.paragraphs[0]
line(p, "게임 닉네임의", 38, SERIF, True, INK, 2)
p = tf.add_paragraph()
line(p, "형태·의미 분석", 38, SERIF, True, INK, 14)
p = tf.add_paragraph()
line(p, "선행연구 18편을 읽고 정리한 결과와, 아직 아무도 하지 않은 일", 14, SANS, False, INK_SOFT)

tf = text(s, 2.2, 15.6, 26, 2)
p = tf.paragraphs[0]
line(p, "AI기반콘텐츠창업워크숍2  ·  2026.10.14", 11, SANS, False, INK_SOFT)

# ══ 2. 한눈에 — 수치 타일 (실제로 센 값만) ════════════════════════════
s = slide()
head(s, "한눈에", "OpenAlex 세 갈래 검색 → 중복 제거 128편 → 주제 적중 72편 → 정리 대상 18편")

tiles = [
    ("18", "편", "본 발표에서 다루는 선행연구"),
    ("11", "개 언어", "선행연구가 다룬 언어의 수"),
    ("44", "년", "1982년부터 2026년까지"),
]
x = 2.2
for num, unit, desc in tiles:
    tf = text(s, x, 6.5, 9, 5)
    p = tf.paragraphs[0]
    r = p.add_run()
    r.text = num
    r.font.name = SERIF
    r.font.size = Pt(54)
    r.font.bold = True
    r.font.color.rgb = ACCENT
    r2 = p.add_run()
    r2.text = "  " + unit
    r2.font.name = SANS
    r2.font.size = Pt(15)
    r2.font.color.rgb = INK_SOFT
    p2 = tf.add_paragraph()
    line(p2, desc, 12, SANS, False, INK_SOFT)
    rule(s, x, 12.2, 8.2)
    x += 10.2

tf = text(s, 2.2, 13.6, 29, 4)
p = tf.paragraphs[0]
line(p, "한국어와 일본어를 다룬 연구는 한 편도 찾지 못했다.", 17, SANS, True, ACCENT, 8)
p = tf.add_paragraph()
line(p, "11개 언어가 모두 유럽·아프리카·중동·중국어권에 몰려 있어서, 한국어 닉네임을 같은 틀로 "
        "분석하는 일은 아직 비어 있는 자리로 남아 있다.",
     13, SANS, False, INK_SOFT)

# ══ 3. 지도 — 2열 대비 ════════════════════════════════════════════════
s = slide()
head(s, "선행연구는 두 갈래로 나뉜다", "그리고 두 갈래는 아직 만나지 않았다")

for i, (label, title, items) in enumerate([
    ("방법론", "무엇으로 분석할 것인가", [
        "Stuart & Botella (2009) — 코퍼스에서 동시출현 행렬을 거쳐",
        "semantic network 로 가는 절차를 단계로 정리",
        "",
        "Omodei, Cointet & Poibeau (2014) — 언어 패턴과 통계를",
        "섞어 키워드를 뽑고 네트워크를 세움 (LREC'14)",
        "",
        "→ 일반 코퍼스를 대상으로 했다. 닉네임에 쓴 사례는 없다.",
    ]),
    ("대상", "무엇을 분석할 것인가", [
        "Leslie & Skipper (1990) — 사회 오노마스틱스의 출발점",
        "Hassanein (2019) — 게임 사용자명의 조어·완곡어법",
        "Kaziaba (2022) — 루넷 5,000건 다층위 분석",
        "Klimova (2020) — 비디오 게임 닉네임의 기능과 변이",
        "Taji (2024) — 스와힐리어 닉네임 형태·의미 분석",
        "",
        "→ 모두 사람이 손으로 분류했다. 최대 7,456건.",
    ]),
]):
    x = 2.2 + i * 15.3
    tf = text(s, x, 5.2, 14, 1)
    p = tf.paragraphs[0]
    line(p, label, 11, SANS, True, ACCENT, 4)
    p = tf.add_paragraph()
    line(p, title, 18, SERIF, True, INK)
    rule(s, x, 7.6, 13.5)
    tf = text(s, x, 8.1, 14, 10)
    first = True
    for it in items:
        p = tf.paragraphs[0] if first else tf.add_paragraph()
        first = False
        if not it:
            line(p, "", 6)
        elif it.startswith("→"):
            line(p, it, 13, SANS, True, ACCENT, 4)
        else:
            line(p, it, 12.5, SANS, False, INK, 3)

# ══ 4. 계보 — 타임라인 ════════════════════════════════════════════════
s = slide()
head(s, "닉네임 연구는 이렇게 흘러왔다", "오프라인 별명 연구에서 출발해 온라인으로, 다시 전산으로")

marks = [
    ("1990", "사회 오노마스틱스", "Leslie & Skipper\n별명 연구의 이론 틀"),
    ("2012", "디지털로 이동", "Hassa\n사용자명을 자기표현으로"),
    ("2015", "전산적 접근", "Jaech & Ostendorf\n사용자명으로 속성 예측"),
    ("2020", "게임으로", "Klimova\n비디오 게임 닉네임"),
    ("2024", "비유럽 언어", "Taji\n스와힐리어 형태·의미"),
]
rule(s, 3.2, 9.4, 27.5, 0.06, ACCENT_SOFT)
x = 2.2
for i, (yr, label, who) in enumerate(marks):
    tf = text(s, x, 6.2, 6.2, 2.6, MSO_ANCHOR.BOTTOM)
    p = tf.paragraphs[0]
    line(p, yr, 20, SERIF, True, ACCENT, 2, PP_ALIGN.CENTER)
    p = tf.add_paragraph()
    line(p, label, 12, SANS, True, INK, 0, PP_ALIGN.CENTER)
    dot = s.shapes.add_shape(MSO_SHAPE.OVAL, Cm(x + 2.95), Cm(9.15), Cm(0.5), Cm(0.5))
    dot.fill.solid()
    dot.fill.fore_color.rgb = ACCENT
    dot.line.fill.background()
    dot.shadow.inherit = False
    tf = text(s, x, 10.3, 6.2, 3.5)
    for j, ln in enumerate(who.split("\n")):
        p = tf.paragraphs[0] if j == 0 else tf.add_paragraph()
        line(p, ln, 11, SANS, False, INK_SOFT, 2, PP_ALIGN.CENTER)
    x += 6.2

tf = text(s, 2.2, 14.6, 29, 3)
p = tf.paragraphs[0]
line(p, "전산적 접근은 2015년에 이미 나왔지만 그때 푼 문제는 사용자명으로 사용자의 "
        "나이와 성별을 맞히는 일이었고, 닉네임을 언어학적 층위로 분류하는 쪽으로는 아무도 가지 않았다.",
     13, SANS, False, INK_SOFT)

# ══ 5. 핵심 논문 — 표 ═════════════════════════════════════════════════
s = slide()
head(s, "핵심 논문", "교수님께서 주신 7편 중 6편의 서지정보를 확정했고, 11편을 새로 찾았다")

rows = [
    ("Leslie & Skipper", "1990", "Names 38(4)", "별명의 사회 오노마스틱스 이론", "77"),
    ("van der Nagel", "2017", "Internet Histories", "사용자명에서 프로필로, 익명성의 변천", "65"),
    ("Jaech & Ostendorf", "2015", "EMNLP", "사용자명으로 사용자 속성 예측", "24"),
    ("Hassa", "2012", "Names 60(2)", "디지털 세계의 자기 노출로서 사용자명", "23"),
    ("Hassanein", "2019", "Int. J. English Linguistics 9(5)", "게임 사용자명의 조어와 완곡어법", "2"),
    ("Klimova", "2020", "Вопросы ономастики 17(3)", "비디오 게임 닉네임의 기능과 변이", "2"),
    ("Kaziaba", "2022", "Nauchnyi Dialog 11(7)", "루넷 자기명명의 인명적 기능", "—"),
    ("Taji", "2024", "Nomina Africana 38(1)", "스와힐리어 닉네임 형태·의미 분석", "2"),
]
shape = s.shapes.add_table(len(rows) + 1, 5, Cm(2.2), Cm(5.2), Cm(29.5), Cm(2))
tb = shape.table
tb.columns[0].width = Cm(6.0)
tb.columns[1].width = Cm(2.0)
tb.columns[2].width = Cm(8.0)
tb.columns[3].width = Cm(11.0)
tb.columns[4].width = Cm(2.5)

for j, h in enumerate(["저자", "연도", "수록", "내용", "피인용"]):
    c = tb.cell(0, j)
    c.text = h
    pr = c.text_frame.paragraphs[0].runs[0]
    pr.font.name, pr.font.size, pr.font.bold = SANS, Pt(11), True
    pr.font.color.rgb = PAPER
    c.fill.solid()
    c.fill.fore_color.rgb = ACCENT

for i, row in enumerate(rows, 1):
    for j, v in enumerate(row):
        c = tb.cell(i, j)
        c.text = v
        pr = c.text_frame.paragraphs[0].runs[0]
        pr.font.name = SANS
        pr.font.size = Pt(10.5)
        pr.font.bold = (j == 0)
        pr.font.color.rgb = INK if j != 4 else INK_SOFT
        c.fill.solid()
        c.fill.fore_color.rgb = PAPER if i % 2 else RGBColor(0xF2, 0xEE, 0xE6)

tf = text(s, 2.2, 16.6, 29, 2)
p = tf.paragraphs[0]
line(p, "Szymański(2013)은 DOI와 수록지를 끝내 확인하지 못해 미확인으로 남긴다.",
     11, SANS, False, INK_SOFT)

# ══ 6. 언어 분포 — 가로 막대 ══════════════════════════════════════════
s = slide()
head(s, "어떤 언어가 연구되었나", "선행연구 16편이 대상으로 삼은 언어권 (방법론 2편 제외)")

bars = [("영어권", 5), ("슬라브어권", 4), ("아프리카어권", 3), ("기타", 4), ("한국어·일본어", 0)]
y = 6.4
for label, n in bars:
    tf = text(s, 2.2, y - 0.15, 7, 1.2)
    p = tf.paragraphs[0]
    line(p, label, 14, SANS, n == 0, ACCENT if n == 0 else INK)
    track = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, Cm(9.4), Cm(y + 0.1), Cm(16), Cm(0.75))
    track.fill.solid()
    track.fill.fore_color.rgb = RGBColor(0xEE, 0xE9, 0xDF)
    track.line.fill.background()
    track.shadow.inherit = False
    if n:
        fill = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, Cm(9.4), Cm(y + 0.1), Cm(16 * n / 5), Cm(0.75))
        fill.fill.solid()
        fill.fill.fore_color.rgb = ACCENT
        fill.line.fill.background()
        fill.shadow.inherit = False
    tf = text(s, 25.8, y - 0.1, 4, 1.2)
    p = tf.paragraphs[0]
    line(p, f"{n}편", 14, SANS, True, ACCENT if n else INK_SOFT)
    y += 1.75

tf = text(s, 2.2, 15.6, 29, 3)
p = tf.paragraphs[0]
line(p, "비유럽 언어 연구가 없다는 말은 틀렸다.", 14, SANS, True, INK, 6)
p = tf.add_paragraph()
line(p, "스와힐리어·응움보어·중국어·페르시아어를 다룬 연구가 이미 있고, 진짜 문제는 연구마다 "
        "분류 체계가 달라서 열한 갈래로 쌓인 결과를 서로 포개 볼 수 없다는 데 있다.",
     13, SANS, False, INK_SOFT)

# ══ 7. 연구 공백 — 3블록 ══════════════════════════════════════════════
s = slide()
head(s, "그래서 무엇이 비어 있나")

gaps = [
    ("분류 체계가 제각각이다",
     "11개 언어가 각각 연구되었지만 분류 틀이 연구마다 다르다. "
     "같은 기준으로 다시 분류해야 언어 간 비교가 된다."),
    ("전산적 접근의 방향이 다르다",
     "Jaech & Ostendorf(2015)는 사용자명으로 나이·성별을 맞혔다. "
     "언어학적 층위로 분류한 전산 연구는 찾지 못했다."),
    ("동기는 설문으로만 물었다",
     "작명 동기를 다룬 연구는 면접·설문에 의존한다. "
     "닉네임과 실제 플레이 행위를 연결한 연구는 없다."),
]
y = 5.3
for title, body in gaps:
    rule(s, 2.2, y, 0.12, 3.0, ACCENT)
    tf = text(s, 2.9, y - 0.2, 28, 3.2)
    p = tf.paragraphs[0]
    line(p, title, 17, SERIF, True, INK, 5)
    p = tf.add_paragraph()
    line(p, body, 13, SANS, False, INK_SOFT)
    y += 4.1

# ══ 8. 제안 — 4단계 (순서가 실제로 의미 있으므로 번호를 쓴다) ═════════
s = slide()
head(s, "제안하는 연구 방향", "앞의 세 공백을 순서대로 겨냥한다")

steps = [
    ("1", "분류 체계를 코드로 옮긴다",
     "Dubiec-Stach의 네 층위(의미·형태·통사·문자)를 LLM 프롬프트로 구현한다. "
     "손으로 하던 분류를 자동화하는 것이 1차 목표다."),
    ("2", "다국어로 넓힌다",
     "같은 체계를 언어별로 적용해 비교 가능한 결과를 만든다. 한국어를 넣어 첫 번째 공백을 직접 메운다."),
    ("3", "semantic network 를 붙인다",
     "닉네임 구성 요소를 키워드로 보고 동시출현 네트워크를 그린다. "
     "Stuart & Botella의 절차를 닉네임 자료에 처음 적용하는 지점이다."),
    ("4", "동기와 행위를 잇는다",
     "분류 결과를 플레이 데이터와 대조한다. 설문 없이 동기를 보는 길이다."),
]
y = 5.3
for num, title, body in steps:
    tf = text(s, 2.2, y, 2, 2)
    p = tf.paragraphs[0]
    line(p, num, 30, SERIF, True, ACCENT_SOFT)
    tf = text(s, 4.3, y + 0.1, 27, 2.6)
    p = tf.paragraphs[0]
    line(p, title, 16, SERIF, True, INK, 4)
    p = tf.add_paragraph()
    line(p, body, 12.5, SANS, False, INK_SOFT)
    y += 3.25

# ══ 9. 참고문헌 — 2열 + DOI ═══════════════════════════════════════════
s = slide()
head(s, "참고문헌", "DOI를 확인한 것만 적는다")

refs_l = [
    "Stuart, K., & Botella, A. (2009). Corpus Linguistics, Network Analysis "
    "and Co-occurrence Matrices. Int. J. English Studies, 9(1). "
    "doi:10.6018/ijes.1.1.99481",
    "Omodei, E., Cointet, J.-P., & Poibeau, T. (2014). Mapping the NLP Domain: "
    "Experiments using the ACL Anthology. LREC'14, 2972–2978. "
    "doi:10.63317/4hcdpzpoxfj8",
    "Leslie, P. L., & Skipper, J. K. (1990). Toward a Theory of Nicknames. "
    "Names, 38(4), 273. doi:10.1179/nam.1990.38.4.273",
    "Hassa, S. (2012). Projecting, Exposing, Revealing Self in the Digital "
    "World. Names, 60(2). doi:10.1179/0027773812z.00000000031",
    "Jaech, A., & Ostendorf, M. (2015). What Your Username Says About You. "
    "EMNLP. doi:10.18653/v1/d15-1240",
    "van der Nagel, E. (2017). From usernames to profiles. "
    "Internet Histories. doi:10.1080/24701475.2017.1389548",
]
refs_r = [
    "Hassanein, H. S. A. (2019). GD Usernames and Euphemism: A Morphosemantic "
    "Analysis. Int. J. English Linguistics, 9(5), 107. doi:10.5539/ijel.v9n5p107",
    "Klimova, M. A. (2020). Nicknames in Video Gaming. Вопросы ономастики, "
    "17(3). doi:10.15826/vopr_onom.2020.17.3.045",
    "Dubiec-Stach, J. (2021). Nick – tożsamość w Internecie. "
    "doi:10.5604/01.3001.0015.6126",
    "Kaziaba, V. V. (2022). Self-Nominations with Function of Anthroponym in "
    "Runet. Nauchnyi Dialog, 11(7), 212–230. doi:10.24224/2227-1295-2022-11-7-212-230",
    "Taji, J. (2024). A morphosemantic analysis of personal nicknames in "
    "Swahili. Nomina Africana, 38(1). doi:10.2989/na.2024.38.1.4.1382",
    "Chobotar, V. I. (2026). Digital onomastics. Current Issues in Philology "
    "and Pedagogical Linguistics. doi:10.29025/2079-6021-2026-2-123-131",
]
for i, col in enumerate([refs_l, refs_r]):
    tf = text(s, 2.2 + i * 15.3, 5.2, 14.3, 11)
    for j, r in enumerate(col):
        p = tf.paragraphs[0] if j == 0 else tf.add_paragraph()
        line(p, r, 9.5, SANS, False, INK, 7)

tf = text(s, 2.2, 16.3, 29.5, 2)
p = tf.paragraphs[0]
line(p, "Szymański (2013) — 서지정보 미확인. 교수님 목록의 "
        "Fomin & Chobotar (2022)는 Chobotar (2026)으로만 확인되어 별건일 수 있다.",
     10, SANS, False, INK_SOFT)

OUT.parent.mkdir(parents=True, exist_ok=True)
prs.save(OUT)
print(f"저장: {OUT}  ({len(prs.slides._sldIdLst)}장)")
