# hooks.py

doc_events = {
    "Patient Appointment": {
        "before_insert": "your_app.your_module.appointment.before_insert",
        "after_insert": "your_app.your_module.appointment.after_insert",
        "before_save": "your_app.your_module.appointment.before_save",
        "on_update": "your_app.your_module.appointment.on_update",
        "on_submit": "your_app.your_module.appointment.on_submit",
        "on_cancel": "your_app.your_module.appointment.on_cancel"
    }
}
