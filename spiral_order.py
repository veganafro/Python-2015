"""
This program looks at a square matrix of single digit elements and prints them in a clock-wise
spiral order
"""



dimensions = input("What's the size of your matrix?\n>")

matrix = input("Enter the elements in each row separated by a comma:\n>")

list_container = matrix.split(",")

top_idx = 0
left_idx = 0
right_idx = int(dimensions) - 1
bottom_idx = int(dimensions) - 1


def spiral_order(elements, top_row, left_column, right_column, bottom_row):
    #look at the top elements between the left and right columns inclusive
    for top_characters in elements[top_row][left_column:right_column + 1]:
        print(top_characters)
    #move down to a new top row
    top_row += 1
    #look at the right elements between the new top row and bottom row inclusive
    for right_characters in elements[top_row:bottom_row + 1]:
        print(right_characters[right_column])
    #move left to a new right column
    right_column -= 1
    #look at the bottom elements between the new right column (inclusive) and left column (exclusive)
    for bottom_characters in elements[bottom_row][right_column:left_column:-1]:
        print(bottom_characters)
    #move up to a new bottom row
    bottom_row -= 1
    #look at the left elements between the previous bottom row (inclusive) and the previous top row (exclusive)
    for left_characters in elements[bottom_row + 1:top_row - 1:-1]:
        print(left_characters[left_column])
    #move right to a new left column
    left_column += 1
    #while the left and right columns/top and bottom rows aren't the same, continue with the new parameters
    if left_column <= right_column and top_row <= bottom_row:
        spiral_order(elements, top_row, left_column, right_column, bottom_row)

spiral_order(list_container, top_idx, left_idx, right_idx, bottom_idx)