import frappe

def run_weekly_pharmacy_check():
    frappe.logger().info("Weekly Pharmacy Check Running...")

    low_stock_items = frappe.get_all(
        "Pharmacy Inventory",
        filters={"stock_quantity": ["<", "reorder_level"]},
        fields=["medicine", "stock_quantity", "reorder_level"]
    )

    for item in low_stock_items:
        frappe.msgprint(f"Low Stock: {item.medicine} ({item.stock_quantity})")

    # You can also email alert automatically
