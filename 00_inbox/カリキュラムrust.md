#rust #medicine #IT 
# Rust 前提知識ゼロからのカリキュラム

**目標：医学×Rustプロジェクトを自分でゼロから書けるようになる**

> このカリキュラムは「理解する」ためではなく「書けるようになる」ために設計されている。
> 各週に必ず手を動かすタスクがある。読むだけでは絶対に進めないこと。

-----

## カリキュラム全体像

|フェーズ|期間        |テーマ                  |ゴール                    |
|----|----------|---------------------|-----------------------|
|0   |Week 0    |環境構築                 |`cargo run` が通る        |
|1   |Week 1–2  |プログラミング基礎            |変数・関数・ループを自分で書ける       |
|2   |Week 3–4  |Rustの型システム           |struct・enum・implを使いこなせる|
|3   |Week 5–6  |Ownership & Borrowing|コンパイラエラーを読んで直せる        |
|4   |Week 7–8  |Trait・エラー処理          |複数の型に共通の振る舞いを定義できる     |
|5   |Week 9–10 |数値計算・ファイルI/O         |CSVに出力してグラフを確認できる      |
|6   |Week 11–12|最初の生理学モデル            |受動膜モデルが動く              |

**ルール**

- 1日30分でいい。毎日続けることが最優先。
- エラーが出たら喜ぶ。Rustのエラーメッセージは親切なので読む。
- 「理解してから書く」ではなく「書きながら理解する」。
- Google・ChatGPT・Claude は使っていい。ただし答えを貼るだけにしない。理解してから自分で書き直す。

-----

## Phase 0 — 環境構築

**期間：** Day 1（1–2時間で終わる）

### やること

#### 1. Rustをインストール

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

インストール後：

```bash
rustc --version   # バージョンが表示されればOK
cargo --version   # cargoはRustのビルドツール兼パッケージマネージャ
```

#### 2. VS Codeのセットアップ

拡張機能 `rust-analyzer` をインストールする。これがないとRustは書けない（エラーがリアルタイムで表示される）。

#### 3. 最初のプロジェクトを作る

```bash
cargo new hello_rust
cd hello_rust
cargo run
```

`Hello, world!` が表示されたらPhase 0完了。

### ファイル構造を確認する

```
hello_rust/
├── Cargo.toml    ← プロジェクトの設定ファイル（依存crateもここに書く）
└── src/
    └── main.rs   ← コードはここに書く
```

`src/main.rs` を開くと：

```rust
fn main() {
    println!("Hello, world!");
}
```

`fn main()` がプログラムのエントリーポイント。プログラムはここから始まる。

-----

## Phase 1 — プログラミング基礎

**期間：** Week 1–2
**参考：** The Rust Book Ch. 1–6（https://doc.rust-lang.org/book/）

### Week 1：変数・型・関数

#### 概念：変数

```rust
fn main() {
    let voltage = -65.0;          // f64（小数）として推論される
    let voltage: f64 = -65.0;     // 型を明示する書き方
    let mut v = -65.0;            // mutをつけると変更できる
    v = v + 1.0;                  // mutがないとコンパイルエラー
    
    println!("Voltage: {} mV", voltage);
}
```

**重要：** Rustの変数はデフォルトで変更不可（immutable）。変更したいときだけ `mut` をつける。

#### 概念：基本的な型

```rust
let v: f64 = -65.0;         // 64ビット浮動小数点（シミュレーションで主に使う）
let n: i32 = -1;            // 32ビット整数
let name: &str = "Na+";     // 文字列スライス（読み取り専用）
let name: String = "Na+".to_string();  // 所有権を持つ文字列
let is_open: bool = true;   // true / false
```

#### 概念：関数

```rust
// fn 関数名(引数名: 型, ...) -> 戻り値の型 { 処理 }
fn add(a: f64, b: f64) -> f64 {
    a + b  // 最後の式が戻り値（returnを省略できる）
}

fn main() {
    let result = add(1.0, 2.0);
    println!("{}", result);  // 3
}
```

#### 概念：条件分岐

```rust
fn classify_potential(v: f64) -> &'static str {
    if v > -55.0 {
        "action potential"
    } else if v > -70.0 {
        "depolarized"
    } else {
        "resting"
    }
}
```

#### 概念：ループ

