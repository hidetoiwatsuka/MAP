---
tags:
  - sleep
  - IT
  - rust
---
# body-sim Curriculum

## Overview

| Phase   | Period                         | Goal                                                                  |
| ------- | ------------------------------ | --------------------------------------------------------------------- |
| Phase 1 | Now – Sep 2025                 | Rust language fundamentals                                            |
| Phase 2 | Sep 2025 – May 2026            | Physiology mechanisms → code (1 lecture/week)                         |
| Phase 3 | Sep 2026 – May 2027 (Year 3)   | Pharmacology → modifier layer on Phase 2 code                         |
| Phase 4 | Sep 2027 – May 2028 (Year 4–6) | System integration during clinical rotations _(概要のみ — Year 3中に詳細化予定)_ |

**Repository:** `body-sim/`

```
body-sim/
├── src/
│   ├── units/          # Shared unit types (mV, mmHg, L/min, mmol/L...)
│   ├── core/           # Subsystem trait, ODE solver, utilities
│   ├── general/        # Section 1: membranes, channels, synapses, muscle
│   ├── cardiovascular/ # Section 2: heart, vessels, circulation control
│   ├── respiratory/    # Section 3: ventilation, gas exchange, control
│   ├── renal/          # Section 4: filtration, tubular, acid-base
│   ├── blood/          # Section 5: hematopoiesis, coagulation
│   ├── gi/             # Section 6: motility, secretion, absorption
│   ├── endocrine/      # Section 7: axes, hormones, metabolism
│   ├── neuro/          # Section 8: sensory, motor, integration
│   ├── pharmacology/   # Phase 3: drug modifier layer
│   │   ├── pk/              # Pharmacokinetics engine
│   │   │   ├── absorption.rs
│   │   │   ├── distribution.rs
│   │   │   ├── metabolism.rs
│   │   │   ├── excretion.rs
│   │   │   └── models.rs    # 1-compartment, 2-compartment, non-linear
│   │   ├── pd/              # Pharmacodynamics engine
│   │   │   ├── receptors.rs
│   │   │   ├── dose_response.rs
│   │   │   └── interactions.rs
│   │   ├── autonomic/       # Cholinergic & adrenergic drugs
│   │   ├── neuro/           # CNS drugs
│   │   ├── antimicrobial/   # Antibiotics, antivirals, antifungals
│   │   ├── cardiovascular/  # Antiarrhythmics, antihypertensives, anticoagulants
│   │   ├── endocrine/       # Hormones, antidiabetics, steroids
│   │   ├── respiratory/     # Bronchodilators, antitussives
│   │   ├── gi/              # Acid secretion, antiemetics, laxatives
│   │   ├── immune/          # Immunosuppressants, anticancer
│   │   └── toxicology/      # Antidotes, poisoning models
│   └── viz/            # Output (CSV/JSON, future WASM)
├── tests/
├── validation/         # Reference data & golden-file tests per section
│   ├── general/             # Nernst equation outputs, Goldman values
│   ├── cardiovascular/      # Normal CO ranges, PV loop shapes
│   ├── respiratory/         # Alveolar gas equation outputs
│   ├── renal/               # GFR ranges, tubular reabsorption %
│   ├── blood/               # Normal coagulation cascade timing
│   ├── gi/                  # Absorption rates
│   ├── endocrine/           # Hormonal axis set-point values
│   ├── neuro/               # Conduction velocities, reflex latencies
│   └── pharmacology/        # PK curves vs published data
├── benches/
└── README.md
```

**Core design patterns used throughout:**

```rust
// Newtype units — compile-time dimensional safety
struct Voltage(f64);       // mV
struct Pressure(f64);      // mmHg
struct FlowRate(f64);      // L/min
struct Concentration(f64); // mmol/L
struct Temperature(f64);   // °C
struct Volume(f64);        // L
struct Compliance(f64);    // L/mmHg
struct Resistance(f64);    // mmHg·min/L

// Subsystem trait — universal interface for integration
trait Subsystem {
    type Input;
    type Output;
    fn step(&mut self, input: Self::Input, dt: f64) -> Self::Output;
}

// Drug trait — Phase 3 addition, multi-target modifier on any Subsystem
trait Drug {
    fn pk_params(&self) -> PKParams;
    fn effects(&self) -> Vec<Box<dyn Effect>>;
}

// Effect trait — single pharmacological effect on a specific target
trait Effect {
    fn target_name(&self) -> &str;
    fn apply(&self, concentration: Concentration, state: &mut dyn std::any::Any);
}

// Multi-target example (e.g., amiodarone):
// drug.effects() → vec![
//     NaChannelBlock { use_dependent: true },
//     KChannelBlock { prolongation: 0.3 },
//     CaChannelBlock { verapamil_like: true },
//     BetaBlock { selectivity: NonSelective },
// ]
```

---

## Phase 1: Rust Basics (Now – Sep 2025)

Phase 2開始前に**絶対必要なもの (CORE)** と**その週が来たら学べばいいもの (JIT)** を区別する。

### Foundation — CORE

- [Development environment setup (rustup, cargo, VS Code + rust-analyzer)](Development%20environment%20setup%20(rustup,%20cargo,%20VS%20Code%20+%20rust-analyzer).md) — _TRPL Ch. 1_
- [Cargo basics (new, build, run, test, Cargo.toml)](Cargo%20basics%20(new,%20build,%20run,%20test,%20Cargo.toml).md) — _TRPL Ch. 1_
- [Git & GitHub (repo creation, commit, push)](Git%20&%20GitHub%20(repo%20creation,%20commit,%20push).md) — _external_
- Create `body-sim` repository

### Rust Fundamentals I — Ownership & Core Types — CORE

- [Variables, data types, functions, control flow](Variables,%20data%20types,%20functions,%20control%20flow.md) — _TRPL Ch. 2–3 / PR Ch. 2–3_
- Ownership — _TRPL Ch. 4_
- Borrowing and references (`&`, `&mut`) — _TRPL Ch. 4_
- Slices — _TRPL Ch. 4_
- Structs and `impl` blocks — _TRPL Ch. 5_
- Enums and `match` — _TRPL Ch. 6_
- Module system (`mod`, `use`, `pub`) — _TRPL Ch. 7_
- `Vec<T>` and `HashMap<K, V>` — _TRPL Ch. 8_

### Rust Fundamentals II — Error Handling & Traits — CORE / JIT 混合

- Error handling (`Result`, `Option`, `?` operator) — _TRPL Ch. 9_ — **CORE**
- Generic types — _TRPL Ch. 10_ — **CORE**
- Traits and trait bounds — _TRPL Ch. 10_ — **CORE**
- Lifetimes — _TRPL Ch. 10_ — **JIT: Week 6+ で必要になったら学ぶ**
- Closures — _TRPL Ch. 13_ — **JIT: Week 5 (signal transduction II) で導入**
- Iterators — _TRPL Ch. 13_ — **JIT: Week 13 (skeletal muscle) で導入**

### Pre-Phase 2 Preparation — CORE

- Build `units/` module with newtype pattern
- Build `core/` module with `Subsystem` trait
- Implement simple Euler solver in `core/`
- Write unit tests for all of the above
- Set up `validation/` directory structure with README explaining the validation approach

