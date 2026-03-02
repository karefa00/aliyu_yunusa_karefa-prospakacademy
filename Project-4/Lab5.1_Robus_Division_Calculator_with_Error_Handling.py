
# Lab 5.5: Basic CSV-like File Parser

DATA_FILE = "products.csv"


def parse_product_data(filename):
    product_list = []

    try:
        with open(filename, "r") as file:
            next(file)  # Skip header

            for line in file:
                try:
                    line = line.strip()
                    parts = line.split(",")

                    if len(parts) != 3:
                        print(f"Warning: Skipping malformed row: {line}")
                        continue

                    product_name = parts[0]
                    price = float(parts[1])
                    quantity = int(parts[2])

                    product_dict = {
                        "Product": product_name,
                        "Price": price,
                        "Quantity": quantity
                    }

                    product_list.append(product_dict)

                except ValueError:
                    print(f"Warning: Skipping invalid data row: {line}")

        return product_list

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return []


# Main Program
product_data = parse_product_data(DATA_FILE)

if product_data:
    print("\n--- Product Inventory Report ---")
    print("Product   | Price     | Quantity | Value")
    print("-------------------------------------------")

    total_inventory_value = 0

    for product in product_data:
        item_value = product["Price"] * product["Quantity"]
        total_inventory_value += item_value

        print(f"{product['Product']:<9} | "
              f"${product['Price']:<9.2f} | "
              f"{product['Quantity']:<8} | "
              f"${item_value:.2f}")

    print("-------------------------------------------")
    print(f"Total Inventory Value: ${total_inventory_value:.2f}")
else:
    print("No valid product data available.")