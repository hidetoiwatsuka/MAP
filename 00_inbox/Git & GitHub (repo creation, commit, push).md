---
tags:
  - memo
---
# Git — Version Control from Zero

---

## What Is Git? — Gitとは何か

Git is a system that records every change you make to your files, so you can go back to any previous version at any time.

Think of it as an unlimited undo history — not just for one file, but for an entire project, across days, weeks, and months.

（ファイルに加えたすべての変更を記録し、いつでも任意の過去の状態に戻れるシステム。プロジェクト全体に対する無制限のundo履歴。）

---

## Why It Exists — なぜ存在するか

Without Git:

- You change something and it breaks. You don't remember what you changed.
- You want to try a risky idea but you're afraid of ruining what works.
- You're working with someone else and you both edit the same file. Whose version wins?
- Your laptop dies. Everything is gone.

Git solves all of these.

（Gitがなければ：何を変えたか忘れる、リスクのある変更が怖い、共同作業でファイルが衝突する、PCが壊れたら全部消える。Gitは全部解決する。）

---

## The Mental Model — メンタルモデル

Git tracks your project through a series of **snapshots**. Each snapshot captures the state of every file at a specific moment. You decide when to take a snapshot, and you label it with a message describing what changed.

（Gitはプロジェクトを一連のスナップショットで追跡する。各スナップショットは特定の瞬間のすべてのファイルの状態を捉える。スナップショットを撮るタイミングは自分で決め、何を変えたか説明するメッセージをつける。）

```
Snapshot 3: "Added login feature"
Snapshot 2: "Fixed button color"
Snapshot 1: "Initial project setup"
```

You can jump to any snapshot. You can compare any two snapshots. You can branch off, try something, and come back if it doesn't work.

---

## Core Concepts — 核心概念

### Repository (repo)

