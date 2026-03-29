---
tags:
  - rust
  - medicine
  - plan
---
# Rust × Medicine — 6-Year Learning Plan

**Medical Student · Semmelweis University · English Medicine Programme**

> **Core concept:** Rust is not learned separately from medicine — it is learned _through_ medicine. Every biological concept becomes a data structure. Every physiological process becomes a simulation. The goal is always to understand Rust more deeply. Medicine is the material.

---

## Philosophy

|Principle|Detail|
|---|---|
|**Rust understanding is the goal**|Medicine provides the problems. Rust provides the tools to model them.|
|**Medical school is the curriculum**|Lecture content drives what gets implemented, not the reverse|
|**Working code over perfect code**|A simulation that runs and teaches is worth more than elegant unfinished code|
|**GitHub as research portfolio**|Every project is public, documented, and accumulates over 6 years|
|**Depth over breadth**|One well-understood cardiac model beats five half-finished ones|

---

## Two Repositories, One Mission

The project lives across two GitHub repositories with distinct purposes:

```
medknowledge/        ← Knowledge modelling — biological concepts as Rust types
rust-physiology/     ← Simulation — physiological processes as running code
```

They are complementary. `medknowledge` models _what things are_. `rust-physiology` models _how things behave_. Eventually, `rust-physiology` imports `medknowledge` as a crate — real enzyme parameters (Km, Vmax) loaded from JSON feed directly into simulations.

---

## Repository 1: `medknowledge`

### Concept

Every biological fact learned in medical school is encoded as a Rust type. The act of writing the struct forces precise thinking about what a concept actually _is_. The act of implementing traits forces thinking about what it _does_.

This is not a database tool. It is a Rust learning exercise that happens to produce a medical knowledge base.

### How Rust concepts map to medical knowledge

|Rust concept|Medical representation|What you learn|
|---|---|---|
|`struct`|Ion, Enzyme, Drug, Receptor|How to model real-world entities with fields|
|`enum`|`ChannelState { Open, Closed, Inactivated }`|How to represent mutually exclusive states safely|
|`trait`|`Transporter`, `Inhibitable`, `Quizzable`|How to define shared behaviour across different types|
|`impl Display`|Flashcard output for any struct|How traits enable polymorphism|
|`Vec<T>` / `HashMap`|Collections of enzymes, ions, drugs|Generics and type parameters in practice|
|`Result<T, E>`|Enzyme reaction failure (inhibition, substrate depletion)|Error handling as part of the type system|
|Ownership / borrowing|Enzyme holds substrate exclusively during catalysis|Why Rust's memory model exists — it mirrors physical reality|
|JSON + `serde`|Loading knowledge data from `data/*.json`|Serialisation, derive macros, real-world crate usage|
|`#[cfg(test)]`|Quiz mode: assert known Km values|How Rust's test system works|

### Repository structure

```
medknowledge/
├── src/
│   ├── main.rs              ← CLI: search, quiz, simulate kinetics
│   ├── biochem/
│   │   ├── enzyme.rs        ← Enzyme struct + Michaelis-Menten
│   │   ├── pathway.rs       ← Metabolic pathway as a graph
│   │   └── kinetics.rs      ← Inhibition types, Hill equation
│   ├── physiology/
│   │   ├── ion.rs           ← Ion struct, Nernst equation
│   │   └── channel.rs       ← ChannelState enum, gating logic
│   └── pharmacology/
│       └── drug.rs          ← Drug struct, mechanism of action
├── data/
│   ├── enzymes.json         ← Accumulated knowledge: add after every lecture
│   ├── ions.json
│   └── drugs.json
└── tests/
    └── knowledge_tests.rs   ← Assert known values: Km of hexokinase = 0.1 mM
```

### The data accumulation loop

```
Attend lecture on enzyme X
        ↓
Add entry to data/enzymes.json
        ↓
cargo run -- quiz enzyme        ← CLI quizzes you from the JSON
        ↓
cargo run -- kinetics hexokinase --substrate 0.5   ← compute v at [S]=0.5mM
        ↓
Knowledge is now a living parameter, not a flashcard
```

### Core code: first implementation (Week 1–4 of Phase 1)

