# Probability Distributions in Machine Learning and Data Science

> **Group 8 — Probability Distribution Class**
> *This document accompanies Group 8's presentation on Probability Distributions in ML/Data Science.*

---

## 1. Introduction

### What Are Probability Distributions?

A **probability distribution** is a mathematical function that describes the likelihood of different outcomes in a random experiment. It tells us *how probabilities are spread* across all possible values of a random variable. In data science, probability distributions are the backbone of statistical modeling — they let us summarize data, quantify uncertainty, and make predictions.

Every time we collect data, that data follows some underlying pattern. Probability distributions give us the language to describe those patterns precisely. Whether we are measuring heights, counting website clicks, or classifying emails as spam, there is a distribution governing the process.

### Why Do Distributions Matter in Data Science?

Distributions matter because nearly every machine learning algorithm — from linear regression to deep learning — relies on probabilistic assumptions about the data. Understanding distributions helps us:

- **Choose the right model** for a given dataset.
- **Interpret model outputs** (e.g., predicted probabilities).
- **Generate synthetic data** for testing and simulation.
- **Detect anomalies** by identifying data points that are unlikely under the assumed distribution.

### Our Focus: The Gaussian (Normal) Distribution

The **Gaussian distribution** (also called the **Normal distribution**) is the primary focus of this presentation. It is a **continuous** distribution — meaning it describes random variables that can take any real-valued number (e.g., height, temperature, blood pressure). The Gaussian is arguably the most important distribution in all of statistics because:

1. Many natural phenomena are approximately normally distributed.
2. The **Central Limit Theorem** guarantees that sample means converge to a normal distribution regardless of the original data's shape.
3. It is the foundation for the **Gaussian Naive Bayes** classifier, a powerful and efficient ML algorithm.

### Supporting Distributions

Alongside the Gaussian, we briefly discuss two **discrete** distributions that play important roles in Naive Bayes classification:

- **Bernoulli Distribution** — models binary outcomes (yes/no, 0/1). Used in **Bernoulli Naive Bayes** for text classification with binary word-presence features.
- **Multinomial Distribution** — models count data across multiple categories. Used in **Multinomial Naive Bayes** for text classification with word-frequency features.

### Why These Distributions Matter for ML Classification

Together, these three distributions power the entire **Naive Bayes family** of classifiers:

| Distribution | Type | Naive Bayes Variant | Typical Use Case |
|---|---|---|---|
| Gaussian | Continuous | Gaussian NB | Continuous measurements (medical data, sensor readings) |
| Bernoulli | Discrete | Bernoulli NB | Binary features (word present/absent in a document) |
| Multinomial | Discrete | Multinomial NB | Count features (word frequencies in documents) |

By understanding which distribution fits your data, you can select the right variant of Naive Bayes — and understand *why* it works.

---

## 2. Mathematical Explanation

### 2.1 Gaussian (Normal) Distribution — Full Treatment

The Gaussian distribution is defined by its **probability density function (PDF)**:

$$f(x) = \frac{1}{\sigma\sqrt{2\pi}} \exp\!\left(-\frac{(x - \mu)^2}{2\sigma^2}\right)$$

This is valid for all $x \in (-\infty, +\infty)$.

#### Parameter and Symbol Breakdown

| Symbol | Name | Meaning |
|---|---|---|
| $x$ | Random variable | The value at which we evaluate the density |
| $\mu$ (mu) | Mean | The center of the distribution; the "average" value |
| $\sigma$ (sigma) | Standard deviation | Measures the spread of the distribution around the mean |
| $\sigma^2$ | Variance | The square of the standard deviation; a measure of dispersion |
| $\pi$ | Pi | The mathematical constant $\approx 3.14159$ |
| $e$ | Euler's number | The base of the natural logarithm $\approx 2.71828$ |
| $\exp(\cdot)$ | Exponential function | Shorthand for $e^{(\cdot)}$ |

The term $\frac{1}{\sigma\sqrt{2\pi}}$ is a **normalizing constant** — it ensures the total area under the curve equals 1 (as required for any valid probability distribution).

The term $\exp\!\left(-\frac{(x - \mu)^2}{2\sigma^2}\right)$ controls the **shape**: it assigns highest density to values near $\mu$ and exponentially decreasing density as $x$ moves away from $\mu$.

#### Summary Statistics

- **Mean (Expected Value):** $E[X] = \mu$
- **Variance:** $\text{Var}(X) = \sigma^2$
- **Standard Deviation:** $\text{SD}(X) = \sigma$

