# bsskill

[简体中文](README.md) | [English](README.en.md) | 日本語 | [한국어](README.ko.md) | [繁體中文](README.zh-TW.md)

> 起業家とコンテンツ制作者のための中国語 AI Skills ツールキット。ビジネス、コンテンツ、実行に関する現実の課題を Agent に渡し、明確な判断と次の具体的な行動を得られます。

[![Version](https://img.shields.io/badge/version-2.17.7-111111.svg)](VERSION)
[![Skills](https://img.shields.io/badge/Skills-27-111111.svg)](docs/新手入门.md#skill-全目录)
[![License](https://img.shields.io/badge/license-CC%20BY--NC%204.0-111111.svg)](LICENSE)

**豆包、WorkBuddy、Claude Code、Codex、および Skills に対応する他の Agent で利用できます。**

bsskill は [dontbesilent](https://x.com/dontbesilent) が作成しました。公開投稿 16,152 件から、4,176 件の構造化知識原子と直接呼び出せる 27 の Skills を整理しています。

[クイックスタート](#クイックスタート) · [インストール](#インストール) · [機能](#機能一覧) · [完全ガイド](docs/新手入门.md) · [リリース](https://github.com/dontbesilent2025/bsskill/releases)

![bsskill のルーティング図](docs/skill-link-map.svg)

## bsskill が解決する課題

複雑な方法論を先に学ぶ必要はありません。どのツールを呼び出すかも覚えなくて大丈夫です。現在のビジネス状況、素材、選択、行き詰まりを `/bss` に渡すと、会話の文脈に応じて適切な Skill を選びます。

| 状況 | 得られるもの |
| --- | --- |
| 顧客が高いと言う | ビジネス診断、リスク、検証アクション |
| テーマはあるが視聴されるコンテンツにできない | 方向性、冒頭、タイトル、台本の改善 |
| やるべきことは分かるが進められない | 停滞要因の分析と着手できる行動 |
| 同じ判断を繰り返し、経験が蓄積しない | 意思決定記録、パターン、スナップショット |
| 原稿やテーマ、事例が散らばっている | 維持可能なコンテンツ資産プロジェクト |

## クイックスタート

インストール後、Agent に入力します。

```text
/bss 子ども向けプログラミング教室を運営しています。40 人の有料生徒がいますが、継続率が低いです。
問題が商品、価格、顧客層のどこにあるか判断したいです。
```

`/bss` は会話の情報を読み、適切な進め方を選択します。1 回終えた後に新しい事実やフィードバックを追加し、再度 `/bss` を入力すると次の作業を判断します。

目的が明確な場合は、Skill を直接呼び出せます。

```text
/bss-diagnosis 子育て中の母親向けに片付けコンサルをしています。高いと言われます。何を変えるべきですか？
/bss-content 「普通の人はパーソナルブランド作りを急がない方がよい」という話を、どうコンテンツにしますか？
/bss-hook 動画台本の最初の 20 秒です。冒頭を改善してください：……
/bss-benchmark 法人向けサービスのコンテンツアカウントを研究したいです。どのベンチマークを調べるべきですか？
```

## 機能一覧

| 目的 | 主な Skill | 主な出力 |
| --- | --- | --- |
| ビジネス、商品、価格、顧客を判断する | `/bss-diagnosis` | 診断、リスク、検証計画 |
| 研究対象を探す | `/bss-benchmark` | 対象リストと研究フレーム |
| テーマ、コンテンツ、タイトル、動画を作る | `/bss-content`、`/bss-hook`、`/bss-xhs-title` | 方向性と公開用原稿 |
| 共感、論理、拡散性を確認する | `/bss-resonate`、`/bss-script-flow`、`/bss-spread` | 優先順位付きの修正案 |
| 概念、目標、問いを明確にする | `/bss-deconstruct`、`/bss-goal`、`/bss-good-question` | 検証可能な定義と目標 |
| 先延ばしや実行の停滞を扱う | `/bss-action`、`/bss-slowisfast` | 停滞分析と次の行動 |
| 長期の意思決定を記録・振り返る | `/bss-decision`、`/bss-save`、`/bss-restore`、`/bss-report` | ローカルの記録とレポート |
| コンテンツ資産と複数 Agent の環境を構築する | `/bss-content-system`、`/bss-agent-migration`、`/bss-bridge` | ローカルプロジェクトと連携計画 |
| ローカル Skill のリスクを監査する | `/bss-skill-cleaner` | リスク報告と確認後の隔離 |

27 Skills の全一覧、入力例、使い分けは [完全ガイド](docs/新手入门.md#skill-全目录) を参照してください。

## インストール

### 豆包、WorkBuddy、Codex、その他 Skills 対応 Agent

ターミナルで実行します。

```bash
npx -y skills add dontbesilent2025/bsskill -g --all
```

Agent に戻り、`/bss 新手入门` と入力して始めてください。

### Claude Code マーケットプレイス

```bash
claude plugin marketplace add dontbesilent2025/bsskill
claude plugin install bss@BenShehskill
```

![Claude Code のインストールデモ](demo.gif)

### 更新

現在の Agent に次のように伝えます。

```text
更新 bsskill
```

公式 bsskill を同期します。`~/.bss/` 内の記録、レポート、意思決定データは変更しません。変更内容は [GitHub Releases](https://github.com/dontbesilent2025/bsskill/releases) を参照してください。

## 仕組み

```text
現実のタスク
   ↓
/bss が文脈を読み、現在の入口を選択
   ↓
1 つの Skill が診断、成果物、記録を作成
   ↓
結果とフィードバックを追加して、次の一歩を決める
```

## ナレッジベースとローカル記録

このリポジトリには 4,176 件の構造化知識原子、Skill 別の方法論ドキュメント、頻出概念の用語集が含まれます。

- データ範囲と項目は [原子ライブラリのガイド](知识库/原子库/README.md) を参照してください。
- 独自の RAG には `知识库/原子库/atoms.jsonl` を使用できます。
- 方法論は [Skill ナレッジパック](知识库/Skill知识包) で確認できます。
- 会話をまたいで作業を続けるには `/bss-save`、`/bss-restore`、`/bss-report` を使用します。データは `~/.bss/` にローカル保存されます。

![bsskill の知識パイプライン](docs/knowledge-pipeline.svg)

## プロジェクト構成

```text
bsskill/
├── skills/                  # 公開中の 27 Skills
├── 知识库/                   # 知識原子、方法論、用語集
├── docs/                    # ガイド、図、デモ素材
├── .claude-plugin/          # Claude Code マーケットプレイス定義
└── tools/                   # ビルドと保守スクリプト
```

ローカルで配布パッケージをビルドするには、次を実行します。

```bash
bash tools/build-skills.sh
```

パッケージは `dist/skills/` に作成されます。名前に `beta` を含むローカル実験 Skill は含まれません。


## ライセンス

[CC BY-NC 4.0](LICENSE) を採用しています。

- 個人利用、学習、研究、非商用プロジェクトで利用できます。
- 派生作品を公開する際は、出典を明記してください。
- 商用利用には別途許可が必要です。作者へ連絡してください。
