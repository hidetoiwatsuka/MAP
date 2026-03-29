---
tags:
  - topiclist
---
# Hacker Curriculum — RE/Security 要塞構築計画 v3

## Overview

|Phase|Period|Goal|
|---|---|---|
|Phase 1|Now – Dec 2025 (9ヶ月)|C言語 + Linux基礎 + 最初のCTF|
|Phase 2|Jan 2026 – Sep 2026 (9ヶ月)|バイナリ解析 + Exploit基礎|
|Phase 3|Oct 2026 – Sep 2027 (12ヶ月)|ネットワーク + 暗号 + 実戦CTF|
|Phase 4|Oct 2027 –|応用: 医療機器セキュリティ / body-sim復活 / 独自ツール開発|

**使う言語は3つだけ:**

- **C** — 解析対象の母国語。Phase 1からメイン
- **x86-64アセンブリ** — バイナリを読む目。Phase 2から
- **Python** — exploit・自動化・CTFツール。Phase 2から必要に応じて

**設計原則:**

- 毎フェーズで「作る」と「壊す」を並行する（コードを書く＋他人のコードを解析する）
- CTFを継続的な学習エンジンとして使う（ドーパミン供給源）
- body-simはPhase 4で復活。その時の自分が最適な言語を選ぶ
- **学期中は週3–5時間。休暇中に集中ブースト。週数は目安であって締切ではない。**
- **理解が追いついていないのに次に進まない。特にポインタとスタックフレームは何週間かかってもいい。**

---

## Phase 1: C + Linux + 最初のCTF (Now – Dec 2025)

### 目標

- Cで「メモリの中で何が起きているか」が見える状態になる
- Linuxのコマンドライン操作が無意識レベルになる
- CTFの簡単な問題を自力で解ける

### Block A: C言語基礎 (8–12 weeks)

ゼロ前提。焦らない。各ステップが体に入ってから次に進む。

#### ステージ1: まずコードが動く (3–4 weeks)

| Week | Topic               | やること                                                                 | なぜ必要か              |
| ---- | ------------------- | -------------------------------------------------------------------- | ------------------ |
| 1    | [[環境構築 + 最初のプログラム]] | gcc をセットアップ。`printf` で文字列と数値を表示。`int`, `float`, `char` の違い           | ここが全ての出発点          |
| 2    | [[変数と制御構文]]         | `if`/`else`, `for`, `while`, `switch`。簡単な計算プログラム（摂氏⇔華氏変換、FizzBuzzなど） | 分岐と繰り返し = プログラムの骨格 |
| 3    | 関数                  | 自分で関数を定義して呼ぶ。引数と戻り値。プロトタイプ宣言。スコープ                                    | コードを分割する力          |
| 3–4  | 配列                  | `int arr[10]`, ループで配列を操作、簡単なソート（バブルソート）                              | メモリ上に並んだデータを扱う感覚   |

**ステージ1の確認テスト:** FizzBuzzを自力で書ける。関数に配列を渡して中身を変更できる。ここがクリアできたら次へ。

#### ステージ2: ポインタ — ここが山 (3–4 weeks)

|Week|Topic|やること|なぜ必要か|
|---|---|---|---|
|5|ポインタ入門|`int *p = &x;` の意味を図に描く。`*`と`&`の違い。ポインタ経由で値を書き換える|REの全てはポインタの理解の上に建つ|
|6|ポインタと配列|配列名がポインタであること。ポインタ演算 (`p+1`)。文字列 = `char*`|Cの文字列操作の前提|
|7|動的メモリ|`malloc`/`free`。スタック vs ヒープの図を自分で描く。メモリリークを意図的に作って観察|バッファオーバーフローの前提知識|
|7–8|文字列操作|`strcpy`, `strcmp`, `strlen` を**自作実装**してから標準ライブラリ版と比較|「なぜバッファオーバーフローが起きるか」を体感する|

