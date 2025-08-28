import frappe

def get_lead(arg):
    session_user_roles = frappe.get_roles(frappe.session.user)
    if frappe.session.user != "Administrator" and (
        "Lead Handling" in session_user_roles
    ):
        return "(`tabLead`._assign like '%{user}%' or `tabLead`.owner = '{user}')".format(
            user=frappe.session.user
        )