---

## Phase 2: Physiology Mechanisms (Sep 2025 – May 2026)

Each entry: **Week | Lecture topic → Rust mechanism(s) | Rust learning goal | Pathology scenario | Validation target**

Flex/catch-up週を明示。各メカニズムを **CORE（必須）** と **STRETCH（余裕があれば）** に分類。

### Numerical Methods Progression

ODEソルバーの段階的導入計画:

|When|Method|Why here|
|---|---|---|
|Phase 1 prep|Euler法|最もシンプル、概念理解|
|Week 10 (action potential)|Euler vs 中点法 比較|HHモデルでEulerが発散する体験 → stiff系の理解|
|Week 19 (arterial circulation)|RK4 導入|Windkesselモデルで精度が必要|
|Week 31 (respiratory control)|Adaptive step size|フィードバック系で時定数が大きく変わる|

### Fall Semester — Section 1: General Physiology

|No|Lecture|Mechanism to code|Rust goal|Pathology scenario|Validation|Priority|
|---|---|---|---|---|---|---|
|1|Fluid compartments|`FluidCompartment` struct, volume distribution model, osmolarity calculation|Structs, impl blocks, unit types|Dehydration: ECF volume ↓50%|Osmolarity = 285-295 mOsm/L (normal)|CORE|
|2|Transport across membranes|`MembraneTransport` enum (passive, facilitated, active), Fick's diffusion|Enums, match, trait methods|Glucose transporter deficiency: facilitated transport → 0|Fick's law output vs analytical solution|CORE|
|3|Transepithelial transports|`Epithelium` struct chaining apical + basolateral transporters|Composition, module organization|Cystic fibrosis: Cl⁻ channel dysfunction|Net transport = sum of apical + basolateral|STRETCH|
|4|Signal transduction I|`Receptor` trait, `GProtein` state machine (inactive→active→hydrolyzed)|Traits, state machine pattern|Cholera toxin: G-protein permanently active|State transition correctness|CORE|
|5|Signal transduction II|`SecondMessenger` enum (cAMP, IP3, DAG), cascade chain|Enum variants with data, **closures (JIT導入)**|Pseudohypoparathyroidism: Gsα deficiency|Cascade amplification factor|CORE|
|6|Ca²⁺ metabolism, vesicular transport|`CalciumStore` (ER, mito, extracellular), `Vesicle` lifecycle enum|Ownership transfer for vesicle release, **lifetimes (JIT導入)**. `Rc<RefCell<T>>`は使わない — `&mut`で十分|Malignant hyperthermia: uncontrolled Ca²⁺ release from SR|Resting [Ca²⁺]i ≈ 100 nM|CORE|
|7|Blood I, blood groups|`BloodType` enum, antigen-antibody matching, `BloodCell` trait|Generics, trait objects|Transfusion reaction: ABO mismatch|ABO matching truth table|STRETCH|
|8|Blood II (hemostasis, coagulation)|Coagulation cascade as state machine, `ClottingFactor` enum|Complex enum, Result for cascade failure|Hemophilia A: Factor VIII = 0 → cascade fails|Cascade completion time ranges|CORE|
|9|Membrane potentials|Nernst equation, Goldman equation, `RestingPotential` calculator|Functions returning unit types, math|Hyperkalemia: K⁺ = 7.0 mEq/L → depolarization|Nernst: EK ≈ -90 mV at [K⁺]o=4, [K⁺]i=140|CORE|
|10|Ion channels, action potential|`IonChannel` state machine (closed→open→inactivated), Hodgkin-Huxley simplified. **Euler vs 中点法を比較してstiff系を体験**|Enum state transitions, ODE solver comparison|Long QT syndrome: K⁺ channel delayed inactivation|AP duration ≈ 2ms (nerve), ≈ 200ms (cardiac)|CORE|
|11|Nerve cells, synaptic transmission|`Synapse` struct, neurotransmitter release/reuptake, `Neurotransmitter` enum|Ownership transfer (NT release = move)|Myasthenia gravis: AChR antibodies → reduced postsynaptic response|EPSP amplitude ranges|CORE|
|12|Autonomic NT, smooth muscle|`SmoothMuscle` state, autonomic modulation (sympathetic vs parasympathetic)|Strategy pattern with closures|Pheochromocytoma: excess catecholamines → sustained contraction|Sympathetic vs parasympathetic response polarity|STRETCH|
|13|Skeletal muscle|`MotorEndplate`, excitation-contraction coupling, cross-bridge cycle|**Iterators (JIT導入)** for cyclic processes|Duchenne MD: progressive force reduction|Twitch force vs tetanic force ratio|CORE|

### Fall Semester — Section 2: Cardiovascular

|Wk|Lecture|Mechanism to code|Rust goal|Pathology scenario|Validation|Priority|
|---|---|---|---|---|---|---|
|14|Cardiac excitation, pacemaker|`PacemakerCell` with funny current, `ConductionSystem` graph|Custom iterator (beat generator)|Sick sinus syndrome: pacemaker rate ↓ to 40 bpm|SA node rate ≈ 60-100 bpm|CORE|
|15|Cardiac cycle|`CardiacCycle` state machine (phases), pressure-volume changes per phase|Complex state machine, logging|Aortic stenosis: increased afterload → PV loop shift|PV loop shape vs Guyton textbook|CORE|
|16|Cardiac output regulation|Frank-Starling curve, `CardiacOutput` from preload/afterload/contractility/HR|Multiple input struct, functional composition|Heart failure: flattened Frank-Starling curve|CO ≈ 5 L/min at rest|CORE|
|17|ECG|`ECGSignal` generator from conduction timing, lead vector projection|Iterators, time-series output to CSV|AV block: PR interval prolongation|Normal PR = 120-200ms, QRS < 120ms|STRETCH|
|18|**Flex/catch-up week**|Week 1-17 の遅れを取り戻す。リファクタリング、テスト追加|`cargo clippy`, テストカバレッジ確認|—|—|—|
|19|Hemodynamics intro|Poiseuille's law, `VesselSegment` with resistance/compliance|Trait impl for different vessel types|Atherosclerosis: radius ↓ 50% → resistance ↑ 16x|Poiseuille: R ∝ 1/r⁴|CORE|
|20|Arterial circulation|Windkessel model (2-element), `ArterialPressure` waveform. **RK4導入**|ODE solver upgrade (Runge-Kutta 4th order)|Aortic stiffness: compliance ↓ → pulse pressure ↑|SBP ≈ 120, DBP ≈ 80 mmHg|CORE|
|21|Microcirculation|Starling forces, `Capillary` filtration/reabsorption model|Builder pattern for parameter setup|Nephrotic syndrome: albumin ↓ → edema|Net filtration ≈ 2-4 L/day (lymph return)|STRETCH|
|22|Venous circulation, lymph|`VenousSystem` with capacitance, `LymphFlow` driven by pressure gradient|Collections (Vec of vessel segments)|Venous insufficiency: valve failure → reflux|Venous return = cardiac output at steady state|STRETCH|
|23|Local control|`LocalRegulation` trait (myogenic, metabolic, endothelial), autoregulation curves|Trait objects, dynamic dispatch|Autoregulation failure: flow becomes pressure-passive|Cerebral flow constant between MAP 60-150 mmHg|CORE|
|24|Reflex control I|`Baroreceptor` struct, afferent signal → reflex arc → efferent response|Channel-like pattern (mpsc preview)|Baroreflex failure: no HR response to BP change|HR inverse response to BP change|CORE|
|25|Reflex control II|`RAAS` cascade, ADH, full reflex integration|Multi-module integration, error propagation|Conn syndrome: aldosterone excess → hypertension + hypokalemia|RAAS cascade: renin → angiotensin I → II → aldosterone|CORE|
|26|**Flex/catch-up week**|Week 19-25 の遅れを取り戻す|リファクタリング、バリデーション追加|—|—|—|
|27|Coronary & cerebral circulation|`CoronaryFlow` (systolic compression), `CerebralAutoregulation`|Specialized Subsystem implementations|MI: coronary occlusion → regional ischemia|Coronary flow ≈ 250 mL/min, mainly diastolic|STRETCH|
|28|Skeletal muscle & splanchnic|Exercise hemodynamics, splanchnic redistribution|Conditional logic, simulation scenarios|Exercise: CO ↑ to 25 L/min, splanchnic flow ↓|Flow redistribution percentages vs textbook|STRETCH|

