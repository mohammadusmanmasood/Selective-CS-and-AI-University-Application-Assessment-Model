# Selective-CS-and-AI-University-Application-Assessment-Model
Tiered Algorithmic Predictive Model utilizing conditional logic to quantify and assess applicant profiles against the rigorous, weighted selection criteria of highly selective Computer Science and Artificial Intelligence programs (Acceptance Rate <= 25%)
* **Objective:** To demonstrate analytical rigor and applied coding by **reverse-engineering and quantifying the weighted features** used by elite institutions.
* **Methodology:** The model utilizes conditional logic in Python to define scoring tiers based on the university's acceptance rate, covering all rates from 0% to 25%.

## Technical Methodology and Modeling
The core logic is implemented as a tiered conditional algorithm in Python, where the weight assigned to each metric (or "feature") dynamically scales according to the rigor of the acceptance rate tier:

| Tier | Acceptance Rate | Primary Modeling Focus |
| :--- | :--- | :--- |
| **Tier 1 (Highest Rigor)** | AR ≤ 5% | Emphasizes **mandatory** high scores in prerequisite subjects (Math/Physics) and extensive practical experience (Technical Portfolio). |
| **Tier 2** | 5% < AR ≤ 15% | Balances strong academic records with a solid, proven technical project count. |
| **Tier 3 (Broader Selection)** | 15% < AR ≤ 25% | Represents a slightly broader entry pool, but still requires highly competitive scores and proven practical interest (minimum projects required is reduced). |

## Feature Engineering & Weighting Rationale
The scoring system was meticulously weighted to reflect the priorities of a highly specialized AI/CS curriculum:

* **A-Levels (Academic Prerequisites):** Given 10 points. The model assigns 0 points if core technical subjects (Math/Physics) are missing or graded poorly, reflecting the non-negotiable quantitative demands of AI programs.
* **Technical Portfolio (Practical Skill):** Given 10 points. **Highest Priority.** This metric is weighted equally to A-Levels, representing direct proof of applied coding and project-based experience (e.g., GitHub, Kaggle).
* **Standardized Tests (SAT/ACT):** Given 10 points. Assesses baseline quantitative aptitude against the competitive global pool.

**The direct application of this model demonstrates my proficiency in designing and implementing complex, real-world algorithmic systems.**
