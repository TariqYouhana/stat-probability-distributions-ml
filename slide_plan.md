# Slide-by-Slide Presentation Blueprint

## Binomial & Negative Binomial Distributions in Machine Learning & Data Science
**Group 8** | **Total Slides: 15** | **Target Presentation Time: 10–12 Minutes**

---

### Slide 1: Title Slide
* **Title:** Binomial & Negative Binomial Distributions in Machine Learning and Data Science
* **Category:** Group 8 Presentation
* **Content:**
  * STA293 | Probability Distribution | Fall'26 | Section 2
  * Submitted to: Afsana Al Sharmin
  * Members: Tasfia Rahman Rodoshi [ID], Tariq Youhana Leon [ID], Shinjiny Anan Apsora [ID], Moumita Akter Mou [ID], Rehnuma Tasnim [ID]
* **Visuals:** Clean, modern gradient banner with subtle discrete point grid; clear title hierarchy.
* **Estimated Time:** ~20 seconds

---

### Slide 2: Why Probability Distributions Matter in Data Science
* **Title:** The Role of Probability Distributions in Modern Data Science
* **Content:**
  * **Quantify Uncertainty:** Measurements contain noise; distributions bound variability and risk.
  * **Foundation of Learning:** Classification, regression, and count modeling rely on assumed distributions.
  * **Hypothesis Testing:** Calculate $p$-values and confidence intervals to validate product experiments.
  * **Core Principle:** Converts uncalibrated feature counts into true posterior probabilities.
* **Visuals:** Two-column card layout with highlighted callout box: *"Distributions are the mathematical lens turning raw noise into actionable intelligence."*
* **Estimated Time:** ~40 seconds

---

### Slide 3: Introducing the Binomial Distribution
* **Title:** The Binomial Distribution: Definition & Foundations
* **Content:**
  * **Nature:** **Discrete** probability distribution on non-negative integers $\{0, 1, \dots, n\}$.
  * **Definition:** Probability of observing exactly $k$ successes in $n$ repeated, identical trials.
  * **The BINS Assumptions:**
    * **B — Binary Outcomes:** Success (1) or Failure (0).
    * **I — Independent Trials:** Outcome of trial $i$ does not alter trial $j$.
    * **N — Number of Trials Fixed:** $n$ is predetermined before sampling.
    * **S — Same Probability:** Success rate $p$ remains constant across all trials.
* **Visuals:** Distinct card breakdown of the BINS criteria with icon tags.
* **Estimated Time:** ~45 seconds

---

### Slide 4: Binomial — Mathematical Formulation (PMF)
* **Title:** Binomial: Probability Mass Function (PMF)
* **Content:**
  * **Formula Box [1]:**
    $$P(X = k) = \binom{n}{k} p^k (1 - p)^{n - k} \quad \text{for } k \in \{0, 1, \dots, n\}$$
  * **Symbol Mapping Table:**
    * $n$: Total number of trials ($n \in \mathbb{N}$)
    * $k$: Specific count of successes ($k \in [0, n]$)
    * $p$: Probability of success per trial ($0 \le p \le 1$)
    * $1 - p$: Probability of failure per trial
    * $p^k(1-p)^{n-k}$: Probability of any single sequence of $k$ successes and $n-k$ failures
    * $\binom{n}{k} = \frac{n!}{k!(n-k)!}$: Combinations of $k$ successes across $n$ positions
  * **Special Case:** When $n = 1$, the Binomial distribution reduces to a single **Bernoulli($p$)** trial.
* **Visuals:** Centered high-contrast formula box with a structured symbol explanation table.
* **Estimated Time:** ~50 seconds

---

