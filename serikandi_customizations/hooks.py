from . import __version__ as app_version

app_name = "serikandi_customizations"
app_title = "Serikandi Customizations"
app_publisher = "Promantia Business Solutions Pvt Ltd"
app_description = "Serikandi Customizations"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "abcd@promantia.com"
app_license = "MIT"

#test
#123456
#22
#4444
#888888888888
fixtures = ["Client Script", 'Workflow State', 'Workflow Action Master',
			{
				"dt": 'Workflow',
				"filters": [
					["name", "in", 
						[
							"Material Request Workflow",
							"Stock Entry Work Flow",
							"Purchase Order Workflow"
							"Purchase Invoice Workflow",
							"Purchase Receipt Workflow"
						]
					]
				]
			},
			{
				"dt": 'Custom Field',
				"filters": [
					["name", "in", 
						[
							"Item-make",
							"Item-model",
							"Item-column_break_29",
							"Item-model_number",
							"Item-serial_number",
							"Item-specification",
							"Material Request-department",
							"Material Request-is_fixed_asset",
							"Material Request-workflow_state",
							"Material Request Item-employee",
							"Material Request-company_abbreviation",
							"Material Request Item-stock_available",
							"Company-sequence_prefix",
							"Stock Entry-reason_for_material_loss",
							"Employee-scp_ac",
							"Employee-og_nog",
							"Employee-local_non_local",
							"Employee-nationality",
							"Employee-tana_date",
							"Employee-employment_pass_expiry",
							"Employee-contract_no",
							"Employee-religion",
							"Employee-medical_expiry",
							"Employee-lpa_expiry",
							"Employee-licence_position",
							"Employee-bru_him_no",
							"Employee-tap_ac",
							"Employee-column_break_92",
							"Employee-ic_no",
							"Employee-job_category",
							"Employee-employee_details",
							"Purchase Order-approved_by",
							"Purchase Order-reviewed_by",
							"Material Request-reviewed_by",
							"Material Request-approved_by",
							"Item-part_number",
							"Material Request-priority",
							"Leave Application-attach_document",
							"Company-company_abbreviation"
							"Employee-section_break_107",
							"Employee-employee_items_allowed",
							"Purchase Order-sqn_items",
							"Supplier Quotation Item-alternative_item"
						]
					]
				]
			},
			{
				"dt": 'Property Setter',
				"filters": [
					["name", "in", 
						[
							"Material Request Item-item_code-reqd",
							"Supplier Quotation Item-uom-columns",
							"Supplier Quotation Item-qty-columns",
							"Supplier Quotation Item-rate-columns",
							"Supplier Quotation Item-lead_time_days-columns",
							"Supplier Quotation Item-lead_time_days-in_list_view"
						]
					]
				]
			},
			{
				"dt": 'Print Format',
				"filters": [
					["name", "in", 
						[
							"Purchase Order Print Format",
							"Material Request Print Format",
							"Sales Invoice Print"
						]
					]
				]
			},
			{
				"dt": 'Role',
				"filters": [
					["name", "in", 
						[
							"Store Manager",
							"Store User"
						]
					]
				]
			}
        ]
# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/serikandi_customizations/css/serikandi_customizations.css"
# app_include_js = "/assets/serikandi_customizations/js/serikandi_customizations.js"

# include js, css files in header of web template
# web_include_css = "/assets/serikandi_customizations/css/serikandi_customizations.css"
# web_include_js = "/assets/serikandi_customizations/js/serikandi_customizations.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "serikandi_customizations/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "serikandi_customizations.install.before_install"
# after_install = "serikandi_customizations.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "serikandi_customizations.uninstall.before_uninstall"
# after_uninstall = "serikandi_customizations.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "serikandi_customizations.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"serikandi_customizations.tasks.all"
# 	],
# 	"daily": [
# 		"serikandi_customizations.tasks.daily"
# 	],
# 	"hourly": [
# 		"serikandi_customizations.tasks.hourly"
# 	],
# 	"weekly": [
# 		"serikandi_customizations.tasks.weekly"
# 	]
# 	"monthly": [
# 		"serikandi_customizations.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "serikandi_customizations.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "serikandi_customizations.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "serikandi_customizations.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"serikandi_customizations.auth.validate"
# ]

