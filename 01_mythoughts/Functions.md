---
tags:
  - concept
  - math
---
## 1. What Is a Function? — 関数とは何か

A function is anything that takes an input and produces an output through some consistent process.

$$\text{input} \xrightarrow{\text{process}} \text{output}$$


The input does not have to be a number. The output does not have to be a number. The process does not have to be a mathematical formula. A function is a **pattern of transformation** — something goes in, something consistent comes out.

（入力は数値である必要はない。出力も数値である必要はない。処理も数式である必要はない。何かが入り、一貫した法則に従って何かが出る — それが関数。）

### Examples across domains（あらゆる領域での例）

|Input|Process|Output|
|---|---|---|
|Light hitting retina|Neural encoding|Visual perception|
|Spoken words|Listener's interpretation|Understanding|
|Ingredients|Recipe|A dish|
|Symptoms|Clinical reasoning|Diagnosis|
|A question|Thinking|An answer|
|Sensory nerve signal|Brain processing|Motor nerve signal|
|DNA sequence|Transcription + Translation|Protein|

Every one of these is a function. The nervous system is a function: sensory input → central processing → motor output. The immune system is a function: antigen in → recognition and response → antibody out. A conversation is a function: what someone says → how you process it → what you say back.

（神経系は関数。免疫系は関数。会話も関数。「入力 → 処理 → 出力」のパターンがある限り、それは関数として捉えられる。）

### The variable is just "whatever goes in"（変数＝「入るもの」）

In math, we write _x_. But _x_ can be anything — a number, a sound, a molecule, a situation, an emotion. The variable is simply a placeholder for "the thing that changes." When the input changes, the output changes. That relationship — input determines output — is the essence of a function.

（数学では _x_ と書くが、_x_ は何でもいい。変わりうるもの、それが変数。入力が変われば出力も変わる。その関係性こそが関数の本質。）

---

## 2. Multiple Inputs — 複数の入力

A function can take more than one input. The output emerges from the **combination** of inputs, not from any single one alone.

$$f(a, b, c, \ldots) \rightarrow \text{output}$$

A diagnosis is not made from one symptom. It comes from the combination of history, physical findings, lab results, and imaging — all fed into clinical reasoning simultaneously. The output (diagnosis) is a function of all those inputs together.

（診断は1つの症状からではなく、病歴・身体所見・検査・画像の組み合わせから生まれる。出力は全入力の関数。）

A chord is not one note. It is the function of multiple notes combined, producing a harmonic quality that none of the individual notes carry alone.

（和音は1つの音ではない。複数の音の組み合わせが、単独では持ちえない響きを生み出す。）

### What "multiple inputs" really means（複数入力の本質）

It means the output **cannot be fully explained by any single input**. You need the whole set. Remove one, and the output changes — or becomes undefined.

---

## 3. Types of Functions — 関数の種類

When the inputs and outputs happen to be numbers, functions produce characteristic shapes. These shapes are not arbitrary — each one reflects a fundamentally different kind of relationship between input and output.

（入出力が数値の場合、関数は特有の形を描く。各形状は、入力と出力の間の本質的に異なる関係を反映している。）

### 3.1 Linear — 一次関数

$$f(x) = ax + b$$

**The relationship:** Output changes at a constant rate as input changes. No surprises — perfectly proportional.（入力の変化に対して出力が一定の割合で変化。比例関係。）

**Shape:** Straight line.

**Where this pattern appears:** Constant-rate infusion of a drug. Distance covered at constant speed. Any situation where "twice the input = twice the change in output."

### 3.2 Quadratic — 二次関数

$$f(x) = ax^2 + bx + c$$

**The relationship:** Output accelerates as input increases. Small inputs cause small effects; large inputs cause disproportionately large effects.（入力が大きくなるほど出力の変化が加速する。）

**Shape:** Parabola — a curve that bends.

**Where this pattern appears:** Kinetic energy (doubles speed → quadruples energy). Fluid resistance in turbulent flow. Any situation with a "squared" relationship.

### 3.3 Exponential — 指数関数

$$f(x) = a^x$$

**The relationship:** Output multiplies by a fixed ratio for each unit increase in input. Growth feeds on itself.（入力が1増えるごとに出力が一定倍される。成長が成長を生む。）

**Shape:** A curve that starts slow, then explodes upward — or decays rapidly toward zero.

**Where this pattern appears:** Bacterial growth (unchecked). Radioactive decay. Compound interest. Viral spread. Any process where "the more there is, the faster it grows" — or "the more there is, the faster it disappears."

### 3.4 Logarithmic — 対数関数

$$f(x) = \log(x)$$

**The relationship:** The inverse of exponential. Large changes in input produce diminishing changes in output. Sensitivity decreases as magnitude increases.（指数の逆。入力が大きくなるほど出力の変化は鈍くなる。）

**Shape:** Rises quickly at first, then flattens.

