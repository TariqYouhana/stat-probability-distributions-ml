# Presentation Speaking Script — Group 8
**Topic:** Positive & Negative Binomial Distributions in Machine Learning and Data Science
**Total Slides:** 15 | **Target Time:** ~11.5 minutes (Pace: ~130–145 words/minute)

---

### Slide 1: Title Slide (~20 seconds)
> "Good morning everyone, and thank you for joining us today. We are Group 8, and in this presentation we will explore the **Positive and Negative Binomial Distributions**—two mathematical duals that form the backbone of discrete modeling, count prediction, and experimentation in Machine Learning and Data Science."

---

### Slide 2: Why Probability Distributions Matter (~40 seconds)
> "Before diving into the formulas, let's ask a fundamental question: why do data scientists care about probability distributions? Every real-world dataset—whether it's website clicks, insurance claims, or test results—contains random noise. Probability distributions give us a mathematical lens to quantify that uncertainty, power predictive models, and run rigorous hypothesis tests. Today we'll look at how one family—the Positive and Negative Binomial—handles both bounded binary counts and unbounded overdispersed counts."

---

### Slide 3: Introducing the Positive Binomial Distribution (~45 seconds)
> "Let's start with what we usually call the standard Binomial—also known as the **Positive Binomial** because it comes from expanding $(p + q)^n$ with a positive exponent $n$. It models the exact number of successes $k$ in a fixed number of trials $n$. For a process to be Positive Binomial, it must satisfy four **BINS** assumptions: **B**inary outcomes (success or failure), **I**ndependent trials, a fixed **N**umber of trials $n$, and the **S**ame success probability $p$ on every trial."

---

### Slide 4: Positive Binomial — Mathematical Formulation (PMF) (~50 seconds)
> "Here is the Probability Mass Function. The probability of observing exactly $k$ successes in $n$ trials is $\binom{n}{k}$ times $p^k$ times $(1-p)^{n-k}$. The binomial coefficient $\binom{n}{k}$ counts how many ways we can arrange $k$ successes across $n$ positions, while $p^k(1-p)^{n-k}$ gives the probability of each specific sequence. Also worth noting: in the simplest case where $n = 1$, the Binomial distribution reduces directly to a single Bernoulli trial."

---

### Slide 5: Positive Binomial — Expectation, Variance & Properties (~45 seconds)
> "From this PMF, we get clean closed-form moments. The expected value is simply $\mu = np$, and the variance is $\sigma^2 = np(1-p)$. Notice something crucial here: because $(1-p)$ is less than 1, the variance is always **strictly less than the mean**—a property called **underdispersion**. Variance peaks at $p = 0.5$, where uncertainty is greatest. And if we want to estimate $p$ from data, Maximum Likelihood Estimation gives us the intuitive sample proportion: $\hat{p} = k/n$."

---

### Slide 6: Positive Binomial — Impact of Probability $p$ (~45 seconds)
> "Visualizing the PMF shows how $p$ controls skewness. On the left, when $p = 0.2$, success is rare, so the distribution is right-skewed. In the middle, at $p = 0.5$, it is perfectly symmetric around the mean of 10. On the right, when $p = 0.8$, success is common, shifting the peak right and creating a left-skewed curve."

---

### Slide 7: Positive Binomial — Scale Dynamics & The CDF (~45 seconds)
> "What happens as we increase the number of trials $n$? On the left, moving from $n=10$ to $n=100$, the distribution widens in absolute terms, yet relative uncertainty shrinks proportional to $1/\sqrt{n}$. On the right is the Cumulative Distribution Function, $F(k)$, which sums the PMF from $0$ up to $k$ in a discrete staircase from $0$ to $1$."

---

### Slide 8: The Normal Approximation (De Moivre–Laplace Theorem) (~45 seconds)
> "Now, what if $n$ is huge, say $10,000$? Computing factorials in $\binom{n}{k}$ becomes slow and numerically unstable. The De Moivre–Laplace theorem solves this: as $n$ grows large—specifically when $np \ge 10$ and $n(1-p) \ge 10$—the discrete Binomial converges smoothly to a continuous Normal distribution with the same mean $np$ and variance $np(1-p)$, as shown in this overlay for $n=50, p=0.4$."