```rust
// forループ
for i in 0..10 {
    println!("{}", i);  // 0から9まで
}

// whileループ
let mut t = 0.0;
while t < 100.0 {
    t += 0.1;
}

// loop（無限ループ、breakで抜ける）
loop {
    // 何か処理
    break;
}
```

#### 週末タスク：ネルンスト方程式を実装する

```rust
fn main() {
    // ネルンスト電位を計算する関数を自分で書く
    // E = (RT/zF) * ln(c_out / c_in)
    // R = 8.314, T = 310.0 (体温K), F = 96485.0
    
    // Na+: z=1, c_out=145mM, c_in=12mM
    // K+:  z=1, c_out=4mM,   c_in=155mM
    // Ca2+: z=2, c_out=2mM,  c_in=0.0001mM
    
    // 期待される答え：Na+ ≈ +60mV, K+ ≈ -97mV, Ca2+ ≈ +123mV
}
```

自分でゼロから書くこと。答えを先に見ない。

-----

### Week 2：Vec・HashMap・パターンマッチング

#### 概念：Vec（配列）

```rust
fn main() {
    let mut voltages: Vec<f64> = Vec::new();
    
    // 値を追加
    voltages.push(-65.0);
    voltages.push(-64.5);
    voltages.push(-63.0);
    
    // インデックスでアクセス
    println!("{}", voltages[0]);  // -65.0
    
    // ループで全要素を処理
    for v in &voltages {
        println!("{}", v);
    }
    
    // 長さ
    println!("Steps: {}", voltages.len());
}
```

#### 概念：HashMap

```rust
use std::collections::HashMap;

fn main() {
    let mut concentrations: HashMap<String, f64> = HashMap::new();
    
    concentrations.insert("Na+".to_string(), 145.0);
    concentrations.insert("K+".to_string(), 4.0);
    concentrations.insert("Ca2+".to_string(), 2.0);
    
    // 値を取得
    if let Some(na) = concentrations.get("Na+") {
        println!("Na+ extracellular: {} mM", na);
    }
}
```

#### 概念：パターンマッチング（match）

```rust
fn describe_ion(name: &str) -> &str {
    match name {
        "Na+" => "fast depolarization",
        "K+"  => "repolarization",
        "Ca2+" => "plateau phase, signaling",
        _     => "unknown ion",  // _ はデフォルトケース
    }
}
```

#### 週末タスク：時系列データを蓄積する

```rust
fn main() {
    let dt = 0.1;    // 時間刻み (ms)
    let t_end = 50.0; // シミュレーション時間 (ms)
    
    // 時刻と電位を Vec に蓄積する
    // t: 0.0, 0.1, 0.2, ... , 50.0
    // v: 定数 -65.0（まだ何も変化しない）
    
    // 最後に全データを println! で出力する
}
```

-----

## Phase 2 — Rustの型システム

**期間：** Week 3–4
**参考：** The Rust Book Ch. 5–6

### Week 3：struct と impl

#### 概念：struct（構造体）

```rust
// 関連するデータをまとめる
struct Ion {
    name: String,
    charge: i32,
    intracellular_mm: f64,
    extracellular_mm: f64,
}

// struct のインスタンスを作る
fn main() {
    let sodium = Ion {
        name: "Na+".to_string(),
        charge: 1,
        intracellular_mm: 12.0,
        extracellular_mm: 145.0,
    };
    
    println!("{}: {}mM inside", sodium.name, sodium.intracellular_mm);
}
```

#### 概念：impl（メソッドの実装）

```rust
struct Ion {
    name: String,
    charge: i32,
    intracellular_mm: f64,
    extracellular_mm: f64,
}

impl Ion {
    // コンストラクタ（慣習的に new と名付ける）
    fn new(name: &str, charge: i32, intra: f64, extra: f64) -> Ion {
        Ion {
            name: name.to_string(),
            charge,
            intracellular_mm: intra,
            extracellular_mm: extra,
        }
    }
    
    // ネルンスト電位を計算するメソッド
    fn nernst_potential(&self) -> f64 {
        // &self = このIonインスタンスへの参照
        let r = 8.314;
        let t = 310.0;
        let f = 96485.0;
        let z = self.charge as f64;
        (r * t / (z * f)) * (self.extracellular_mm / self.intracellular_mm).ln() * 1000.0
    }
}

fn main() {
    let na = Ion::new("Na+", 1, 12.0, 145.0);
    let k  = Ion::new("K+",  1, 155.0, 4.0);
    
    println!("E_Na = {:.1} mV", na.nernst_potential());
    println!("E_K  = {:.1} mV", k.nernst_potential());
}
```

