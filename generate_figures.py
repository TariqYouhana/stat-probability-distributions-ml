import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy import stats
import json

# Style configuration
sns.set_style('whitegrid')
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 12
plt.rcParams['figure.dpi'] = 200
np.random.seed(42)

PRIMARY = '#2563EB'      # Blue
ACCENT = '#7C3AED'       # Purple
SUCCESS = '#10B981'      # Green
DANGER = '#DC2626'       # Red
ORANGE = '#F59E0B'       # Orange

print("--- Generating Binomial Figures ---")

# 1. Slide 6: Effect of changing probability p (n = 20 fixed)
fig, axes = plt.subplots(1, 3, figsize=(15, 4.5), sharey=True)
n_fixed = 20
p_vals = [0.2, 0.5, 0.8]
colors = [ORANGE, PRIMARY, ACCENT]
titles = [
    'Right-Skewed: p = 0.2\n(Success is rare)',
    'Symmetric: p = 0.5\n(Equally likely outcomes)',
    'Left-Skewed: p = 0.8\n(Success is common)'
]

for ax, p, color, title in zip(axes, p_vals, colors, titles):
    k = np.arange(0, n_fixed + 1)
    pmf = stats.binom.pmf(k, n_fixed, p)
    ax.bar(k, pmf, color=color, alpha=0.85, edgecolor='white', width=0.8)
    mean_val = n_fixed * p
    ax.axvline(x=mean_val, color=DANGER, linestyle='--', linewidth=2, label=f'Mean μ = {mean_val:.1f}')
    ax.set_title(title, fontsize=12, fontweight='bold')
    ax.set_xlabel('Number of Successes (k)', fontsize=11)
    ax.set_xticks(range(0, n_fixed + 1, 4))
    ax.legend(fontsize=10, loc='upper left' if p > 0.5 else 'upper right')

axes[0].set_ylabel('Probability P(X = k)', fontsize=12)
plt.suptitle('Figure 6: Impact of Probability p on Binomial Shape (Fixed n = 20)', 
             fontsize=14, fontweight='bold', y=1.03)
plt.tight_layout()
plt.savefig('fig_binomial_pmf_variations.png', bbox_inches='tight')
plt.close()
print("Saved fig_binomial_pmf_variations.png")

# 2. Slide 7A: Effect of changing trial count n (p = 0.5 fixed)
fig, axes = plt.subplots(1, 3, figsize=(15, 4.5))
n_list = [10, 30, 100]
colors_n = [PRIMARY, ACCENT, SUCCESS]

for ax, n_val, color in zip(axes, n_list, colors_n):
    k = np.arange(0, n_val + 1)
    pmf = stats.binom.pmf(k, n_val, 0.5)
    ax.bar(k, pmf, color=color, alpha=0.8, edgecolor='none', width=1.0)
    mean_val = n_val * 0.5
    std_val = np.sqrt(n_val * 0.5 * 0.5)
    ax.set_title(f'n = {n_val} trials (p = 0.5)\nμ = {mean_val:.1f}, σ = {std_val:.2f}', fontsize=12, fontweight='bold')
    ax.set_xlabel('Successes (k)', fontsize=11)
    ax.set_ylabel('Probability' if ax == axes[0] else '')

plt.suptitle('Figure 7A: As n Increases, the Distribution Smooths and Widens', 
             fontsize=14, fontweight='bold', y=1.03)
plt.tight_layout()
plt.savefig('fig_binomial_n_variations.png', bbox_inches='tight')
plt.close()
print("Saved fig_binomial_n_variations.png")

# 3. Slide 7B: Cumulative Distribution Function (CDF) Step Plot
fig, ax = plt.subplots(figsize=(9, 5))
n_cdf = 20
p_cdf = 0.6
k_cdf = np.arange(0, n_cdf + 1)
cdf_vals = stats.binom.cdf(k_cdf, n_cdf, p_cdf)