```rust
// src/biochem/enzyme.rs

#[derive(Debug, serde::Deserialize)]
pub struct Enzyme {
    pub name: String,
    pub km_mm: f64,           // Michaelis constant (mM)
    pub vmax: f64,            // Maximum reaction velocity
    pub location: String,     // "cytosol", "mitochondria", "lysosome"
    pub inhibitors: Vec<String>,
    pub cofactors: Vec<String>,
}

impl Enzyme {
    /// Michaelis-Menten equation
    /// Writing this once makes the equation permanent knowledge
    pub fn velocity(&self, substrate_conc: f64) -> f64 {
        (self.vmax * substrate_conc) / (self.km_mm + substrate_conc)
    }

    /// At Km, velocity is exactly half of Vmax — encode this as a test
    pub fn at_km(&self) -> f64 {
        self.velocity(self.km_mm)  // always returns vmax / 2
    }
}

impl std::fmt::Display for Enzyme {
    fn fmt(&self, f: &mut std::fmt::Formatter) -> std::fmt::Result {
        write!(
            f,
            "[{}]\n  Km = {} mM | Vmax = {}\n  Location: {}\n  Inhibitors: {}\n  Cofactors: {}",
            self.name,
            self.km_mm,
            self.vmax,
            self.location,
            self.inhibitors.join(", "),
            self.cofactors.join(", ")
        )
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn velocity_at_km_is_half_vmax() {
        let hexokinase = Enzyme {
            name: "Hexokinase".into(),
            km_mm: 0.1,
            vmax: 1.0,
            location: "cytosol".into(),
            inhibitors: vec!["Glucose-6-phosphate".into()],
            cofactors: vec!["ATP".into(), "Mg²⁺".into()],
        };
        let v = hexokinase.at_km();
        assert!((v - 0.5).abs() < 1e-10);
    }
}
```

### Example data entry (add after each lecture)

```json
[
  {
    "name": "Hexokinase",
    "km_mm": 0.1,
    "vmax": 1.0,
    "location": "cytosol",
    "inhibitors": ["Glucose-6-phosphate"],
    "cofactors": ["ATP", "Mg2+"]
  },
  {
    "name": "Pyruvate kinase",
    "km_mm": 0.4,
    "vmax": 1.0,
    "location": "cytosol",
    "inhibitors": ["ATP", "Alanine"],
    "cofactors": ["K+", "Mg2+"]
  }
]
```

---

## Repository 2: `rust-physiology`

### Concept

Where `medknowledge` models _what_ biological entities are, `rust-physiology` models _how_ they behave dynamically over time. These are simulations — differential equations, numerical integration, emergent phenomena.

Eventually imports from `medknowledge` so simulations run with real parameter values.

---

## Phase 1 — Rust Fundamentals + First Neuron Model

**Timeline:** Year 1, Months 1–3 **Status:** 🔴 Starting now

### Learning Goal

Survive the Rust learning curve. Write the first biologically meaningful simulation. Build `medknowledge` skeleton in parallel.

### Rust Concepts Covered

- Ownership, borrowing, references
- Structs, `impl` blocks, basic traits
- `Display`, `Debug` traits
- File I/O, CSV output
- `serde` + JSON (for `medknowledge` data layer)
- Cargo, crates.io basics

### Projects

#### Week 1–4: Parallel start — Rustbook + medknowledge skeleton

- Read _The Rust Programming Language_, Ch. 1–10
- Simultaneously: scaffold `medknowledge` repo, implement `Enzyme` struct
- Add 5–10 enzymes from current biochemistry lectures to `data/enzymes.json`
- CLI command: `cargo run -- show hexokinase` prints the Display output

#### Week 5–8: Passive Membrane Model (RC Circuit)

The simplest possible neuron — a resistor and capacitor in parallel.

```rust
fn euler_step(v: f64, dt: f64, i_ext: f64) -> f64 {
    let c_m = 1.0;    // membrane capacitance (µF/cm²)
    let g_l = 0.1;    // leak conductance (mS/cm²)
    let e_l = -65.0;  // leak reversal potential (mV)
    let dv = (i_ext - g_l * (v - e_l)) / c_m;
    v + dv * dt
}
```

**Success criterion:** Membrane potential changes in response to external current. Output to CSV.

Add to `medknowledge`: `Ion` struct with intracellular/extracellular concentrations. Nernst equation as a method. Use these values in the model.

#### Week 9–12: Hodgkin-Huxley Model

The full action potential. Na⁺ and K⁺ voltage-gated channels. The shape of an action potential emerging from code is the milestone.

**Success criterion:** A single action potential waveform that matches a physiology textbook figure.

---

## Phase 2 — Cardiac Electrophysiology

**Timeline:** Year 1 (second half) – Year 2 **Status:** 🟡 Planned

### Motivation

Direct connection to TDK research under Dr. Kássa Krisztián István (AF catheter ablation, HPSD/SPSD, voltage mapping). Understanding the computational basis of AF makes reading ablation literature significantly deeper.

