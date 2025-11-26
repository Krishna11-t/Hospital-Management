# Copyright (c) 2025, Krishna Teja and contributors
# For license information, please see license.txt

# DocType: Pharmacy (or your Issuance DocType)
# Script Type: DocType Event
# Trigger: After Submit

import frappe

def update_stock(doc, method):
    for item in doc.medicines:
        # Fetch Inventory Document
        stock = frappe.get_doc("Pharmacy Inventory", item.medicine)

        # Validate stock availability
        if stock.stock_quantity < item.qty:
            frappe.throw(
                f"Not enough stock for {item.medicine}. "
                f"Available: {stock.stock_quantity}, Required: {item.qty}"
            )

        # Reduce stock
        stock.stock_quantity = stock.stock_quantity - item.qty

        # Save update
        stock.save(ignore_permissions=True)

        # Log and notify
        frappe.msgprint(
            f"Stock updated: {item.medicine} → (-{item.qty}). "
            f"Current Stock: {stock.stock_quantity}"
        )