### Fall Semester — Section 3: Respiratory

|No|Lecture|Mechanism to code|Rust goal|Pathology scenario|Validation|Priority|
|---|---|---|---|---|---|---|
|29|Pulmonary ventilation|`LungVolumes` struct, dead space, `AlveolarVentilation` calculator, compliance curve|Structs with derived calculations|COPD: compliance ↑, FEV1/FVC ↓|TV ≈ 500 mL, VA ≈ 4.2 L/min|CORE|
|30|Gas exchange|`GasExchange` using Fick's diffusion across alveolar membrane, PAO2/PACO2|Generic diffusion trait (reuse from wk2)|Pulmonary fibrosis: diffusion capacity ↓|PAO2 ≈ 100 mmHg (alveolar gas equation)|CORE|
|31|Pulmonary circulation, V/Q|`VQRatio` model, zone model (West zones 1-3), shunt/dead space|Enums with associated data, pattern matching|PE: dead space ↑ (ventilated but not perfused)|V/Q ≈ 0.8 overall|STRETCH|
|32|Gas transport, hypoxia|`Hemoglobin` O2 dissociation curve (Hill equation), CO2 transport, `HypoxiaType` enum|Math functions, curve fitting|CO poisoning: left-shifted O2 dissociation curve|P50 ≈ 26.7 mmHg, Hill coefficient ≈ 2.8|CORE|
|33|Control of respiration. **Adaptive step size導入**|`RespiratoryCenter` with chemoreceptor input (central/peripheral), feedback loop|Feedback control pattern, PID-like controller, **adaptive step size ODE**|Central sleep apnea: chemoreceptor sensitivity ↓|Ventilatory response to CO2: ΔVE/ΔPCO2|CORE|

### Fall Semester — Section 4: Renal

|No|Lecture|Mechanism to code|Rust goal|Pathology scenario|Validation|Priority|
|---|---|---|---|---|---|---|
|34|Renal circulation, GFR|`Glomerulus` filtration model, `RenalBloodFlow` autoregulation|Subsystem trait implementation|CKD: GFR = 15 mL/min (stage 4)|GFR ≈ 120 mL/min, RBF ≈ 1.2 L/min|CORE|
|35|Tubular functions|`TubularSegment` enum (PCT, LoH, DCT, CD), transport processes per segment|Enum with per-variant methods, iterators over segments|Fanconi syndrome: PCT reabsorption failure|Na⁺ reabsorption: ~67% PCT, ~25% LoH|CORE|
|36|Concentration/dilution|Countercurrent multiplier model, `MedullaryGradient`, urine concentration|Nested loops, convergence algorithms|Diabetes insipidus: no ADH → dilute urine (50 mOsm/L)|Urine osmolarity range: 50-1200 mOsm/L|CORE|
|37|Osmo/volume regulation|`OsmoRegulator` with ADH feedback, volume receptors → RAAS integration|Cross-module integration (renal + cardiovascular)|SIADH: excess ADH → hyponatremia|Plasma Na⁺ ≈ 135-145 mEq/L|CORE|
|38|Acid-base I|Henderson-Hasselbalch, `AcidBaseStatus` enum (normal, acidosis, alkalosis), renal compensation|Pattern matching, Result types for diagnosis|Diabetic ketoacidosis: metabolic acidosis pH 7.1|pH = 7.35-7.45, HCO3⁻ = 22-26 mEq/L|CORE|
|39|Acid-base II|Respiratory compensation, `BloodGas` struct, clinical interpretation logic|Complex decision trees, integration testing|Mixed acid-base disorder|Winter's formula for expected PCO2|STRETCH|

### Fall Semester — Adaptation & Review

|No|Lecture|Mechanism to code|Rust goal|Priority|
|---|---|---|---|---|
|40|CV + Respiratory adaptation I|Exercise model: connect cardiac output ↔ ventilation ↔ gas exchange|**First multi-system integration**|CORE|
|41|**Flex/catch-up week**|Fall semester の遅れを取り戻す。STRETCH項目をスキップした場合はここで再評価|リファクタリング|—|
|42|Competition exam|Review, refactor, write integration tests|Code quality, documentation|CORE|
|43|Consultation|Clean up semester 1 code|`cargo clippy`, `cargo doc`|CORE|

---

### Spring Semester — Section 6: Gastrointestinal

|No|Lecture|Mechanism to code|Rust goal|Pathology scenario|Validation|Priority|
|---|---|---|---|---|---|---|
|1|GI motor functions|`GIMotility` trait, peristalsis state machine, `MMC` cycle|Trait with default implementations|Achalasia: LES fails to relax|MMC cycle ≈ 90-120 min|CORE|
|2|GI secretion I|`SalivaryGland`, `GastricSecretion` with HCl/pepsinogen, parietal cell model|Builder pattern for secretory units|Zollinger-Ellison: gastrin excess → HCl overproduction|Gastric pH ≈ 1-2, basal acid output ≈ 5 mEq/hr|CORE|
|3|GI secretion II|`PancreaticSecretion`, `BileProduction`, enterohepatic circulation|Module organization (avoid `Rc`/`Weak` — use ownership or `&mut` passing)|Gallstone: bile flow obstruction → fat malabsorption|Bile salt pool ≈ 2-4 g, recycled 6-8x/day|STRETCH|
|4|Digestion & absorption|`Nutrient` enum (carb, protein, fat), absorption transporter per segment|Generics over nutrient types|Celiac disease: villous atrophy → malabsorption|Carb absorption ≈ 95% in jejunum|CORE|

### Spring Semester — Section 7: Endocrine

