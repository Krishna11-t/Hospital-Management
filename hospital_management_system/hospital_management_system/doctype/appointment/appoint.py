import frappe

def validate_double_booking(doc, method):
    existing = frappe.db.exists(
        "Appointment",
        {
            "doctor": doc.doctor,
            "appointment_date": doc.appointment_date,
            "appointment_time": doc.appointment_time,
            "name": ["!=", doc.name]   # Exclude current document
        }
    )

    if existing:
        frappe.throw("This time slot is already booked! Please choose another time.")