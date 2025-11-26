scheduler_events = {
    "weekly": [
        "your_app.your_module.doctype.pharmacy_inventory.pharmacy_inventory.weekly_pharmacy_check"
    ]
}

import frappe

def weekly_pharmacy_check():
    low_stock_items = frappe.get_all(
        "Pharmacy Inventory",
        filters=[["stock_quantity", "<", "reorder_level"]],
        fields=["medicine_name", "stock_quantity", "reorder_level"]
    )

    if not low_stock_items:
        return

    message = "<h3>Weekly Pharmacy Stock Check</h3><ul>"
    for item in low_stock_items:
        message += f"<li>{item['medicine_name']} → {item['stock_quantity']} (Reorder Level: {item['reorder_level']})</li>"
    message += "</ul>"

    # Send notification to pharmacy manager
    frappe.sendmail(
        recipients=["pharmacy.manager@example.com"],
        subject="Weekly Pharmacy Replenishment Alert",
        message=message
    )