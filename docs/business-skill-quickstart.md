# 业务 Skill 快速入门

## 概述

业务 Skill 是一套面向一线业务人员的 AI 辅助工具，通过原子知识库沉淀团队经验，让每位业务人员都能随时调用经过验证的销售方法、客户成功策略和售前方案技巧。

## 包含三个 Skill

| Skill | 命令 | 覆盖场景 |
|-------|------|---------|
| 销售跟进 | `/sales-followup` | 客户开拓、需求挖掘、报价谈判、签约转化、客户留存 |
| 客户成功 | `/customer-success` | 客户 onboarding、问题排查、满意度提升、续约增购 |
| 售前方案 | `/pre-sales-solution` | 客户需求分析、方案撰写、POC 测试、竞标 |

## 快速开始

### 一线人员使用

1. 遇到业务卡点时，输入对应命令：
   ```
   /sales-followup 客户卡在报价阶段，说太贵了，怎么处理？
   /customer-success 客户活跃度下降了，怎么提升？
   /pre-sales-solution 客户要做 POC，怎么设计测试场景？
   ```

2. Skill 会基于原子知识库中的案例和方法论，给出诊断和下一步建议。

### 知识管理员录入

1. **单条录入**（会议后随时新增）：
   ```bash
   python3 tools/add-business-atom.py \
     --knowledge "销售转化最高的场景是客户主动询价后的24小时内" \
     --type case \
     --topics "销售跟进,客户开拓" \
     --skills "sales-followup" \
     --original "2026-07-14 销售复盘会"
   ```

2. **交互式录入**（批量录入多条）：
   ```bash
   python3 tools/add-business-atom.py --interactive
   ```

3. **查看统计**：
   ```bash
   python3 tools/add-business-atom.py --stats
   ```

## 知识原子录入规范

1. **每次提炼 3-5 条**，不要贪多
2. `knowledge` 必须是**一句话可验证的陈述**，不是描述
3. `type` 优先选 `case`（案例）和 `method`（方法），`principle`（原则）只在反复验证后使用
4. **人工录入节奏**：每日新增 + 随时新增
5. **每周汇总一次**，生成 Skill知识包聚合文档

## 目录结构

```
知识库/
├── 业务原子库/
│   ├── README.md              ← 录入规范说明
│   └── atoms.jsonl            ← 知识原子数据
└── Skill知识包/               ← 按主题聚合的经验文档（待生成）
    ├── sales_跟进方法论.md
    ├── cs_成功策略.md
    └── pre_sales_方案技巧.md

skills/
├── dbs-business/              ← 业务工具箱主入口
│   └── SKILL.md
├── sales-followup/            ← 销售跟进 Skill
│   └── SKILL.md
├── customer-success/          ← 客户成功 Skill
│   └── SKILL.md
└── pre-sales-solution/        ← 售前方案 Skill
    └── SKILL.md

tools/
└── add-business-atom.py       ← 原子录入工具
```

## 下一步

1. 先录入第一批原子（建议 10-20 条）
2. 测试三个 Skill 是否能正常触发
3. 每周定期维护知识库
