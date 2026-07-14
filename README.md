# BenShehskill 基于dbskill二次开发

简体中文 | [English](README.en.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [繁體中文](README.zh-TW.md)

> 面向一线业务团队的 AI Skills 工具箱。覆盖销售跟进、客户成功、售前方案全流程，通过原子知识库沉淀团队经验，让每位业务人员都能随时调用经过验证的方法论。

[![Version](https://img.shields.io/badge/version-2.17.10-111111.svg)](VERSION)
[![Skills](https://img.shields.io/badge/Skills-31-111111.svg)](docs/新手入门.md#skill-全目录)
[![License](https://img.shields.io/badge/license-CC%20BY--NC%204.0-111111.svg)](LICENSE)

**支持：豆包、WorkBuddy、Claude Code、Codex，以及其他支持 Skills 的 Agent。**

[快速开始](#快速开始) · [安装](#安装) · [能力一览](#能力一览) · [业务 Skill 入门](docs/business-skill-quickstart.md) · [更新日志](https://github.com/Bensheh67/BenShehskill/releases)

![dbskill 动态路由图](docs/skill-link-map.svg)

## bsskill 解决什么问题

你不需要先学会一套复杂的方法，也不需要知道该调用哪个工具。把当下的业务、材料、选择或卡点交给 `/bss`，它会根据对话上下文选择当前适合的 Skill。

| 真实处境 | 你会得到 |
| --- | --- |
| 客户总说贵，不知道该改价格、产品还是客群 | 商业模式诊断、风险判断和验证动作 |
| 有一个选题，却做不出能被人看完的内容 | 内容方向、开头、标题与逐字稿优化 |
| 知道该做什么，却迟迟推不动 | 对行动卡点的分析和一条可开始的动作 |
| 反复面对同类选择，经验无法积累 | 可回填的决策记录、规律与阶段快照 |
| 文稿、选题、案例散落在多个文件夹 | 可持续维护的内容资产工程 |

## 快速开始

安装完成后，直接在 Agent 中输入：

```text
/bss 我做少儿编程课，已经有 40 个付费学员，但续费率很低。
我需要判断问题出在产品、定价，还是我找错了客户。
```

`/bss` 会读取当前对话信息，选择合适的分析路径。完成一轮后，继续补充新的事实或反馈，再输入 `/bss`，它会判断当前该推进什么。

已经知道需求时，可以直接调用具体 Skill：

```text
/bss-diagnosis 我做面向宝妈的收纳咨询，客户总觉得贵。我该调整什么？
/bss-content 我想讲"普通人别急着做个人 IP"，这个选题怎样做成内容？
/bss-hook 这是我短视频前 20 秒的逐字稿，帮我优化开头：……
/bss-benchmark 我想研究企业服务内容账号，应该找哪些对标？
```

## 能力一览

| 工作目标 | 主要入口 | 常见产出 |
| --- | --- | --- |
| 判断生意、产品、定价与客户 | `/bss-diagnosis` | 商业诊断、风险、验证方案 |
| 找对标并提炼可学习的部分 | `/bss-benchmark` | 对标筛选与研究框架 |
| 做选题、内容、标题与短视频 | `/bss-content`、`/bss-hook`、`/bss-xhs-title` | 内容方向与可发布文案 |
| 检查文稿共鸣、逻辑与传播性 | `/bss-resonate`、`/bss-script-flow`、`/bss-spread` | 修改意见与优先级 |
| 澄清概念、目标和问题 | `/bss-deconstruct`、`/bss-goal`、`/bss-good-question` | 可验证的定义与行动目标 |
| 处理拖延、贪快和行动受阻 | `/bss-action`、`/bss-slowisfast` | 卡点分析与下一步动作 |
| 记录、复盘长期决策 | `/bss-decision`、`/bss-save`、`/bss-restore`、`/bss-report` | 本地决策档案与报告 |
| 建立内容资产与多端 Agent 工作台 | `/bss-content-system`、`/bss-agent-migration`、`/bss-bridge` | 本地工程、主题地图与桥接方案 |
| 审查本地 Skill 风险 | `/bss-skill-cleaner` | 风险报告与确认后的隔离操作 |
| **销售跟进** | `/bss-sales-followup` | 客户开拓、需求挖掘、报价谈判、签约转化、客户留存 |
| **客户成功** | `/bss-customer-success` | 客户 onboarding、问题排查、满意度提升、续约增购 |
| **售前方案** | `/bss-pre-sales-solution` | 客户需求分析、方案撰写、POC 测试、竞标 |

完整的 31 个 Skill、适用时机、输入示例和常见衔接方式，见 [新手入门与 Skill 全目录](docs/新手入门.md#skill-全目录)。

## 业务 Skill 快速入门

业务 Skill 覆盖销售跟进、客户成功、售前方案三个场景，通过原子知识库沉淀团队经验。

详细使用说明见 [业务 Skill 快速入门](docs/business-skill-quickstart.md)。

快速开始：

```bash
# 录入第一条经验
python3 tools/add-business-atom.py \
  --knowledge "客户主动询价后的24小时内响应，转化率最高" \
  --type case \
  --topics "销售跟进,客户开拓" \
  --skills "bss-sales-followup"
```

## 安装

### 豆包、WorkBuddy、Codex 与其他支持 Skills 的 Agent

安装全部 Skill（商业诊断 + 业务）：

```bash
npx -y skills add Bensheh67/BenShehskill -g --all
```

安装后回到 Agent，输入 `/bss 新手入门` 即可开始。

### Claude Code 插件市场

```bash
claude plugin marketplace add Bensheh67/BenShehskill
claude plugin install bss@BenShehskill
```

![Claude Code 插件安装演示](demo.gif)

### 更新

已安装 bsskill 时，直接对当前 Agent 说：

```text
更新 bsskill
```

它会同步官方 BenShehskill，不会修改你在 `~/.bss/` 中的存档、报告和决策记录。版本变化见 [GitHub Releases](https://github.com/Bensheh67/BenShehskill/releases)。

## bsskill 怎样工作

```text
真实任务
   ↓
/bss 读取上下文并选择当前入口
   ↓
一个 Skill 完成诊断、产出或记录
   ↓
补充结果与反馈，再决定下一步
```

bsskill 的重点是推进眼前真实的任务。它会先处理当前最有价值的结点，再根据实际结果衔接后续工作。

## 知识库与本地记录

仓库公开了 4,176 条结构化知识原子、按 Skill 整理的方法论文档与高频概念词典。

- 想查看数据范围和字段，阅读 [原子库说明](知识库/原子库/README.md)。
- 想构建自己的 RAG，可使用 `知识库/原子库/atoms.jsonl`。
- 想了解各项方法，浏览 [Skill 知识包](知识库/Skill知识包)。
- 想跨对话保留工作，使用 `/bss-save`、`/bss-restore` 与 `/bss-report`。数据默认保存在用户本机的 `~/.bss/`。

![dbskill 知识来源图](docs/knowledge-pipeline.svg)

## 项目结构

```text
bsskill/
├── skills/                  # 31 个正式发布的 Skills（27 商业诊断 + 4 业务）
├── 知识库/                   # 知识原子、方法论文档与概念词典
│   ├── 原子库/              # 原原子库（4176 条推文知识）
│   └── 业务原子库/          # 业务原子库（团队经验沉淀）
├── docs/                    # 新手入门、图示与演示素材
├── .claude-plugin/          # Claude Code 插件市场定义
└── tools/                   # 构建与维护脚本
```

本地构建发布包：

```bash
bash tools/build-skills.sh
```

构建产物位于 `dist/skills/`；名称带 `beta` 的本地试验 Skill 不会进入发布包。

## 许可证

本项目采用 [CC BY-NC 4.0](LICENSE) 许可证。

- 个人使用、学习、研究与非商业项目可以直接使用。
- 公开发布衍生作品时，请注明来源。
- 商业用途需要单独授权，请联系作者。
