import frappe

def before_insert(doc, event):
    frappe.logger().info(f"Creating Appointment for patient: {doc.patient}")

def after_insert(doc, event):
    frappe.msgprint(f"Appointment Created Successfully: {doc.name}")

def before_save(doc, event):
    # auto status if empty
    if not doc.status:
        doc.status = "Scheduled"

def on_update(doc, event):
    frappe.logger().info(f"Appointment Updated: {doc.name}")

def on_submit(doc, event):
    frappe.msgprint(f"Appointment Submitted: {doc.name}")

def on_cancel(doc, event):
    frappe.msgprint(f"Appointment Cancelled: {doc.name}")