#### 概念：Display trait の実装（printlnで直接使えるようにする）

```rust
use std::fmt;

impl fmt::Display for Ion {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "[{}] E_rev = {:.1} mV | {}mM in / {}mM out",
            self.name,
            self.nernst_potential(),
            self.intracellular_mm,
            self.extracellular_mm
        )
    }
}

fn main() {
    let na = Ion::new("Na+", 1, 12.0, 145.0);
    println!("{}", na);  // Display が呼ばれる
}
```

#### 週末タスク：`Membrane` struct を作る

```rust
// 以下のstructとメソッドを自分で実装する

struct Membrane {
    voltage: f64,     // 膜電位 (mV)
    c_m: f64,         // 膜容量 (µF/cm²)
}

impl Membrane {
    fn new(v_init: f64) -> Membrane { /* ... */ }
    
    // Euler法で1ステップ進める
    fn step(&mut self, i_ext: f64, i_ion: f64, dt: f64) {
        // dV/dt = (I_ext - I_ion) / C_m
        // V_next = V + dV/dt * dt
        // &mut self が必要な理由を考えながら書く
    }
}
```

-----

### Week 4：enum と match の本格活用

#### 概念：enum（列挙型）

```rust
// イオンチャネルの状態を型で表現する
#[derive(Debug)]  // println!("{:?}", state) できるようにする
enum ChannelState {
    Closed,
    Open,
    Inactivated,
}

fn main() {
    let state = ChannelState::Open;
    
    // match は必ず全ケースを網羅しなければならない
    let current = match state {
        ChannelState::Open        => 1.0,  // 電流が流れる
        ChannelState::Closed      => 0.0,
        ChannelState::Inactivated => 0.0,
    };
    
    println!("Current: {}", current);
}
```

#### 概念：enum にデータを持たせる

```rust
enum SimulationEvent {
    Stimulus { time: f64, amplitude: f64 },  // 刺激イベント
    ChannelOpen { channel_id: usize },        // チャネルが開いた
    End,                                       // シミュレーション終了
}

fn handle_event(event: SimulationEvent) {
    match event {
        SimulationEvent::Stimulus { time, amplitude } => {
            println!("Stimulus at t={} ms, I={} µA", time, amplitude);
        }
        SimulationEvent::ChannelOpen { channel_id } => {
            println!("Channel {} opened", channel_id);
        }
        SimulationEvent::End => {
            println!("Simulation complete");
        }
    }
}
```

#### 概念：Option型（値があるかないか）

```rust
// Option<T> = Some(値) または None
// 「見つかるかもしれない」値を安全に扱う

fn find_ion(ions: &Vec<Ion>, name: &str) -> Option<f64> {
    for ion in ions {
        if ion.name == name {
            return Some(ion.nernst_potential());
        }
    }
    None  // 見つからなかった
}

fn main() {
    // ...
    match find_ion(&ions, "Na+") {
        Some(e) => println!("E_Na = {:.1} mV", e),
        None    => println!("Na+ not found"),
    }
}
```

#### 週末タスク：NaChannelとKChannelを実装する

```rust
// 以下をゼロから書く

enum ChannelState { Closed, Open, Inactivated }

struct NaChannel {
    state: ChannelState,
    g_max: f64,      // 最大コンダクタンス (mS/cm²)
    e_rev: f64,      // 逆転電位 (mV)
}

impl NaChannel {
    fn new() -> NaChannel { /* ... */ }
    
    fn current(&self, voltage: f64) -> f64 {
        // ChannelState::Open のときだけ電流を返す
        // I = g_max * (V - E_rev)
    }
    
    // 電位に応じて状態を更新する（単純化した版）
    fn update_state(&mut self, voltage: f64) {
        // voltage > -55.0 → Open
        // voltage <= -55.0 でOpenだった → Inactivated
        // それ以外 → Closed
    }
}
```

-----

## Phase 3 — Ownership & Borrowing