ax.step(k_cdf, cdf_vals, where='post', color=PRIMARY, linewidth=2.5, label=f'Binomial CDF (n={n_cdf}, p={p_cdf})')
ax.plot(k_cdf, cdf_vals, 'o', color=PRIMARY, markersize=5)
k_mid = 12
f_mid = stats.binom.cdf(k_mid, n_cdf, p_cdf)
ax.axhline(y=0.5, color='gray', linestyle=':', alpha=0.7)
ax.axvline(x=k_mid, color=DANGER, linestyle='--', alpha=0.7, label=f'Median k={k_mid} (P(X ≤ {k_mid}) = {f_mid:.2f})')

ax.set_xlabel('Successes (k)', fontsize=12)
ax.set_ylabel('Cumulative Probability F(k) = P(X ≤ k)', fontsize=12)
ax.set_title('Figure 7B: Cumulative Distribution Function (Discrete Step Curve)', fontsize=13, fontweight='bold')
ax.set_xticks(range(0, n_cdf + 1, 2))
ax.set_ylim(-0.02, 1.05)
ax.legend(fontsize=11)
plt.tight_layout()
plt.savefig('fig_binomial_cdf.png', bbox_inches='tight')
plt.close()
print("Saved fig_binomial_cdf.png")

# 4. Slide 8: De Moivre-Laplace Normal Approximation to Binomial
fig, ax = plt.subplots(figsize=(10, 5.2))
n_approx = 50
p_approx = 0.4
mu_approx = n_approx * p_approx       # 20.0
var_approx = n_approx * p_approx * (1 - p_approx) # 12.0
sigma_approx = np.sqrt(var_approx)    # 3.464

k_vals = np.arange(0, n_approx + 1)
pmf_vals = stats.binom.pmf(k_vals, n_approx, p_approx)
ax.bar(k_vals, pmf_vals, width=0.8, color='#93C5FD', edgecolor='#2563EB', alpha=0.7, label=f'Binomial PMF (n={n_approx}, p={p_approx})')

x_norm = np.linspace(5, 35, 300)
pdf_norm = stats.norm.pdf(x_norm, loc=mu_approx, scale=sigma_approx)
ax.plot(x_norm, pdf_norm, color=DANGER, linewidth=2.5, label=f'Normal Approximation: N(μ={mu_approx:.1f}, σ²={var_approx:.1f})')

ax.set_xlim(8, 32)
ax.set_xlabel('Number of Successes (k)', fontsize=12)
ax.set_ylabel('Probability Density / Mass', fontsize=12)
ax.set_title('Figure 8: De Moivre–Laplace Theorem: Binomial Converging to Normal Curve', fontsize=13, fontweight='bold')
ax.legend(fontsize=11)
plt.tight_layout()
plt.savefig('fig_normal_approximation.png', bbox_inches='tight')
plt.close()
print("Saved fig_normal_approximation.png")

# 5. Slide 13: 1,000 Sample Simulation vs Theoretical PMF (Mandatory Demo)
n_sim = 20
p_sim = 0.6
N_samples = 1000

sim_samples = np.random.binomial(n=n_sim, p=p_sim, size=N_samples)
sample_mean = float(np.mean(sim_samples))
sample_var = float(np.var(sim_samples, ddof=1))
sample_std = float(np.std(sim_samples, ddof=1))

theo_mean = float(n_sim * p_sim)                    # 12.0
theo_var = float(n_sim * p_sim * (1 - p_sim))       # 4.8
theo_std = float(np.sqrt(theo_var))                 # 2.19089

fig, ax = plt.subplots(figsize=(10, 5.5))
bins = np.arange(-0.5, n_sim + 1.5, 1)
counts, _, _ = ax.hist(sim_samples, bins=bins, density=True, color='#60A5FA', 
                       edgecolor='white', alpha=0.75, label=f'Simulated Frequencies (N={N_samples})')

