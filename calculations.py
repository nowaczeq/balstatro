from math import comb

# Function to calculate probability using hypergeometric distribution
def univ_hypergeometric(N: int, K: int, n: int, k: int) -> float:
    """
    Calculate the probability of drawing exactly k successes from a population using the hypergeometric distribution.

    Args:
        N (int): Total population size.
        K (int): Number of success states in the population.
        n (int): Number of draws.
        k (int): Desired number of successful outcomes.

    Returns:
        float: The probability of exactly k successes in n draws from a population of size N with K successes.
        
    Formula:
        P(X = k) = [C(K, k) * C(N - K, n - k)] / C(N, n)
    """
    if k > K or n > N or (n - k) > (N - K):
        return 0.0  # Impossible case

    numerator = comb(K, k) * comb(N - K, n - k)
    denominator = comb(N, n)

    if denominator == 0:
        return 0.0

    return numerator / denominator

def multiv_hypergeometric(N: int, K_x: list[int], n: int, k_x: list[int]) -> float:
    """
    Calculate the probability of drawing exactly k_x[i] successes for each category i from
    a population of size N with K_x[i] success states in each category, using the multivariate 
    hypergeometric distribution.

    Args:
        N (int): Total population size.
        K_x (list[int]): List of counts of success states in each category in the population.
        n (int): Number of draws.
        k_x (list[int]): List of desired number of successful outcomes in each category.

    Returns:
        float: Probability of drawing exactly the specified successes in n draws.
    
    Formula:
        P(X = k) = [C(K_1, k_1) * C(K_2, k_2) * ... * C(K_x, k_x) 
        * C(N - K_1 - K_2 - ... - K_x, n - k_1 - k_2 - ... - k_2)]
        / C(N, n)
    """

    # Ensure that at least two categories have been supplied for success states
    if not (isinstance(K_x, list)) or not (isinstance(k_x, list)):
        raise ValueError("Univariate arguments passes to multivariate version of hypergeometric calculation. Change function to hypergeometric() instead")

    # Ensure that the count of successful categories is the same
    if len(K_x) != len(k_x):
        raise ValueError(f"Hypergeometric: K_x is of length {len(K_x)}, k_x is of length {len(k_x)} - must be the same for successful hypergeometric probability calculation.")
    
    # Eliminate impossible cases
    if sum(k_x) > n or sum(K_x) > N or any(k > K for k, K in zip(k_x, K_x)):
        return 0.0  # Impossible case
    
    # Calculate the first part of the numerator (combination of success states and desired successes)
    numerator = 1
    for K, k in zip(K_x, k_x):
        numerator *= comb(K, k)

    # Calculate the second part of the numerator (number of ways to choose other cards)
    numerator  *= comb(N - sum(K_x), n - sum(k_x))


    # Calculate the denominator
    denominator = comb(N, n)
    if denominator == 0:
        return 0.0

    # Return the calculated probability 
    return numerator / denominator