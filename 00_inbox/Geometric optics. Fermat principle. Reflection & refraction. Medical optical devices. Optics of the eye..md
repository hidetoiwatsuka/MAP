![02_Geometric_optics_20250917.pdf](00_Assets/Attachments/02_Geometric_optics_20250917.pdf)

# Geometric Optics — Medical Biophysics I

> **Lecturer:** Miklós Kellermayer | **Date:** 17 Sept 2025 | **Dept:** Biophysics & Radiation Biology, Semmelweis University

---

## 1. What is Geometric Optics?

**Core idea:** When the aperture is **much larger than λ**, we can ignore wave behavior and treat light as **rays** (straight lines).

|Concept|Meaning|Why it matters|
|---|---|---|
|**Light ray**|A mathematical line representing energy propagation direction|Simplifies analysis — no need for wave equations|
|**Optical axis**|Line connecting the midpoints of optical components (lenses, mirrors)|Reference line for all ray diagrams|
|**Principle of reversibility**|Any ray path can be traced in either direction|Lets you work backwards from image to object|

---

## 2. Reflection

> **One-liner:** Light bounces off a surface — angle in = angle out.

- **α** = angle of incidence (measured from the **normal**, not the surface)
- **α'** = angle of reflection
- **Law:** α = α'
- All three — incident ray, reflected ray, and normal — lie in the **same plane**

---

## 3. Refraction & Snell's Law

> **One-liner:** Light bends when crossing a boundary between two media with different refractive indices.

### Snell's Law

$$\frac{\sin\alpha}{\sin\beta} = \frac{c_1}{c_2} = \frac{n_2}{n_1}$$

|Symbol|Meaning|
|---|---|
|α|Angle of incidence|
|β|Angle of refraction|
|n₁, n₂|Refractive indices of medium 1 and 2|
|c₁, c₂|Speed of light in medium 1 and 2|

**Key intuition:** When light enters a **denser** medium (n₂ > n₁), it bends **toward** the normal (β < α).

### Fermat's Principle of Least Time

- Light doesn't travel the shortest **distance** — it travels the shortest **time**
- In the slower (denser) medium, light minimizes its path length
- This is **why** refraction happens: it's the time-optimal route

---

## 4. Dispersion

> **One-liner:** Refractive index depends on frequency → different colors bend differently.

- **Higher frequency** (violet) → **higher n** → bends more
- **Lower frequency** (red) → **lower n** → bends less
- A **prism** exploits this to decompose white light into its spectrum

---

## 5. Refractometry (Analytical Application)

> **One-liner:** Use the critical angle to measure refractive index → determine solute concentration.

### How it works

At **grazing incidence** (α = 90°), sin(90°) = 1, so Snell's law simplifies to:

$$n_1 = n_2 \sin\beta_h$$

where β_h is the **critical angle**.

### Concentration measurement

For dilute solutions:

$$n_1 = n_0 + k \cdot c$$

|Symbol|Meaning|
|---|---|
|n₀|Refractive index of pure solvent|
|k|Proportionality constant|
|c|Solute concentration|

### Conditions of applicability

- Sample must be **liquid**
- Sample must be **transparent**
- Sample n must be **less than** the prism n

---

## 6. Total Internal Reflection (TIR)

> **One-liner:** When light tries to leave a dense medium at too steep an angle, it gets completely reflected back.

- Occurs in the **denser** medium (n₂ > n₁)
- When β > β_h (critical angle) → **no refraction**, 100% reflection
- **Snell window:** From underwater, you see the entire sky compressed into a cone defined by the critical angle; outside that cone = mirror-like reflection of the bottom

### Biomedical Application: Optical Fibers & Endoscopy

**Fiber structure:**

|Component|Property|
|---|---|
|**Core**|High refractive index — carries the light|
|**Coating (cladding)**|Low refractive index — ensures TIR|
|**Ordered bundle**|Maintains spatial arrangement → transmits images faithfully|

**Endoscopy types and targets:**

|Procedure|Target|
|---|---|
|Arthroscopy|Joints|
|Bronchoscopy|Trachea & bronchi|
|Colonoscopy|Colon|
|Colposcopy|Vagina & cervix|
|Cystoscopy|Urinary bladder, urethra, prostate|
|EGD|Upper GI tract (esophagus → duodenum)|
|ERCP|Biliary tract & pancreatic duct|
|Laparoscopy|Abdominal organs (stomach, liver, ovaries)|
|Laryngoscopy|Larynx|
|Proctoscopy|Rectum & sigmoid colon|
|Thoracoscopy|Pleura, mediastinum, pericardium|

