# portfolio — STATUS

**State:** v4 built locally (2026-07-23), NOT yet committed — Will reviews, then a commit publishes
via auto-sync. Site live at <https://projectsofwill.github.io/> (user site, serves `index.html`
from main). Marked `noindex` while iterating.

## v4 refresh pass (2026-07-23) — AI page catch-up, 07-07 → 07-23

- Fixed two now-false claims: "llm fallback" cap (backup provider was decommissioned 07-21 after a
  real outage missed surfaces) replaced by a "liveness watchdog" cap; "headroom" compression-proxy
  cap removed (torn down 07-22, replacement claudex reverted same day). Both moved to the
  "built, measured, killed" list (unnamed there: "compression proxy", "llm failover").
- Shared brain added: data-tier table row, §02 intro now says "shared task board and a shared
  memory bank", security pii cap updated (isolated banks, no fallback provider to leak to).
- Second pass (same day, Will feedback): Hindsight IS now named + linked (vectorize-io/hindsight),
  with how-it-works prose (typed extraction, temporal expiry, hybrid recall, cross-agent briefing).
  Old §04 "Memory + optimizations" split into §04 Memory and §05 Optimizations (security/record/
  gateway/starter renumbered 06-09, jumpnav updated). §04 gained two diagrams: a 4-card store grid
  (flat memory / wiki / hindsight / alfred db, each with its wall) and a 4-node "how a memory gets
  made" flow (session end → distill+scrub → bank → briefed next session). New "injection defense"
  cap (researcher gets no recall; external-content memories recall as claims-with-source).
  Data-tier row renamed shared brain → hindsight; milestone + kill-list now name it too.
- Ninth pass (same day, Will feedback): Mandarin section edits. Build-time claims removed
  ("inside a week", "that weekend" → "It is what I study on now"). 4 phone screenshots added as a
  CSS scroll-snap carousel (no JS): uploads → shots/mandarin-{1..4}.webp (440px, WebP q78, 88KB
  total), inlined as data URIs via build.py (FONTS list generalized to ASSETS with {{SHOT1-4}}
  placeholders — shots/ is now a build input, keep it committed). Order: daily loop, course map,
  review card, graded reading. index.html 149KB → 273KB.
- Eighth pass (same day, Will feedback): "Build your own" links-line now points at the real
  public repo (github.com/projectsofwill/claude-os-starter, replaces the GitHub-profile link);
  newsletter link removed from that section (footer + Hermes-cap archive links kept); the
  now-false "shared on request" meta line removed. DRIFT FLAG: public starter repo last pushed
  jun 27, but the local starter got the 07-06 post-freeze refresh — public copy is a month stale.
- Seventh pass (same day, Will feedback): deal-brain de-jargoned. "Held-out ground-truth manifest"
  paragraph rewritten as the answer-key story with human-readable P1 results (within one level 99%
  of the time, two-trained-humans agreement, ~$2 per 100 deals, weak pillar named); QWK deliberately
  NOT on the page. Chip: "architecture locked" → "first agent shipped and measured". MEDDPICC row:
  "coverage Σ/16" → plain rubric sentence.
- Sixth pass (same day, Will feedback): RevOps view renamed Projects (route #/revops → #/projects,
  nav, views map, keyboard "1", home row; no stale refs). New §03 "Mandarin study app" added to it:
  offline iOS app, bundled curriculum.sqlite (88 lessons, HSK 3.0, synthesized pinyin, audio
  packs), spec-to-TestFlight-inside-a-week story, 4-row layer table. SENSITIVITY DECISION: the
  course ("Mandarin Blueprint") and the content-extraction pipeline are deliberately NOT named on
  the page — repo docs mark the extraction personal-use-only; page says "a course site" only.
  Home index row meta updated. Projects intro rewritten to cover the personal third project.
- Fifth pass (same day, Will feedback): milestones re-evaluated against the full TIMELINE. Added
  jun 27 "Both user-facing agents complete" (Alfred calendar-write + Arnold Oura-gated coaching;
  the agents were missing entirely) and jul 23 "The loop closes" (Phase 6 phone recall, deployed
  today). Now 10 milestones: ship fast (jun 11-24) → harden (jun 27-jul 06) → get smart
  (jul 14-23). Considered and excluded: mandarin-blueprint iOS app (off-narrative for the infra
  page, would need supporting prose; flagged to Will as an option), cockpit (adopted, not built),
  OneBrain (already in the kill list), deal-brain (RevOps page), IG sync (subsumed by capture v2).