|No|Lecture|Mechanism to code|Rust goal|Pathology scenario|Validation|Priority|
|---|---|---|---|---|---|---|
|5|Endocrine regulation intro|`HormonalAxis` trait (hypothalamus→pituitary→target), negative feedback|Trait generics, associated types|Feedback disruption: remove negative feedback → hormone excess|Feedback loop settles to set-point within tolerance|CORE|
|6|Hypothalamus-pituitary, GH|`HPAxis<GH>` implementation, GH→IGF-1 cascade, feedback|Generic trait instantiation|Acromegaly: GH excess → IGF-1 ↑|GH pulsatile pattern, IGF-1 age-dependent range|CORE|
|7|Adrenal cortex I|`HPAAxis` (CRH→ACTH→cortisol), zona glomerulosa/fasciculata/reticularis|Enum variants, nested modules|Addison's disease: cortisol ≈ 0 → ACTH ↑↑|Cortisol diurnal rhythm: AM peak ≈ 10-20 μg/dL|CORE|
|8|Adrenal cortex II|Aldosterone regulation (RAAS integration), cortisol effects on metabolism|Cross-module deps (renal + endocrine)|Conn syndrome: aldosterone excess (from CV section too)|Aldosterone ≈ 5-30 ng/dL|STRETCH|
|9|Thyroid|`HPTAxis` (TRH→TSH→T3/T4), deiodination, metabolic effects|Reusing HormonalAxis trait|Graves' disease: TSH receptor antibody → T3/T4 ↑↑, TSH ↓|TSH ≈ 0.4-4.0 mIU/L, T4 ≈ 5-12 μg/dL|CORE|
|10|Energy balance|`EnergyBalance` calculator (BMR, TEF, activity), food intake regulation|Arithmetic trait implementations (Add, Sub)|Obesity: positive energy balance sustained|BMR ≈ Harris-Benedict equation output|STRETCH|
|11|Calcium metabolism|`CalciumHomeostasis` (PTH, calcitonin, vitamin D), bone remodeling|Multi-organ feedback (bone, kidney, intestine)|Hypoparathyroidism: PTH ↓ → Ca²⁺ ↓, PO4 ↑|Serum Ca²⁺ ≈ 8.5-10.5 mg/dL|CORE|
|12|Bone physiology|`Bone` struct, osteoblast/osteoclast balance, growth plate model|State patterns, lifecycle|Osteoporosis: resorption > formation|Bone mineral density T-score|STRETCH|
|13|Reproductive I — sexual development|`SexDifferentiation` enum, gonadal axis setup|Complex enum hierarchies|5α-reductase deficiency|Binary differentiation logic|STRETCH|
|14|Reproductive II — male|`HPGAxis<Male>`, testosterone production, spermatogenesis cycle|Generic specialization|Klinefelter syndrome: primary hypogonadism|Testosterone ≈ 300-1000 ng/dL|STRETCH|
|15|Reproductive III — female|`HPGAxis<Female>`, menstrual cycle state machine (follicular→ovulation→luteal)|Complex state machine with timers|PCOS: anovulation, LH/FSH ratio ↑|Cycle length ≈ 28 days, LH surge at day 14|CORE|
|16|Reproductive IV — pregnancy|`Pregnancy` modifier on female axis, hCG/progesterone dynamics, lactation|Composition: wrapping existing systems|Ectopic pregnancy: hCG rise pattern abnormal|hCG doubling time ≈ 48 hrs (early pregnancy)|STRETCH|
|17|**Flex/catch-up week**|Endocrine section の遅れを取り戻す。STRETCHスキップ分を再評価|リファクタリング|—|—|—|
|18–21|Intermediary metabolism I–IV|`Insulin`/`Glucagon` balance, fed/fasted state machine, diabetes model, exercise metabolism, starvation adaptation|**Async patterns** (concurrent metabolic pathways), **Rayon** for parallel pathway simulation|T1DM: insulin = 0; T2DM: insulin resistance; Starvation: ketoacidosis|Fasting glucose ≈ 70-100 mg/dL, HbA1c < 5.7%|CORE|

### Spring Semester — Section 8: Neurophysiology

|No|Lecture|Mechanism to code|Rust goal|Pathology scenario|Validation|Priority|
|---|---|---|---|---|---|---|
|22|Nerve and glia cells|`Neuron` struct (reuse from sem1), `GliaCell` enum (astrocyte, oligodendrocyte, microglia)|Refactoring existing code, code reuse|Multiple sclerosis: demyelination → conduction slowing|Conduction velocity: myelinated ≈ 70-120 m/s|CORE|
|23|EEG, sleep|`EEGSignal` generator (alpha, beta, delta, theta waves), `SleepStage` state machine|Signal processing, iterators|Epilepsy: abnormal synchronization|Alpha ≈ 8-13 Hz, beta ≈ 13-30 Hz|STRETCH|
|24|Sensory I — general principles|`SensoryReceptor` trait (threshold, adaptation, receptive field)|Trait design for extensibility|Receptor adaptation failure|Weber fraction, two-point discrimination|CORE|
|25|Sensory II — somatosensory|`MechanoreceptorType` enum (Meissner, Pacinian, Merkel, Ruffini), afferent pathway|Enum dispatch, trait objects|Diabetic neuropathy: receptor density ↓|Adaptation rates per receptor type|STRETCH|
|26|Sensory III — pain|`NociceptorType`, gate control theory model, referred pain mapping|HashMap for dermatome mapping|Chronic pain: gate permanently open|Dermatome map correctness|CORE|
|27|**Flex/catch-up week**|Neuro前半の遅れを取り戻す|リファクタリング|—|—|—|
|28|Hearing & equilibrium I|`Cochlea` tonotopic model (frequency→position), `HairCell` transduction|Mathematical transforms|Presbycusis: high-frequency hearing loss|Frequency range: 20 Hz - 20 kHz|STRETCH|
|29|Hearing & equilibrium II|`VestibularSystem` (semicircular canals, otolith), head position → signal|3D vector types, spatial math|BPPV: otolith displacement|Angular acceleration detection threshold|STRETCH|
|30|Vision I|`Retina` struct (rods, cones), phototransduction cascade, `ColorVision`|Nested structs, complex composition|Color blindness: cone type missing|Rod sensitivity vs cone sensitivity curves|STRETCH|
|31|Vision II|Receptive fields (center-surround), visual pathway to cortex|2D array processing|Homonymous hemianopia: pathway lesion|Center-surround inhibition pattern|STRETCH|
|32|Motor I — spinal cord|`SpinalReflex` (stretch, withdrawal), `MotorNeuron` pool|Command pattern|Upper motor neuron lesion: hyperreflexia|Reflex arc latency ≈ 25-35 ms (knee jerk)|CORE|
|33|Motor II — supraspinal|`PosturalReflex`, descending tracts (corticospinal, rubrospinal)|Enum-based routing|Stroke: corticospinal tract lesion → contralateral weakness|Tract routing correctness|STRETCH|
|34|Motor III — cerebellum, basal ganglia|`Cerebellum` error correction model, `BasalGanglia` direct/indirect pathway|Feedback vs feedforward control patterns|Parkinson's: dopamine ↓ → indirect pathway overactive|Error correction convergence rate|STRETCH|
|35|Thermoregulation|`Thermostat` model (set point, error signal), skin circulation control|PID controller, cross-system (CV + neuro)|Fever: set point ↑ to 39°C; Hypothermia: core temp 32°C|Core temp ≈ 37°C ± 0.5°C|CORE|
|36|Autonomic integration|`AutonomicNervousSystem` integrating sympathetic/parasympathetic across all systems|**Major integration point** — touches every module|Autonomic neuropathy: HR variability ↓|Sympathetic/parasympathetic balance ratios|CORE|
|37|**Flex/catch-up week**|Neuro後半の遅れを取り戻す|リファクタリング|—|—|—|
|38|Learning & memory|`SynapticPlasticity` (LTP/LTD), Hebbian learning rule|Mutable state, history tracking|Alzheimer's: LTP impaired|Potentiation decay time constant|STRETCH|
|39|Behavioral regulation|`Motivation` model, reward circuit, emotion as autonomic + endocrine modifier|Cross-module orchestration|Depression: reward circuit hypoactive|—|STRETCH|
|40|Aging|Parameter degradation across all systems over time|**Macro** for applying aging modifiers|Normal aging: GFR ↓1 mL/min/year after 40|Age-dependent parameter curves|STRETCH|
|41|Exercise physiology|Full-body exercise response: CV + respiratory + metabolic + endocrine + thermoregulation|**Full system integration test**|Exercise in heart failure patient|VO2max prediction vs actual|CORE|
|42|Competition|Final review|Benchmarks, documentation|—|CORE||
|43|Consultation|Polish|`cargo doc`, README, examples|—|CORE||

