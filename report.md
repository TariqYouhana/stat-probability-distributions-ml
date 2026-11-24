# Academic Presentation Report
## Positive & Negative Binomial Distributions in Machine Learning and Data Science
**Group 8** | **Course:** Probability Distributions & Statistical Modeling | **Total Slides:** 15

---

## Executive Summary
This report documents the complete 15-slide presentation on the **Positive and Negative Binomial Distributions** and their foundational roles in Machine Learning and Data Science. Rather than treating these distributions in isolation, the presentation frames them as **mathematical duals**: the Positive Binomial models **bounded success counts** in fixed trials ($\sigma^2 < \mu$, underdispersed), while the Negative Binomial models **unbounded failure counts** before fixed successes ($\sigma^2 > \mu$, overdispersed). Together, they underpin A/B testing, Click-Through Rate (CTR) modeling, Logistic Regression, and Generalized Linear Models (GLMs) for overdispersed real-world count data. All theoretical claims are validated through two 1,000-observation Python simulations.

---

## Slide-by-Slide Content & Visual Breakdown

### Slide 1: Title Slide
* **Content:** Presents the project title (*Positive & Negative Binomial Distributions in Machine Learning and Data Science*), Group 8 identifier, course title, team members, and date.
* **Visuals:** Modern navy-blue header layout with clean typography.

### Slide 2: The Role of Probability Distributions in Modern Data Science
* **Content:** Explains why distributions are essential in data science: quantifying measurement noise, providing parametric foundations for ML models, and enabling hypothesis testing ($p$-values and confidence intervals).
* **Visuals:** Two-column card layout with highlighted core principle callout.

### Slide 3: The Positive Binomial Distribution: Definition & Foundations
* **Content:** Defines the Positive Binomial distribution as a discrete distribution on $\{0, 1, \dots, n\}$ derived from $(p+q)^n$ with a positive exponent. Details the four **BINS** assumptions: **B**inary outcomes, **I**ndependent trials, **N**umber of trials fixed, and **S**ame probability $p$.
* **Visuals:** Structured 4-card BINS breakdown.

### Slide 4: Positive Binomial: Probability Mass Function (PMF)
* **Content:** Displays the PMF:
  $$P(X = k) = \binom{n}{k} p^k (1 - p)^{n - k}$$
  Maps every symbol ($n, k, p, 1-p, \binom{n}{k}$) and notes the special case: when $n = 1$, Binomial reduces to a single **Bernoulli($p$)** trial.
* **Visuals:** High-contrast formula box paired with a symbol mapping table.

### Slide 5: Positive Binomial: Expectation, Dispersion & Properties
* **Content:** Presents Mean $\mu = np$, Variance $\sigma^2 = np(1 - p)$, and Std Dev $\sigma = \sqrt{np(1 - p)}$. Highlights **underdispersion** ($\sigma^2 < \mu$), peak variance at $p = 0.5$, and the Maximum Likelihood Estimator $\hat{p}_{\text{MLE}} = k/n$.
* **Visuals:** Moment cards and variance sensitivity callout.

### Slide 6: Shape Dynamics: How Success Probability Governs Skewness
* **Content:** Demonstrates how $p$ shapes skewness at fixed $n = 20$: $p < 0.5$ produces right-skew, $p = 0.5$ produces symmetry, and $p > 0.5$ produces left-skew.
* **Visuals:** Embedded `fig_binomial_pmf_variations.png` showing three side-by-side PMF bar plots ($p = 0.2, 0.5, 0.8$).

### Slide 7: Scale Dynamics & Cumulative Distribution Function (CDF)
* **Content:** Illustrates how increasing $n$ widens absolute spread ($\sigma \propto \sqrt{n}$) while shrinking relative uncertainty ($\sigma/\mu \propto 1/\sqrt{n}$). Defines the discrete step-wise CDF $F(k) = P(X \le k)$.
* **Visuals:** Dual embedded figures: `fig_binomial_n_variations.png` ($n = 10, 30, 100$) and `fig_binomial_cdf.png`.

### Slide 8: Bridging Discrete & Continuous: De Moivre–Laplace Limit
* **Content:** Explains the De Moivre–Laplace theorem: for large $n$ ($np \ge 10$ and $n(1-p) \ge 10$), $\text{Binomial}(n, p) \approx \mathcal{N}(np, np(1-p))$, avoiding costly factorial computation and enabling $Z$-tests with $\pm 0.5$ continuity correction.
* **Visuals:** Embedded `fig_normal_approximation.png` ($n = 50, p = 0.4$ bars overlaid with continuous Normal PDF).