- Fourth pass (same day, Will feedback): brand-voice sweep over all prose. The page was already
  written against the voice rules, so this removed the copywriter tics that had crept in: "Two
  builds, one message" → plain rule statement; "The sharpest beat" → "The example I lead with";
  "It is not a demo" → "I live on it"; "8 calls, 1 question, 0 shared context" → "Eight places to
  look..."; "Prompt injection is assumed, not hoped away" → first-person design statement;
  "Down loudly beats degraded quietly" → "I'd rather be down loudly than degraded quietly";
  fragment section-opener in Optimizations → full sentence; "anything you need to trust" →
  "anything I need to trust"; dropped ", not a mood". Verified zero em dashes / "not just" on the
  page. Deliberately KEPT: thesis h1, "walls, not conventions", "config, not code"-pattern
  contrasts, "An alert I trust beats a fallback I don't" (X-not-Y contrasts match Will's samples).
- Third pass (same day, Will feedback): build record clarified. Milestones are now builds only
  (jul 21 "failover decommissioned" removed; its story stays in the kill list). Right column split
  into three groups: "Built, measured, killed" (semantic index, compression proxy, llm failover,
  cloud research runs), "Considered, never built" (multiplexed gateway, graph retrieval/graphify),
  "Skipped, then earned in" (hindsight: written tripwire tripped → adopted). Intro sentence
  rewritten to name the three outcomes.
- Kill-list "memory frameworks" rewritten: the written tripwire TRIPPED in July, episodic layer
  adopted scoped to cross-agent recall (measurement gated the adoption like it gated the skip).
- Second harness (codex-worker): sentence in §01 multi-model prose, build-node text in the
  build/critique/ship flow, new "second harness" cap in the Claude OS group.
- Alfred meta: "own bot and gateway" (07-22 split). Cadence daily lane +1: model-auth liveness
  probe. Skills line added: /spinoff · /handback.
- Milestones +3: jul 14 shared brain live, jul 21 failover decommissioned, jul 22 second harness.
- Stats: wiki 330+ → 420 (counted research/ .md excl. raw+index), skills 16 → 20 (counted
  ops/global/skills). Newsletter stays 8 (live archive checked 07-23: latest issue 06-28).
- Fixed a duplicated nested `<section id="architecture">` open tag (markup bug from v3).

## Where things stand

- Two-view page (hash-routed): RevOps Systems (Deal Desk Engine + live deal-router widget,
  deal-brain) and AI Infrastructure (architecture, agents + capabilities toggles, ingest engine,
  memory + optimizations + skills, security, build-your-own).
- Design: extracted from harryjatkins.com (dark default, grey ramp, mono meta labels, keyboard
  modes: L theme, 1/2/H page nav). Amber reserved for AI-at-the-edges.
- Decisions locked: employer not named on the page; LinkedIn wired
  (linkedin.com/in/williamwliu); root user-site URL chosen over /portfolio.
- Diagram pass on the AI page (2026-07-07), all CSS-grid based, theme-aware, vertical-stacking
  under 900px, verified in dark/light/mobile renders:
  - Section 03 ingest table → 6-node flow (amber top-border + `llm pass` chips on AI stages,
    dashed human gate, green `trusted store` chip, legend reusing the home-page swatches).
  - Section 01 `.arch` 3-node row → `.topo` 4-node topology (adds Phone·anywhere node with
    telegram link, service chips inside the VPS node, dashed Tailscale U-path PC↔VPS with
    knocked-out label). `.arch` CSS removed. Plus a 3-node model flow (build·claude →
    critique·codex → ship·gated, with gemini-tiebreak exit line) between topo and data-tier table.
  - Section 02 gained "The cadence, unattended" strip after the profile table: always / daily /
    weekly lanes with tick-marked events (08:00 brief, 10:00 people, 2× instagram, researcher
    sweep, backup, sun newsletter).
- Content pass (2026-07-07, same session): stats row now proof-of-life (8 newsletter issues per
  Will, 330+ wiki pages counted from research/, kept 5+/16/15min; dropped 6-services and 3-families,
  both visible in diagrams now). Jump-nav bar under stats (scrollIntoView via data-jump, does not
  touch the hash router; respects reduced motion). New section 06 "The build record": milestone
  timeline (jun 11 newsletter → jul 06 skill prune, dates from repo git history + Hermes STATUS)
  + "built, measured, killed" list (semantic index, memory frameworks, multiplexed gateway, cloud
  research runs). New section 07 "ai-gateway" (reusable Cloudflare Worker + 4-layer guardrail
  table; deliberately NO liveness claim, repo shows no deploy). "Build your own" renumbered 06→08.
- Section 02 rework (Will feedback, 2026-07-07): profile can/cannot table removed; each capgroup
  now ends in `.fence` footer rows (CAN / CANNOT, cannot-value emphasized; Hermes group carries two,
  labeled orchestrator/researcher; Claude OS got its own: cannot push or rewrite history, hooks
  deny it). Intro rewritten to be accurate: "Four groups, and only two of them are agents."
- Inline source links added: Karpathy gist (ingest + memory), Google OKF SPEC.md (okf indexes cap),
  mem0 (kill-list memory-frameworks), newsletter public archive (hermes group), Cloudflare Workers
  (gateway), Tailscale (architecture). All target=_blank rel=noopener, matching existing pattern.
- Fact notes: local newsletter-archive repo has 6 issue files but Will states 8 shipped (repo may
  trail the live archive); "always on from day one" is Will's statement; VPS date jun 24 is the
  Hermes STATUS as-built date.

## Next

1. Will's content iteration pass (continuing on the Mac).
2. Remove `noindex` + announce when Will calls it launched.
3. ~~Swap the "Build your own" link when claude-os-starter goes public~~ — done (eighth pass);
   remaining: push the 07-06 starter refresh to the public repo (it's a month stale).

## Open questions

- Whether to add an OG share image (`og:image`) before sharing the link anywhere.
