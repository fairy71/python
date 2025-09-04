import pandas as pd

# Load the dataset from a CSV file
try:
    df = pd.read_csv('sales_data.csv')
except FileNotFoundError:
    print("Error: 'sales_data.csv' not found. Please ensure the file is in the correct directory.")
    # Create a dummy DataFrame for demonstration if file not found
    data = {
        'OrderID': range(1, 11),
        'Product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Laptop', 'Webcam', 'Mouse', 'Headphones', 'Laptop', 'Keyboard'],
        'Category': ['Electronics', 'Electronics', 'Electronics', 'Electronics', 'Electronics', 'Electronics', 'Electronics', 'Electronics', 'Electronics', 'Electronics'],
        'Quantity': [1, 2, 1, 1, 1, 3, 2, 1, 1, 1],
        'Price': [1200, 25, 75, 300, 1150, 40, 20, 50, 1300, 80],
        'SaleDate': pd.to_datetime(['2024-01-10', '2024-01-12', '2024-01-15', '2024-02-01', '2024-02-05', '2024-02-10', '2024-03-01', '2024-03-05', '2024-03-10', '2024-03-15']),
        'CustomerSegment': ['New', 'Existing', 'New', 'Existing', 'New', 'New', 'Existing', 'Existing', 'New', 'Existing']
    }
    df = pd.DataFrame(data)
    print("Dummy DataFrame created for demonstration.")

print("Initial DataFrame head:")
print(df.head())