---

### Slide 9: Introducing the Negative Binomial Distribution (~55 seconds)
> "Now let's flip the question around—this brings us to the **Negative Binomial Distribution**. In the Positive Binomial, we fixed the number of trials $n$ and counted successes. In the Negative Binomial, we **fix the target number of successes $r$**, and we count how many **failures $k$** occur *before* we hit that $r$-th success. It's called 'negative' because its probabilities come from expanding $(1-q)^{-r}$ with a negative exponent. Its PMF is $\binom{k+r-1}{k} p^r (1-p)^k$ for $k = 0, 1, 2, \dots$ all the way to infinity. When $r=1$, it reduces to the Geometric distribution."

---

### Slide 10: Negative Binomial — Properties, Overdispersion & Graphs (~55 seconds)
> "Here is why Data Scientists love the Negative Binomial. Its mean is $\mu = \frac{r(1-p)}{p}$, and its variance is $\sigma^2 = \frac{r(1-p)}{p^2}$, which can be rewritten as $\mu + \frac{\mu^2}{r}$. Because we add that positive $\frac{\mu^2}{r}$ term, **the variance is always strictly greater than the mean**! This property—called **overdispersion**—makes the Negative Binomial essential for real-world count data that is too noisy for Poisson or Positive Binomial. As you can see in the plots, it is always right-skewed, with a heavier tail when $p$ is small or $r$ is small."

---

### Slide 11: Positive vs. Negative Binomial — Mathematical Duality (~55 seconds)
> "This slide puts both distributions side by side to highlight their mathematical duality. Positive Binomial fixes trials $n$, counts bounded successes, and is **underdispersed** ($\sigma^2 < \mu$). Negative Binomial fixes successes $r$, counts unbounded failures, and is **overdispersed** ($\sigma^2 > \mu$). In machine learning, Positive Binomial powers **Logistic Regression** via Binary Cross-Entropy loss, while Negative Binomial powers **Negative Binomial Regression** for overdispersed count targets."

---

### Slide 12: Machine Learning & Data Science Applications (~50 seconds)
> "So where do we use each one in industry? On the left, **Positive Binomial** handles bounded binary counts: **A/B Testing** at companies like Netflix and Meta to test conversion lift, and **Click-Through Rate (CTR)** prediction in ad auctions. On the right, **Negative Binomial** handles unbounded, overdispersed counts: predicting **insurance claims**, **hospital ER visits**, **software bug counts**, or **repeat customer purchases**—scenarios where variance far exceeds the mean."

---

### Slide 13: Practical Demo A — Positive Binomial Simulation (~50 seconds)
> "To verify this in Python, we ran two 1,000-sample simulations. First, for Positive Binomial with $n=20$ and $p=0.60$, our 1,000 simulated batches produced a sample mean of **12.0720** versus the theoretical **12.0000**, and a sample variance of **4.8076** versus **4.8000**—notice variance is less than the mean. Our MLE estimate $\hat{p} = 0.6036$ recovered the true $p = 0.60$ almost identically."

---

### Slide 14: Practical Demo B — Negative Binomial Simulation (~55 seconds)
> "Next, we simulated 1,000 samples from a Negative Binomial with target $r=5$ successes and $p=0.40$. Our simulated mean was **7.4860** against the theoretical **7.5000**. And look at the variance: **20.0398** versus theoretical **18.7500**—giving a dispersion ratio $\sigma^2 / \mu$ of **2.68**, over twice the mean! And our MLE $\hat{p} = \frac{r}{r+\bar{x}}$ recovered **0.4004** against the true $0.4000$. The purple histogram aligns tightly with the red theoretical curve."

---

### Slide 15: Conclusion, Limitations & References (~40 seconds)
> "To wrap up: the Positive and Negative Binomial distributions form a complete toolkit for discrete modeling—Positive for bounded binary successes, and Negative for unbounded overdispersed counts. In practice, remember their key limitations: real-world events can violate independence via network effects, probabilities can drift over time, and datasets with excessive zeros may require Zero-Inflated Negative Binomial models. Thank you all for listening—we'd be happy to take your questions!"
