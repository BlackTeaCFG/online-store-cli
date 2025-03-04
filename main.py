from products.products import ProductCatalog

def main():
    print("Hello, Online Store CLI!")
    print("Welcome to our command-line shopping application")
    
    # Example of using the product catalog
    catalog = ProductCatalog()
    
    # Add some sample products
    catalog.add_product("Laptop", 999.99, "High-performance laptop", 10)
    catalog.add_product("Smartphone", 499.99, "Latest model smartphone", 20)
    
    print("\nAvailable products:")
    for product in catalog.list_products():
        print(f"- {product.name}: ${product.price} ({product.quantity} in stock)")

if __name__ == "__main__":
    main()