We write $X \sim \mathcal{N}(\mu, \sigma^2)$ to denote that $X$ follows a Normal distribution with mean $\mu$ and variance $\sigma^2$.

#### Key Properties

1. **Symmetry:** The Gaussian curve is perfectly symmetric about $x = \mu$. The left and right halves are mirror images.

2. **Bell-Shaped Curve:** The PDF produces the famous "bell curve" — peaked at the center and tapering off in both tails.

3. **The 68–95–99.7 Rule (Empirical Rule):**
   - Approximately **68%** of observations fall within $\mu \pm 1\sigma$
   - Approximately **95%** of observations fall within $\mu \pm 2\sigma$
   - Approximately **99.7%** of observations fall within $\mu \pm 3\sigma$

   This rule provides a quick way to assess how "unusual" a data point is.

4. **Central Limit Theorem (CLT) Connection:** The CLT states that the sampling distribution of the sample mean $\bar{X}$ approaches a normal distribution as the sample size $n$ increases, regardless of the original population's distribution:

   $$\bar{X} \xrightarrow{d} \mathcal{N}\!\left(\mu, \frac{\sigma^2}{n}\right) \quad \text{as } n \to \infty$$

   This is why the Gaussian distribution is so prevalent — it emerges naturally whenever we average many independent observations.

5. **The Standard Normal:** When $\mu = 0$ and $\sigma = 1$, we get the **standard normal distribution** $Z \sim \mathcal{N}(0, 1)$. Any normal variable can be standardized via:

   $$Z = \frac{X - \mu}{\sigma}$$

#### Assumptions

For the Gaussian distribution to be an appropriate model, we generally assume:

- The data is **continuous** (not counts or categories).
- The data is roughly **symmetric** around the mean.
- Most values **cluster near the mean**, with fewer observations in the tails.
- There are no heavy outliers or skewness that would violate the bell-curve shape.

---

### 2.2 Bernoulli Distribution — Lighter Treatment

The **Bernoulli distribution** models a single trial with exactly two outcomes: success ($k = 1$) or failure ($k = 0$).

#### Probability Mass Function (PMF)

$$P(X = k) = p^{k}(1 - p)^{1 - k}, \quad k \in \{0, 1\}$$

Where $p$ is the probability of success ($0 \le p \le 1$).

This expands to:

- $P(X = 1) = p$ (success)
- $P(X = 0) = 1 - p$ (failure)

#### Summary Statistics

- **Mean:** $E[X] = p$
- **Variance:** $\text{Var}(X) = p(1 - p)$

#### When to Use It

The Bernoulli distribution applies whenever you have a **binary outcome**: a coin flip, whether an email is spam or not, whether a word appears in a document or not. In Bernoulli Naive Bayes, each feature is treated as a Bernoulli random variable (present = 1, absent = 0).

---

### 2.3 Multinomial Distribution — Lighter Treatment

The **Multinomial distribution** generalizes the Bernoulli to scenarios with **multiple categories**. It models the counts of outcomes across $k$ categories over $n$ independent trials.

#### Probability Mass Function (PMF)

$$P(X_1 = x_1, \ldots, X_k = x_k) = \frac{n!}{x_1!\, x_2!\, \cdots\, x_k!}\, p_1^{x_1}\, p_2^{x_2}\, \cdots\, p_k^{x_k}$$

where:

- $n = x_1 + x_2 + \cdots + x_k$ is the total number of trials
- $p_i$ is the probability of category $i$, with $\sum_{i=1}^{k} p_i = 1$
- $x_i$ is the observed count for category $i$

#### Summary Statistics (for each category $i$)

- **Mean:** $E[X_i] = n \cdot p_i$
- **Variance:** $\text{Var}(X_i) = n \cdot p_i(1 - p_i)$

#### When to Use It

The Multinomial distribution is appropriate when data represents **counts across multiple categories** — for example, word frequencies in a document. In Multinomial Naive Bayes, the features represent how often each word appears, not just whether it appears.

---

## 3. Graphical Representation

### The Gaussian Bell Curve

The Gaussian PDF produces the iconic **bell curve**:

- It is **unimodal** — there is a single peak at $x = \mu$.
- It is **symmetric** — the curve is a mirror image on either side of $\mu$.
- The tails extend infinitely in both directions but approach zero, meaning extreme values are possible but increasingly unlikely.

### Effect of Parameters on the Curve Shape

**Changing $\mu$ (the mean):**
- Shifting $\mu$ to the right moves the entire bell curve to the right along the $x$-axis.
- Shifting $\mu$ to the left moves it to the left.
- The *shape* of the curve (its width and height) does not change — only its **position** shifts.