### Rust Concepts Covered

- Lifetimes
- Generics and trait bounds
- `Rayon` crate for parallel computation (cell arrays)
- `ndarray` for matrix operations
- `plotters` for in-Rust graph rendering

### Projects

#### Project 2.1: Single Cardiomyocyte Action Potential

Implement the **O'Hara-Rudy (ORd) model** — the standard human ventricular action potential model used in modern electrophysiology research.

Key currents to implement:

- I_Na (fast sodium)
- I_CaL (L-type calcium)
- I_Kr, I_Ks (rapid and slow delayed rectifier potassium)
- I_K1 (inward rectifier)
- I_NaCa (NCX exchanger)

Each current modelled as a struct in `medknowledge/physiology/channel.rs`. Parameters loaded from JSON.

#### Project 2.2: Atrial Cell Network — Reentry Simulation

- 2D grid of coupled atrial myocytes
- Implement gap junction conductance
- Induce reentry by S1-S2 stimulation protocol
- Observe spiral wave formation — the computational correlate of AF

#### Project 2.3: AF Substrate Model

- Implement fibrosis as reduced gap junction conductance in patches
- Compare trigger-based vs. substrate-based AF initiation
- Relate findings directly to Dr. Kássa's LVA (low-voltage area) mapping work

**Research integration:** Bring simulation outputs to lab meetings. Ask Dr. Kássa whether the model parameters match what he observes clinically.

---

## Phase 3 — Pharmacology + Biochemistry + Enzymes

**Timeline:** Year 2–3 **Status:** 🟡 Planned

_Synchronized with biochemistry and pharmacology coursework. `medknowledge` grows significantly during this phase._

### Rust Concepts Covered

- Trait objects (`dyn Trait`)
- Error handling (`Result`, `anyhow`, `thiserror`)
- Benchmarking (`criterion` crate)
- WebAssembly compilation (`wasm-pack`) — run simulations in the browser

### Projects

#### Project 3.1: Antiarrhythmic Drug Simulation

Extend the cardiac model from Phase 2. Add `Drug` struct to `medknowledge`. Model channel block by:

- Class I drugs (Na⁺ channel blockers): flecainide, propafenone
- Class III drugs (K⁺ channel blockers): amiodarone, sotalol

Implement **state-dependent block** — drugs bind differently to open vs. inactivated channels. Use `ChannelState` enum already defined in `medknowledge`.

#### Project 3.2: Enzyme Kinetics Simulator

Build on top of `medknowledge`'s `Enzyme` struct. Extend to:

- Competitive inhibition
- Noncompetitive inhibition
- Uncompetitive inhibition
- Allosteric regulation (Hill equation)

**Output:** CLI parameter sweep — vary [S], [I], Km, Vmax, print velocity table or export to CSV.

#### Project 3.3: Metabolic Pathway Flux

- Glycolysis as a system of ODEs, enzyme parameters from `data/enzymes.json`
- TCA cycle with cofactor tracking (NAD⁺/NADH, FAD/FADH₂)
- ATP yield calculation under normal vs. hypoxic conditions

**Clinical connection:** Simulate cardiac metabolism during ischemia — relevant to understanding myocardial infarction.

---

## Phase 4 — Organ-Level Physiology + Whole-Body Integration

**Timeline:** Year 3–4 **Status:** 🔵 Future

### Rust Concepts Covered

- Async/await (`tokio`)
- Advanced data structure optimisation
- FFI (calling C libraries / Python interop via PyO3)

### Projects

#### Project 4.1: Cardiovascular System — Hemodynamics

- Frank-Starling law: cardiac output as a function of preload
- Windkessel model: aortic compliance and peripheral resistance
- Feedback loop: baroreceptor reflex

#### Project 4.2: Respiratory System