---

## Phase 3: Pharmacology (Sep 2026 – May 2027, Year 3)

**Goal:** Add a pharmacology layer to the Phase 2 physiology codebase. Every drug class becomes a modifier on existing `Subsystem` implementations. No new organ systems — only intervention points on what already exists.

**Textbook:** Katzung, Basic and Clinical Pharmacology, 15th ed.

**Core design pattern — Drug as Multi-Target Modifier:**

```rust
/// A drug produces one or more effects on different targets
trait Drug {
    fn pk_params(&self) -> PKParams;
    fn effects(&self) -> Vec<Box<dyn Effect>>;
}

/// A single pharmacological effect on a specific target
trait Effect {
    fn target_name(&self) -> &str;
    fn apply(&self, concentration: Concentration, state: &mut dyn std::any::Any);
}

struct PKParams {
    bioavailability: f64,           // F (0.0–1.0)
    volume_of_distribution: Volume, // Vd
    clearance: FlowRate,            // CL
    half_life: f64,                 // t½ (hours)
    protein_binding: f64,           // fraction bound
}

struct PKModel {
    dose: f64,
    params: PKParams,
    time_since_dose: f64,
}

impl PKModel {
    fn plasma_concentration(&self) -> Concentration {
        // C(t) = (F · D / Vd) · e^(-ke · t)
        // ke = CL / Vd
    }
}

// Multi-target example: Amiodarone
struct Amiodarone;
impl Drug for Amiodarone {
    fn pk_params(&self) -> PKParams { /* t½ ≈ 40-55 days, huge Vd */ }
    fn effects(&self) -> Vec<Box<dyn Effect>> {
        vec![
            Box::new(NaChannelBlock { use_dependent: true }),     // Class I
            Box::new(KChannelBlock { prolongation_ms: 50.0 }),    // Class III (primary)
            Box::new(CaChannelBlock { reduction: 0.2 }),          // Class IV
            Box::new(BetaBlock { selectivity: NonSelective }),    // Class II
        ]
    }
}

enum Interaction {
    PK(PKInteraction),
    PD(PDInteraction),
}

enum PKInteraction {
    EnzymeInduction { target_cyp: CYP450, fold_change: f64 },
    EnzymeInhibition { target_cyp: CYP450, ki: f64 },
    DisplacementFromProtein { displaced_drug: String, new_free_fraction: f64 },
    AlteredAbsorption { factor: f64 },
}

enum PDInteraction {
    Synergism { effect_multiplier: f64 },
    Antagonism { effect_reduction: f64 },
}
```

### Semester 5 — Pharmacology I

#### Block A: General Pharmacology (Weeks 1–2)

|Wk|Lecture|Practice|Mechanism to code|Rust goal|Phase 2 module used|
|---|---|---|---|---|---|
|1|Introduction to Pharmacology, pharmacogenomics, toxicology basics|Pharmacodynamics I: drug receptors, receptor theories, drug-receptor interactions|`Receptor` enum (ion channel, GPCR, kinase, nuclear), `DrugReceptorBinding` with Kd/EC50/Emax, agonist/partial agonist/antagonist/inverse agonist models|Enum variants with associated data, trait method dispatch|`general/` signal transduction|
|2|Pharmacokinetics I|Pharmacodynamics II: quantal dose-response, therapeutic indices, tolerance, drug interactions|`PKModel` (1-compartment: absorption → distribution → metabolism → excretion), `TherapeuticIndex` calculator (LD50/ED50), `Tolerance` state modifier|Builder pattern for PK parameter assembly, math functions|`core/` ODE solver|

#### Block B: Pharmacokinetics Deep Dive (Week 3)

|Wk|Lecture|Practice|Mechanism to code|Rust goal|Phase 2 module used|
|---|---|---|---|---|---|
|3|Pharmacokinetics II|Cholinergic: parasympathomimetics, parasympatholytics, centrally acting anticholinergics|`MultiCompartmentPK` (2-compartment model), `CYP450` enum (1A2, 2C9, 2C19, 2D6, 3A4), `FirstPassMetabolism`; `Cholinomimetic` and `Cholinolytic` as Drug impls on `Synapse`|Generics over compartment count, trait impl for existing structs|`general/` synaptic transmission|

#### Block C: Autonomic Pharmacology (Week 4)

|Wk|Lecture|Practice|Mechanism to code|Rust goal|Phase 2 module used|
|---|---|---|---|---|---|
|4|Skeletal muscle pharmacology|Adrenergic: sympathomimetics, sympatholytics|`NMJBlocker` enum (depolarizing/non-depolarizing) modifying `MotorEndplate`, `Sympathomimetic` (direct α/β agonist) and `Sympatholytic` (α/β blocker) — each producing multiple `Effect`s on `SmoothMuscle`, `PacemakerCell`, `VesselSegment`|Strategy pattern — drug swaps the modulation closure on existing systems; **multi-target `effects()` pattern in practice**|`general/` NMJ, smooth muscle; `cardiovascular/` pacemaker|

#### Block D: Pain & Inflammation (Weeks 5–6)

|Wk|Lecture|Practice|Mechanism to code|Rust goal|Phase 2 module used|
|---|---|---|---|---|---|
|5|NSAIDs, minor analgesics|Uric acid drugs, headache drugs|`COXInhibitor` enum (non-selective, COX-2 selective), prostaglandin pathway modifier, `UricAcidDrug` (xanthine oxidase inhibitor, uricosuric)|Enum dispatch with different effect profiles|New: `pharmacology/inflammation` pathway|
|6|Opioid receptor drugs|1st midterm; Summary of Product Characteristics|`OpioidReceptor` subtypes (μ, κ, δ), `Opioid` Drug impl (full agonist, partial agonist, antagonist), respiratory depression as side effect on `RespiratoryCenter`|Cross-module effect — drug targeting pain also modifies respiratory control via `effects()` returning both `PainEffect` and `RespiratoryEffect`|`respiratory/` control, `neuro/` pain|