**Changing $\sigma$ (the standard deviation):**
- A **smaller** $\sigma$ produces a taller, narrower curve — the data is tightly concentrated around $\mu$.
- A **larger** $\sigma$ produces a shorter, wider curve — the data is more spread out.
- The area under the curve always remains equal to 1.

For example:
- $\mathcal{N}(0, 0.5^2)$ — tall and narrow, centered at 0
- $\mathcal{N}(0, 1)$ — the standard normal
- $\mathcal{N}(0, 2^2)$ — short and wide, centered at 0

### The Cumulative Distribution Function (CDF)

The CDF of the Gaussian, $\Phi(x)$, gives the probability that a random variable $X$ is less than or equal to $x$:

$$\Phi(x) = P(X \le x) = \int_{-\infty}^{x} f(t)\, dt$$

Graphically, the CDF is an **S-shaped (sigmoid) curve** that:

- Starts near 0 for very small $x$ (far left tail)
- Passes through 0.5 at $x = \mu$ (the median equals the mean)
- Approaches 1 for very large $x$ (far right tail)

The CDF is useful for computing probabilities like $P(a \le X \le b) = \Phi(b) - \Phi(a)$.

### Bernoulli Bar Plot

The Bernoulli distribution, being discrete with only two outcomes, is best visualized as a **bar plot** with two bars:
- One bar at $k = 0$ with height $1 - p$
- One bar at $k = 1$ with height $p$

> **Note:** The actual plots (histograms, bell curves, CDF, parameter comparisons, and bar plots) are generated in the accompanying **Jupyter notebook (Part A)**. See the notebook for the full visual demonstration.

---

## 4. Real-life Applications

### Example 1: Email Spam Filtering Using Naive Bayes

**Problem:** Given an incoming email, classify it as **spam** or **not spam** (ham).

**How it works:**

1. Each email is converted into a feature vector based on the words it contains.
2. **Bernoulli Naive Bayes** treats each word as a binary feature: is the word *present* (1) or *absent* (0) in the email? The presence/absence of each word is modeled as a Bernoulli random variable.
3. **Multinomial Naive Bayes** treats each word as a count feature: how many *times* does each word appear? The distribution of word counts across the vocabulary follows a multinomial distribution.
4. Using Bayes' theorem, the classifier computes the probability of "spam" vs. "ham" given the observed word features and picks the class with the higher probability.

**Why these distributions are appropriate:**

- Word presence (yes/no) is inherently a **binary** outcome → Bernoulli is a natural fit.
- Word frequency (how often a word occurs) is **count data** across many categories (words) → Multinomial is a natural fit.

**Data Science impact:** Naive Bayes spam filters are fast, scalable, and surprisingly accurate. They power spam detection in email services worldwide.

### Example 2: Medical Diagnosis Using Gaussian Naive Bayes

**Problem:** Given a patient's clinical measurements, predict whether they have a particular disease (e.g., diabetes).

**How it works:**

1. Features include continuous measurements such as **blood pressure**, **blood glucose level**, **BMI**, and **age**.
2. Within each class (disease vs. no disease), these measurements are assumed to follow a **Gaussian distribution**.
3. **Gaussian Naive Bayes** estimates the mean $\mu$ and variance $\sigma^2$ of each feature for each class from the training data.
4. For a new patient, the classifier computes the likelihood of their measurements under each class's Gaussian model, applies Bayes' theorem, and assigns the class with the highest posterior probability.

**Why the Gaussian distribution is appropriate:**

- Physiological measurements like blood pressure and glucose are **continuous** values.
- They tend to be **approximately normally distributed** in a healthy population (and separately within a diseased population).
- The bell-curve assumption lets us compute likelihoods efficiently with just two parameters ($\mu$ and $\sigma^2$) per feature per class.

**Data Science impact:** Gaussian NB is used as a fast baseline classifier in medical diagnostics, bioinformatics, and any domain where features are continuous and roughly normally distributed.

---

## 5. Practical Demonstration Overview

The practical component of this presentation is implemented in a **Jupyter notebook** structured in two parts.

### Part A: Exploring the Gaussian Distribution

In Part A, we demonstrate the properties of the Gaussian distribution through simulation and visualization:

1. **Random Sampling:** Generate **1,000+ random observations** from a Gaussian distribution with known parameters (e.g., $\mu = 0$, $\sigma = 1$) using `numpy.random.normal()`.