**ステージ2の確認テスト:** `char *` で文字列を動的確保し、コピーし、解放できる。segfaultが出た時に「なぜか」を説明できる。

#### ステージ3: 構造化 (2–4 weeks)

|Week|Topic|やること|なぜ必要か|
|---|---|---|---|
|9|構造体|`struct`, `typedef`, 構造体のポインタ (`struct Node *`)|データ構造の基礎|
|10|ファイルI/O|`fopen`/`fread`/`fwrite`, テキストファイルとバイナリファイルの読み書き|ファイルフォーマット解析の第一歩|
|11–12|まとめプロジェクト|下のミニプロジェクトから1つ選んで完走する|学んだことの統合|

**各週の裏課題:** 書いたCプログラムを `gcc -S` でアセンブリ出力し、自分のコードがどう変換されるか**眺めるだけでいい**。理解できなくて正常。Phase 2で読めるようになる。

#### Phase 1 ミニプロジェクト候補（1つ選んで完走する）

- [ ] 簡易wc — ファイルの行数・単語数・バイト数を数える
- [ ] XOR暗号ツール — ファイルをXORで暗号化/復号する
- [ ] 学生成績管理 — 構造体の配列で学生データを管理、ファイルに保存/読み込み
- [ ] 簡易電卓 — 標準入力から式を読んで計算結果を返す

### Block B: Linux深掘り (Block Aと並行して進める)

|Topic|やること|なぜ必要か|
|---|---|---|
|ファイルシステム|`/proc`, `/sys`, パーミッション, シンボリックリンク|システムの内部構造を知る|
|プロセス管理|`ps`, `top`, `strace`, `ltrace`, `/proc/[pid]/maps`|実行中のプログラムの内部を覗く第一歩|
|ネットワーク基礎|`netstat`, `ss`, `curl`, `nc` (netcat), `tcpdump`|Phase 3のネットワーク解析の下地|
|シェルスクリプト|bash scripting, パイプ, リダイレクト, `grep`/`sed`/`awk`|自動化 + CTFで頻繁に使う|
|権限とセキュリティ|`chmod`, `chown`, SUID/SGID, capabilities|権限昇格の前提知識|

**実践:** OverTheWire Bandit (全34レベル) を完走する。これがLinuxの基礎体力テスト。

### Block C: 最初のCTF (Block A ステージ2以降から並行)

Block Aステージ1の間はCTFに手を出さなくていい。まずCが最低限動くようになってから。

|Platform|何をやるか|目標|
|---|---|---|
|OverTheWire Bandit|Linux基礎 + シェル操作|全レベルクリア|
|OverTheWire Narnia|簡単なバッファオーバーフロー|Level 0–3 (Phase 1では無理なら0–1でもOK)|
|picoCTF|General Skills + Cryptography (Easy)|15問以上|
|CryptoHack|暗号の基礎（XOR, Base64）|Introduction完了|

---

## Phase 2: バイナリ解析 + Exploit基礎 (Jan 2026 – Sep 2026)

### 前提

Phase 1でCの基礎が体に入っていること。ポインタ、malloc/free、構造体が「考えなくても書ける」状態。

### 目標

- x86-64アセンブリが「読める」状態になる
- Ghidra/IDAでバイナリを開いて構造を把握できる
- ELFバイナリの内部構造を理解する
- 基本的なexploit (stack overflow, format string) を書ける
- Pythonでexploitスクリプトを書ける

### Block D: x86-64 アセンブリ (8 weeks)

