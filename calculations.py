from math import comb

# Function to calculate probability using hypergeometric distribution
def hypergeometric(N: int, K: int, n: int, k: int) -> float:
    """
    P(X = k) = [C(K, k) * C(N - K, n - k)] / C(N, n)
    """
    if k > K or n > N or (n - k) > (N - K):
        return 0.0  # Impossible case

    numerator = comb(K, k) * comb(N - K, n - k)
    denominator = comb(N, n)

    if denominator == 0:
        return 0.0

    return numerator / denominator