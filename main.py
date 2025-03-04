# main.py
from products.products import ProductCatalog
from orders.orders import OrderManager

def main():
    print("Hello, Online Store CLI!")
    print("Welcome to our command-line shopping application")
    
    # Example of using the product catalog
    catalog = ProductCatalog()
    
    # Add some sample products
    laptop_id = catalog.add_product("Laptop", 999.99, "High-performance laptop", 10)
    phone_id = catalog.add_product("Smartphone", 499.99, "Latest model smartphone", 20)
    
    print("\nAvailable products:")
    for product in catalog.list_products():
        print(f"- {product.name}: ${product.price} ({product.quantity} in stock)")
    
    # Create an order
    order_manager = OrderManager(catalog)
    order = order_manager.create_order("John Doe", "john@example.com")
    
    # Add products to the order
    order_manager.add_product_to_order(order.id, laptop_id, 1)
    order_manager.add_product_to_order(order.id, phone_id, 2)
    
    # Display order info
    print("\nOrder created:")
    print(f"Order #{order.id} for {order.customer_name}")
    print(f"Total amount: ${order.total_amount:.2f}")
    print(f"Status: {order.status}")

if __name__ == "__main__":
    main()