**期間：** Week 5–6
**参考：** The Rust Book Ch. 4

これがRust最大の壁。焦らない。コンパイラのエラーを読んで直すを繰り返すだけ。

### Week 5：Ownershipの理解

#### なぜOwnershipが必要か

```rust
// 他の言語ではこれが通る（危険）
// Rustではコンパイルエラーになる（安全）

fn main() {
    let s1 = String::from("glucose");
    let s2 = s1;          // s1の所有権がs2にmoveする
    
    println!("{}", s1);   // エラー: s1はもう無効
    // これを許すと、s1とs2が同じメモリを指す→二重解放の危険
}
```

**生物学的直感：** 基質分子は一度に一つの酵素の活性部位にしか結合できない。Rustのownershipはこれと同じ排他性をメモリで実現している。

#### Copyトレイト（コピーされる型）

```rust
// 数値型（f64, i32, bool など）はCopyトレイトを持つ
// moveではなくコピーされる

fn main() {
    let v1: f64 = -65.0;
    let v2 = v1;           // コピーされる（v1は引き続き有効）
    
    println!("{}", v1);    // OK
    println!("{}", v2);    // OK
}

// String はCopyではない → move
fn main() {
    let s1 = String::from("Na+");
    let s2 = s1;           // move
    // println!("{}", s1); // エラー
}
```

#### 関数とOwnership

```rust
fn print_ion_name(name: String) {  // Stringの所有権がここに移る
    println!("{}", name);
}  // ここでnameがdropされる（メモリ解放）

fn main() {
    let ion_name = String::from("Na+");
    print_ion_name(ion_name);    // 所有権が関数に移る
    // println!("{}", ion_name); // エラー：ion_nameはもう無効
}
```

### Week 6：Borrowing（借用）

#### 不変参照

```rust
fn print_ion(ion: &Ion) {  // &は「参照として借りる」
    println!("{}", ion.name);
    // ionを変更しようとするとエラー
}  // ここで所有権は返される（dropされない）

fn main() {
    let na = Ion::new("Na+", 1, 12.0, 145.0);
    print_ion(&na);   // &をつけて参照を渡す
    print_ion(&na);   // naはまだ使える
    println!("{}", na.name);  // OK
}
```

#### 可変参照

```rust
fn update_voltage(membrane: &mut Membrane, new_v: f64) {
    membrane.voltage = new_v;  // &mutがないとエラー
}

fn main() {
    let mut mem = Membrane::new(-65.0);
    update_voltage(&mut mem, -64.0);  // &mutをつける
    
    // 可変参照は同時に1つしか存在できない
    let r1 = &mut mem;
    // let r2 = &mut mem;  // エラー：可変参照は1つだけ
}
```

#### よく出るエラーと対処法

```
error[E0382]: borrow of moved value: `ion`
→ 所有権がmoveした後に使おうとしている
→ 対処：&ionで参照を渡す、または.clone()でコピーを作る

error[E0596]: cannot borrow as mutable, as it is not declared as mutable
→ mutをつけ忘れた
→ 対処：let mut にする

error[E0502]: cannot borrow as mutable because it is also borrowed as immutable
→ 不変参照と可変参照を同時に持とうとしている
→ 対処：不変参照のスコープが終わってから可変参照を作る
```

#### 週末タスク：Simulationを参照渡しで書く

```rust
struct Simulation {
    membrane: Membrane,
    history: Vec<(f64, f64)>,  // (時刻, 電位) のペア
}

impl Simulation {
    // membrane を参照で受け取るバージョンと
    // 所有権で受け取るバージョンの違いを体験する
    
    fn record(&mut self, t: f64) {
        // self.history に (t, self.membrane.voltage) を追加する
    }
    
    fn run(&mut self, t_end: f64, dt: f64, i_ext: f64) {
        // ループしながら step と record を呼ぶ
    }
}
```

-----

## Phase 4 — Trait・エラー処理

**期間：** Week 7–8
**参考：** The Rust Book Ch. 10, 9

### Week 7：Trait

#### 概念：Trait の定義と実装