|Week|Topic|やること|なぜ必要か|
|---|---|---|---|
|1–2|レジスタとデータ移動|汎用レジスタ (rax–r15), `mov`, `lea`, メモリアドレッシング。自分のCプログラムを`objdump -d`して見比べる|全ての逆アセンブリ出力の基本単位|
|3|算術・論理演算 + フラグ|`add`, `sub`, `xor`, `and`, `cmp`, `test`, EFLAGS|条件分岐の理解|
|4|制御フロー|`jmp`, `je/jne/jg/jl`, `call`, `ret`, ループ構造。Cのif/for/whileが逆アセンブリでどう見えるか|逆アセンブリからif/for/whileを復元する|
|5–6|スタックフレームと関数呼び出し|`push`, `pop`, `rbp`/`rsp`, calling convention (System V AMD64), 引数渡し (rdi, rsi, rdx, rcx, r8, r9), 戻り値 (rax)|**関数呼び出しの理解 = REの核心技術。ここは2週間かける**|
|7–8|NASMで小プログラム + まとめ|Hello World, 簡単な計算, syscall直打ち。Phase 1のCプログラムを全部`objdump -d`して復習|「アセンブリで書ける」→「逆アセンブリが怖くなくなる」|

### Block E: ELFとリンカ (4 weeks)

|Week|Topic|やること|なぜ必要か|
|---|---|---|---|
|1–2|ELFフォーマット|ELFヘッダ, セクション (.text, .data, .bss, .rodata), セグメント。`readelf`, `objdump` を使い倒す|バイナリの「地図」が読める|
|3|動的リンク|PLT/GOT, `ld-linux.so`, `ldd`|GOT overwrite攻撃の前提|
|4|ローダとメモリレイアウト|仮想メモリ, `mmap`, ASLR, PIE, stack canary|exploit緩和技術の理解|

### Block F: リバースエンジニアリング実践 (8 weeks)

|Week|Topic|やること|なぜ必要か|
|---|---|---|---|
|1–2|Ghidra入門|自分のCプログラムをGhidraで開く → デコンパイル結果と元コードを比較|ツールの使い方 + 「翻訳」の感覚|
|3–4|Static analysis|ストリップされたバイナリの解析, 関数の特定, データ構造の復元|CTFのreversing問題の基本スキル|
|5–6|Dynamic analysis|`gdb` + `pwndbg`/`gef`, ブレークポイント, メモリ検査, `strace`/`ltrace`|実行時の挙動を追跡する|
|7–8|crackme練習|crackmes.one の Level 1–3, CTF reversing問題 (picoCTF, CSAW)|**実戦で全スキルを統合**|

### Block G: Exploit基礎 + Python導入 (8 weeks)

Pythonはここで初めて登場する。exploitスクリプトを書くために必要な分だけ学ぶ。

|Week|Topic|やること|なぜ必要か|
|---|---|---|---|
|1–2|Python最低限|変数, リスト, ループ, 関数, ファイルI/O, `struct`モジュール (バイト列操作)。**Cが分かっている状態で学ぶから速い**|pwntools を使うための前提|
|3–4|Stack buffer overflow|ret2winの基本パターン, セキュリティ機構なしの環境で練習。`pwntools`でexploitスクリプトを書く|exploit の「Hello World」|
|5–6|Shellcode|NOP sled, shellcode injection, `execve` syscall|コード実行の原理|
|7–8|Format string|`%x`, `%n` を使った情報リーク + 書き込み|メモリ読み書きの別経路|

---

## Phase 3: ネットワーク + 暗号 + 実戦CTF (Oct 2026 – Sep 2027)

### 目標

- ネットワークプロトコルをパケットレベルで理解する
- 暗号の実装と攻撃手法を知る
- CTFで中級レベルの問題を安定して解ける
- ROP含む現代のexploit手法を使える
- 自作ツールが1つ完成している
- 「要塞」の輪郭が見える

### Block H: ネットワーク深層 (8 weeks)

