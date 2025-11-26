import frappe

def after_submit(doc, event):
    # Loop through each medicine in the prescription child table
    for item in doc.medicines:

        # Fetch Pharmacy Inventory by the medicine item code/name
        stock = frappe.get_doc("Pharmacy Inventory", item.medicine)

        # Calculate new quantity
        current_qty = stock.stock_quantity or 0
        new_qty = current_qty - item.qty

        # Prevent negative stock
        if new_qty < 0:
            frappe.throw(f"Not enough stock for {item.medicine}. Available: {current_qty}")

        # Update stock
        stock.stock_quantity = new_qty
        stock.save(ignore_permissions=True)

        frappe.msgprint(f"Stock updated for {item.medicine}: -{item.qty}")