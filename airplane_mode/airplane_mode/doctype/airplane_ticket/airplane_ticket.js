// Copyright (c) 2024, Ashwini Khadse and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Airplane Ticket", {
// 	refresh(frm) {

// 	},
// });

// frappe.ui.form.on("Airplane Ticket Add-on Item", {
//     amount(frm, cdt, cdn) {
//         let total = 0;

//         frm.doc.add_ons.forEach(function(d) {
//             total += d.amount;
//         });
//         total+=frm.doc.flight_price;
//         frm.set_value("total_amount", total);
//     }
// });

// frappe.ui.form.on('Airplane Ticket Add On', {
//     add_on: function(frm, cdt, cdn) {
//         var child = locals[cdt][cdn];
//         var duplicate = frm.doc.add_ons.some(addon => addon.add_on === child.add_on && addon.name !== child.name);
//         if (duplicate) {
//             frappe.msgprint('Add-on already added!');
//             frappe.model.clear_table(frm.doc, 'add_ons');
//         }
//     }
// });