k_axis = np.arange(0, n_sim + 1)
pmf_theo = stats.binom.pmf(k_axis, n_sim, p_sim)
ax.plot(k_axis, pmf_theo, 'ro-', linewidth=2, markersize=6, label=f'Theoretical PMF (n={n_sim}, p={p_sim})')

ax.set_xlabel('Number of Successes (k)', fontsize=12)
ax.set_ylabel('Relative Frequency / Probability', fontsize=12)
ax.set_title('Figure 13: 1,000 Simulated Observations vs Theoretical Binomial PMF', fontsize=13, fontweight='bold')
ax.set_xticks(range(4, 21, 2))
ax.set_xlim(3.5, 20.5)
ax.legend(fontsize=11)
plt.tight_layout()
plt.savefig('fig_binomial_simulation.png', bbox_inches='tight')
plt.close()
print("Saved fig_binomial_simulation.png")

# 6. Slide 14: Applied A/B Testing Distributions
nA, pA = 1000, 0.10   # Control: 10% conversion
nB, pB = 1000, 0.13   # Variant: 13% conversion

fig, ax = plt.subplots(figsize=(10, 5))
kA = np.arange(70, 160)
kB = np.arange(70, 160)

ax.plot(kA, stats.binom.pmf(kA, nA, pA), color=PRIMARY, linewidth=2.5, label='Layout A (Control): n=1000, p=10% (μ=100)')
ax.fill_between(kA, stats.binom.pmf(kA, nA, pA), color=PRIMARY, alpha=0.25)

ax.plot(kB, stats.binom.pmf(kB, nB, pB), color=SUCCESS, linewidth=2.5, label='Layout B (Variant): n=1000, p=13% (μ=130)')
ax.fill_between(kB, stats.binom.pmf(kB, nB, pB), color=SUCCESS, alpha=0.25)

ax.set_xlabel('Conversions out of 1,000 Visitors', fontsize=12)
ax.set_ylabel('Probability', fontsize=12)
ax.set_title('Figure 14: A/B Testing Evaluation via Binomial Sampling Distributions', fontsize=13, fontweight='bold')
ax.legend(fontsize=11)
plt.tight_layout()
plt.savefig('fig_ab_testing_distributions.png', bbox_inches='tight')
plt.close()
print("Saved fig_ab_testing_distributions.png")

# Save computed metrics for inclusion across markdown, slides, and notebook
metrics = {
    "n_sim": n_sim,
    "p_sim": p_sim,
    "N_samples": N_samples,
    "sample_mean": round(sample_mean, 4),
    "theo_mean": round(theo_mean, 4),
    "mean_diff": round(abs(sample_mean - theo_mean), 4),
    "sample_var": round(sample_var, 4),
    "theo_var": round(theo_var, 4),
    "var_diff": round(abs(sample_var - theo_var), 4),
    "sample_std": round(sample_std, 4),
    "theo_std": round(theo_std, 4),
    "std_diff": round(abs(sample_std - theo_std), 4),
    "mle_p": round(sample_mean / n_sim, 4)
}

with open('metrics_binomial.json', 'w') as f:
    json.dump(metrics, f, indent=2)

print("\n--- Summary of Simulation Metrics ---")
print(f"Sample Mean:     {sample_mean:.4f}  (Theoretical: {theo_mean:.4f})  | Error: {abs(sample_mean - theo_mean):.4f}")
print(f"Sample Variance: {sample_var:.4f}  (Theoretical: {theo_var:.4f})  | Error: {abs(sample_var - theo_var):.4f}")
print(f"Sample Std Dev:  {sample_std:.4f}  (Theoretical: {theo_std:.4f})  | Error: {abs(sample_std - theo_std):.4f}")
print(f"MLE p-hat:       {sample_mean / n_sim:.4f}  (True p: {p_sim:.4f})")
print("All Binomial figures generated and metrics saved successfully!")