### Slide 5: Binomial — Expectation, Variance & Properties
* **Title:** Binomial: Expectation, Dispersion & Properties
* **Content:**
  * **Mean (Expected Value) [1]:** $\mu = E[X] = np$
  * **Variance [1]:** $\sigma^2 = Var(X) = np(1 - p)$
  * **Standard Deviation:** $\sigma = \sqrt{np(1 - p)}$
  * **Key Insights:**
    * **Underdispersion:** Since $(1 - p) \le 1$, variance is always **strictly less than the mean** ($\sigma^2 < \mu$ for $p > 0$).
    * Maximum variance occurs at $p = 0.5$ (maximal uncertainty); approaches 0 as $p \to 0$ or $p \to 1$.
    * **MLE Estimator [1]:** $\hat{p}_{\text{MLE}} = \frac{k}{n}$ (sample proportion).
* **Visuals:** Moment definition cards + variance sensitivity box.
* **Estimated Time:** ~45 seconds

---

### Slide 6: Binomial — Impact of Probability $p$
* **Title:** Shape Dynamics: How Success Probability Governs Skewness
* **Content:**
  * **$p < 0.5$:** Right-skewed (positive skew). Success is infrequent; peak shifts left.
  * **$p = 0.5$:** Perfectly symmetric bell shape. Mode = Median = Mean = $np$. Skewness is zero.
  * **$p > 0.5$:** Left-skewed (negative skew). Success is frequent; peak shifts right.
* **Visuals:** Embedded high-resolution figure: `fig_binomial_pmf_variations.png` (Three side-by-side plots for $p = 0.2, 0.5, 0.8$ with mean lines).
* **Estimated Time:** ~45 seconds

---

### Slide 7: Binomial — Scale Dynamics & The CDF
* **Title:** Scale Dynamics & Cumulative Distribution Function (CDF)
* **Content:**
  * **Effect of Increasing $n$:** Distribution widens in absolute terms ($\sigma \propto \sqrt{n}$), but relative uncertainty ($\sigma / \mu \propto 1/\sqrt{n}$) contracts tightly.
  * **Cumulative Distribution Function (CDF):**
    $$F(k) = P(X \le k) = \sum_{i=0}^k \binom{n}{i} p^i (1 - p)^{n - i}$$
  * Step-wise discrete cumulative function ranging monotonically from $0.0$ to $1.0$ (at $n=20, p=0.6$, median $k=12$ gives $P(X \le 12) = 0.584$).
* **Visuals:** Dual figure card layout: `fig_binomial_n_variations.png` and `fig_binomial_cdf.png`.
* **Estimated Time:** ~45 seconds

---

### Slide 8: The Normal Approximation (De Moivre–Laplace Theorem)
* **Title:** Bridging Discrete & Continuous: De Moivre–Laplace Limit
* **Content:**
  * When $n$ is sufficiently large, Binomial counts approximate a continuous Gaussian curve:
    $$\text{Binomial}(n, p) \;\approx\; \mathcal{N}\big(\mu = np, \;\sigma^2 = np(1 - p)\big)$$
  * **Rule of Thumb:** Valid when $np \ge 10$ and $n(1 - p) \ge 10$.
  * **Continuity Correction:** Adjust discrete boundaries by $\pm 0.5$ when calculating area under the continuous curve.
* **Visuals:** Embedded figure: `fig_normal_approximation.png` ($n=50, p=0.4$ discrete bars overlaid with continuous normal curve).
* **Estimated Time:** ~45 seconds

---

### Slide 9: Introducing the Negative Binomial Distribution
* **Title:** The Negative Binomial Distribution: Definition & PMF
* **Content:**
  * **The Flipped Question:** Instead of fixing trials $n$ and counting successes, **fix the target successes $r$** and count the **failures $X = k$** before the $r$-th success.
  * **Convention:** $X =$ number of failures before the $r$-th success ($X = 0, 1, 2, \dots$). If we count total trials $Y = X + r$ instead, $E[Y] = r/p$; the variance is unchanged.
  * **Probability Mass Function (PMF) [1]:**
    $$P(X = k) = \binom{k + r - 1}{k} p^r (1 - p)^k \quad \text{for } k \in \{0, 1, 2, \dots, \infty\}$$
  * **Parameters:** $r \in \{1, 2, 3, \dots\}$ (fixed target number of successes, a positive integer), $p \in (0, 1]$ (success probability per trial).
  * **Special Case:** When $r = 1$, it reduces to the **Geometric** distribution.