#### Block E: Anesthetics (Week 7)

|Wk|Lecture|Practice|Mechanism to code|Rust goal|Phase 2 module used|
|---|---|---|---|---|---|
|7|Local anesthetics|Prescription writing basics|`LocalAnesthetic` blocking `IonChannel` (Na+ channel state-dependent block: use-dependent, rate-dependent), `NerveBlockade` model|State machine modification — adding "blocked" state to existing channel FSM|`general/` ion channels, action potential|

#### Block F: Neuropsychopharmacology (Weeks 8–10)

|Wk|Lecture|Practice|Mechanism to code|Rust goal|Phase 2 module used|
|---|---|---|---|---|---|
|8|Antipsychotics|Sedative-hypnotics, anxiolytics|`D2Blocker` modifying dopaminergic `Synapse`, `GABAModulator` (benzodiazepine, barbiturate, Z-drug) enhancing `IonChannel` (GABA-A Cl⁻ conductance)|Modifier stacking — multiple drugs affecting same channel differently via `Vec<Box<dyn Effect>>`|`neuro/` synaptic transmission, `general/` ion channels|
|9|Extrapyramidal drugs, nootropics|Antidepressants, mood stabilizers|`MAOInhibitor`, `SSRI`, `SNRI`, `TCA` — each modifying neurotransmitter reuptake in `Synapse`; `LithiumMod` modifying `SecondMessenger` (IP3/cAMP)|Trait objects — `Vec<Box<dyn Drug>>` applied to same synapse|`general/` signal transduction, `neuro/`|
|10|General anesthetics|Anticonvulsants (antiepileptics)|`InhalationAnesthetic` (MAC, Meyer-Overton), `IVAnesthetic`; `Anticonvulsant` — single drug with `effects()` returning Na+ channel, Ca²+ channel, GABA enhancement, and glutamate block effects|**Multi-target pattern showcase** — one drug, four different `Effect` implementations|`general/` ion channels, `neuro/`|

#### Block G: Antimicrobials (Weeks 11–13)

|Wk|Lecture|Practice|Mechanism to code|Rust goal|Phase 2 module used|
|---|---|---|---|---|---|
|11|Antivirals|Cell wall synthesis inhibitor antibiotics; 2nd midterm|`Antibiotic` trait with `MIC`, `mechanism` (cell wall, protein synthesis, nucleic acid, folate), `spectrum` (narrow/broad); `BetaLactam` struct family|Trait hierarchy — base Antibiotic trait, specialized sub-traits per mechanism|New: `pharmacology/antimicrobial/`|
|12|Antifungals, antimycobacterials|Protein synthesis inhibitor antibiotics|`Antifungal` (azole → CYP450 interaction, polyene → membrane), `Aminoglycoside`, `Macrolide`, `Tetracycline` — each with concentration-dependent vs time-dependent kill kinetics|Enum with per-variant behavior, time-series simulation|`pharmacology/antimicrobial/`|
|13|Anthelmintics, antiprotozoals, antiparasitics|Nucleic acid synthesis inhibitors, disinfectants|`Fluoroquinolone`, `Rifamycin`, `Sulfonamide`; `DrugResistance` enum modeling resistance mechanisms|HashMap<Organism, Vec<Resistance>> pattern|`pharmacology/antimicrobial/`|

#### Block H: Special Topics (Week 14)

|Wk|Lecture|Practice|Mechanism to code|Rust goal|Phase 2 module used|
|---|---|---|---|---|---|
|14|Biological drugs, orphan drugs, advanced therapies|Vitamins, traditional medicines, anorectic drugs|`BiologicalDrug` struct (monoclonal antibody, fusion protein), PK differences from small molecules (no CYP450, no oral bioavail); semester review & refactor|Trait object vs enum design decision — when to use which|All modules — integration test|

### Semester 6 — Pharmacology II

#### Block I: Cardiovascular Pharmacology (Weeks 1–4)

|Wk|Lecture|Practice|Mechanism to code|Rust goal|Phase 2 module used|
|---|---|---|---|---|---|
|1|Anticoagulants, antiplatelet agents|Fibrinolytics, drugs against bleeding, drugs acting on blood cell production|`Anticoagulant` enum (heparin → AT-III potentiation, warfarin → vitamin K antagonism, DOAC → direct Xa/thrombin), `Antiplatelet` (aspirin → COX-1, P2Y12 inhibitor), modifying `CoagulationCascade` state machine|Complex enum modifying existing state machine at multiple points|`blood/` coagulation cascade|
|2|Drugs influencing cardiac electrophysiology|Positive inotropic agents|`Antiarrhythmic` using Vaughan-Williams classification — each class implemented as `Effect` on specific ion channels in `PacemakerCell` and `ConductionSystem`; amiodarone as multi-target showcase; `Digoxin` modifying Na+/K+-ATPase → intracellular Ca²⁺|**Direct connection to AF research** — antiarrhythmic drug effects on atrial electrophysiology; **multi-target Drug trait in clinical context**|`cardiovascular/` cardiac excitation, pacemaker|
|3|Diuretics, antidiuretics|Antihypertensives (sympatholytics, nitrates, Ca-channel blockers, RAAS drugs)|`Diuretic` enum per segment (loop → LoH, thiazide → DCT, K-sparing → CD) modifying `TubularSegment` transport; `ACEInhibitor`, `ARB`, `CCB` modifying `RAAS` and `VesselSegment`|Cross-module: drug acts on renal → changes CV parameters → baroreceptor adapts|`renal/` tubular, `cardiovascular/` RAAS, hemodynamics|
|4|Drugs acting on blood glucose|Drugs influencing O₂ supply/demand of heart, microcirculation drugs|`Insulin` and `OralAntidiabetic` enum (metformin, sulfonylurea, SGLT2i, GLP-1 RA) modifying `EnergyBalance` and glucose handling; `AntianginalDrug` (nitrate → preload reduction, β-blocker → O₂ demand reduction)|Multi-target simulation — diabetic patient on metformin + SGLT2i + ACEi|`endocrine/` insulin/glucagon, `cardiovascular/` coronary flow|

#### Block J: Respiratory & Lipid Pharmacology (Week 5)

|Wk|Lecture|Practice|Mechanism to code|Rust goal|Phase 2 module used|
|---|---|---|---|---|---|
|5|Lipid drugs (½), Bronchodilators & anti-inflammatory (½)|Expectorants, antitussives, antihistamines, smooth muscle drugs|`Statin` (HMG-CoA reductase inhibitor), `Fibrate`; `Beta2Agonist` and `ICS` modifying bronchial `SmoothMuscle` and inflammation; `Antihistamine` (H1 blocker)|Trait generics — same Drug trait for different organ targets|`respiratory/` ventilation, `gi/` smooth muscle|

