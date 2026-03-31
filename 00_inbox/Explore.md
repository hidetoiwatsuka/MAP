# Concepts to Explore

既存のフレームワークを拡張・挑戦・深化させる概念のリスト。既に構築したものとの接続で整理。

---

## Foundation Layer

他の全ての概念を支える基盤。

### Functions

あらゆる現象に適用できるinput → process → outputの普遍的パターン。全conceptの背骨。 → [Functions](Functions.md)

### Learning

input-output-feedbackサイクルの反復による関数獲得。煩悩がブートストラップ。 → [Learning](Learning.md)

### Category Theory

構造同士の「関係」の数学。ものが何であるかではなく、どう関係するか（射 / morphism）だけで全てを記述する。関数が言語なら、圏論はその文法。異なる領域に同じ構造が現れるパターンを_functor_として形式化する。 **入口:** Bartosz Milewski "Category Theory for Programmers"（無料、重い数学的前提なし）。

### Information Theory

シャノンの枠組み。情報＝不確実性の減少。エントロピー＝系の中の驚きの量。[Learning](Learning.md)で記述した「驚きの漸進的減少」を定量化する。神経科学のfree energy principle（脳＝予測誤差最小化装置）、通信のS/N比、圧縮（最小の構造で最大の情報を表現する方法）に接続。 **入口:** シャノンの1948年原論文（意外に読みやすい）。James Stone "Information Theory: A Tutorial Introduction"。

---

## Structure Layer

ものがどう接続し、組織化され、関係するかについての概念。

### Graph Theory

接続の数学。ノード（実体）とエッジ（関係）。神経回路、社会ネットワーク、代謝経路、Obsidian vault — すべてグラフ。個々の要素を見ていては見えない性質（最短経路、ボトルネック、クラスター、中心性）を明らかにする。接続の構造が、接続されたもの自体の性質よりも重要なことが多い。 **入口:** 自分のObsidian vaultのグラフビューを開く。それがグラフ。どのノードが最も接続が多いか？どれが孤立しているか？クラスターはどこか？

### Emergence

部分の性質からは予測できない性質が全体から生まれる現象。水は「濡れる」が水素と酸素は濡れない。意識は存在するが個々のニューロンには意識がない。[Sustainable Human Relationships](Sustainable%20Human%20Relationships.md)で愛を創発特性と定義した理由、関数の合成が単なる足し算にならない理由、還元主義の限界を説明する。 **未解決の問い:** 創発は形式化可能か、それとも本質的に形式的記述に抵抗するか？後者なら — 複雑な現象を説明しようとするあらゆるモデルにとって何を意味するか？

### Complexity and Criticality

秩序とカオスの間を漂うシステム。砂山モデル：漸進的蓄積→突然の雪崩。雪崩のタイミングは予測不能だが、蓄積→崩壊のパターンは普遍的。[Life and Happiness](Life%20and%20Happiness.md)は人生を波として記述したが、現実の人生には滑らかな曲線に従わない突然の相転移（別れ、突破、崩壊）が含まれる。小さな入力が巨大な出力を生む理由（ラクダの背を折る最後の藁）と、大きな入力が何も生まないケースを説明する。 **入口:** Per Bak "How Nature Works"。Melanie Mitchell "Complexity: A Guided Tour"。

---

## Reasoning Layer

思考・判断・信念の更新についての概念。

### Bayesian Inference

事前信念 + 新しい証拠 = 更新された信念。学習ループの数学的形式化：モデルを持ち（事前）、データに遭遇し（証拠）、モデルを更新する（事後）。核心的洞察：**ゼロから始めることはない** — すべての評価は既に信じていることに形作られる。[Learning](Learning.md)のループを直接形式化する。同じ証拠を見て正反対の結論に達する理由も説明する — 異なる事前信念が異なる事後信念を生む。確証バイアスを「強い事前信念下での合理的行動」として説明。

$$P(\text{model} | \text{data}) = \frac{P(\text{data} | \text{model}) \cdot P(\text{model})}{P(\text{data})}$$

**入口:** 3Blue1Brownのベイズの定理動画。Allen Downey "Think Bayes"（無料、Python）。

### Gödel's Incompleteness Theorems

十分に強力な論理体系には、その体系内では証明も反証もできない真な命題が必ず存在する。いかなるシステムも自分自身を完全に記述できない。盲点は努力不足ではなく構造的不可能性による。[Life and Happiness](Life%20and%20Happiness.md)は基準点の移動により絶対的幸福は不可能と論じたが、ゲーデルはさらに深いことを証明する：基準点が固定されていても、**いかなる自己参照的評価システムにも固有の限界がある**。自分の評価システムを内側から完全に評価することはできない。欠陥ではなく数学的必然。 **接続:** [Learning](Learning.md)が「完了」しない理由。内的関数システムは自分自身を完全にモデル化できない。地図と領土の間には常に還元不能な隙間がある。

### Ergodicity

多くの人の平均結果と、一人の人間の時間平均は同じではない。100人が1回ずつギャンブル ≠ 1人が100回ギャンブル。1回でも破産しうるなら、時間平均（実際の体験）はアンサンブル平均（統計的期待値）から壊滅的に乖離する。素朴な最適化への挑戦。「平均的にうまくいく」は個人の人生にとって無意味かもしれない。リスクと破滅は経路依存 — 平均ではなく順序が重要。キャリア選択・健康リスク・資金計画に直結。 **入口:** Ole Petersのエルゴード性経済学。Nassim Taleb "Skin in the Game"での扱い。

