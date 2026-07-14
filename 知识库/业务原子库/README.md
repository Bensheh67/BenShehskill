# 业务原子库说明

## 数据来源

- 团队会议记录
- 销售跟进复盘
- 客户成功案例
- 售前方案文档
- 业务方法论沉淀

## 字段说明

| 字段 | 类型 | 说明 |
|------|------|------|
| id | string | 格式：{季度}_{序号}，如 2026Q3_001 |
| knowledge | string | 提炼后的知识点陈述句（一句话可验证） |
| original | string | 原始材料摘录（会议记录/文档片段） |
| url | string | 来源链接（可选） |
| date | string | 录入日期 |
| topics | string[] | 主题分类（见下方分类体系） |
| skills | string[] | 关联 Skill |
| type | string | principle / method / case / anti-pattern / insight / tool |
| confidence | string | high / medium / low |

## 主题分类体系

| 分类 | 说明 | 归属 Skill |
|------|------|------------|
| 销售跟进 | 客户开拓、需求挖掘、报价谈判、签约转化、客户留存 | /sales-followup |
| 客户成功 | 客户 onboarding、问题排查、满意度提升、续约增购 | /customer-success |
| 售前方案 | 客户需求分析、方案撰写、POC 测试、竞标 | /pre-sales-solution |

## 文件结构

- `atoms.jsonl` — 全量合并
- `atoms_{季度}.jsonl` — 按季度拆分
- `atoms_{季度}_{分类}.jsonl` — 按季度+分类拆分（可选）

## 录入规范

1. 每次提炼 3-5 条，不要贪多
2. `knowledge` 必须是**一句话可验证的陈述**，不是描述
3. `type` 优先选 `case`（案例）和 `method`（方法），`principle`（原则）只在反复验证后使用
4. 人工录入节奏：每日新增 + 随时新增
5. 每周汇总一次，生成 Skill知识包聚合文档
