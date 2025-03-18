# **Case Study: Small Shop Inventory and Sales Management (OOP & Menu-Driven)**  

## **Objective**  
This case study helps new programmers practice **file handling, object-oriented programming (OOP), and user input handling** in Python.  

## **Sample Data**

**Products**
```csv
product_id,product_name,price,quantity
101,Soap,20,50
102,Shampoo,120,30
103,Toothpaste,60,40
104,Rice,500,20
105,Sugar,45,25
```

**Sales**
```csv
sale_id,product_id,product_name,quantity_sold,total_price
1,102,Shampoo,2,240
1,101,Soap,3,60
2,104,Rice,1,500
```

## **Features**  
✅ **Manage inventory** (add, view, and update products).  
✅ **Record sales with multiple products** in one sale.  
✅ **Update inventory when a sale is made**.

✅ **Display inventory and sales reports in a **tabular format**.  
✅ **Menu-driven interface** for easy interaction.  

---

## **Class Structure**
- **`Product`**: Represents a product with ID, name, price, and stock quantity.  
- **`Inventory`**: Manages product storage, addition, and updates.  
- **`Sale`**: Represents a single sale, which can include multiple products.  
- **`SalesManager`**: Handles sales processing and record-keeping.  
- **`ShopSystem`**: Provides a menu-driven interface for users.  

---

## **Features Implemented**
✅ **Object-Oriented Design** (Classes: `Product`, `Inventory`, `Sale`, `SalesManager`, `ShopSystem`).  
✅ **File Handling** (`inventory.csv` and `sales.csv`).  
✅ **Exception Handling** .
✅ **Menu-Driven System** (User interacts via a simple interface).  
✅ **Validation** (Check if products exist before selling).  
✅ **Tabular Display** (`tabulate` for inventory and sales reports).  
✅ **One Sale Includes Multiple Products**.  

---

## **Expected Output**
Example:
```
--- Small Shop Management System ---
1. View Inventory
2. Add Product to Inventory
3. Process a Sale
4. View Sales Report
5. Exit
Enter your choice: 3
Enter Sale ID: 1001
Enter Product ID to sell: 101
Enter quantity for Soap: 3
Enter Product ID to sell (or 'done' to finish): done
Sale 1001 recorded successfully.
```