#### Block K: Endocrine Pharmacology (Weeks 6–8)

|Wk|Lecture|Practice|Mechanism to code|Rust goal|Phase 2 module used|
|---|---|---|---|---|---|
|6|Corticosteroids and antagonists|Pituitary/hypothalamic hormones, thyroid drugs; 3rd midterm|`Glucocorticoid` modifying `HPAAxis` (exogenous cortisol → CRH/ACTH suppression), `ThyroidDrug` (levothyroxine, thioamide) modifying `HPTAxis`|Feedback disruption — drug breaks negative feedback loop, model the consequences|`endocrine/` HPA, HPT axes|
|7|Female sexual hormones, contraceptives|Androgens, antiandrogens, anabolic steroids|`OralContraceptive` modifying `HPGAxis<Female>` (suppress ovulation by disrupting FSH/LH surge), `Antiandrogen` modifying `HPGAxis<Male>`|State machine override — drug forces specific state in menstrual cycle FSM|`endocrine/` reproductive axes|
|8|Toxicology basics|Bone mineral homeostasis drugs|`Bisphosphonate` modifying osteoclast activity in `Bone`, `VitaminDSupplement` and `PTHAnalog` modifying `CalciumHomeostasis`; `Antidote` trait (chelator, receptor antagonist, enzyme reactivator)|Cross-module feedback — Ca²⁺ drug affects bone + kidney + intestine simultaneously|`endocrine/` calcium, bone|

#### Block L: GI Pharmacology (Week 9)

|Wk|Lecture|Practice|Mechanism to code|Rust goal|Phase 2 module used|
|---|---|---|---|---|---|
|9|Drugs influencing gastric acid secretion, mucosal protection|Antiemetics, prokinetics, laxatives, antidiarrheals, liver/bile drugs|`PPI` (proton pump inhibitor) and `H2Blocker` modifying `GastricSecretion` parietal cell model; `Prokinetic` modifying `GIMotility`|Modifier composition — PPI + H2 blocker + antacid stacking on same target|`gi/` secretion, motility|

#### Block M: Immunopharmacology & Oncology (Weeks 10–12)

|Wk|Lecture|Practice|Mechanism to code|Rust goal|Phase 2 module used|
|---|---|---|---|---|---|
|10|Immunopharmacology (cytotoxic, intracellular signaling inhibitors, cytokine inhibitors)|Cytotoxic anticancer drugs|`Immunosuppressant` enum (calcineurin inhibitor, mTOR inhibitor, antimetabolite), `CytotoxicAgent` (alkylating agent, antimetabolite, topoisomerase inhibitor, mitotic spindle inhibitor)|Enum with complex variant data, Result types for treatment response vs toxicity|New: `pharmacology/immune/`|
|11|Small molecule signal inhibitors, hormonal anticancer drugs|Toxicology I; 4th midterm|`TyrosineKinaseInhibitor` modifying cell signaling, `HormonalAnticancer` (tamoxifen → estrogen receptor, aromatase inhibitor)|Trait object collections — `Vec<Box<dyn Drug>>` for combination chemotherapy|`endocrine/`, `pharmacology/immune/`|
|12|Anticancer antibodies, immunostimulant anticancer agents|Toxicology II|`MonoclonalAntibody` (anti-VEGF, anti-HER2, anti-PD1), `CheckpointInhibitor`; PK modeling of biologics (long half-life, no CYP metabolism)|Different PK model branch — biologics vs small molecules|`pharmacology/immune/`|

#### Block N: Integration & Toxicology (Weeks 13–14)

|Wk|Lecture|Practice|Mechanism to code|Rust goal|Phase 2 module used|
|---|---|---|---|---|---|
|13|PD and PK basics of drug interactions|Drugs and pregnancy; Toxicology exam|`InteractionEngine` — given `Vec<Box<dyn Drug>>`, compute net PK (CYP induction/inhibition, protein binding displacement) and PD (synergism/antagonism) via collected `effects()`; `PregnancyModifier` (teratogenicity categories, placental transfer model)|**Major integration** — interaction engine touching all PK/PD modules|All modules|
|14|Pharmacogenomics, personalized medicine, pediatric/geriatric pharmacology|Contrast agents, consultation|`Pharmacogenome` struct (CYP2D6 poor/rapid metabolizer, HLA-B*5701), parameter scaling for age (pediatric: allometric, geriatric: reduced clearance); full system review|Trait-based parameter variation (same drug, different patient → different PK)|All modules|

### Phase 3 Summary: What Pharmacology Adds to body-sim

|Component|What it does|How it connects|
|---|---|---|
|`Drug` trait|Universal interface for any pharmacological agent, **multi-target via `effects()`**|Applies to any Phase 2 `Subsystem` target|
|`Effect` trait|Single pharmacological effect on a specific target|Allows one drug to modify multiple subsystems|
|`PKModel`|Computes plasma concentration over time|Feeds concentration into each `Effect::apply()`|
|`InteractionEngine`|Resolves multi-drug PK/PD interactions|Takes `Vec<Box<dyn Drug>>`, collects all `effects()`, outputs net effect|
|`Antiarrhythmic` (Class I–IV)|Modifies cardiac ion channels — **amiodarone as multi-target showcase**|**Direct AF research connection**|
|`PregnancyModifier`|Adjusts PK parameters for maternal physiology|Reuses Phase 2 pregnancy endocrine model|
|`Pharmacogenome`|Patient-specific PK parameter variation|Trait-based scaling across all drug implementations|
|Toxicology module|Poisoning models with antidotes|Extreme-parameter scenarios on existing systems|

### Rust Skills Acquired in Phase 3

|Skill|Where practiced|
|---|---|
|Trait objects (`dyn Drug`, `dyn Effect`)|Drug collections, combination therapy, multi-target effects|
|Modifier/decorator pattern|Drug as wrapper on existing subsystems|
|Strategy pattern with closures|Different drug mechanisms as interchangeable closures|
|Complex enum dispatch|Drug classification hierarchies|
|Cross-module integration|Every drug touches 2+ Phase 2 modules|
|Builder pattern|PK parameter assembly, patient profile construction|
|Error handling with Result|Treatment response vs adverse effect vs toxicity|
|HashMap for lookup tables|Drug-receptor binding, CYP450 substrate mapping|
|Trait-based parameter variation|Pharmacogenomics, age-dependent scaling|
|Integration testing|Multi-drug scenarios, clinical case simulations|

---

## Phase 4: System Integration (Year 4–6, Semester 7–12)

> **Note:** This phase is an outline only — to be detailed during Year 3 based on actual clinical rotation schedules and body-sim progress. Week counts and integration targets below are preliminary estimates.

**Goal:** Connect Phase 2 mechanisms + Phase 3 drug layer into organ-system-level simulations. Each clinical rotation = build + refine that system. Input/output units managed globally via `units/` module. Systems connect through `Subsystem` trait. Drug effects available on every system via `Drug` trait.

### Year 4 (Semester 7–8)