```rust
// 「イオンチャネル」という共通の振る舞いを定義する
trait IonChannel {
    fn conductance(&self, voltage: f64) -> f64;
    fn reversal_potential(&self) -> f64;
    
    // デフォルト実装（overrideしなくてもいい）
    fn current(&self, voltage: f64) -> f64 {
        self.conductance(voltage) * (voltage - self.reversal_potential())
    }
}

struct LeakChannel {
    g: f64,   // コンダクタンス
    e: f64,   // 逆転電位
}

struct NaChannel {
    g_max: f64,
    m: f64,   // 活性化変数
    h: f64,   // 不活性化変数
}

// 両方に同じtraitを実装する
impl IonChannel for LeakChannel {
    fn conductance(&self, _voltage: f64) -> f64 {
        self.g  // リークは電位依存性なし
    }
    fn reversal_potential(&self) -> f64 { self.e }
}

impl IonChannel for NaChannel {
    fn conductance(&self, _voltage: f64) -> f64 {
        self.g_max * self.m.powi(3) * self.h  // m³h
    }
    fn reversal_potential(&self) -> f64 { 60.0 }
}
```

#### Traitオブジェクト：異なる型を同じVecに入れる

```rust
fn main() {
    // Box<dyn IonChannel> = traitオブジェクト
    let channels: Vec<Box<dyn IonChannel>> = vec![
        Box::new(LeakChannel { g: 0.003, e: -65.0 }),
        Box::new(NaChannel { g_max: 120.0, m: 0.05, h: 0.6 }),
    ];
    
    let voltage = -65.0;
    let total_current: f64 = channels.iter()
        .map(|ch| ch.current(voltage))
        .sum();
    
    println!("Total current: {:.3} µA/cm²", total_current);
}
```

### Week 8：エラー処理

#### Result型

```rust
use std::num::ParseFloatError;

// 成功: Ok(値)、失敗: Err(エラー)
fn parse_concentration(s: &str) -> Result<f64, ParseFloatError> {
    s.parse::<f64>()  // 文字列を f64 に変換（失敗することがある）
}

fn main() {
    match parse_concentration("145.0") {
        Ok(c)  => println!("Concentration: {} mM", c),
        Err(e) => println!("Parse error: {}", e),
    }
    
    // ? 演算子：エラーなら即座に return Err(...)
    // 関数内でのみ使える
}
```

#### ファイル読み込みとエラー処理

```rust
use std::fs;
use std::io;

fn load_parameters(path: &str) -> Result<String, io::Error> {
    fs::read_to_string(path)  // ファイルが存在しない場合 Err になる
}

fn main() {
    match load_parameters("params.txt") {
        Ok(content) => println!("Loaded: {}", content),
        Err(e)      => println!("Failed to load: {}", e),
    }
}
```

#### 週末タスク：JSONからIonデータを読み込む

`Cargo.toml` に追加：

```toml
[dependencies]
serde = { version = "1.0", features = ["derive"] }
serde_json = "1.0"
```

```rust
use serde::Deserialize;

#[derive(Debug, Deserialize)]
struct IonData {
    name: String,
    charge: i32,
    intracellular_mm: f64,
    extracellular_mm: f64,
}

// data/ions.json を読み込んで Vec<IonData> を返す関数を書く
// エラー処理も含めて
```

`data/ions.json`：

```json
[
  {"name": "Na+", "charge": 1, "intracellular_mm": 12.0, "extracellular_mm": 145.0},
  {"name": "K+",  "charge": 1, "intracellular_mm": 155.0, "extracellular_mm": 4.0}
]
```

-----

## Phase 5 — 数値計算・ファイルI/O

**期間：** Week 9–10

### Week 9：数値計算の基礎

#### Euler法の実装

```rust
// 微分方程式: dV/dt = f(t, V)
// 数値解: V(t+dt) = V(t) + f(t, V(t)) * dt

fn euler<F>(f: F, y0: f64, t0: f64, t_end: f64, dt: f64) -> Vec<(f64, f64)>
where
    F: Fn(f64, f64) -> f64,  // f(t, y) -> dy/dt
{
    let mut t = t0;
    let mut y = y0;
    let mut result = vec![(t, y)];
    
    while t < t_end {
        let dy = f(t, y);
        y += dy * dt;
        t += dt;
        result.push((t, y));
    }
    
    result
}

fn main() {
    // 単純なRC回路のテスト
    // dV/dt = (V_rest - V) / tau
    let tau = 10.0;    // 時定数 (ms)
    let v_rest = -65.0;
    
    let trajectory = euler(
        |_t, v| (v_rest - v) / tau,
        -50.0,   // 初期電位
        0.0,
        100.0,
        0.1,
    );
    
    println!("t=0: {:.2}", trajectory[0].1);
    println!("t=50: {:.2}", trajectory[500].1);  // -65に近づいているはず
}
```

