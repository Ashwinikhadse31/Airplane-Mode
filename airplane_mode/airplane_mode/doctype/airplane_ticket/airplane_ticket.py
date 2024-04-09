# Copyright (c) 2024, Ashwini Khadse and contributors
# For license information, please see license.txt

# import frappe
# from frappe.model.document import Document


# class AirplaneTicket(Document):
# 	pass

from frappe.model.document import Document

class AirplaneTicket(Document):
    def validate(self):
        self.calculate_total_amount()
        self.remove_duplicate_add_ons()

    def calculate_total_amount(self):
        total = self.flight_price or 0
        for add_on in self.get("add_ons"):
            total += add_on.amount or 0
        self.total_amount = total

    def remove_duplicate_add_ons(self):
        unique_add_ons = []
        for add_on in self.get("add_ons"):
            if add_on.add_on not in unique_add_ons:
                unique_add_ons.append(add_on.add_on)
            else:
                frappe.throw("Add-on already added!")
                self.clear_table("add_ons")

# Register the Airplane Ticket DocType with Frappe
def register():
    from frappe.model.meta import Meta
    if not Meta.get_meta("Airplane Ticket"):
        meta = Meta.get_meta("DocType", "Airplane Ticket")
        meta.add_field({"fieldname": "flight_price", "fieldtype": "Currency", "mandatory": 1})
        meta.add_field({"fieldname": "total_amount", "fieldtype": "Currency"})
        meta.save()

