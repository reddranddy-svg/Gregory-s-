def manage_array():
    # 1. Create an array (list) of any size
    size = int(input("Enter the initial size of the array: "))
    arr = []
    
    print(f"Enter {size} elements:")
    for i in range(size):
        element = input(f"Element {i+1}: ")
        arr.append(element)
        
    print("\nInitial Array:", arr)

    # 2. Insert a value into the array
    insert_value = input("\nEnter a value to insert: ")
    position = int(input(f"Enter the index (0 to {len(arr)}) where you want to insert it: "))
    
    if 0 <= position <= len(arr):
        arr.insert(position, value=insert_value)
        print("Array after insertion:", arr)
    else:
        print("Invalid position! Insertion failed.")

    # 3. Delete a value from the array
    delete_value = input("\nEnter the value you want to delete: ")
    
    if delete_value in arr:
        arr.remove(delete_value)
        print("Array after deletion:", arr)
    else:
        print(f"Value '{delete_value}' not found in the array.")

    print("\nFinal Array:", arr)

if __name__ == "__main__":
    manage_array()