---

## Perception Layer

処理が始まる前に入力がどう構造化されるかについての概念。

### Affordance

アフォーダンスとは、環境が行為者に行動の可能性を「差し出す」こと。椅子は「座れる」をアフォードする。取っ手は「引ける」をアフォードする。入力は中立的データではなく、可能な出力の形を既に含んでいる。知覚と行動は別の段階ではなく結合している。[Functions](Functions.md)のinput → process → outputモデルへの挑戦。入力が既に行動可能性をエンコードしているなら、入力と処理の境界は曖昧になる。環境は処理されるべきデータではなく、関数のパートナー。 **問い:** アフォーダンスが実在するなら、[Learning](Learning.md)は内的関数の構築だけではなく、常にそこにあったが見えなかったアフォーダンスを知覚できるようになることでもある。

### Fourier Analysis

どんな複雑な周期的信号も単純なsin波とcos波の重ね合わせに分解できる。複雑さは重層化された単純さ。[Functions](Functions.md)で不規則関数の分析として言及済みだが、**知覚原理**としてより深い探索に値する：脳が感覚入力を同じ方法で分解している可能性 — 複雑な刺激を周波数成分に分解してから意味を再構成。音楽制作（EQ・コンプ・シンセシス）、医療信号処理（ECG・EEG）、画像圧縮（JPEG）、脳が構造化された入力を解析する方法のモデルに接続。

---

## Thermodynamic Layer

すべてのシステムに対する根本的制約についての概念。

### Entropy and Life

熱力学第二法則：孤立系のエントロピー（無秩序）は常に増大する。生命はその局所的違反 — 無秩序に向かう宇宙の中で維持される秩序のポケット。ただしこの違反にはコストがある：内的秩序を維持するために、生命システムは環境に無秩序を輸出しなければならない（熱・廃棄物・劣化）。フレームワーク全体を一つの原理の下に統一する。[Learning](Learning.md) = 秩序ある内的関数の構築（エネルギーのコストで局所エントロピーを減少）。[Sustainable Human Relationships](Sustainable%20Human%20Relationships.md) = 秩序ある社会構造の維持（継続的エネルギー投入が必要 — それが交換）。[Life and Happiness](Life%20and%20Happiness.md) = エントロピーに抗して秩序を維持する進行中のプロジェクト。維持のコストが利用可能なエネルギーを超えた時、システムは劣化する — 老化、燃え尽き、関係の崩壊。 **最も深いリフレーム:** 生きることは無料ではない。構築するすべての関数、維持するすべての関係、持続するすべての幸福の瞬間 — すべてにエネルギーコストがかかる。人生とは、そのコストを効果的に支払うプロジェクト。 **入口:** シュレーディンガー "生命とは何か"（短く、基礎的）。Jeremy Englandの散逸駆動適応の研究。

---

## Meta Layer

思考プロセスそのものについての概念。

### Metacognition

考えることについて考える。自分の内的関数を入力として受け取り、評価・監視・修正する高階関数。

$$f_{\text{meta}}(f_{\text{internal}}) \rightarrow f_{\text{improved}}$$

このconceptノートプロジェクト全体がまさにこれ。暗黙のメンタルモデルを抽出し、明示化し、評価し、精錬する。メタ認知は他のすべての関数の獲得を加速する関数 — 学習そのものに適用された学習関数。ほとんどの人は内的関数を検査せずに実行する。メタ認知は世界観を「持つ」ことと「検証する」ことの差。検証された関数はより速く更新される。

### Dynamical Systems

時間とともにルールに従って変化するシステムの数学。平衡・振動・分岐・カオス — すべて形式化。[Life and Happiness](Life%20and%20Happiness.md)の評価ループは力学系。[Sustainable Human Relationships](Sustainable%20Human%20Relationships.md)の交換バランスは力学系。形式化すれば：どの条件で系は安定するか？いつ振動するか？いつカオスになるか？が明らかになる。 **入口:** Steven Strogatz "Nonlinear Dynamics and Chaos" — 数学で最もアクセスしやすい教科書の一つ。

---

## Suggested Exploration Order

すべてを同時に探索する必要はない。依存関係と関連性に基づく推奨経路：

```
1. Bayesian Inference ─── 既に直感的に理解している学習ループの形式化
        │
2. Information Theory ─── ベイズが記述するものを定量化
        │
3. Entropy and Life ──── すべての熱力学的基盤
        │
4. Emergence ──────────── 合成 ≠ 足し算である理由
        │
5. Dynamical Systems ──── ループと波を形式化
        │
6. Complexity / Criticality ── 力学系を相転移に拡張
        │
7. Category Theory ────── 究極の抽象化層
```

並行トラック（興味に基づいていつでも）：

- Gödel → あらゆるシステムの限界について考えたいなら
- Ergodicity → リスクと人生戦略を再考したいなら
- Affordance → input/outputモデル自体に挑戦したいなら
- Metacognition → 既にやっている。準備ができたら形式化
- Graph Theory → Obsidian vault設計に実用的
- Fourier Analysis → 数学・音楽制作・医療信号を橋渡し

---

## Related Concepts

- [Functions](Functions.md)
- [Learning](Learning.md)
- [Sustainable Human Relationships](Sustainable%20Human%20Relationships.md)
- [Life and Happiness](Life%20and%20Happiness.md)