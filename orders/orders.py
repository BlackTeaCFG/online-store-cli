from datetime import datetime

class Order:
    STATUS_PENDING = "pending"
    STATUS_PROCESSING = "processing"
    STATUS_SHIPPED = "shipped"
    STATUS_DELIVERED = "delivered"
    STATUS_CANCELLED = "cancelled"
    
    def __init__(self, id, customer_name, customer_email):
        self.id = id
        self.customer_name = customer_name
        self.customer_email = customer_email
        self.items = {}  # product_id -> quantity
        self.created_at = datetime.now()
        self.status = self.STATUS_PENDING
        self.total_amount = 0.0
    
    def add_item(self, product, quantity=1):
        """Add product to order"""
        if product.id in self.items:
            self.items[product.id] += quantity
        else:
            self.items[product.id] = quantity
            
        self.total_amount += product.price * quantity
        return True
    
    def remove_item(self, product_id):
        """Remove product from order"""
        if product_id in self.items:
            del self.items[product_id]
            return True
        return False
    
    def update_status(self, new_status):
        """Update order status"""
        valid_statuses = [
            self.STATUS_PENDING, 
            self.STATUS_PROCESSING,
            self.STATUS_SHIPPED,
            self.STATUS_DELIVERED,
            self.STATUS_CANCELLED
        ]
        
        if new_status in valid_statuses:
            self.status = new_status
            return True
        return False
    
    def __str__(self):
        return f"Order(id={self.id}, customer={self.customer_name}, items={len(self.items)}, total=${self.total_amount:.2f})"


class OrderManager:
    def __init__(self, product_catalog):
        self.orders = {}
        self.next_id = 1
        self.product_catalog = product_catalog
    
    def create_order(self, customer_name, customer_email):
        """Create a new order"""
        order_id = self.next_id
        self.next_id += 1
        
        order = Order(order_id, customer_name, customer_email)
        self.orders[order_id] = order
        return order
    
    def get_order(self, order_id):
        """Get order by ID"""
        return self.orders.get(order_id)
    
    def add_product_to_order(self, order_id, product_id, quantity=1):
        """Add product to an existing order"""
        order = self.get_order(order_id)
        product = self.product_catalog.get_product(product_id)
        
        if not order or not product:
            return False
            
        if product.quantity < quantity:
            return False  # Not enough inventory
            
        # Update inventory
        self.product_catalog.update_product(product_id, quantity=product.quantity - quantity)
        
        # Add to order
        return order.add_item(product, quantity)
    
    def list_orders(self):
        """Get all orders"""
        return list(self.orders.values())
    
    def search_orders_by_customer(self, customer_email):
        """Search orders by customer email"""
        results = []
        
        for order in self.orders.values():
            if order.customer_email.lower() == customer_email.lower():
                results.append(order)
                
        return results