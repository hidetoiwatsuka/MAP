![[immun s, thymus, tonsils.pdf]]



## classification of Lymphatic Organs and Tissues
| primary lymphatic organ                                              | secondary lymphatic organs and tissues |
| -------------------------------------------------------------------- | -------------------------------------- |
| provide stem cells to mature to T or B cells                         | site where most immune response occur  |
| red bone marrow gives rise to T cells                                | Encapsulated : lymph nodes and spleen  |
| thymus gland, cite where pre T cells from the red bone marrow mature | non-Encapsulated : lymphatic lodules   |

### Thymus

![Pasted image 20260324114208.png](Pasted%20image%2020260324114208.png)(100a)

#### capsule : thin dense connective tissue
![Pasted image 20260324120234.png](Pasted%20image%2020260324120234.png)(100a)

#### cortex & medulla (Lobule)

```rust
// ============================================================
//  T Cell Selection in the Thymus
//  胸腺におけるT細胞の選択
// ============================================================

fn main() {
    // --- Positive Selection (Thymus Cortex) ---
    // 陽性選択（胸腺皮質）

    let tcr_recognizes_self_mhc = true;
    let mhc_class = "ClassII"; // "ClassI" or "ClassII"

    if tcr_recognizes_self_mhc {
        // survive → proceed to medulla (negative selection)
        // 生存 → 髄質へ進む（陰性選択）

        if mhc_class == "ClassII" {
            println!("Recognized MHC class II → become CD4+");
            // MHCクラスII認識 → CD4+になる
        } else if mhc_class == "ClassI" {
            println!("Recognized MHC class I → become CD8+");
            // MHCクラスI認識 → CD8+になる
        }
    } else {
        // no survival signal → apoptosis (death by neglect)
        // 生存シグナルなし → アポトーシス（放置死）
        println!("No MHC recognition → apoptosis (death by neglect)");
    }

    // --- Negative Selection (Thymus Medulla) ---
    // 陰性選択（胸腺髄質）

    let self_antigen_affinity = "low"; // "high" or "low"

    if self_antigen_affinity == "high" {
        // too dangerous (would attack own body) → apoptosis
        // 危険すぎる（自己を攻撃する恐れ）→ アポトーシス
        println!("High self-antigen affinity → apoptosis (clonal deletion)");
    } else {
        // safe → released to periphery as mature naive T cell
        // 安全 → 末梢へ放出（成熟ナイーブT細胞として）
        println!("Safe → released as mature naive T cell");
    }
}
```

![Pasted image 20260324122339.png](Pasted%20image%2020260324122339.png)(100a)
#### Thymus cellular components
**cortex**

Cortical thymic epithelial cells (cTECs) 
- form the cytoreticular framework (structural support) 
- present self-MHC to thymocytes → positive selection 

Macrophages 
- phagocytose apoptotic thymocytes (failed positive selection)


**medulla**

Medullary thymic epithelial cells (mTECs) 
- present self-antigens via AIRE → negative selection 

Dendritic cells (not eosinophils) 
- also present self-antigens → negative selection 

Macrophages 
- phagocytose apoptotic thymocytes (failed negative selection)

Hassall's body 
- concentrically layered keratinized epithelial cells 
- terminally differentiated (matured) mTECs 
- secrete cytokines (e.g. TSLP) 
- function: may promote regulatory T cell differentiation
### Tonsils

[Types of Immunity.canvas](Types%20of%20Immunity.canvas)

### Lymph nodes

### Spleen
