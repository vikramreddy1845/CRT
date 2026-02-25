def pascal_triangle(n):
    
    triangle = []
    
    for i in range(n):
        row = [1]
        
        if i > 0:
            for j in range(1, i):
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
            row.append(1)
        
        triangle.append(row)
    
    return triangle


def print_pascal_triangle(n):
    
    triangle = pascal_triangle(n)
    
    for row in triangle:
        print(" ".join(map(str, row)))



if __name__ == "__main__":
    num_rows = 5
    print_pascal_triangle(num_rows)