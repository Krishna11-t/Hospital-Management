import frappe

def send_daily_reminders():
    # Your logic for sending appointment reminders
    frappe.logger().info("Daily Reminder Scheduler Running...")
    
    # Example
    appointments = frappe.get_all("Appointment", filters={
        "status": "Scheduled"
    })

    for appt in appointments:
        doc = frappe.get_doc("Appointment", appt.name)
        frappe.sendmail(
            recipients=[doc.patient_email],
            subject="Appointment Reminder",
            message=f"Reminder: Your appointment is scheduled on {doc.date}"
        )