A project folder that Git is tracking. Created by `git init` (new project) or `git clone` (copy someone else's project). Inside, Git creates a hidden `.git/` folder where all history is stored.

（Gitが追跡しているプロジェクトフォルダ。`.git/`という隠しフォルダに全履歴が保存される。）

### Commit

A snapshot. One saved state of your project. Each commit has a unique ID, a message, a timestamp, and a record of exactly what changed.

（スナップショット。プロジェクトの保存された状態1つ分。固有のID、メッセージ、タイムスタンプ、変更内容の記録を持つ。）

### Staging Area (Index)

A preparation zone between your working files and a commit. You choose which changes to include in the next snapshot. This lets you make a commit that captures only specific changes, not everything.

（作業ファイルとcommitの間の準備領域。次のスナップショットにどの変更を含めるか選べる。）

### Branch

A parallel timeline. You can branch off from the main line, work on something experimental, and merge it back if it works — or discard it if it doesn't. The main branch is typically called `main`.

（並行するタイムライン。本線から分岐して実験し、うまくいけば合流、だめなら破棄。）

### Remote

A copy of your repository stored on the internet (usually GitHub, GitLab, or Bitbucket). Functions as backup and as a collaboration hub.

（インターネット上のリポジトリのコピー。バックアップと共同作業のハブ。通常はGitHub。）

---

## The Three Zones — 3つのゾーン

Git organizes your files into three zones:

```
Working Directory    →    Staging Area    →    Repository
(作業ディレクトリ)          (ステージング)          (リポジトリ)

  あなたが編集する場所   →   次のcommitに含める    →   確定した履歴
                            変更を選ぶ場所
         
  git add で右へ →              git commit で右へ →
```

A file moves through these zones:

1. You edit a file → it's modified in the **Working Directory**
2. You `git add` it → it moves to the **Staging Area**
3. You `git commit` → it's permanently recorded in the **Repository**

---

## Essential Commands — 基本コマンド

### Setup

```bash
git config --global user.name "Your Name"       # Gitに名前を登録
git config --global user.email "you@email.com"   # メールアドレスを登録
```

These are attached to every commit you make. Do this once.

### Starting a Project

```bash
git init                  # 現在のフォルダをGitリポジトリにする
git clone <url>           # 既存のリモートリポジトリをコピーして持ってくる
```

### The Core Loop

This is what you'll do every day:

```bash
# 1. 状態を確認
git status                # 何が変更されたか確認

# 2. 変更をステージング
git add main.rs           # 特定のファイルをステージ
git add .                 # 全変更をステージ

# 3. コミット（スナップショットを撮る）
git commit -m "describe what you changed"

# 4. 必要に応じて繰り返す
```

That's it. `status` → `add` → `commit`. This is 90% of Git.

（これがGitの90%。status → add → commit の繰り返し。）

### Viewing History

```bash
git log                   # コミット履歴を表示（詳細）
git log --oneline         # 一行ずつ簡潔に表示
git diff                  # まだステージしてない変更を表示
git diff --staged         # ステージ済みだがコミットしてない変更を表示
```

### Undoing Things

```bash
git checkout -- file.txt  # ファイルを最後のcommitの状態に戻す（変更を破棄）
git reset HEAD file.txt   # ステージングを取り消す（ファイルは変更されたまま）
git revert <commit-id>    # 特定のcommitを打ち消す新しいcommitを作る
```

---

## Working with GitHub — GitHubとの連携

GitHub is not Git. Git is the local tool. GitHub is a website that hosts remote copies of Git repositories.

（GitHubはGitではない。Gitはローカルツール。GitHubはリモートコピーをホストするウェブサイト。）

### Connecting to GitHub

```bash
# 新しいリポジトリをGitHubに作った後：
git remote add origin https://github.com/username/repo.git
git push -u origin main
```

### Daily Sync

```bash
git push                  # ローカルのcommitをGitHubに送信
git pull                  # GitHubの変更をローカルに取得
```

### The Flow

```
ローカルPC                          GitHub
    │                                  │
    │  git push ──────────────────→    │  バックアップ
    │                                  │  他の人が見れる
    │  git pull  ←──────────────────   │  他の人の変更を取得
    │                                  │
```

---

## Branches — ブランチ

Branches let you work on something without affecting the main codebase. When you're done, you merge it back.

（ブランチはメインのコードに影響を与えずに作業する手段。完成したら合流。）

```bash
git branch                     # ブランチ一覧を表示
git branch feature-login       # 新しいブランチを作成
git checkout feature-login     # そのブランチに切り替え
git checkout -b feature-login  # 作成と切り替えを同時に

# 作業してcommitする...

git checkout main              # mainブランチに戻る
git merge feature-login        # feature-loginの変更をmainに統合
git branch -d feature-login    # 統合済みのブランチを削除
```

Visual model:

```
main:     ──①──②──③──────────⑥──
                  \            /
feature:           ──④──⑤──
```

③で分岐。④⑤で実験。⑥でmainに合流（merge）。

---

## .gitignore

A file that tells Git "don't track these." Any filename or pattern listed here is invisible to Git.

（Gitに「これらは追跡するな」と伝えるファイル。）

```gitignore
/target          # Rustのビルド出力
node_modules/    # npmの依存パッケージ
.env             # パスワードやAPIキーが入った設定ファイル
*.log            # すべてのログファイル
.DS_Store        # macOSが自動生成するファイル
```

Rule of thumb: if it can be regenerated or contains secrets, put it in `.gitignore`.

（再生成可能なもの、秘密情報を含むものは`.gitignore`に入れる。）

---

## Common Workflow — 実践的なワークフロー

A typical session:

```bash
cd ~/projects/my_app          # プロジェクトに移動
git status                    # 状態確認
# コードを書く...
git status                    # 何が変わったか確認
git add .                     # 全変更をステージ
git commit -m "Add user input validation"
git push                      # GitHubにバックアップ
```

How often to commit: whenever you complete a small, coherent piece of work. Not every line change, not after 3 days of work. Think of it as "one commit = one thought."

（commitの頻度：小さくまとまった作業が完了するたび。1行ごとではなく、3日分まとめてでもなく。「1 commit = 1つの思考」。）

---

## Mistakes and Recovery — ミスとリカバリー

Git is designed to be forgiving. Almost nothing is truly irreversible.

|Situation|Command|
|---|---|
|コミットメッセージを間違えた|`git commit --amend -m "new message"`|
|addを取り消したい|`git reset HEAD file.txt`|
|ファイルを最後のcommitに戻したい|`git checkout -- file.txt`|
|直前のcommitを取り消したい|`git revert HEAD`|
|全部壊してやり直したい|`git log --oneline`で戻りたい地点を見つけて`git reset --hard <commit-id>`|

`git reset --hard`は本当に変更を消すから注意。それ以外はほぼ安全。

---

## Git as a Function — 関数としてのGit

Git itself is a function:

$$f(\text{project state at time } t) \xrightarrow{\text{commit}} \text{recorded snapshot}$$

And the entire commit history is an integration — the accumulated sum of every change over time:

$$\text{Current project} = \int_{0}^{n} \text{commit}_i$$

`git diff` is differentiation — "what changed between two states?" `git log` is the integral — "what is the total accumulated history?"

（`git diff`は微分 — 「2つの状態間で何が変わったか？」。`git log`は積分 — 「累積された全履歴は何か？」）


finder での path の確認方法。
```
otion + 右クリック
```

---

## Related Concepts

- [Functions](Functions.md) — Git commands as input-output transformations
- [Terminal Commands](Terminal%20Commands.md) — Git runs in the terminal
- [Learning](Learning.md) — commit history is externalized learning — making the invisible visible

