# TEST1_5 for CS132SP_2025
# Using this source I was able to understand how to create the program below using Dynamic Programming
# https://www.geeksforgeeks.org/binomial-coefficient-dp-9/

# This Function is very similar to the Binomial Coefficient function with a bit of a twist
# Mystery Function M
def M(n, k):
    # Creates the Dynamically Progammed table, with n+1 rows and k+1 columns
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    # Base Case, if n >= 0 and k == 0:
    for i in range (n + 1):
        dp[i][0] = 1

    # Filling DP table, (k * M(n-1, k-1)) + M(n-1, k)
    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            dp[i][j] = (j * dp[i - 1][j-1]) + dp[i - 1][j]

    return dp[n][k]

# Main function, asks for user input
def main():
    print("""This program computes, using dynamic programming,
the Mystery Function M(n,k):
M(n,k) = k*M(n-1,k-1) + M(n-1,k)
M(n,0) = 1 for all n >= 0
M(i,j) = 0 for all j > i\n""")
    
    # Asks for user inputs
    n_input = int(input("Enter n: "))
    k_input = int(input("Enter k: "))

    # Calls Mystery function, passing in user values
    deliverable = M(n_input, k_input)

    # Prints the deliverable value of M(n,k)
    print(f"The value of M({n_input},{k_input}) is {deliverable}")

main()