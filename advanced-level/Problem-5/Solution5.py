from scipy.stats import pearsonr

def calculate_correlation(x, y):
    if len(x) != len(y) or len(x) < 2:
        return None
    correlation, _ = pearsonr(x, y)
    return correlation

# Test the function
x = [1, 2, 3]
y = [2, 4, 6]
print(calculate_correlation(x, y))