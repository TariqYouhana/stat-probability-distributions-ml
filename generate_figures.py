import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.show = lambda *args, **kwargs: None

import numpy as np
import seaborn as sns
from scipy import stats
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import json

# Set consistent style
sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 12
np.random.seed(42)

print('--- PART A: Distribution Exploration ---')

# Parameters for Gaussian distribution
mu = 50        # True mean
sigma = 10     # True standard deviation
n_samples = 1000

# Generate random samples
samples = np.random.normal(loc=mu, scale=sigma, size=n_samples)

# A1. Histogram with theoretical PDF overlay (SLIDE 13)
fig, ax = plt.subplots(figsize=(10, 6))
ax.hist(samples, bins=40, density=True, alpha=0.6, color='#2563EB', 
        edgecolor='white', label=f'Histogram (n={n_samples})')
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 300)
pdf = stats.norm.pdf(x, loc=mu, scale=sigma)
ax.plot(x, pdf, color='#DC2626', linewidth=2.5, label=f'Theoretical PDF (μ={mu}, σ={sigma})')
ax.set_xlabel('Value', fontsize=13)
ax.set_ylabel('Density', fontsize=13)
ax.set_title('Gaussian Distribution: 1,000 Random Samples vs Theoretical PDF', fontsize=14, fontweight='bold')
ax.legend(fontsize=11)
plt.tight_layout()
plt.savefig('fig_histogram_overlay.png', dpi=200, bbox_inches='tight')
plt.close()
print("Saved fig_histogram_overlay.png")

# A2. Calculate sample statistics (SLIDE 13)
sample_mean = float(np.mean(samples))
sample_var = float(np.var(samples, ddof=1))
sample_std = float(np.std(samples, ddof=1))
theo_mean = float(mu)
theo_var = float(sigma**2)
theo_std = float(sigma)

print(f"Sample Mean: {sample_mean:.4f} | Theoretical: {theo_mean:.4f}")
print(f"Sample Var:  {sample_var:.4f} | Theoretical: {theo_var:.4f}")
print(f"Sample Std:  {sample_std:.4f} | Theoretical: {theo_std:.4f}")

# A3. Effect of Changing Parameters (SLIDE 5)
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
x_range = np.linspace(-10, 30, 400)
for mean_val, color in zip([0, 5, 10, 15], ['#2563EB', '#D97706', '#10B981', '#DC2626']):
    pdf_vals = stats.norm.pdf(x_range, loc=mean_val, scale=3)
    axes[0].plot(x_range, pdf_vals, linewidth=2, label=f'μ = {mean_val}', color=color)
axes[0].set_title('Effect of Changing μ (σ = 3 fixed)', fontsize=13, fontweight='bold')
axes[0].set_xlabel('x')
axes[0].set_ylabel('f(x)')
axes[0].legend()

x_range = np.linspace(-15, 15, 400)
for std_val, color in zip([1, 2, 3, 5], ['#2563EB', '#D97706', '#10B981', '#DC2626']):
    pdf_vals = stats.norm.pdf(x_range, loc=0, scale=std_val)
    axes[1].plot(x_range, pdf_vals, linewidth=2, label=f'σ = {std_val}', color=color)
axes[1].set_title('Effect of Changing σ (μ = 0 fixed)', fontsize=13, fontweight='bold')
axes[1].set_xlabel('x')
axes[1].set_ylabel('f(x)')
axes[1].legend()
plt.tight_layout()
plt.savefig('fig_parameter_effects.png', dpi=200, bbox_inches='tight')
plt.close()
print("Saved fig_parameter_effects.png")

# A4. CDF Plot (SLIDE 5)
fig, ax = plt.subplots(figsize=(10, 6))
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 300)
cdf = stats.norm.cdf(x, loc=mu, scale=sigma)
ax.plot(x, cdf, color='#2563EB', linewidth=2.5, label=f'CDF (μ={mu}, σ={sigma})')
for z, pct in zip([-1, 0, 1], ['15.87%', '50%', '84.13%']):
    x_val = mu + z * sigma
    y_val = stats.norm.cdf(x_val, loc=mu, scale=sigma)
    ax.plot(x_val, y_val, 'ro', markersize=8)
    ax.annotate(f'({x_val:.0f}, {pct})', xy=(x_val, y_val), 
                xytext=(x_val + 2, y_val - 0.08), fontsize=10,
                arrowprops=dict(arrowstyle='->', color='red'))