**Two objectives:**

1. **Diagnostic** — visual inspection, biopsy, contrast agent delivery
2. **Therapeutic** — surgery, cauterization, foreign body removal

---

## 7. Lenses & Image Formation

> **One-liner:** A lens = infinitely many prisms → bends parallel rays to a focal point.

### Three principal rays for ray diagrams

|Ray|Rule|
|---|---|
|**Parallel ray**|Enters parallel to axis → exits through focal point F|
|**Central ray**|Passes through lens center → undeviated|
|**Focal ray**|Enters through F → exits parallel to axis|

### Lens Equation

$$D = \frac{1}{f} = \frac{1}{t} + \frac{1}{k}$$

|Symbol|Meaning|
|---|---|
|D|Optical power (diopters, m⁻¹)|
|f|Focal length|
|t|Object distance|
|k|Image distance|

### Magnification

$$N = \frac{K}{T} = \frac{k}{t}$$

- **N > 1** (magnified) when object is within **2f**
- **Real image** — can be projected on a screen (forms on the opposite side)
- **Virtual image** — cannot be projected; needs an accessory lens to observe

---

## 8. Compound Microscope

> **One-liner:** Two lenses in series — objective makes a real intermediate image, eyepiece magnifies it into a virtual image.

**Image formation chain:**

```
Object → [Objective lens] → Intermediate real image (magnified, inverted)
       → [Eyepiece lens]  → Virtual image (further magnified)
       → [Eye lens]       → Real image on retina
```

- Final image: **magnified, inverted, virtual**
- The retina acts as the projection screen
- Conventional viewing distance = **25 cm**

---

## 9. Optics of the Human Eye

> **One-liner:** The eye is a compound lens system (total ~62 dptr) that forms a demagnified, inverted, real image on the retina.

### Refractive indices of eye components

|Structure|n|Contribution|
|---|---|---|
|Air|1.00|—|
|**Cornea**|**1.37**|**~48 dptr** (largest single contributor!)|
|Aqueous humour|1.33|−6 dptr|
|Lens|1.41|8 + 12 dptr|
|Vitreous body|1.34|—|

**Why the cornea dominates:** The refractive index difference (n − n') is greatest at the **air–cornea** interface. D = (n − n') / r.

### Accommodation

||Farsight (relaxed)|Nearsight (active)|
|---|---|---|
|Ciliary muscle|Relaxed|Contracted|
|Zonules (ligaments)|Stretched (taut)|Relaxed (slack)|
|Lens shape|Flattened|Bulged (more curved)|
|Effect|Lower D → focus on distant objects|Higher D → focus on near objects|

**Accommodation power** = difference in diopters between the far point and near point of the eye.

### Refraction Errors

|Condition|Problem|Image falls...|Correction|
|---|---|---|---|
|**Myopia** (nearsightedness)|Eye too long / lens too strong|In front of retina|**Negative (concave) lens**|
|**Hypermetropia** (farsightedness)|Eye too short / lens too weak|Behind retina|**Positive (convex) lens**|

---

## 10. Optical Trapping (Laser Tweezers)

> **One-liner:** Refraction creates photon momentum change → force → you can grab microscopic objects with focused light.

### Physics

- Refraction through a microsphere changes photon momentum: **ΔP**
- Force on the particle: **F = ΔP / Δt**

### Two forces in the trap

|Force|Direction|Origin|
|---|---|---|
|**Gradient force**|Toward beam focus (inward)|Intensity gradient of focused laser|
|**Scatter force** (light pressure)|Along beam propagation (downward)|Photon momentum transfer|

**Equilibrium** between these two forces = **stable trap**

### Applications

- Trapping **polystyrene microspheres** (3 μm)
- Trapping **bacterial cells** (E. coli)
- Single-molecule force measurements in biophysics

---

## Quick Reference: Key Equations

|Equation|Name|Context|
|---|---|---|
|α = α'|Law of reflection|Reflection|
|sin α / sin β = n₂ / n₁|Snell's law|Refraction|
|n₁ = n₂ sin β_h|Critical angle|TIR / Refractometry|
|n₁ = n₀ + k·c|Concentration–refractive index|Refractometry|
|D = 1/f = 1/t + 1/k|Lens equation|Lenses|
|N = k / t|Magnification|Lenses|
|D = (n − n') / r|Surface refractive power|Eye optics|
|F = ΔP / Δt|Optical force|Optical trapping|