|Week|Topic|やること|なぜ必要か|
|---|---|---|---|
|1|TCP/IPスタック|OSIモデルを実感するため、Wiresharkで自分の通信を全部見る|全ネットワークセキュリティの基盤|
|2|TCP詳細|3-way handshake, シーケンス番号, ウィンドウ, `RST`/`FIN`|TCP攻撃の前提|
|3|DNS|クエリ/レスポンスの構造, DNS spoofing の原理|名前解決の脆弱性|
|4|HTTP/HTTPS|リクエスト/レスポンスの生パケット, TLSハンドシェイクの概要|Web系CTFの基礎|
|5–6|Wireshark + pcap解析|CTFのforensics問題 (pcap解析), フィルタリング, 抽出|パケットの中身を「読める」状態|
|7–8|ネットワークプログラミング|Cでソケットプログラミング (TCP client/server), raw socket|パケットを「作れる」状態|

### Block I: 高度Exploit + ROP (6 weeks)

|Week|Topic|やること|なぜ必要か|
|---|---|---|---|
|1–2|Phase 2復習 + ASLR/PIE bypass|情報リーク手法, GOT overwrite|現代のexploit環境への適応|
|3–4|ROP (Return-Oriented Programming)|gadget探索 (`ropper`/`ROPgadget`), chain構築, ret2libc|**現代のexploitの核心技術**|
|5–6|Heap exploitation入門|Use-after-free, double free, tcache poisoning の概念|CTF中級〜上級のpwnで必須|

### Block J: 暗号 (6 weeks)

|Week|Topic|やること|なぜ必要か|
|---|---|---|---|
|1|古典暗号 + XOR|Caesar, Vigenère, XOR暗号, 頻度分析|暗号的思考の入口|
|2|ブロック暗号|AES (構造の理解), ECB vs CBC, padding oracle|最も多いCTF暗号問題|
|3|ストリーム暗号|RC4の構造, nonce reuse攻撃|プロトコルの脆弱性|
|4|ハッシュ|SHA-256, MD5, length extension attack, rainbow table|パスワードクラッキングの原理|
|5|公開鍵暗号|RSA (数学から), 小さい指数攻撃, Wiener's attack|CTFのcrypto定番|
|6|TLS/PKI|証明書, CA, ハンドシェイクの詳細|実世界のセキュリティ|

**実践:** CryptoHack全セクション + CTFのcrypto問題

### Block K: Web Security 基礎 (4 weeks)

|Week|Topic|やること|なぜ必要か|
|---|---|---|---|
|1|SQLi|SQL injection (UNION-based, blind), `sqlmap`|最も古典的なWeb脆弱性|
|2|XSS|Reflected, Stored, DOM-based XSS|ブラウザセキュリティの基礎|
|3|認証・セッション|Cookie, JWT, CSRF, セッション固定|認証の仕組みと壊し方|
|4|SSRF + その他|SSRF, XXE, ディレクトリトラバーサル|サーバーサイドの脆弱性|

**実践:** PortSwigger Web Security Academy (無料)

### Block L: 自作ツール (Phase 3後半、並行)

**1つ選んで完走する。** 言語はCでもPythonでもいい。全部やろうとしない。

|Project|やること|学べること|
|---|---|---|
|ELFパーサー|ELFフォーマットを手動パース（C推奨）|バイトレベルの操作|
|hexdump|自作hexdumpツール（C推奨）|ファイルI/O, フォーマット出力|
|パケットスニファー|raw socketでパケットをキャプチャして表示（C推奨）|ネットワークプログラミング|
|CTFツール|CTFで繰り返し使う処理を自動化するスクリプト集（Python推奨）|自分の作業を効率化する|
|簡易ポートスキャナー|TCP connect scanを実装（CまたはPython）|ネットワーク + ソケット|

### Block M: 実戦CTF (通年で並行)

|レベル|Platform / CTF|目標|
|---|---|---|
|入門復習|picoCTF 残り|全カテゴリ制覇|
|中級|CTFtime の週末CTF参加|月1回以上参加|
|中級|pwnable.kr / pwnable.tw|Toddler's Bottle → Rookiss|
|フォレンジクス|CyberDefenders, Blue Team Labs|実際のインシデント分析|
|継続|HackTheBox|Easy → Medium マシン|

---

## Phase 4: 応用 — 医療×セキュリティ (Oct 2027 –)