ax.set_xlabel('Value', fontsize=13)
ax.set_ylabel('Cumulative Probability', fontsize=13)
ax.set_title('Cumulative Distribution Function (CDF) of the Gaussian', fontsize=14, fontweight='bold')
ax.legend(fontsize=11)
ax.axhline(y=0.5, color='gray', linestyle='--', alpha=0.5)
ax.axvline(x=mu, color='gray', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('fig_cdf.png', dpi=200, bbox_inches='tight')
plt.close()
print("Saved fig_cdf.png")

# A5. Empirical Rule 68-95-99.7 (SLIDE 3)
fig, ax = plt.subplots(figsize=(10, 6))
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 500)
y_pdf = stats.norm.pdf(x, loc=mu, scale=sigma)
ax.plot(x, y_pdf, 'k-', linewidth=2)
colors = ['#93C5FD', '#BFDBFE', '#DBEAFE']
labels = ['99.7% (μ ± 3σ)', '95% (μ ± 2σ)', '68% (μ ± 1σ)']
sigmas = [3, 2, 1]
for s, color, label in zip(sigmas, colors, labels):
    x_fill = np.linspace(mu - s*sigma, mu + s*sigma, 300)
    y_fill = stats.norm.pdf(x_fill, loc=mu, scale=sigma)
    ax.fill_between(x_fill, y_fill, alpha=0.6, color=color, label=label)
ax.set_xlabel('Value', fontsize=13)
ax.set_ylabel('Density', fontsize=13)
ax.set_title('The 68-95-99.7 Rule (Empirical Rule)', fontsize=14, fontweight='bold')
ax.legend(fontsize=11, loc='upper right')
for s in [-3, -2, -1, 0, 1, 2, 3]:
    ax.axvline(x=mu + s*sigma, color='gray', linestyle=':', alpha=0.4)
    if s != 0:
        ax.text(mu + s*sigma, -0.002, f'{s}σ', ha='center', fontsize=9, color='gray')
    else:
        ax.text(mu, -0.002, 'μ', ha='center', fontsize=10, fontweight='bold')
plt.tight_layout()
plt.savefig('fig_empirical_rule.png', dpi=200, bbox_inches='tight')
plt.close()
print("Saved fig_empirical_rule.png")

# A6. Bernoulli & Multinomial (SLIDE 6)
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
p_values = [0.3, 0.5, 0.7]
bar_width = 0.2
for i, p in enumerate(p_values):
    x_positions = np.array([0, 1]) + i * bar_width
    probs = [1 - p, p]
    axes[0].bar(x_positions, probs, width=bar_width, alpha=0.85, label=f'p = {p}')
axes[0].set_xticks([0 + bar_width, 1 + bar_width])
axes[0].set_xticklabels(['X = 0 (Failure)', 'X = 1 (Success)'])
axes[0].set_ylabel('Probability')
axes[0].set_title('Bernoulli Distribution (Varying p)', fontsize=13, fontweight='bold')
axes[0].legend()
axes[0].set_ylim(0, 1)

categories = ['Cat A', 'Cat B', 'Cat C', 'Cat D']
probs_set = [
    [0.4, 0.3, 0.2, 0.1],
    [0.25, 0.25, 0.25, 0.25],
]
labels_multi = ['Skewed', 'Uniform']
bar_width = 0.35
x_pos = np.arange(len(categories))
for i, (probs, lbl) in enumerate(zip(probs_set, labels_multi)):
    axes[1].bar(x_pos + i * bar_width, probs, width=bar_width, alpha=0.85, label=lbl)
axes[1].set_xticks(x_pos + bar_width / 2)
axes[1].set_xticklabels(categories)
axes[1].set_ylabel('Probability')
axes[1].set_title('Multinomial Distribution (Single Trial)', fontsize=13, fontweight='bold')
axes[1].legend()
axes[1].set_ylim(0, 0.6)
plt.tight_layout()
plt.savefig('fig_bernoulli_multinomial.png', dpi=200, bbox_inches='tight')
plt.close()
print("Saved fig_bernoulli_multinomial.png")


print('\n--- PART B: Gaussian Naive Bayes Classifier ---')

# B1. Generate Synthetic Dataset (SLIDE 14)
n_class0 = 500
X_class0 = np.random.multivariate_normal(
    mean=[2, 3], 
    cov=[[1.5, 0.3], [0.3, 1.0]], 
    size=n_class0
)
n_class1 = 500
X_class1 = np.random.multivariate_normal(
    mean=[5, 6], 
    cov=[[1.2, -0.2], [-0.2, 1.3]], 
    size=n_class1
)
X = np.vstack([X_class0, X_class1])
y = np.array([0] * n_class0 + [1] * n_class1)

