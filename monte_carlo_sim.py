import numpy as np
import matplotlib.pyplot as plt

# PARAMETERS
S0 = 100        # Initial Stock Price
T = 1.0         # Time horizon (1 year)
mu = 0.07       # Expected Annual Return (Drift) -> 7%
sigma = 0.20    # Annual Volatility -> 20%
n_steps = 252   # Trading days in a year
n_sims = 1000   # Number of simulations

# MATHEMATICAL MODEL: GBM 
dt = T / n_steps
random_shocks = np.random.normal(0, 1, (n_steps, n_sims))
S = np.zeros((n_steps + 1, n_sims))
S[0] = S0

for t in range(1, n_steps + 1):
    S[t] = S[t-1] * np.exp((mu - 0.5 * sigma**2) * dt + 
                           sigma * np.sqrt(dt) * random_shocks[t-1])

# RISK METRICS CALCULATION
final_prices = S[-1]
expected_mean = np.mean(final_prices)
VaR_95 = np.percentile(final_prices, 5) # 5th percentile

# VISUALIZATION
plt.figure(figsize=(12, 6))
plt.plot(S[:, :50], alpha=0.4) # Show first 50 paths
plt.title(f'Monte Carlo Simulation: GBM ({n_sims} Scenarios)')
plt.xlabel('Trading Days')
plt.ylabel('Price')
plt.axhline(S0, color='black', linestyle='--', label='Start Price')

# ADDING TEXT BOX WITH STATISTICS 
# Displaying key metrics directly on the chart
stats_text = (f"Initial Price: {S0}\n"
              f"Exp. Mean: {expected_mean:.2f}\n"
              f"VaR (95%): {VaR_95:.2f}")

# Position the text box in the top-left corner
plt.text(0.02, 0.85, stats_text, transform=plt.gca().transAxes,
         fontsize=12, verticalalignment='top',
         bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

plt.grid(True, alpha=0.3)
plt.legend(loc='upper right')

# Save
plt.savefig('monte_carlo_results.png')
print("Simulation complete. Results saved as 'monte_carlo_results.png'.")

plt.show()