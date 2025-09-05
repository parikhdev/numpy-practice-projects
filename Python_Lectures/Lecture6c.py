def print_list(lst):
    if not lst:
        return
    print(lst[0])
    print_list(lst[1:])

# Example usage
print_list([1, 2, 3, 4, 5])