fig, ax = plt.subplots(figsize=(8, 6))
scatter = ax.scatter(X[:, 0], X[:, 1], c=y, cmap='coolwarm', alpha=0.7, edgecolors='w', linewidth=0.5)
ax.set_xlabel('Feature 1', fontsize=13)
ax.set_ylabel('Feature 2', fontsize=13)
ax.set_title('Synthetic Dataset: 2 Classes, 2 Gaussian Features', fontsize=14, fontweight='bold')
plt.colorbar(scatter, label='Class', ticks=[0, 1])
plt.tight_layout()
plt.savefig('fig_synthetic_data.png', dpi=200, bbox_inches='tight')
plt.close()
print("Saved fig_synthetic_data.png")

# B2. Feature Distributions per Class (SLIDE 8)
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
feature_names = ['Feature 1', 'Feature 2']
for i, ax in enumerate(axes):
    ax.hist(X[y == 0, i], bins=30, density=True, alpha=0.5, color='#2563EB', label='Class 0')
    ax.hist(X[y == 1, i], bins=30, density=True, alpha=0.5, color='#DC2626', label='Class 1')
    for cls, color in zip([0, 1], ['#2563EB', '#DC2626']):
        data = X[y == cls, i]
        mu_fit, sigma_fit = stats.norm.fit(data)
        x_rng = np.linspace(data.min() - 1, data.max() + 1, 200)
        ax.plot(x_rng, stats.norm.pdf(x_rng, mu_fit, sigma_fit), 
                color=color, linewidth=2, linestyle='--')
    ax.set_title(f'{feature_names[i]} Distribution by Class', fontsize=13, fontweight='bold')
    ax.set_xlabel(feature_names[i])
    ax.set_ylabel('Density')
    ax.legend()
plt.suptitle('Gaussian NB Assumption: Feature Distributions within Classes', 
             fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig('fig_feature_distributions.png', dpi=200, bbox_inches='tight')
plt.close()
print("Saved fig_feature_distributions.png")

# B3. Train GNB
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
gnb = GaussianNB()
gnb.fit(X_train, y_train)
y_pred = gnb.predict(X_test)
accuracy = float(accuracy_score(y_test, y_pred))
print(f"Test Accuracy: {accuracy*100:.2f}%")

# B4. Confusion Matrix (SLIDE 14)
cm = confusion_matrix(y_test, y_pred)
fig, ax = plt.subplots(figsize=(6, 5))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
            xticklabels=['Class 0', 'Class 1'],
            yticklabels=['Class 0', 'Class 1'],
            annot_kws={'size': 16})
ax.set_xlabel('Predicted Label', fontsize=13)
ax.set_ylabel('True Label', fontsize=13)
ax.set_title('Confusion Matrix — Gaussian Naive Bayes', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('fig_confusion_matrix.png', dpi=200, bbox_inches='tight')
plt.close()
print("Saved fig_confusion_matrix.png")

# B5. Decision Boundary (SLIDE 14)
h = 0.05
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
Z = gnb.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)

fig, ax = plt.subplots(figsize=(10, 7))
ax.contourf(xx, yy, Z, alpha=0.3, cmap='coolwarm')
ax.contour(xx, yy, Z, colors='k', linewidths=0.7)
scatter = ax.scatter(X[:, 0], X[:, 1], c=y, cmap='coolwarm', 
                     alpha=0.6, edgecolors='w', linewidth=0.5, s=25)
ax.set_xlabel('Feature 1', fontsize=13)
ax.set_ylabel('Feature 2', fontsize=13)
ax.set_title('Gaussian Naive Bayes — Decision Boundary & Data Space', fontsize=14, fontweight='bold')
plt.colorbar(scatter, label='Class', ticks=[0, 1])
plt.tight_layout()
plt.savefig('fig_decision_boundary.png', dpi=200, bbox_inches='tight')
plt.close()
print("Saved fig_decision_boundary.png")

# Save summary stats to json for exact inclusion
stats_dict = {
    "sample_mean": round(sample_mean, 4),
    "theo_mean": theo_mean,
    "sample_var": round(sample_var, 4),
    "theo_var": theo_var,
    "sample_std": round(sample_std, 4),
    "theo_std": theo_std,
    "accuracy": round(accuracy * 100, 2),
    "cm": cm.tolist()
}
with open("metrics.json", "w") as f:
    json.dump(stats_dict, f, indent=2)

print("\nAll figures generated and metrics saved successfully!")
