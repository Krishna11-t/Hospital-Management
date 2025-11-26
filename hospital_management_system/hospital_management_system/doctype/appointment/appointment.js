// Copyright (c) 2025, Krishna Teja and contributors
// For license information, please see license.txt

frappe.ui.form.on ("Appointment", {
    validate: function (frm) {
        if (!frm.doc.doctor || !frm.doc.appointment_date || !frm.doc.from_time || !frm.doc.to_time) {
            return;
        }

        frappe.call({
            method: "frappe.client.get_list",
            args: {
                doctype: "Appointment",
                fields: ["name", "from_time", "to_time"],
                filters: {
                    doctor: frm.doc.doctor,
                    appointment_date: frm.doc.appointment_date,
                    name: ["!=", frm.doc.name], // exclude current doc
                    status: ["!=", "Cancelled"]
                }
            },
            callback: function (r) {
                if (!r.message) return;

                let conflict = r.message.some(a => {
                    return (
                        (frm.doc.from_time < a.to_time) &&
                        (frm.doc.to_time > a.from_time)
                    );
                });

                if (conflict) {
                    frappe.msgprint({
                        title: "Double Booking Detected",
                        indicator: "red",
                        message: "The selected time overlaps with an existing appointment for this doctor."
                    });
                    frappe.validated = false; 
                }
            }
        });
    }
});