### Slide 9: The Negative Binomial Distribution: Definition & PMF
* **Content:** Introduces the Negative Binomial by flipping the question: fix target successes $r$ and count random failures $k \in \{0, 1, 2, \dots\}$ before the $r$-th success. Explains its origin in the negative-power series $(1 - q)^{-r}$ and states the PMF:
  $$P(X = k) = \binom{k + r - 1}{k} p^r (1 - p)^k$$
  Notes that $r = 1$ yields the **Geometric($p$)** distribution.
* **Visuals:** Highlighted PMF formula box + "Flipped Question" comparison card.

### Slide 10: Negative Binomial: Moments, Overdispersion & Shape Dynamics
* **Content:** Derives Mean $\mu = \frac{r(1-p)}{p}$ and Variance $\sigma^2 = \frac{r(1-p)}{p^2} = \mu + \frac{\mu^2}{r}$. Emphasizes **overdispersion** ($\sigma^2 > \mu$) as its signature property, plus MLE $\hat{p}_{\text{MLE}} = \frac{r}{r + \bar{x}}$.
* **Visuals:** Embedded `fig_negbinom_pmf_variations.png` illustrating shape shifts across varying $p$ and varying $r$.

### Slide 11: Positive vs. Negative Binomial: Mathematical Duality
* **Content:** Side-by-side comparison table contrasting fixed parameters ($n$ vs $r$), random variable ($k$ successes vs $k$ failures), generating expansions ($(p+q)^n$ vs $(1-q)^{-r}$), moments, and dispersion ($\sigma^2 < \mu$ vs $\sigma^2 > \mu$). Briefly notes their ML regression counterparts: **Logistic Regression** (Binary Cross-Entropy) vs **Negative Binomial Regression**.
* **Visuals:** Comparison table + embedded `fig_comparison_pos_neg.png` side-by-side distribution plot.

### Slide 12: Real-World ML Applications: Positive vs. Negative Binomial
* **Content:** Two-column application overview:
  * *Positive Binomial:* A/B Testing conversion rates ($Z$-tests) and Click-Through Rate (CTR) auction modeling.
  * *Negative Binomial:* Negative Binomial Regression (GLMs) for overdispersed counts—insurance claims, hospital ER visits, software bug counts, and repeat customer purchases.
* **Visuals:** Clean two-column industry use-case cards.

### Slide 13: Practical Demo A: Positive Binomial 1,000-Sample Simulation
* **Content:** Simulates $N = 1,000$ observations from $\text{Binomial}(n=20, p=0.60)$. Empirical mean (**12.0720** vs 12.0000), variance (**4.8076** vs 4.8000), std dev (**2.1926** vs 2.1909), and MLE $\hat{p}$ (**0.6036** vs 0.6000) confirm underdispersion and convergence.
* **Visuals:** Embedded `fig_binomial_simulation.png` + moment comparison table.

### Slide 14: Practical Demo B: Negative Binomial 1,000-Sample Simulation
* **Content:** Simulates $N = 1,000$ observations from $\text{NegBin}(r=5, p=0.40)$. Empirical mean (**7.4860** vs 7.5000), variance (**20.0398** vs 18.7500), std dev (**4.4766** vs 4.3301), dispersion ratio (**2.6770** vs 2.5000 $> 1$), and MLE $\hat{p}$ (**0.4004** vs 0.4000) confirm overdispersion and heavy right tail.
* **Visuals:** Embedded `fig_negbinom_simulation.png` + moment comparison table.

### Slide 15: Conclusion, Limitations & Academic References
* **Content:** Summarizes the Positive/Negative Binomial duality, outlines real-world limitations (independence violations, non-stationary $p$, zero-inflation requiring ZINB), and provides 4 academic references.
* **Visuals:** Dark navy closing slide with structured summary cards and citations.

---

## Academic References
1. Casella, G., & Berger, R. L. (2002). *Statistical Inference* (2nd ed.). Duxbury Press.
2. Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*. Springer.
3. Hilbe, J. M. (2011). *Negative Binomial Regression* (2nd ed.). Cambridge University Press.
4. Hastie, T., Tibshirani, R., & Friedman, J. (2009). *The Elements of Statistical Learning* (2nd ed.). Springer.