* **Visuals:** Formula box + "Flipped Question" & Convention card.
* **Estimated Time:** ~55 seconds

---

### Slide 10: Negative Binomial — Properties, Overdispersion & Graphs
* **Title:** Negative Binomial: Moments, Overdispersion & Shape Dynamics
* **Content:**
  * **Mean [1]:** $\mu = E[X] = \frac{r(1 - p)}{p}$
  * **Variance [1, 3]:** $\sigma^2 = Var(X) = \frac{r(1 - p)}{p^2} = \mu + \frac{\mu^2}{r}$
  * **Mechanism (Poisson–Gamma Mixture) [3]:** NB arises as a Poisson-Gamma mixture: $X \mid \lambda \sim \text{Poisson}(\lambda)$, $\lambda \sim \text{Gamma}(\text{shape } r, \text{scale } (1-p)/p)$. Hence $\text{Var} = \text{mean} + \text{mean}^2 / r > \text{mean}$.
  * **MLE Estimator:** $\hat{p}_{\text{MLE}} = \frac{r}{r + \bar{x}}$
  * **Shape:** Always right-skewed with an infinite tail; becomes more symmetric as $r$ grows.
* **Visuals:** Embedded high-res figure: `fig_negbinom_pmf_variations.png` (varying $p$ and varying $r$).
* **Estimated Time:** ~55 seconds

---

### Slide 11: Binomial vs. Negative Binomial — Complementary Views
* **Title:** Binomial vs. Negative Binomial: Complementary Views
* **Content:**
  * **Comparison Table:**
    * *Fixed Parameter:* Trials $n$ (Binomial) vs. Target Successes $r$ (Negative Binomial)
    * *Random Variable $k$:* Successes $\in \{0..n\}$ vs. Failures $\in \{0..\infty\}$
    * *Mean ($\mu$):* $np$ vs. $\frac{r(1-p)}{p}$
    * *Variance ($\sigma^2$):* $np(1-p) < \mu$ (Underdispersed) vs. $\frac{r(1-p)}{p^2} > \mu$ (Overdispersed) [3]
  * **Connection to ML Loss & GLMs:** Binomial underlies **Logistic Regression** (Binary Cross-Entropy loss for $p(x) = \sigma(\beta^T x)$) [2, 4]; Negative Binomial underlies **Negative Binomial Regression** for overdispersed count targets [3].
* **Visuals:** Side-by-side comparison table + embedded figure `fig_comparison_pos_neg.png`.
* **Estimated Time:** ~55 seconds

---

### Slide 12: Machine Learning & Data Science Applications (Combined)
* **Title:** Real-World ML Applications: Binomial vs. Negative Binomial
* **Content:**
  * **Left Column — Binomial (Bounded Binary Counts):**
    * **A/B Testing:** Measuring conversion lift between Layout A ($n=1000, p=10\%$) vs. B ($n=1000, p=13\%$) via pooled $Z$-test ($Z = 2.1027$, one-sided $p = 0.0177$, two-sided $p = 0.0355$, pooled SE $= 0.0143$).
    * **Click-Through Rate (CTR):** Predicting ad clicks $k \sim \text{Binomial}(n, \text{pCTR})$ across $n$ impressions in real-time ad auctions.
    * **Logistic Regression [2, 4]:** Binary Cross-Entropy optimizes Binomial log-likelihood.
  * **Right Column — Negative Binomial (Overdispersed Counts) [3]:**
    * **Negative Binomial Regression (GLMs) [3]:** Overdispersion is common in real count data (e.g., ER visits, insurance claims, RNA-seq reads) where variance $\gg$ mean.
    * **Customer & Churn Analytics:** Modeling repeat purchases or support tickets before customer churn.
