import numpy as np
from tqdm import tqdm

# Solution
def increment(counters: np.ndarray, value: np.uint64, c: int):
    rands = np.random.random(c).astype(np.float64)
    probs = np.minimum(1.0, value / (2 ** counters).astype(np.float64))
    counters += (rands < probs)

def estimate(counters: np.ndarray) -> np.uint64:
    estimates = (2 ** counters - 1).astype(np.uint64)
    return np.mean(estimates, dtype=np.float64).astype(np.uint64)

def approximate_stream_sum(stream: np.ndarray, c: int) -> np.uint64:
    counters = np.zeros(c, dtype=np.uint64)
    
    for value in stream:
        increment(counters, np.uint64(value), c)
        
    return estimate(counters)

# Analysis
def calculate_accuracy(m: np.uint64, n: np.uint64, c: int, trials: int):
    errors = np.zeros(trials)
    
    # Pre-generate all random integers for all trials
    all_random_integers = np.random.randint(1, n + 1, size=(trials, m))
    # all_random_integers = np.full((trials, m), n, dtype=np.uint64)
    for i in tqdm(range(trials)):
        random_integers = all_random_integers[i]
        actual_sum = np.sum(random_integers, dtype=np.uint64)
        approx_sum = approximate_stream_sum(random_integers, c)
        errors[i] = abs(np.float64(actual_sum) - np.float64(approx_sum)) / np.float64(actual_sum)
    
    return {
        'avg_error': np.mean(errors),
        'md_error': np.median(errors),
        'std_error': np.std(errors),
        'max_error': np.max(errors),
        'min_error': np.min(errors),
        'percentile_95': np.percentile(errors, 95),
        'iqr': np.percentile(errors, 75) - np.percentile(errors, 25)
    }

if __name__ == "__main__":
    m = 10**3
    n = 10**3
    c = 1000
    trials = 1000

    results = calculate_accuracy(m, n, c, trials)

    print(f"\nResults for m={m}, n={n}, c={c}:")
    print(f"Average relative error: {results['avg_error']:.2%}")
    print(f"Median relative error: {results['md_error']:.2%}")
    print(f"Standard deviation: {results['std_error']:.2%}")
    print(f"Maximum relative error: {results['max_error']:.2%}")
    print(f"Minimum relative error: {results['min_error']:.2%}")
    print(f"95th percentile error: {results['percentile_95']:.2%}")
    print(f"IQR of error: {results['iqr']:.2%}")