2. **Histogram with Theoretical Overlay:** Plot a histogram of the simulated data and overlay the **theoretical PDF** curve using `scipy.stats.norm.pdf()`. This visually confirms that the simulated data follows the expected bell-curve shape.

3. **Sample vs. Theoretical Statistics:** Calculate and compare:
   - Sample mean ($\bar{x}$) vs. theoretical mean ($\mu$)
   - Sample variance ($s^2$) vs. theoretical variance ($\sigma^2$)
   - As $n$ grows large, the sample statistics should closely match the theoretical values.

4. **CDF Visualization:** Plot the cumulative distribution function using `scipy.stats.norm.cdf()` to show the S-shaped curve and demonstrate probability calculations.

5. **Parameter Effect Demonstration:** Plot multiple Gaussian curves with different $\mu$ and $\sigma$ values on the same axes to illustrate how parameters affect the shape and position of the distribution.

### Part B: Building a Gaussian Naive Bayes Classifier

In Part B, we apply the Gaussian distribution to a real machine learning task:

1. **Synthetic Dataset Generation:** Use `numpy` to generate a synthetic dataset with:
   - **2 classes** (e.g., Class 0 and Class 1)
   - **2 features** per observation (so we can visualize decision boundaries in 2D)
   - Each class's features are drawn from Gaussian distributions with different means

2. **Model Training:** Train a `GaussianNB` classifier from `sklearn.naive_bayes` on the training data.

3. **Accuracy Evaluation:** Report the classification accuracy on a held-out test set.

4. **Decision Boundary Visualization:** Plot the decision boundary — the line (or curve) that separates the two classes — overlaid on the data points, using `matplotlib`.

### Libraries Used

- `scipy.stats` — for Gaussian PDF, CDF, and statistical functions
- `sklearn.naive_bayes` — for the GaussianNB classifier
- `matplotlib` — for plotting histograms, curves, and decision boundaries
- `seaborn` — for enhanced statistical visualizations
- `numpy` — for random number generation and numerical computations

---

## 6. Gaussian Naive Bayes Classifier

### Bayes' Theorem — The Foundation

At the heart of every Naive Bayes classifier is **Bayes' theorem**:

$$P(C \mid X) = \frac{P(X \mid C) \cdot P(C)}{P(X)}$$

Where:

| Term | Name | Meaning |
|---|---|---|
| $P(C \mid X)$ | **Posterior** | Probability of class $C$ given the observed features $X$ |
| $P(X \mid C)$ | **Likelihood** | Probability of observing features $X$ given class $C$ |
| $P(C)$ | **Prior** | Prior probability of class $C$ (before seeing the data) |
| $P(X)$ | **Evidence** | Total probability of observing features $X$ (a normalizing constant) |

The classifier assigns the class $C^*$ that maximizes the posterior:

$$C^* = \arg\max_{C} \; P(X \mid C) \cdot P(C)$$

(We can drop $P(X)$ from the denominator because it is the same for all classes.)

### The "Naive" Assumption

The key simplification that makes Naive Bayes computationally efficient is the **conditional independence assumption**: given the class label, all features are assumed to be **independent** of each other.

If $X = (x_1, x_2, \ldots, x_d)$ is a $d$-dimensional feature vector, then:

$$P(X \mid C) = P(x_1 \mid C) \cdot P(x_2 \mid C) \cdot \ldots \cdot P(x_d \mid C) = \prod_{i=1}^{d} P(x_i \mid C)$$

This is "naive" because in practice, features are rarely truly independent. For example, a patient's blood pressure and BMI are likely correlated. Nevertheless, this assumption works surprisingly well in many applications.

### How Gaussian NB Models the Likelihood

In **Gaussian Naive Bayes**, each feature $x_i$ within each class $C$ is assumed to follow a **Gaussian (Normal) distribution**:

$$P(x_i \mid C) = \frac{1}{\sigma_{iC}\sqrt{2\pi}} \exp\!\left(-\frac{(x_i - \mu_{iC})^2}{2\sigma_{iC}^2}\right)$$

Where:
- $\mu_{iC}$ is the mean of feature $i$ for class $C$
- $\sigma_{iC}^2$ is the variance of feature $i$ for class $C$

So for $d$ features and $k$ classes, the model stores $2 \times d \times k$ parameters (one mean and one variance per feature per class).

### Maximum Likelihood Estimation (MLE)

The parameters $\mu_{iC}$ and $\sigma_{iC}^2$ are estimated from the training data using **Maximum Likelihood Estimation (MLE)**:

$$\hat{\mu}_{iC} = \frac{1}{n_C} \sum_{j \in C} x_{ij}$$

$$\hat{\sigma}_{iC}^2 = \frac{1}{n_C} \sum_{j \in C} (x_{ij} - \hat{\mu}_{iC})^2$$

Where $n_C$ is the number of training samples in class $C$, and the sums are over all samples $j$ belonging to class $C$.

In plain English: **the mean is just the average of that feature for samples in that class**, and **the variance is the average squared deviation from that mean**.

### Classification Workflow

1. **Training:** For each class $C$ and each feature $i$, compute $\hat{\mu}_{iC}$ and $\hat{\sigma}_{iC}^2$ from training data.
2. **Prediction:** For a new observation $X = (x_1, \ldots, x_d)$:
   - Compute $P(C) \cdot \prod_{i=1}^{d} P(x_i \mid C)$ for each class $C$
   - Assign the class with the **highest value**

### Comparison: Gaussian NB vs. Bernoulli NB vs. Multinomial NB

| Aspect | Gaussian NB | Bernoulli NB | Multinomial NB |
|---|---|---|---|
| **Feature Type** | Continuous (real-valued) | Binary (0 or 1) | Counts (non-negative integers) |
| **Distribution Assumed** | Gaussian | Bernoulli | Multinomial |
| **Likelihood Model** | $P(x_i \mid C) = \mathcal{N}(\mu_{iC}, \sigma_{iC}^2)$ | $P(x_i \mid C) = p_{iC}^{x_i}(1-p_{iC})^{1-x_i}$ | $P(\mathbf{x} \mid C) \propto \prod p_{iC}^{x_i}$ |
| **Typical Application** | Medical diagnosis, sensor data | Document classification (word presence) | Document classification (word counts) |
| **When to Use** | Features are continuous and roughly normal | Features are binary indicators | Features are frequency counts |

**Rule of thumb:**
- Continuous features (e.g., height, blood pressure) → **Gaussian NB**
- Binary features (e.g., word present/absent) → **Bernoulli NB**
- Count features (e.g., word frequency) → **Multinomial NB**

---

## 7. Conclusion

### Key Characteristics of the Gaussian Distribution

- It is a **continuous** distribution defined by two parameters: the mean $\mu$ and the variance $\sigma^2$.
- Its PDF produces the symmetric **bell curve**, with the peak at $\mu$.
- The **68–95–99.7 rule** provides a quick summary of how data spreads around the mean.
- Thanks to the **Central Limit Theorem**, it appears naturally in many real-world settings.
- It is computationally convenient: only two parameters need to be estimated per feature per class.

### When to Use Each Naive Bayes Variant

| Data Type | Recommended Variant |
|---|---|
| Continuous features (approximately normal) | Gaussian NB |
| Binary features (presence/absence) | Bernoulli NB |
| Count features (frequencies) | Multinomial NB |

### Limitations to Keep in Mind

1. **The "naive" independence assumption** rarely holds in real-world data. Features are often correlated (e.g., blood pressure and cholesterol). Despite this, Naive Bayes often performs well in practice — it gets the *ranking* of classes right even when the exact probabilities are poorly calibrated.

2. **Gaussian NB assumes normality** of features within each class. If the features are heavily skewed, multimodal, or have heavy tails, the Gaussian assumption may be a poor fit. In such cases, data transformation (e.g., log-transform) or a different model may be more appropriate.

3. **Small sample sizes** can lead to poor estimates of $\mu$ and $\sigma^2$, especially for rare classes.

Despite these limitations, Naive Bayes classifiers remain a **fast, interpretable, and effective** baseline for many classification tasks in data science.

---

## 8. References

1. Wackerly, D. D., Mendenhall, W., & Scheaffer, R. L. (2014). *Mathematical Statistics with Applications* (7th ed.). Cengage Learning. — Comprehensive treatment of probability distributions, expected values, and the Central Limit Theorem.

2. Scikit-learn Developers. (2024). *sklearn.naive_bayes.GaussianNB — scikit-learn documentation*. Retrieved from [https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html) — Official documentation for the Gaussian Naive Bayes implementation in Python.

3. Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*. Springer. — Foundational text covering probabilistic models, Bayesian classification, and the role of the Gaussian distribution in machine learning.

4. Murphy, K. P. (2012). *Machine Learning: A Probabilistic Perspective*. MIT Press. — In-depth coverage of Naive Bayes classifiers and their distributional assumptions.

---

*Prepared by Group 8 — Probability Distributions in Machine Learning and Data Science*
