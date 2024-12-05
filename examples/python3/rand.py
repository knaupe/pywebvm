import numpy as np

def print_ascii_histogram(data, bins=10, symbol='#'):
    """
    Print an ASCII histogram for the given data.
    """
    counts, bin_edges = np.histogram(data, bins=bins)
    max_count = max(counts)
    width = 50  # Maximum width for the histogram in characters

    print("\nASCII Histogram:")
    for i in range(len(counts)):
        bar = symbol * int(counts[i] * width / max_count)
        print(f"{bin_edges[i]:>7.2f} - {bin_edges[i + 1]:>7.2f} | {bar} ({counts[i]})")

def generate_random_data(distribution="normal", size=10000):
    """
    Generate random data based on the selected distribution.
    """
    if distribution == "normal":
        return np.random.normal(50, 10, size)  # Mean=50, Std Dev=10
    elif distribution == "uniform":
        return np.random.uniform(0, 100, size)  # Range [0, 100]
    elif distribution == "exponential":
        return np.random.exponential(10, size)  # Scale=10
    elif distribution == "binomial":
        return np.random.binomial(100, 0.5, size)  # n=100, p=0.5
    else:
        raise ValueError("Unsupported distribution!")

def get_expected_values_and_description(distribution):
    """
    Get the theoretical mean, standard deviation, and histogram shape for the given distribution.
    """
    if distribution == "normal":
        return (50, 10, "Bell-shaped (Gaussian curve)")
    elif distribution == "uniform":
        # For uniform [0, 100], mean = (a + b) / 2, std = sqrt((b - a)^2 / 12)
        a, b = 0, 100
        mean = (a + b) / 2
        std = np.sqrt((b - a) ** 2 / 12)
        return (mean, std, "Flat (equal height across range)")
    elif distribution == "exponential":
        # For exponential, mean = scale, std = scale
        scale = 10
        return (scale, scale, "Bottom-skewed (steep decay)")
    elif distribution == "binomial":
        # For binomial, mean = n * p, std = sqrt(n * p * (1 - p))
        n, p = 100, 0.5
        mean = n * p
        std = np.sqrt(n * p * (1 - p))
        return (mean, std, "Bell-shaped (discrete bins)")
    else:
        raise ValueError("Unsupported distribution!")

def display_distribution_data(distribution, data):
    """
    Display formatted summary statistics and ASCII histogram for a distribution.
    """
    expected_mean, expected_std, histogram_shape = get_expected_values_and_description(distribution)
    actual_mean = np.mean(data)
    actual_std = np.std(data)
    print(f"\n{distribution.capitalize()} Distribution Data (10000 values):")
    print(f"Expected shape: {histogram_shape}")
    print(f"Mean: {actual_mean:.2f} (expected {expected_mean:.2f})")
    print(f"Std Dev: {actual_std:.2f} (expected {expected_std:.2f})")
    print(f"Min: {np.min(data):.2f}, Max: {np.max(data):.2f}")
    print_ascii_histogram(data, bins=20)

def main():
    print("Welcome to the NumPy Random Data Demonstration!")
    print("Select a distribution to generate random data:")
    print("0. All Distributions")
    print("1. Normal (Gaussian) Distribution")
    print("2. Uniform Distribution")
    print("3. Exponential Distribution")
    print("4. Binomial Distribution")
    
    choice = input("\nEnter your choice (0/1/2/3/4) [default = 0]: ").strip()
    if not choice or choice not in {"0", "1", "2", "3", "4"}:
        print("Invalid or no input received, defaulting to '0' (All Distributions).")
        choice = "0"
    
    distribution_map = {
        "1": "normal",
        "2": "uniform",
        "3": "exponential",
        "4": "binomial"
    }

    if choice == "0":
        for dist_name in ["normal", "uniform", "exponential", "binomial"]:
            data = generate_random_data(distribution=dist_name, size=10000)
            display_distribution_data(dist_name, data)
    elif choice in distribution_map:
        distribution = distribution_map[choice]
        data = generate_random_data(distribution=distribution, size=10000)
        display_distribution_data(distribution, data)

if __name__ == "__main__":
    main()
