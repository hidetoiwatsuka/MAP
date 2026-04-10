
## 1. What is an ECG?

A recording of voltage associated with the electrical activity of the heart, measured between defined body-surface electrode positions as a function of time: U(t).

💡 心臓の電荷分布は**電気双極子**で近似できる。正負の電荷数が等しいためモノポール項=0、最初の非ゼロ項が双極子。体表面では高次項（四重極以上）は距離依存性により無視可能。

---

## 2. The cardiac dipole and multipole expansion

The electric field of the heart results from the combined activity of all cardiac muscle cells. At any instant, the net charge distribution can be approximated by a **dipole-moment vector** (cardiac dipole) that changes direction and magnitude quasi-periodically with the cardiac cycle.

In a homogeneous medium the dipole produces a symmetric field. In reality, tissues of different conductivity (lungs, ribs, muscle, fat) distort the field — hence the equipotential contour map on the chest is asymmetric.

💡 多重極展開で、双極子の電場はモノポールより距離の3乗で減衰し、四重極はさらに速く減衰する。だから体表面では双極子近似で十分。

---

## 3. Action potential differences: skeletal vs. cardiac muscle

### Skeletal muscle

- Action potentials have **uniform duration** (~1–2 ms)
- Depolarization and repolarization fronts propagate in the **same direction**
- Surface electrodes detect waves of **opposite polarity**

### Ventricular cardiac muscle

- Action potential duration **decreases from endocardium → epicardium**
- Epicardial cells (depolarized later) repolarize **earlier** than endocardial cells
- Repolarization front propagates **inward** (opposite to depolarization)
- Surface electrodes detect waves of the **same polarity**

### Atrial cardiac muscle

- Behaves like skeletal muscle: depolarization and repolarization waves have **opposite polarity**

💡 これがQRS complexとT waveが同じ向き（Lead IIで共に上向き）になる物理的理由。虚血で心内膜-心外膜間の活動電位持続時間勾配が崩れるとT波が反転する — 臨床的に極めて重要。

---

## 4. The normal ECG waveform

The cardiac conduction sequence and corresponding ECG features:

|Step|Event|ECG feature|
|---|---|---|
|1|SA node fires|(too small to detect)|
|2|Atrial depolarization|**P wave**|
|3|AV node delay|**PQ interval**|
|4|Ventricular depolarization via His → Tawara → Purkinje|**QRS complex**|
|5|Ventricular repolarization|**T wave**|
|6|Rest until next SA node firing|**TP segment**|

The atrial repolarization wave is hidden within the QRS complex. Signals from conduction elements (SA node, AV node, His bundle) are below the noise level.

💡 ECGは心房信号と心室信号の重ね合わせ。伝導系の電気信号はμVオーダーで通常のECGの分解能では見えない。

---

## 5. The integral vector

At any moment, all elementary dipoles on the depolarization/repolarization wavefront are summed vectorially → **integral vector**. Its arrowhead traces loops in 3D space during the cardiac cycle.

The integral vector constructed from the **R wave** amplitudes is called the **Mean Electrical Axis (MEA)**. The angle α between MEA and the horizontal is the **angle of the mean electrical axis**.

💡 積分ベクトルの軌跡を可視化したものがベクトル心電図（VCG）。リサージュ図形に似た閉ループになる。

---

## 6. Electrodes

### Active (different) electrode

Electric potential changes continuously during the cardiac cycle. All R, L, F, C1–C6 electrodes are active.

### Inactive (indifferent) electrode — Wilson Central Terminal (CT)

$$\phi_{CT} = \frac{\phi_L + \phi_R + \phi_F}{3} \approx 0$$

Three limb electrodes connected through equal resistors (100 kΩ) to a common point. Potential variations cancel out, providing a near-constant zero reference.

💡 体表面に電位が一定の点は存在しないので、3点の電位平均を取って「仮想的なゼロ電位」を作る工夫。

---

## 7. Types of leads

### 7a. Einthoven's standard limb leads (bipolar, frontal plane)

Potential difference between two active electrodes:

|Lead|Electrodes|Voltage|
|---|---|---|
|I|Left arm − Right arm|U_I = φ_L − φ_R|
|II|Left foot − Right arm|U_II = φ_F − φ_R|
|III|Left foot − Left arm|U_III = φ_F − φ_L|

These three points form **Einthoven's triangle** (equilateral, heart at center).