**Where this pattern appears:** Human perception (Weber-Fechner law — doubling brightness doesn't feel twice as bright). pH scale. Decibel scale. Richter scale. Nature often uses logarithmic compression to handle enormous ranges of input.

### 3.5 Trigonometric — 三角関数

$$f(x) = \sin(x), \quad \cos(x)$$

**The relationship:** Output oscillates — it repeats the same pattern endlessly. Defined by period (how long one cycle takes) and amplitude (how far it swings).（出力が振動し、同じパターンを繰り返す。）

**Shape:** Waves.

**Where this pattern appears:** Any rhythm or cycle. Heartbeat. Breathing. Circadian rhythm. Sound waves. Alternating current. Seasons.

### 3.6 Hyperbolic / Inverse — 反比例関数

$$f(x) = \frac{k}{x}$$

**The relationship:** As one quantity increases, the other decreases — but never reaches zero. There is always a residual.（一方が増えると他方が減る。しかし決してゼロにはならない。）

**Shape:** A curve that approaches the axes but never touches them (asymptotes).

**Where this pattern appears:** Boyle's law (pressure × volume = constant). The relationship between speed and travel time for a fixed distance.

### 3.7 Sigmoid — シグモイド関数

$$f(x) = \frac{1}{1 + e^{-x}}$$

**The relationship:** Output is bounded. Below a threshold, almost no response. Around the threshold, rapid change. Above the threshold, saturation — more input doesn't change the output much.（出力に上限がある。閾値以下はほぼ無反応、閾値付近で急変、閾値以上で飽和。）

**Shape:** S-curve.

**Where this pattern appears:** Dose-response curves in pharmacology. Oxygen-hemoglobin dissociation. Adoption of new technology. Learning curves. Any system with a "tipping point" and a ceiling.

### Why these shapes matter（これらの形が重要な理由）

When you see data and recognize a shape, you immediately know the **type of relationship** at play. You don't need the exact equation — the shape tells you whether the system is proportional, accelerating, self-reinforcing, oscillating, saturating, or decaying. The shape is the story.

（形を認識すれば、その系がどんな関係性で動いているかが即座にわかる。形は物語。）

---

## 4. Composing Functions — 関数の合成

Functions can be combined to build larger, more complex functions. This is how complex systems are constructed — not from one giant rule, but from layers of simpler rules connected together.

（関数は組み合わせてより大きく複雑な関数を構築できる。複雑なシステムは1つの巨大なルールではなく、単純なルールの層が接続されて構成される。）

### 4.1 Series — 直列（出力を次の入力にする）

The output of one function becomes the input of the next.

$$x \xrightarrow{f} f(x) \xrightarrow{g} g(f(x))$$

This is a chain. Each link transforms and passes forward.

**Examples:**

- Food → digestion → nutrients → metabolism → ATP → muscle contraction → movement. Each arrow is a function. The whole chain is one large composite function: food → movement.
- DNA → mRNA → protein → enzyme activity → metabolic product. Gene expression is a series composition.

（食物→消化→栄養素→代謝→ATP→筋収縮→運動。各矢印が関数。全体が1つの大きな合成関数。）

### 4.2 Parallel — 並列（複数の出力を合わせる）

Multiple functions run independently, and their outputs are combined by another function.

$$f(x) \searrow$$ $$\qquad \qquad h(f(x),\ g(x)) \rightarrow \text{output}$$ $$g(x) \nearrow$$

**Examples:**

- Sympathetic tone → HR, Preload → SV. Then: CO = HR × SV. Two parallel functions feeding into a combining function.
- In music production: dry signal and wet signal processed separately, then mixed at the output bus.

（交感神経→HR、前負荷→SV、そしてCO = HR × SV。2つの並列関数が結合関数に入力される。音楽制作でのドライ/ウェット信号のミックスも同じ構造。）

### 4.3 Feedback — フィードバック（出力が入力に戻る）

The output of a function is fed back as input to itself or an earlier function in the chain. This creates loops — systems that regulate themselves.

$$x \xrightarrow{f} y \xrightarrow{\text{feedback}} x' \xrightarrow{f} y'$$

- **Negative feedback（負のフィードバック）:** Output opposes the input. The system stabilizes. Thermoregulation: body temperature rises → sweating increases → temperature falls → sweating decreases. Homeostasis is built on negative feedback loops.
- **Positive feedback（正のフィードバック）:** Output amplifies the input. The system escalates. Blood clotting cascade: each step accelerates the next until the wound is sealed.

（負のフィードバック＝安定化。正のフィードバック＝増幅。ホメオスタシスは負のフィードバックの産物。）

### 4.4 Differentiation and Integration — 微分と積分

These are **meta-functions** — functions that operate on other functions.

**Differentiation（微分）** asks: "How fast is the output changing right now?" It takes a function and returns a new function that describes the rate of change at every point.

$$f(x) \xrightarrow{\text{differentiate}} f'(x) = \text{rate of change}$$

This is not limited to math. Whenever you ask "is this getting better or worse, and how quickly?" — you are differentiating.

（「今どのくらい速く変化しているか？」を問う操作。「良くなっているか悪くなっているか、どれだけ速く？」と問う時、あなたは微分している。）

**Integration（積分）** asks: "What is the total accumulated effect?" It takes a function and returns the cumulative sum over a range.

$$f(x) \xrightarrow{\text{integrate}} F(x) = \text{accumulated total}$$

Whenever you ask "how much in total?" — total exposure, total distance, total energy expended — you are integrating.

（「累積でどれだけか？」を問う操作。総曝露量、総距離、総エネルギー消費を問う時、あなたは積分している。）

They are inverses of each other:

$$f(x) \xrightarrow{\text{differentiate}} f'(x) \xrightarrow{\text{integrate}} f(x) + C$$

---

## 5. Analyzing Irregular Functions — 規則性のない関数の分析

Real-world data rarely follows a clean mathematical shape. But the function still exists — input still determines output. We just can't write it as a neat equation. The tools below let us work with these messy, real functions.

（現実のデータが綺麗な数式に従うことは稀。しかし関数は存在する — 入力は依然として出力を決定している。数式にできないだけ。以下のツールはそうした「乱雑な現実の関数」を扱う方法。）

### 5.1 Regression — 回帰分析

**What it does:** Takes scattered data points and finds the known function shape that best fits them. "This messy data behaves most like a ____."

（散らばったデータに最も近い既知の関数形を当てはめる。「この乱雑なデータは__に最も近い挙動をしている」）

- **Linear regression（線形回帰）:** Fits a straight line. Is the relationship roughly proportional?
- **Nonlinear regression（非線形回帰）:** Fits exponential, logarithmic, sigmoid, or other curves.
- **Multiple regression（重回帰）:** Multiple inputs, one output. How much does each input contribute?

The function was always there in the data. Regression makes it visible.

### 5.2 Fourier Analysis — フーリエ解析

**What it does:** Takes any complex, seemingly irregular waveform and decomposes it into a sum of simple waves (sine and cosine).

$$f(x) = a_0 + \sum_{n=1}^{\infty} \left( a_n \cos(nx) + b_n \sin(nx) \right)$$

Any repeating pattern, no matter how complex, is actually many simple patterns layered on top of each other. Fourier analysis separates those layers.

（どんな複雑な繰り返しパターンも、実は多数の単純パターンの重ね合わせ。フーリエ解析はその層を分離する。）

**Where this applies:** ECG noise filtering. EEG frequency band analysis (δ, θ, α, β waves). Audio signal processing — an equalizer is applied Fourier analysis. Compression algorithms (JPEG, MP3).

### 5.3 Numerical Methods — 数値解法

**What they do:** When you have discrete data points instead of a continuous equation, these methods approximate differentiation and integration directly from the data.

- **Numerical differentiation（数値微分）:** Estimate the rate of change between adjacent data points (finite difference method).
- **Numerical integration（数値積分）:** Estimate the area under the curve using trapezoids (trapezoidal rule) or curved segments (Simpson's rule).

（連続的な数式がなくても、離散データから微分・積分を近似できる。）

**Where this applies:** Calculating AUC from irregularly sampled blood concentration data. Any situation where you have measurements at specific time points but no equation.

### 5.4 Interpolation — 補間

**What it does:** Estimates values between known data points. "I measured at these points — what happened in between?"

（既知のデータ点の間の値を推定する。「ここで測定した。その間に何が起きたか？」）

- **Linear interpolation（線形補間）:** Connect adjacent points with straight lines. Simple but jagged.
- **Spline interpolation（スプライン補間）:** Connect points with smooth curves. More realistic for natural phenomena.

### 5.5 Statistical Description — 統計的記述

**What it does:** When the function's output includes randomness or noise, statistics characterize the pattern within the noise.

（関数の出力にランダム性やノイズが含まれる場合、統計がノイズの中のパターンを特徴づける。）

- **Probability density function, PDF（確率密度関数）:** Describes how likely each output value is. The bell curve (normal distribution) is the most common shape.
- **Correlation（相関）:** Measures how strongly two variables move together (−1 to +1). Correlation does not prove one causes the other — it only shows they are linked.
- **Moving average（移動平均）:** Smooths noisy data by averaging neighboring points, revealing the underlying trend.

---

## Summary — まとめ

|Concept|概念|Core idea|
|---|---|---|
|Function|関数|Input → process → output. Universal pattern.|
|Variable|変数|Whatever goes in. Not limited to numbers.|
|Multiple inputs|複数入力|Output determined by combination, not any single input.|
|Function types|関数の種類|Each shape = a different kind of relationship.|
|Series composition|直列合成|Output of one becomes input of the next.|
|Parallel composition|並列合成|Multiple functions feed into a combiner.|
|Feedback|フィードバック|Output loops back as input. Self-regulation or amplification.|
|Differentiation|微分|How fast is it changing?|
|Integration|積分|How much in total?|
|Regression|回帰|Fit a known shape to messy data.|
|Fourier analysis|フーリエ解析|Decompose complexity into simple waves.|
|Numerical methods|数値解法|Approximate calculus from discrete data.|
|Interpolation|補間|Estimate between measured points.|
|Statistics|統計|Find pattern within noise.|