### ここでbody-simが復活する

Phase 1–3で積み上げた「システムの内部が全部見える」能力を、医療領域に持ち込む。

**body-simの言語はこの時点で決める。** C、Python、Rust、あるいは別の何か — Phase 1–3の経験を踏まえて最適なものを選ぶ。今は決めない。

|Project|内容|Phase 1–3のスキルがどう活きるか|
|---|---|---|
|body-sim復活|Physiology + Pharmacologyモデル|低レイヤーの理解, システム設計力|
|医療機器セキュリティ研究|ペースメーカー, インスリンポンプ, 病院ネットワークの脆弱性分析|RE + ネットワーク + プロトコル解析|
|ECGデータ解析ツール|PhysioNetデータの独自パーサー + 異常検出|バイナリパース, 信号処理|
|AF ablation simulator|TDK研究との接続 — 電気生理データの可視化・シミュレーション|全スキルの統合|
|自作セキュリティツール|独自のfuzzer, scanner, または解析ツール|「要塞」の成果物|

---

## 医学との並走ルール

1. **学期中はSemmelweisの授業・試験が最優先。** CTFや開発は空き時間と休暇に。
2. **試験前2週間はIT完全停止。** 切り替えを明確にする。
3. **TDK研究は継続。** AF研究のデータ解析でPython/Rは引き続き使う。これは「IT」ではなく「医学研究ツール」として扱う。
4. **Phase 4でbody-simに戻る時、3年分のPhysiology/Pharmacologyの知識が頭に入っている。** コードに落とす速度は今とは比較にならない。
5. **週数は目安。理解が追いついていないのに次に進まない。** 特にポインタ（Phase 1）とスタックフレーム（Phase 2）は何週間かかってもいい。

---

## 「要塞」の定義 — 到達確認チェックリスト

Phase 3終了時点で以下ができていれば、要塞の基礎は建っている：

- [ ] ストリップされたELFバイナリをGhidraで開いて、主要な関数の動作を説明できる
- [ ] Stack overflow → ROP chainのexploitを自力で書ける
- [ ] Wiresharkでパケットキャプチャを見て、プロトコルの異常を指摘できる
- [ ] RSAの基本的な攻撃 (小さい指数, common modulus) を実装できる
- [ ] HackTheBoxのMediumマシンを自力でrootできる
- [ ] 自作ツールが1つ完成している
- [ ] CTFで中級問題を安定して解けるカテゴリが2つ以上ある
- [ ] Cで低レイヤーのプログラムを書ける
- [ ] Pythonでexploitスクリプトと自動化ツールを書ける

---

## 参考リソース

### 書籍

- **Hacking: The Art of Exploitation** (Jon Erickson) — **Phase 1–2のメイン教材。** C、アセンブリ、ネットワーク、exploitが1冊で繋がる。この本1冊でPhase 1–2の8割をカバーできる。
- **Practical Binary Analysis** (Dennis Andriesse) — ELF, 逆アセンブリ, バイナリ計装
- **Practical Reverse Engineering** (Bruce Dang) — x86, ARM, カーネル
- **The Linux Programming Interface** (Michael Kerrisk) — Linuxシステムプログラミングの聖典
- **Cryptography Engineering** (Ferguson, Schneier, Kohno) — 暗号の実践

### オンライン

- **OverTheWire** (wargames) — bandit, narnia, behemoth
- **picoCTF** — 初心者CTF
- **CryptoHack** — 暗号
- **pwnable.kr / .tw** — バイナリexploit
- **HackTheBox** — 実践ラボ
- **PortSwigger Web Security Academy** — Web脆弱性
- **CTFtime.org** — CTFイベントカレンダー
- **LiveOverflow (YouTube)** — RE/CTFの解説

---

_言語は3つだけ。C, Python, アセンブリ。これで要塞は建つ。_ _body-simは死んでいない。Phase 4で、低レイヤーの目を持った状態で帰ってくる。_