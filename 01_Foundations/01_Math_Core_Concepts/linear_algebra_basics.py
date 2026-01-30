import numpy as np

def dot_product(v1, v2):
    """
    Calculate the dot product of two vectors v1 and v2.
    Vectors are represented as lists of numbers.
    
    Formula: sum(v1[i] * v2[i])
    """
    # TODO: Implement this function without using numpy
    result = 0
    if len(v1) != len(v2):
        raise ValueError("Vectors must have the same length")
    
    for i in range(len(v1)):
        result += v1[i] * v2[i]
    
    return result

def matrix_multiply(A, B):
    """
    Calculate the matrix multiplication of 2D matrices A and B.
    Matrices are represented as lists of lists.
    
    Formula: C[i][j] = sum(A[i][k] * B[k][j])
    """
    # TODO: Implement this function without using numpy
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])
    
    if cols_A != rows_B:
         raise ValueError("Number of columns in A must equal number of rows in B")
    
    # Initialize result matrix with zeros
    C = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
    
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                C[i][j] += A[i][k] * B[k][j]
    
    return C

def main():
    # Test Vectors
    v1 = [1, 2, 3]
    v2 = [4, 5, 6]
    
    print(f"Vectors:\n v1: {v1}\n v2: {v2}")
    
    # Your implementation
    dp_custom = dot_product(v1, v2)
    # Numpy implementation for verification
    dp_numpy = np.dot(v1, v2)
    
    print(f"Dot Product (Custom): {dp_custom}")
    print(f"Dot Product (Numpy):  {dp_numpy}")
    
    # Test Matrices
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    
    print(f"\nMatrices:\n A: {A}\n B: {B}")
    
    # Your implementation
    mm_custom = matrix_multiply(A, B)
    # Numpy implementation for verification
    mm_numpy = np.matmul(A, B)
    
    print(f"Matrix Mult (Custom): {mm_custom}")
    print(f"Matrix Mult (Numpy):  \n{mm_numpy}")

if __name__ == "__main__":
    main()
