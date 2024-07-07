# Sum Triangle

def generate_sum_triangle(rows):
    triangle = []

    for row_number in range(rows):
        row = [1] * (row_number + 1)  
        for j in range(1, row_number):
            row[j] = triangle[row_number - 1][j - 1] + triangle[row_number - 1][j]

        triangle.append(row)

    return triangle

def print_sum_triangle(triangle):
    for row in triangle:
        print(" ".join(map(str, row)))

rows = int(input("Enter the number of rows:"))
triangle = generate_sum_triangle(rows)
print_sum_triangle(triangle)