|Rotation|Weeks|System to build|Integration target|
|---|---|---|---|
|Cardiology, Heart Surgery, Angiology, Vascular Surgery|5|`CardiovascularSystem` — connect electrophys → mechanics → hemodynamics → vascular → regulation|Core loop: heart generates pressure → vessels distribute flow → baroreceptors regulate. **+ Phase 3 antiarrhythmics, antihypertensives, anticoagulants**|
|Internal Medicine I (Metabolism, Endocrinology, GI, Nephrology)|5|`MetabolicSystem` — connect GI absorption → insulin/glucagon → renal excretion → acid-base|Nutrient input → hormonal regulation → renal output. **+ Phase 3 antidiabetics, diuretics, PPIs**|
|Pulmonology & Thoracic Surgery|3|`RespiratorySystem` — connect ventilation → gas exchange → transport → chemoreceptor control|Connect to CV system (pulmonary circulation). **+ Phase 3 bronchodilators, ICS**|
|Emergency Medicine|2|`ShockModel` — hemorrhagic, cardiogenic, septic|Multi-system failure scenarios. **+ Phase 3 vasopressors, antidotes**|
|Dermatology|3|`SkinSystem` — thermoregulation, barrier function|Connect to CV (skin circulation) + neuro (thermoreceptors)|
|Ophthalmology|3|`VisualSystem` — retina → pathway → cortex|Standalone sensory pipeline|
|ENT|2|`AudioVestibularSystem`|Standalone sensory pipeline|
|Surgery|4|Stress response model: surgical trauma → neuroendocrine activation|CV + endocrine + immune integration. **+ Phase 3 anesthetic PK models**|
|Traumatology & Orthopedics|4|`MusculoskeletalSystem` — bone, skeletal muscle, reflexes|Connect to neuro (motor) + endocrine (Ca²⁺, GH). **+ Phase 3 bisphosphonates, muscle relaxants**|
|Medical Imaging|2|Visualization module upgrade — WASM output|`viz/` module enhancement|
|Oral Surgery|1|—|—|
|Lab Medicine|1|Diagnostic output: blood gas, CBC, metabolic panel from simulation|Test harness: run simulation → generate lab values|
|Clinical Pharmacology|2|Phase 3 `InteractionEngine` refinement — polypharmacy clinical cases|**Phase 3 integration testing with real clinical scenarios**|
|Clinical ECG|—|ECG generator upgrade with pathological patterns|Enhance cardiovascular module|

### Year 5 (Semester 9–10)

|Rotation|Weeks|System to build|Integration target|
|---|---|---|---|
|Internal Medicine II (Hematology, Infectology, Immunology, Rheumatology)|5|`ImmuneSystem` — innate + adaptive, `HematopoieticSystem`|Connect to infection model, inflammation cascade. **+ Phase 3 antibiotics, immunosuppressants**|
|Neurology & Neurosurgery|4|`NervousSystem` — full CNS integration (sensory + motor + autonomic)|Connect to every other system via autonomic pathway. **+ Phase 3 antiepileptics, neuropsych drugs**|
|Pediatrics|5|`DevelopmentModel` — growth curves, organ maturation parameters|Age-dependent parameter scaling across all systems. **+ Phase 3 pediatric PK scaling**|
|Obstetrics & Gynecology|4|`PregnancyModel` — maternal CV adaptation, fetal circulation|Modified CV + endocrine + renal. **+ Phase 3 PregnancyModifier, teratogenicity**|
|Psychiatry|4|Neurotransmitter balance model, psychopharmacology|Extend neuro module. **+ Phase 3 SSRI, antipsychotics, mood stabilizers**|
|Intensive Therapy & Anaesthesiology|3|`CriticalCareSimulator` — ventilator model, vasopressor response|**Multi-system real-time simulation + Phase 3 full drug stack**|
|Sports Medicine|1|Exercise physiology refinement|Full integration stress test|
|Urology|3|Renal system extension — obstruction, renal failure model|Enhance renal module. **+ Phase 3 diuretics**|
|Oncology|2|Cell growth model — uncontrolled proliferation|Cell biology module extension. **+ Phase 3 anticancer drugs**|
|Public Health|3|Population-level parameter distributions|Statistical layer|
|Clinical Genetics|2|Genetic modifiers on system parameters|**+ Phase 3 Pharmacogenome integration**|
|Medical Rehabilitation|1|Recovery curves, physiotherapy response|Time-dependent parameter restoration|
|Forensic Medicine|2|Post-mortem parameter decay, toxicology scenarios|Systems running in reverse/degradation. **+ Phase 3 toxicology module**|

### Year 6 (Semester 11–12) — Final Integration

|Rotation|Weeks|Goal|
|---|---|---|
|Internal Medicine|8|Full-body simulation: patient case → set parameters → apply drugs → run all systems → generate clinical findings|
|Surgery|6|Surgical stress model, anesthesia effects, recovery|
|Pediatrics|6|Age-scaled full-body simulation with pediatric drug dosing|
|OB/GYN|4|Pregnancy full simulation (maternal + fetal) with drug safety modeling|
|Neurology|3|Neurological exam simulation|
|Psychiatry|3|Behavioral model integration with psychopharmacology|
|Emergency|2|Acute scenario simulator (MI, PE, stroke, trauma) with emergency drug protocols|
|Facultative (6 weeks)|6|**WASM web demo**, documentation, portfolio polish|

---

## Testing & Validation Strategy

### Unit Tests (per module)

- Every public function has at least one test
- Edge cases: zero inputs, maximum values, negative values where applicable
- Property-based testing for mathematical functions (e.g., Nernst equation)

### Validation Tests (`validation/` directory)

- Golden-file tests: known input → expected output compared against textbook/published values
- Each section has its own validation data files (CSV or JSON)
- Tolerance ranges defined per measurement (e.g., GFR: 90-130 mL/min for "normal")

### Integration Tests (`tests/`)

- Multi-module scenarios: exercise response, hemorrhagic shock, drug administration
- Clinical case tests: set pathological parameters → verify system response matches expected clinical picture
- Phase 3: drug interaction scenarios verified against known interaction profiles

### Benchmark Tests (`benches/`)

- Per-module step performance
- Full-system simulation timing
- Regression tracking across commits

---

## Final Deliverable

A Rust crate (`body-sim`) that:

1. Models the human body as interconnected physiological systems
2. Each system built from mechanism-level components (Phase 2)
3. Drug effects layer modifies any system through typed interfaces — **including multi-target drugs via `Effect` trait** (Phase 3)
4. Systems communicate through typed interfaces (Subsystem trait)
5. Units enforced at compile time (newtype pattern)
6. Can simulate clinical scenarios (set pathological parameters + drug regimen → observe system response)
7. Supports polypharmacy simulation with interaction detection (InteractionEngine)
8. Patient-specific modeling via Pharmacogenome and age scaling
9. Outputs to CSV/JSON for analysis, and WASM for browser demo
10. Fully tested, **validated against published physiological values**, documented, benchmarked

**Portfolio presentation:**

- GitHub repo with clean commit history following the curriculum
- README with physiological and pharmacological background for each module
- WASM demo: interactive browser simulation with drug intervention controls
- Connection to TDK research (AF ablation simulation + antiarrhythmic drug modeling as flagship feature)
- `validation/` directory demonstrating rigorous testing against published data