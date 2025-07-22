# Imports
import random
import numpy as np
import matplotlib as plt 
import matplotlib.pyplot as plt
from scipy.stats import expon

# 1. Coin Toss Simulation
def coin_toss_simulation(n=10000):
    heads = sum(1 for _ in range(n) if random.choice(['H', 'T']) == 'H')
    tails = n - heads
    print(f"Coin Toss - Heads: {heads/n:.4f}, Tails: {tails/n:.4f}")

# 2. Dice Sum Simulation
def dice_sum_simulation(n=10000):
    count_7 = sum(1 for _ in range(n) if sum([random.randint(1, 6), random.randint(1, 6)]) == 7)
    print(f"Probability of sum 7 when rolling two dice: {count_7/n:.4f}")

# 3. Probability of At Least One 6
def probability_at_least_one_6(trials=10000):
    success = 0
    for _ in range(trials):
        if 6 in [random.randint(1, 6) for _ in range(10)]:
            success += 1
    print(f"Probability of at least one 6 in 10 rolls: {success/trials:.4f}")

# 4. Conditional Probability & Bayes
def conditional_probability_simulation(trials=1000):
    colors = ['R']*5 + ['G']*7 + ['B']*8
    prev, count_rb = None, 0
    blue_followed_by_red = 0
    for _ in range(trials):
        current = random.choice(colors)
        if prev == 'B':
            count_rb += 1
            if current == 'R':
                blue_followed_by_red += 1
        prev = current
    if count_rb > 0:
        cond_prob = blue_followed_by_red / count_rb
        print(f"P(Red | Blue before) = {cond_prob:.4f}")
    else:
        print("Not enough blue balls drawn for conditional probability.")
    # Bayes' Theorem Approximation
    p_r = 5 / 20
    p_b = 8 / 20
    p_b_given_r = 8 / 20
    bayes_theorem = (p_b_given_r * p_r) / p_b
    print(f"Bayes Theorem Approximation: {bayes_theorem:.4f}")

# 5. Discrete Random Variable
def discrete_random_variable():
    values = [1, 2, 3]
    probs = [0.25, 0.35, 0.4]
    sample = np.random.choice(values, size=1000, p=probs)
    mean = np.mean(sample)
    variance = np.var(sample)
    std_dev = np.std(sample)
    print(f"Mean: {mean:.4f}, Variance: {variance:.4f}, Std Dev: {std_dev:.4f}")

# 6. Exponential Distribution
def exponential_distribution():
    data = np.random.exponential(scale=5, size=2000)
    plt.hist(data, bins=50, density=True, alpha=0.6, color='skyblue', label='Histogram')
    x = np.linspace(0, max(data), 1000)
    pdf = expon.pdf(x, scale=5)
    plt.plot(x, pdf, 'r', label='PDF')
    plt.title('Exponential Distribution (mean=5)')
    plt.xlabel('Value')
    plt.ylabel('Density')
    plt.legend()
    plt.show()

# 7. Central Limit Theorem
def central_limit_theorem():
    data = np.random.uniform(0, 1, 10000)
    plt.hist(data, bins=50, alpha=0.5, label='Original Uniform Data')
    sample_means = [np.mean(np.random.choice(data, 30)) for _ in range(1000)]
    plt.hist(sample_means, bins=50, alpha=0.7, label='Sample Means')
    plt.title('Central Limit Theorem')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.legend()
    plt.show()

# 8. Run All Simulations
def run_all():
    coin_toss_simulation()
    dice_sum_simulation()
    probability_at_least_one_6()
    conditional_probability_simulation()
    discrete_random_variable()
    exponential_distribution()
    central_limit_theorem()

# Run all
run_all()
