import frappe

def before_insert(doc, event):
    frappe.logger().info(f"Creating Appointment for: {doc.patient}")

def after_insert(doc, event):
    frappe.msgprint(f"Appointment Created: {doc.name}")

def before_save(doc, event):
    # Set default status only if not already set
    if not doc.status:
        doc.status = "Scheduled"

def on_update(doc, event):
    frappe.logger().info(f"Appointment Updated: {doc.name}")

def on_submit(doc, event):
    frappe.msgprint("Appointment submitted successfully!")

def on_cancel(doc, event):
    frappe.msgprint("Appointment cancelled!")

def on_trash(doc, event):
    frappe.logger().warning(f"Appointment Deleted: {doc.name}")
