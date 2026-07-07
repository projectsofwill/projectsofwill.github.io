# portfolio — STATUS

**State:** v3 built and deployed (2026-07-07). Site live at <https://projectsofwill.github.io/>
(user site, serves `index.html` from main). Marked `noindex` while iterating.

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
3. "Build your own" section links to the GitHub profile until claude-os-starter goes public; swap
   the link when it does.

## Open questions

- Whether to add an OG share image (`og:image`) before sharing the link anywhere.
