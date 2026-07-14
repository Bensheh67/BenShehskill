# bsskill

[简体中文](README.md) | English | [日本語](README.ja.md) | [한국어](README.ko.md) | [繁體中文](README.zh-TW.md)

> A Chinese AI Skills toolkit for entrepreneurs and content creators. Give your Agent a real business, content, or execution problem, and get a clear judgment plus the next action you can take.

[![Version](https://img.shields.io/badge/version-2.17.7-111111.svg)](VERSION)
[![Skills](https://img.shields.io/badge/Skills-27-111111.svg)](docs/新手入门.md#skill-全目录)
[![License](https://img.shields.io/badge/license-CC%20BY--NC%204.0-111111.svg)](LICENSE)

**Supported in Doubao, WorkBuddy, Claude Code, Codex, and other Agents that support Skills.**

Created by [dontbesilent](https://x.com/dontbesilent), bsskill distills 4,176 structured knowledge atoms and 27 directly callable Skills from 16,152 public posts.

[Quick start](#quick-start) · [Install](#install) · [Capabilities](#capabilities) · [Full guide](docs/新手入门.md) · [Releases](https://github.com/dontbesilent2025/bsskill/releases)

![bsskill routing map](docs/skill-link-map.svg)

## What bsskill helps you solve

You do not need to learn a complex methodology first, or know which tool to invoke. Give `/bss` your current business situation, material, decision, or blocker. It selects the relevant Skill from the conversation context.

| Situation | What you get |
| --- | --- |
| Customers say your offer is expensive | Business diagnosis, risks, and validation actions |
| You have a topic but cannot turn it into watchable content | Content direction, hooks, titles, and script improvements |
| You know what to do but cannot move forward | Analysis of the blocker and one concrete starting action |
| You keep facing similar decisions without accumulating experience | Decision records, patterns, and snapshots |
| Your drafts, topics, and cases are scattered | A maintainable content-asset project |

## Quick start

After installation, enter this in your Agent:

```text
/bss I run coding classes for children. I have 40 paid students, but renewals are low.
Help me determine whether the issue is the product, pricing, or customer segment.
```

`/bss` reads the current conversation and selects an appropriate path. Add new facts or feedback after a round, then call `/bss` again to determine what to work on next.

When you already know the task, call a Skill directly:

```text
/bss-diagnosis I offer home-organization consulting for mothers. Clients say it is expensive. What should I change?
/bss-content I want to discuss “ordinary people should not rush into building a personal brand.” How can I turn this into content?
/bss-hook Here are the first 20 seconds of my video script. Improve the opening: …
/bss-benchmark I want to study enterprise-service content accounts. Which benchmarks should I research?
```

## Capabilities

| Goal | Main Skills | Typical output |
| --- | --- | --- |
| Evaluate a business, product, price, or customer | `/bss-diagnosis` | Diagnosis, risks, validation plan |
| Find and study benchmarks | `/bss-benchmark` | Benchmark shortlist and research framework |
| Create topics, content, titles, and videos | `/bss-content`, `/bss-hook`, `/bss-xhs-title` | Direction and publishable copy |
| Review resonance, logic, and reach | `/bss-resonate`, `/bss-script-flow`, `/bss-spread` | Prioritized edits |
| Clarify concepts, goals, and questions | `/bss-deconstruct`, `/bss-goal`, `/bss-good-question` | Testable definitions and goals |
| Work through procrastination and execution blocks | `/bss-action`, `/bss-slowisfast` | Blocker analysis and next action |
| Record and review long-term decisions | `/bss-decision`, `/bss-save`, `/bss-restore`, `/bss-report` | Local decision archive and reports |
| Build content assets and multi-Agent workflows | `/bss-content-system`, `/bss-agent-migration`, `/bss-bridge` | Local project, topic map, and bridge plan |
| Audit local Skill risks | `/bss-skill-cleaner` | Risk report and confirmed isolation |

See the [full guide and Skill directory](docs/新手入门.md#skill-全目录) for all 27 Skills, examples, and workflows.

## Install

### Doubao, WorkBuddy, Codex, and other Agents supporting Skills

Run in a terminal:

```bash
npx -y skills add dontbesilent2025/bsskill -g --all
```

Return to your Agent and enter `/bss 新手入门` to begin.

### Claude Code marketplace

```bash
claude plugin marketplace add dontbesilent2025/bsskill
claude plugin install bss@BenShehskill
```

![Claude Code installation demo](demo.gif)

### Update

Ask your current Agent:

```text
更新 bsskill
```

This syncs the official bsskill and does not modify records, reports, or decisions under `~/.bss/`. See [GitHub Releases](https://github.com/dontbesilent2025/bsskill/releases) for changes.

## How it works

```text
A real task
   ↓
/bss reads context and selects the current entry point
   ↓
One Skill produces a diagnosis, output, or record
   ↓
Add results and feedback, then decide the next step
```

## Knowledge base and local records

The repository includes 4,176 structured knowledge atoms, methodology documents organized by Skill, and a high-frequency concept glossary.

- Read the [atom library guide](知识库/原子库/README.md) for data scope and fields.
- Use `知识库/原子库/atoms.jsonl` to build your own RAG.
- Browse the [Skill knowledge packs](知识库/Skill知识包) for the methods.
- Use `/bss-save`, `/bss-restore`, and `/bss-report` for work across conversations. Data stays locally in `~/.bss/`.

![bsskill knowledge pipeline](docs/knowledge-pipeline.svg)

## Project structure

```text
bsskill/
├── skills/                  # 27 published Skills
├── 知识库/                   # Knowledge atoms, methods, and glossary
├── docs/                    # Guide, diagrams, and demo assets
├── .claude-plugin/          # Claude Code marketplace definition
└── tools/                   # Build and maintenance scripts
```

Build distribution packages locally:

```bash
bash tools/build-skills.sh
```

Packages are created in `dist/skills/`. Local experimental Skills whose names contain `beta` are excluded.


## License

Licensed under [CC BY-NC 4.0](LICENSE).

- Personal use, study, research, and non-commercial projects are welcome.
- Please attribute the source when you publish derivative work.
- Commercial use requires separate authorization. Contact the author.
