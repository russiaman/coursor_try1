import os

def get_size_format(size):
    # Convert size to human readable format
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            return f"{size:.2f} {unit}"
        size /= 1024.0
    return f"{size:.2f} PB"

def scan_directory():
    # Ask user for directory path
    path = input("Please enter the path to the directory you want to scan: ")
    
    # Check if the path exists
    if not os.path.exists(path):
        print(f"Error: The path '{path}' does not exist.")
        return
    
    # Check if it's a directory
    if not os.path.isdir(path):
        print(f"Error: '{path}' is not a directory.")
        return
    
    print("\nContents of the directory:")
    print("-" * 80)
    print(f"{'Type':<8} {'Name':<40} {'Size':<15}")
    print("-" * 80)
    
    # List all items in the directory
    try:
        for item in os.listdir(path):
            full_path = os.path.join(path, item)
            # Add a marker to indicate if it's a directory
            if os.path.isdir(full_path):
                print(f"[DIR]   {item:<40} {'-':<15}")
            else:
                size = os.path.getsize(full_path)
                size_str = get_size_format(size)
                print(f"[FILE]  {item:<40} {size_str:<15}")
    except PermissionError:
        print("Error: Permission denied to access this directory.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    scan_directory() 