#### 指数関数・対数：ゲーティング変数

```rust
// ボルツマン関数（定常ゲーティング変数）
fn boltzmann(v: f64, v_half: f64, k: f64) -> f64 {
    1.0 / (1.0 + (-(v - v_half) / k).exp())
}

// 時定数（電位依存）
fn time_constant(v: f64, tau_max: f64, v_half: f64, k: f64) -> f64 {
    tau_max / (boltzmann(v, v_half, k) * (1.0 - boltzmann(v, v_half, k)))
}

fn main() {
    // Na+チャネルのm変数（活性化）
    // v_half ≈ -40mV, k ≈ 7mV
    for v in (-90..=50).step_by(10) {
        let m_inf = boltzmann(v as f64, -40.0, 7.0);
        println!("V={:4} mV: m_inf = {:.3}", v, m_inf);
    }
}
```

### Week 10：CSVへの出力

`Cargo.toml` に追加：

```toml
[dependencies]
csv = "1.2"
```

```rust
use std::fs::File;
use csv::Writer;

fn save_to_csv(data: &Vec<(f64, f64)>, path: &str) -> Result<(), Box<dyn std::error::Error>> {
    let file = File::create(path)?;
    let mut wtr = Writer::from_writer(file);
    
    wtr.write_record(&["time_ms", "voltage_mv"])?;
    
    for (t, v) in data {
        wtr.write_record(&[t.to_string(), v.to_string()])?;
    }
    
    wtr.flush()?;
    Ok(())
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    // Euler法で軌跡を計算
    let data = euler(/* ... */);
    
    // CSVに保存
    save_to_csv(&data, "output/membrane_potential.csv")?;
    println!("Saved to output/membrane_potential.csv");
    
    Ok(())
}
```

#### グラフの確認

PythonがインストールされていればCSVから即座にグラフを描ける：

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("output/membrane_potential.csv")
plt.plot(df["time_ms"], df["voltage_mv"])
plt.xlabel("Time (ms)")
plt.ylabel("Voltage (mV)")
plt.title("Membrane Potential")
plt.show()
```

Rustのコードを書いて、Pythonで確認する——このループが最初の数ヶ月の基本ワークフローになる。

-----

## Phase 6 — 最初の生理学モデル

**期間：** Week 11–12

### 受動膜モデル（RC回路）を完成させる

これがPhase 1からPhase 5で学んだ全てを統合した最初の完成物。

```
目標：
- struct Membrane が動く
- JSON からパラメータを読み込む
- Euler法でシミュレーションを実行する
- CSV に出力する
- グラフが教科書の図と一致する
```

#### プロジェクト構造

```
passive_membrane/
├── Cargo.toml
├── data/
│   └── params.json        ← パラメータ
├── output/
│   └── .gitkeep
└── src/
    ├── main.rs            ← エントリーポイント
    ├── membrane.rs        ← Membrane struct
    └── io.rs              ← CSV入出力
```

#### `src/membrane.rs`

```rust
pub struct Membrane {
    pub voltage: f64,   // mV
    pub c_m: f64,       // µF/cm²
    pub g_l: f64,       // mS/cm² (リークコンダクタンス)
    pub e_l: f64,       // mV (リーク逆転電位)
}

impl Membrane {
    pub fn new(v_init: f64, c_m: f64, g_l: f64, e_l: f64) -> Self {
        Membrane { voltage: v_init, c_m, g_l, e_l }
    }
    
    pub fn step(&mut self, i_ext: f64, dt: f64) {
        let i_leak = self.g_l * (self.voltage - self.e_l);
        let dv = (i_ext - i_leak) / self.c_m;
        self.voltage += dv * dt;
    }
}
```

#### `src/main.rs`

```rust
mod membrane;
mod io;