* **Visuals:** Clean two-column application layout comparing bounded vs. unbounded count use cases.
* **Estimated Time:** ~50 seconds

---

### Slide 13: Practical Demo Part A — Binomial Simulation
* **Title:** Practical Demo A: Binomial 1,000-Sample Simulation
* **Content:**
  * **Parameters:** $n = 20, p = 0.60, N = 1,000$ simulated batches.
  * **Moment Comparison Table:**
    * Mean: Theoretical = **12.0000** | Simulated = **12.0720** (Diff: 0.0720)
    * Variance: Theoretical = **4.8000** | Simulated = **4.8076** (Diff: 0.0076)
    * Std Dev: Theoretical = **2.1909** | Simulated = **2.1926** (Diff: 0.0017)
    * MLE $\hat{p} = \bar{x} / n = \mathbf{0.6036}$ (True $p = 0.6000$) [1]
  * **Takeaway:** Consistent with the Law of Large Numbers; confirms underdispersion ($\sigma^2 = 4.81 < \mu = 12.07$).
* **Visuals:** Embedded high-res figure: `fig_binomial_simulation.png` + formatted comparison table.
* **Estimated Time:** ~50 seconds

---

### Slide 14: Practical Demo Part B — Negative Binomial Simulation
* **Title:** Practical Demo B: Negative Binomial 1,000-Sample Simulation
* **Content:**
  * **Parameters:** $r = 5, p = 0.40, N = 1,000$ simulated observations.
  * **Moment Comparison Table:**
    * Mean: Theoretical = **7.5000** | Simulated = **7.4860** (Diff: 0.0140)
    * Variance: Theoretical = **18.7500** ($7.5 + 11.25$) | Simulated = **20.0398** (Diff: 1.2898)
    * Std Dev: Theoretical = **4.3301** | Simulated = **4.4766** (Diff: 0.1465)
    * Dispersion Ratio ($\sigma^2/\mu$): **2.6770** (Theoretical: **2.5000** $> 1.0$) [3]
    * MLE $\hat{p} = r / (r + \bar{x}) = \mathbf{0.4004}$ (True $p = 0.4000$)
  * **Takeaway:** Empirically demonstrates overdispersion ($\text{Var} = 20.04 > \text{Mean} = 7.49$); variance is noisier due to the heavy right tail.
* **Visuals:** Embedded high-res figure: `fig_negbinom_simulation.png` + formatted comparison table.
* **Estimated Time:** ~55 seconds

---

### Slide 15: Conclusion, Limitations & Academic References
* **Title:** Conclusion, Limitations & Academic References
* **Content:**
  * **Key Takeaways:** Complementary views — Binomial models **bounded successes** ($\sigma^2 < \mu$), while Negative Binomial models **unbounded overdispersed counts** ($\sigma^2 > \mu$). The Binomial underlies A/B testing and logistic regression [2, 4]; the Negative Binomial underlies count regression for overdispersed data [3]. Both simulations are consistent with theory (Binomial errors under 1%; Negative Binomial variance noisier due to heavy right tail).
  * **Real-World Limitations:** Independence violations, non-stationary $p$, and zero-inflation (ZINB).
  * **References:** [1] Casella & Berger (2002), [2] Bishop (2006), [3] Hilbe (2011), [4] Hastie et al. (2009).
  * **AI Acknowledgment:** AI tools were used to help draft text, code and figures: [EDIT: describe actual use]. The group checked all results.
  * **Closing:** "Thank You! Questions & Discussion 🙋"
* **Visuals:** Dual summary card layout with dark navy finish and formatted citations.
* **Estimated Time:** ~40 seconds

---

### Total Presentation Time: **~11.5 minutes** (Ideal for 10–12 minute slot).