- Alveolar gas exchange (Fick's law)
- Oxygen-hemoglobin dissociation curve (Hill equation)
- Effect of pH, temperature, 2,3-DPG on affinity
- Ventilation/perfusion matching

#### Project 4.3: Renal Physiology

- GFR and filtration dynamics
- Tubular reabsorption: Na⁺, glucose (Tm model)
- Acid-base regulation
- RAAS simulation (renin-angiotensin-aldosterone)

---

## Phase 5 — Clinical Integration + Research Tooling

**Timeline:** Year 5–6 **Status:** 🔵 Future

### Projects

#### Project 5.1: ECG Parser and Arrhythmia Detector

- Parse raw 12-lead ECG data (MIT-BIH Arrhythmia Database format)
- Implement QRS detection (Pan-Tompkins algorithm)
- Classify: sinus rhythm, AF, flutter, VT
- Written entirely in Rust — fast enough for real-time processing

#### Project 5.2: Ablation Data Analysis Tool

- Process electrogram (EGM) signals from EP lab data
- Compute local activation times, fractionation index
- Reconstruct voltage maps from point-by-point catheter data
- Directly useful for Dr. Kássa's research group

#### Project 5.3: Publication and Open-Source Release

- Full rustdoc documentation on every crate
- Publish `medknowledge` to crates.io as a reusable library
- Write a methods paper or short report on one of the simulation projects
- GitHub repositories become a public-facing research portfolio

---

## Full Repository Structure (GitHub)

```
medknowledge/                      ← Repo 1: knowledge modelling
├── src/
│   ├── main.rs                    ← CLI: show, quiz, kinetics commands
│   ├── biochem/
│   │   ├── enzyme.rs              ← Enzyme struct + kinetics
│   │   ├── pathway.rs             ← Metabolic graph structure
│   │   └── kinetics.rs            ← Inhibition, Hill equation
│   ├── physiology/
│   │   ├── ion.rs                 ← Ion struct, Nernst equation
│   │   └── channel.rs             ← ChannelState enum
│   └── pharmacology/
│       └── drug.rs                ← Drug struct, mechanism of action
├── data/
│   ├── enzymes.json               ← Add entry after every biochem lecture
│   ├── ions.json
│   └── drugs.json
└── tests/
    └── knowledge_tests.rs         ← Assert known values

rust-physiology/                   ← Repo 2: simulation
├── neuro/
│   ├── passive_membrane/          ← Phase 1: RC circuit
│   └── hodgkin_huxley/            ← Phase 1: Full HH model
├── cardiac/
│   ├── ord_model/                 ← Phase 2: O'Hara-Rudy single cell
│   ├── cell_network/              ← Phase 2: 2D reentry simulation
│   └── af_substrate/              ← Phase 2: AF model
├── pharmacology/
│   ├── channel_block/             ← Phase 3: Drug-channel interaction
│   └── pk_pd/                     ← Phase 3: PK/PD modeling
├── biochemistry/
│   ├── enzyme_kinetics/           ← Phase 3: simulation using medknowledge data
│   └── metabolism/                ← Phase 3: Glycolysis + TCA
├── hemodynamics/                  ← Phase 4
├── respiratory/                   ← Phase 4
├── renal/                         ← Phase 4
└── clinical/
    ├── ecg_parser/                ← Phase 5
    └── ablation_tools/            ← Phase 5
```

---

## Weekly Rhythm

|Day|Activity|
|---|---|
|Monday|Read: 1 chapter of Rust Book or physiology paper|
|Tuesday|Implement: write new code based on Monday's reading|
|Wednesday|Debug + test: make it actually work|
|Thursday|Connect to medicine: add lecture content to `data/*.json` in `medknowledge`|
|Friday|Commit + document: push to GitHub with a proper README update|
|Weekend|Optional: explore extensions, read related papers|

**Target: 2–3 hours on weekdays, 1–2 hours on weekends = ~12–15 hours/week**

---

## Key Resources

### Rust

- [The Rust Programming Language](https://doc.rust-lang.org/book/) — free, essential
- [Rust by Example](https://doc.rust-lang.org/rust-by-example/)
- [Scientific Computing in Rust](https://www.scientificcomputing.rs/) — niche but relevant
- [serde.rs](https://serde.rs/) — for JSON data loading in `medknowledge`

### Computational Physiology

- Keener & Sneyd, _Mathematical Physiology_ (Vol. 1 & 2) — the reference textbook
- O'Hara et al. (2011) — original ORd model paper (PLOS Comp Bio)
- Hodgkin & Huxley (1952) — the original paper is readable and worth reading

### Electrophysiology (TDK-relevant)

- Nattel et al. — AF mechanisms reviews
- Dr. Kássa's own publications — read with the simulation context in mind

---

## Success Metrics (End of 6 Years)

- [ ] `medknowledge` contains 100+ biological entities (enzymes, ions, channels, drugs) accumulated across 6 years of lectures
- [ ] `medknowledge` published to crates.io and used by `rust-physiology` as a dependency
- [ ] 10+ implemented physiological simulations in `rust-physiology`
- [ ] Ablation data analysis tool used in actual lab work with Dr. Kássa
- [ ] At least 1 conference presentation or paper involving computational methods
- [ ] Rust proficiency sufficient to read and contribute to open-source scientific computing projects

---

_Last updated: 2026-03-25_ _Hideto Iwatsuka · Semmelweis University · English Medicine Programme, Year 1_