use membrane::Membrane;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let mut mem = Membrane::new(-65.0, 1.0, 0.1, -65.0);
    
    let dt = 0.1;       // ms
    let t_end = 200.0;  // ms
    let i_ext = 1.0;    // µA/cm²（20-80msの間だけ印加）
    
    let mut history: Vec<(f64, f64)> = Vec::new();
    let mut t = 0.0;
    
    while t <= t_end {
        let current = if t >= 20.0 && t <= 80.0 { i_ext } else { 0.0 };
        mem.step(current, dt);
        history.push((t, mem.voltage));
        t += dt;
    }
    
    io::save_csv(&history, "output/result.csv")?;
    println!("Done. {} data points saved.", history.len());
    
    Ok(())
}
```

### 成功の確認方法

グラフが以下の形になっていれば正しい：

```
電位 (mV)
  -40 |              ___________
  -50 |           __/           \__
  -60 |        __/                 \__
  -65 |_______/                       \_______
       0      20          80          200
              電流開始    電流終了       時間 (ms)
```

- 電流印加前：-65mVで安定
- 電流印加中：指数関数的に上昇
- 電流終了後：指数関数的に-65mVに戻る

この形が出たとき、Hodgkin-Huxley モデルに進む準備が整っている。

-----

## 詰まったときのデバッグ手順

1. **エラーメッセージを最後まで読む** — Rustのエラーは親切。`help:`の提案を試す。
2. **問題を最小化する** — エラーが出たコードを削って、どこが問題か特定する。
3. **`println!("{:?}", value)`で値を確認する** — `#[derive(Debug)]`をstructに追加する必要がある。
4. **The Rust Bookの該当章を読む** — エラーの種類（E0382など）でBook内を検索する。
5. **Rust Playgroundで試す** — https://play.rust-lang.org/ でコード断片を試せる。

-----

## 参考資料

|資料               |用途                     |URL                                       |
|-----------------|-----------------------|------------------------------------------|
|The Rust Book    |基礎から順番に学ぶ              |https://doc.rust-lang.org/book/           |
|Rust by Example  |コード例で学ぶ                |https://doc.rust-lang.org/rust-by-example/|
|Rust Playground  |ブラウザでRustを試す           |https://play.rust-lang.org/               |
|crates.io        |crateを探す               |https://crates.io/                        |
|docs.rs          |crateのドキュメント           |https://docs.rs/                          |
|Keener & Sneyd   |数理生理学の教科書              |Mathematical Physiology Vol.1             |
|HH original paper|Hodgkin & Huxley (1952)|J. Physiol. 117: 500–544                  |

-----

## 各フェーズの完了チェックリスト

### Phase 0

- [ ] `rustup` と `cargo` がインストールされている
- [ ] VS Code + rust-analyzer が動いている
- [ ] `cargo new` でプロジェクトを作り `cargo run` が通る

### Phase 1

- [ ] ネルンスト方程式を関数として書ける
- [ ] Na+, K+, Ca2+の逆転電位を計算できる
- [ ] Vec に時系列データを蓄積してループで出力できる

### Phase 2

- [ ] `Ion` struct と `nernst_potential()` メソッドを自分で書ける
- [ ] `Display` trait を実装して `println!("{}", ion)` が動く
- [ ] `ChannelState` enum と `match` でチャネル電流を計算できる

### Phase 3

- [ ] moveとborrowの違いを説明できる
- [ ] `&T` と `&mut T` の使い分けができる
- [ ] よく出るコンパイラエラー3種類を自力で直せる

### Phase 4

- [ ] `IonChannel` trait を定義して複数の型に実装できる
- [ ] `Vec<Box<dyn IonChannel>>` に異なるチャネルを入れて電流を合計できる
- [ ] JSONからデータを読み込み `Result` でエラー処理できる

### Phase 5

- [ ] Euler法を汎用関数として実装できる
- [ ] シミュレーション結果をCSVに出力できる
- [ ] PythonまたはRustでグラフを確認できる

### Phase 6

- [ ] 受動膜モデルが正しい形の波形を出す
- [ ] パラメータをJSONから読み込んで変更できる
- [ ] コードが複数ファイルに分割されている

全チェックが埋まったとき、Hodgkin-Huxley モデルに進む準備が整っている。

-----

*Last updated: 2026-03-25*
*Hideto Iwatsuka · Semmelweis University · English Medicine Programme, Year 1*