Key relation: **U_II = U_I + U_III** (Einthoven's law)

💡 3誘導のうち独立なのは2つだけ。任意の2つから3つ目を計算できる。

### 7b. Wilson's chest leads (unipolar, horizontal plane)

Six precordial electrodes (C1–C6) measured against CT:

$$U_{V_n} = \phi_{C_n} - \frac{\phi_L + \phi_R + \phi_F}{3}$$

### 7c. Goldberger's augmented leads (pseudo-unipolar, frontal plane)

The measured limb electrode is **omitted** from CT → "truncated CT":

|Lead|Voltage|
|---|---|
|aVR|φ_R − (φ_L + φ_F)/2|
|aVL|φ_L − (φ_R + φ_F)/2|
|aVF|φ_F − (φ_R + φ_L)/2|

"a" = augmented (1.5× amplitude gain vs. true unipolar). The truncated CT is not perfectly constant → hence "pseudo-unipolar".

💡 なぜGoldbergerは測定電極をCTから外すのか → 外さないと信号が極めて小さくなる。外すと振幅が1.5倍になるが、参照電極の時間安定性がやや犠牲になる。

---

## 8. The 12-lead ECG system

|Plane|Leads|Count|
|---|---|---|
|Frontal|I, II, III, aVR, aVL, aVF|6|
|Horizontal|V1–V6|6|

Together: 12 spatial projections of the cardiac dipole's temporal variation.

💡 各誘導は心臓の異なる「窓」。例えばV1–V2は右室・中隔、V5–V6は左室側壁を主に反映する。

---

## 9. Vectorcardiography

Maps the 3D trajectory of the integral vector using:

|Axis|Lead|
|---|---|
|x|I|
|y|aVF|
|z|−V2|

Three planar projections: frontal (xy), horizontal (xz), sagittal (yz). Produces closed loops (Lissajous-like curves).

---

## 10. Construction of MEA (practical method)

1. Measure R-wave amplitude in any two Einthoven leads (e.g. I and II)
2. Map these amplitudes with correct polarity onto the corresponding sides of Einthoven's triangle (conventionally at the midpoint)
3. Construct perpendiculars at the endpoints of each lead vector
4. The intersection of these perpendiculars defines the endpoints of the **integral vector**
5. Measure angle α between MEA and horizontal with a protractor

💡 正常範囲は−30°〜+90°。左軸偏位（<−30°）や右軸偏位（>+90°）は心肥大や脚ブロックを示唆する。

---

## 11. ECG recorder: instrumentation

### Differential amplifier

- ECG signal: ~mV order
- Power-line noise (50 Hz): ~several volts, uniform over body ("common mode")
- Differential amplifier amplifies only the **difference** between two inputs:

$$(U_I + U_N) - (U_N) = U_I$$

The N electrode (right foot) connects to instrument ground.

### Frequency band

- Lower cutoff: **0.2–0.3 Hz** — removes baseline drift from electrode-skin galvanic effects
- Upper cutoff: **80–100 Hz** — removes high-frequency noise

### Optional filters

- 50 Hz notch filter (power-line hum)
- 35 Hz low-pass (muscle fibrillation, e.g. exercise ECG) — used only when justified, as it deforms the signal

### Calibration

- Standard: **1 mV = 10 mm** (sensitivity 1 cm/mV)
- Paper speed: **25 mm/s** or 50 mm/s

💡 差動増幅器がECGの根幹技術。同相除去比（CMRR）が高いほど、数Vのノイズの中からmVの信号を正確に取り出せる。

---

## 12. Typical ECG values (Lead II, healthy adult)

|Parameter|Value|
|---|---|
|Heart rate|60–100 bpm (avg ~75)|
|P wave duration|80–120 ms|
|P wave amplitude|0.1–0.3 mV|
|PQ interval|120–200 ms|
|QRS duration|60–100 ms|
|R wave amplitude (Lead II)|0.5–1.5 mV|
|ST segment|~80 ms, isoelectric|
|QT interval|350–440 ms|
|T wave amplitude|0.1–0.5 mV|

---

## Summary: logical structure

```
ECG = U(t) recording of the cardiac dipole's body-surface projection
  │
  ├─ Physical basis
  │    ├─ Multipole expansion → dipole approximation
  │    ├─ Skeletal vs cardiac AP duration → polarity of waves
  │    └─ Integral vector (sum of elementary dipoles at wavefront)
  │
  ├─ Conduction pathway → waveform
  │    SA → P │ AV delay → PQ │ His/Purkinje → QRS │ repol → T
  │
  ├─ Electrode system
  │    ├─ Active electrodes (R, L, F, C1–C6)
  │    └─ Inactive reference: Wilson CT = (φL+φR+φF)/3
  │
  ├─ 12-lead system
  │    ├─ Frontal: Einthoven (bipolar) + Goldberger (pseudo-unipolar)
  │    └─ Horizontal: Wilson (unipolar)
  │
  ├─ MEA construction
  │    R-wave amplitudes on Einthoven's triangle → integral vector → angle α
  │
  └─ Instrumentation
       Differential amplifier + bandpass (0.2–100 Hz) + notch filter (50 Hz)
```