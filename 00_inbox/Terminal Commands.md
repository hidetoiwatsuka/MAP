---
tags:
  - commands
  - IT
---
ターミナルで使う基本コマンドのリファレンス。macOS / Linux共通。

---

## Navigation

### pwd

現在いるディレクトリのフルパスを表示する。「自分が今どこにいるか」の確認。

```bash
pwd
# /Users/hideto/Desktop/my_app
```

### cd

ディレクトリを移動する。

```bash
cd my_folder        # my_folderに入る
cd ..               # 一つ上の階層に戻る
cd ../..            # 二つ上に戻る
cd ~                # ホームディレクトリに直帰
cd -                # 直前にいたディレクトリに戻る
cd ~/Desktop        # ホームからの絶対パスで移動
```

### ls

現在のディレクトリの中身を一覧表示する。

```bash
ls                  # ファイルとフォルダを表示
ls -l               # 詳細表示（サイズ、日時、権限）
ls -a               # 隠しファイル（ドットファイル）も表示
ls -la              # 両方組み合わせ
ls my_folder        # 指定フォルダの中身を表示
```

---

## File Operations

### touch

空のファイルを作成する。既存ファイルに使うとタイムスタンプだけ更新。

```bash
touch main.rs
touch notes.md
```

### mkdir

ディレクトリを作成する。

```bash
mkdir my_folder               # フォルダ作成
mkdir -p parent/child/grand   # 中間フォルダも一括作成
```

### cp

ファイルやフォルダをコピーする。

```bash
cp file.txt copy.txt          # ファイルコピー
cp -r my_folder backup/       # フォルダごとコピー（-r必須）
```

### mv

ファイルやフォルダを移動する。リネームにも使う。

```bash
mv file.txt ~/Desktop/        # ファイルを移動
mv old_name.rs new_name.rs    # ファイル名変更
mv my_folder/ ~/Documents/    # フォルダを移動
```

### rm

ファイルやフォルダを削除する。ゴミ箱を経由しない。永久削除。

```bash
rm file.txt                   # ファイル削除
rm -r my_folder               # フォルダごと削除
rm -i file.txt                # 確認してから削除
```

Macでゴミ箱に送りたい場合：

```bash
mv file.txt ~/.Trash/
```

---

## Viewing Content

### cat

ファイルの中身を全部表示する。短いファイル向き。

```bash
cat main.rs
```

### less

ファイルの中身をスクロール可能な形で表示する。長いファイル向き。`q`で終了。

```bash
less main.rs
```

### head / tail

ファイルの先頭または末尾だけ表示する。

```bash
head -n 20 main.rs    # 最初の20行
tail -n 20 main.rs    # 最後の20行
```

### wc

ファイルの行数・単語数・バイト数を数える。

```bash
wc main.rs            # 行数 単語数 バイト数
wc -l main.rs         # 行数だけ
```

---

## Search

### find

ファイルやフォルダを名前で検索する。

```bash
find . -name "*.rs"             # 現在地以下の全.rsファイル
find ~/Desktop -name "notes*"   # Desktopからnotes始まりを検索
find . -type d -name "src"      # ディレクトリだけ検索
```

### grep

ファイルの中身をテキスト検索する。

```bash
grep "fn main" main.rs              # main.rsの中で"fn main"を探す
grep -r "TODO" .                     # 現在地以下の全ファイルから再帰検索
grep -rn "error" src/                # 行番号付きで検索
grep -i "hello" file.txt            # 大文字小文字を区別しない
```

---

## System Info

### which

コマンドの実行ファイルがどこにあるか表示する。

```bash
which cargo       # /Users/hideto/.cargo/bin/cargo
which python3     # /usr/bin/python3
```

### echo

テキストを表示する。変数の中身の確認に便利。

```bash
echo "hello"
echo $PATH        # PATH環境変数の中身を表示
echo $HOME        # ホームディレクトリのパス
```

### env

環境変数を一覧表示する。

```bash
env               # 全環境変数
env | grep RUST   # Rust関連の環境変数だけ
```

---

## Process Management

### Ctrl + C

実行中のプロセスを強制終了する。`cargo run`で動いているプログラムを止める時など。

### Ctrl + Z

プロセスを一時停止する。`fg`で再開。

### Ctrl + D

ターミナルセッションを終了する。`exit`と同じ。

---

## Pipes and Redirection

コマンドの出力を別のコマンドの入力にしたり、ファイルに保存したりする。

```bash
ls -la | grep ".rs"           # lsの結果から.rsだけ抽出
cat main.rs | wc -l           # main.rsの行数をカウント
echo "hello" > file.txt       # file.txtに書き込み（上書き）
echo "world" >> file.txt      # file.txtに追記
cargo build 2>&1 | less       # ビルドログをスクロール表示
```

`|`（パイプ）はコマンドの出力を次のコマンドの入力にする — これも[[Functions]]の直列合成。

---

## Permissions

### chmod

ファイルの権限を変更する。

```bash
chmod +x script.sh            # 実行権限を付与
chmod 644 file.txt            # 所有者=読書、他=読のみ
chmod 755 script.sh           # 所有者=全権限、他=読+実行
```

### chown

ファイルの所有者を変更する。

```bash
sudo chown user:group file.txt
```

---

## Package Managers

### Homebrew (macOS)

```bash
brew install <package>        # インストール
brew update                   # Homebrew自体を更新
brew upgrade                  # インストール済みパッケージを更新
brew list                     # インストール済み一覧
brew uninstall <package>      # アンインストール
```

### Cargo (Rust)

```bash
cargo new my_app              # 新規プロジェクト作成
cargo build                   # コンパイル
cargo run                     # コンパイル+実行
cargo build --release         # 最適化ビルド
cargo test                    # テスト実行
cargo add <crate>             # 依存関係を追加
cargo update                  # 依存関係を更新
```

### npm (Node.js)

```bash
npm install <package>         # ローカルインストール
npm install -g <package>      # グローバルインストール
npm list                      # インストール済み一覧
npm uninstall <package>       # アンインストール
```

### pip (Python)

```bash
pip install <package>
pip list
pip uninstall <package>
```

---

## Git Basics

```bash
git init                      # 現在のフォルダをGitリポジトリにする
git clone <url>               # リモートリポジトリをコピー
git status                    # 変更状態を確認
git add .                     # 全変更をステージ
git commit -m "message"       # コミット
git push                      # リモートに送信
git pull                      # リモートから取得
git log --oneline             # コミット履歴を簡潔に表示
git diff                      # 変更内容を表示
```

---

## Useful Shortcuts

|Shortcut|機能|
|---|---|
|Tab|コマンドやパスの自動補完|
|↑ / ↓|コマンド履歴の移動|
|Ctrl + A|行頭に移動|
|Ctrl + E|行末に移動|
|Ctrl + W|直前の単語を削除|
|Ctrl + U|カーソルより前を全削除|
|Ctrl + L|画面クリア（clearと同じ）|
|Ctrl + R|コマンド履歴を検索|

---

## Related Concepts

- [[Functions]] — パイプ（`|`）はまさに関数の直列合成
- [[Learning]] — コマンドも反復で内的関数になる