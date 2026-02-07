import sqlite3
import pandas as pd

def run_assignment():
    db_path = 'company_xyz.db' # Ensure this matches the provided DB name
    
    try:
        conn = sqlite3.connect(db_path)
        
        # SQL Query addressing all business rules
        query = """
        SELECT 
            c.customer_id AS Customer, 
            c.age AS Age, 
            i.item_name AS Item, 
            CAST(SUM(o.quantity) AS INTEGER) AS Quantity
        FROM Customer c
        JOIN Sales s ON c.customer_id = s.customer_id
        JOIN Orders o ON s.sales_id = o.sales_id
        JOIN Items i ON o.item_id = i.item_id
        WHERE c.age BETWEEN 18 AND 35
        GROUP BY c.customer_id, i.item_id
        HAVING Quantity > 0
        """
        
        # Extract and export
        df = pd.read_sql_query(query, conn)
        df.to_csv('output.csv', sep=';', index=False)
        print("Success: output.csv has been generated.")
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if 'conn' in locals():
            conn.close()

if __name__ == "__main__":
    run_assignment()
