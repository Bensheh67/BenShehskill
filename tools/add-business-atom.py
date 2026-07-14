#!/usr/bin/env python3
"""
业务原子库录入工具。

用法：
  # 新增一条原子
  python3 tools/add-business-atom.py --knowledge "销售转化最高的场景是客户主动询价后的24小时内" --type case --topics "销售跟进,客户开拓" --skills "sales-followup" --date 2026-07-14 --original "会议纪要 2026-07-14"

  # 从会议纪要批量导入（交互式）
  python3 tools/add-business-atom.py --interactive

  # 查看当前原子总数
  python3 tools/add-business-atom.py --stats
"""

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[1]
ATOMS_FILE = ROOT_DIR / "知识库" / "业务原子库" / "atoms.jsonl"


def get_next_id() -> str:
    """获取下一个原子 ID。"""
    existing = []
    if ATOMS_FILE.exists():
        with open(ATOMS_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    existing.append(json.loads(line))

    if not existing:
        return "2026Q3_001"

    # 取最大的序号
    max_num = 0
    for atom in existing:
        atom_id = atom.get("id", "")
        try:
            num = int(atom_id.split("_")[1])
            if num > max_num:
                max_num = num
        except (IndexError, ValueError):
            continue

    quarter = datetime.now().strftime("%YQ%d")
    return f"{quarter}_{max_num + 1:03d}"


def add_atom(knowledge: str, atom_type: str, topics: list, skills: list,
             original: str = "", url: str = "", date: str = None,
             confidence: str = "medium", quiet: bool = False):
    """添加一条知识原子。"""
    if not date:
        date = datetime.now().strftime("%Y-%m-%d")

    atom = {
        "id": get_next_id(),
        "knowledge": knowledge,
        "original": original,
        "url": url,
        "date": date,
        "topics": topics,
        "skills": skills,
        "type": atom_type,
        "confidence": confidence,
    }

    ATOMS_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(ATOMS_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(atom, ensure_ascii=False) + "\n")

    if not quiet:
        print(f"已添加原子: {atom['id']}")
        print(f"  知识: {knowledge}")
        print(f"  类型: {atom_type}")
        print(f"  主题: {', '.join(topics)}")
        print(f"  关联: {', '.join(skills)}")

    return atom


def interactive_add():
    """交互式录入模式。"""
    print("=== 业务原子库录入 ===")
    print("输入 'quit' 退出，输入 'skip' 跳过当前条目\n")

    while True:
        knowledge = input("1. 知识原子（一句话陈述）: ").strip()
        if knowledge in ("quit", "skip"):
            if knowledge == "quit":
                print("录入结束。")
                break
            continue

        if not knowledge:
            print("知识原子不能为空，请重新输入。\n")
            continue

        atom_type = input("2. 类型 [case/method/principle/anti-pattern/insight] (默认 case): ").strip()
        if not atom_type:
            atom_type = "case"

        topics_input = input("3. 主题分类（逗号分隔，如：销售跟进,客户开拓）: ").strip()
        topics = [t.strip() for t in topics_input.split(",") if t.strip()] if topics_input else []

        skills_input = input("4. 关联 Skill（逗号分隔，如：sales-followup,pre-sales-solution）: ").strip()
        skills = [s.strip() for s in skills_input.split(",") if s.strip()] if skills_input else []

        original = input("5. 原始材料摘录（可选）: ").strip()

        date = input("6. 日期（YYYY-MM-DD，留空用今天）: ").strip()
        if not date:
            date = datetime.now().strftime("%Y-%m-%d")

        confidence = input("7. 置信度 [high/medium/low] (默认 medium): ").strip()
        if not confidence:
            confidence = "medium"

        add_atom(
            knowledge=knowledge,
            atom_type=atom_type,
            topics=topics,
            skills=skills,
            original=original,
            date=date,
            confidence=confidence,
        )
        print()


def show_stats():
    """显示原子库统计信息。"""
    if not ATOMS_FILE.exists():
        print("原子库为空。")
        return

    atoms = []
    with open(ATOMS_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                atoms.append(json.loads(line))

    total = len(atoms)
    print(f"=== 业务原子库统计 ===")
    print(f"总原子数: {total}")

    if not atoms:
        return

    # 按类型统计
    type_count = {}
    for atom in atoms:
        t = atom.get("type", "unknown")
        type_count[t] = type_count.get(t, 0) + 1

    print("\n按类型分布:")
    for t, count in sorted(type_count.items()):
        print(f"  {t}: {count}")

    # 按主题统计
    topic_count = {}
    for atom in atoms:
        for topic in atom.get("topics", []):
            topic_count[topic] = topic_count.get(topic, 0) + 1

    print("\n按主题分布:")
    for topic, count in sorted(topic_count.items(), key=lambda x: -x[1]):
        print(f"  {topic}: {count}")

    # 按 Skill 统计
    skill_count = {}
    for atom in atoms:
        for skill in atom.get("skills", []):
            skill_count[skill] = skill_count.get(skill, 0) + 1

    print("\n按 Skill 分布:")
    for skill, count in sorted(skill_count.items(), key=lambda x: -x[1]):
        print(f"  {skill}: {count}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--knowledge", help="知识原子（一句话陈述）")
    parser.add_argument("--type", dest="atom_type", default="case",
                        choices=["case", "method", "principle", "anti-pattern", "insight", "tool"],
                        help="原子类型")
    parser.add_argument("--topics", help="主题分类，逗号分隔")
    parser.add_argument("--skills", help="关联 Skill，逗号分隔")
    parser.add_argument("--original", help="原始材料摘录")
    parser.add_argument("--url", help="来源链接")
    parser.add_argument("--date", help="日期 YYYY-MM-DD")
    parser.add_argument("--confidence", default="medium", choices=["high", "medium", "low"])
    parser.add_argument("--interactive", action="store_true", help="交互式录入")
    parser.add_argument("--stats", action="store_true", help="显示统计信息")
    parser.add_argument("--quiet", action="store_true", help="静默模式")

    args = parser.parse_args()

    if args.interactive:
        interactive_add()
    elif args.stats:
        show_stats()
    elif args.knowledge:
        topics = [t.strip() for t in args.topics.split(",") if t.strip()] if args.topics else []
        skills = [s.strip() for s in args.skills.split(",") if s.strip()] if args.skills else []
        add_atom(
            knowledge=args.knowledge,
            atom_type=args.atom_type,
            topics=topics,
            skills=skills,
            original=args.original or "",
            url=args.url or "",
            date=args.date,
            confidence=args.confidence,
            quiet=args.quiet,
        )
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
