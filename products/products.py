class Product:
    def __init__(self, id, name, price, description="", quantity=0):
        self.id = id
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity
    
    def __str__(self):
        return f"Product(id={self.id}, name={self.name}, price={self.price}, quantity={self.quantity})"


class ProductCatalog:
    def __init__(self):
        self.products = {}
        self.next_id = 1
    
    def add_product(self, name, price, description="", quantity=0):
        """Add a new product to the catalog"""
        product_id = self.next_id
        self.next_id += 1
        
        product = Product(product_id, name, price, description, quantity)
        self.products[product_id] = product
        return product_id
    
    def get_product(self, product_id):
        """Get a product by ID"""
        return self.products.get(product_id)
    
    def update_product(self, product_id, **kwargs):
        """Update product properties"""
        product = self.get_product(product_id)
        if not product:
            return False
        
        for key, value in kwargs.items():
            if hasattr(product, key):
                setattr(product, key, value)
        
        return True
    
    def delete_product(self, product_id):
        """Remove a product from the catalog"""
        if product_id in self.products:
            del self.products[product_id]
            return True
        return False
    
    def list_products(self, in_stock_only=False):
        """Get all products in the catalog, with option to show only in-stock items"""
        if in_stock_only:
            return [p for p in self.products.values() if p.quantity > 0]
        return list(self.products.values())
    
    def search_products(self, keyword):
        """Search products by name or description"""
        keyword = keyword.lower()
        results = []
        
        for product in self.products.values():
            if keyword in product.name.lower() or keyword in product.description.lower():
                results.append(product)
                
        return results