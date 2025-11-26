scheduler_events = {
    "daily": [
        "your_app.your_module.doctype.appointment.appointment.send_daily_reminders"
    ]
}

import frappe

def send_daily_reminders():
    appointments = frappe.get_all(
        "Patient Appointment",
        filters={"status": "Scheduled"},
        fields=["name", "patient", "appointment_date", "appointment_time"]
    )

    for appt in appointments:
        frappe.sendmail(
            recipients=[frappe.db.get_value("Patient", appt.patient, "email")],
            subject=f"Appointment Reminder - {appt.appointment_date}",
            message=f"Dear Patient, this is a reminder for your appointment on {appt.appointment_date} at {appt.appointment_time}."
        )