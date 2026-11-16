# Copyright (c) 2026, Shyamkumar Pandey and contributors
# For license information, please see license.txt

app_name = "dyeing"
app_title = "Erpnext Textile Dyeing Recipe Manager"
app_publisher = "Shyamkumar Pandey"
app_description = "Erpnext Textile Dyeing Recipe Manager for Frappe and ERPNext"
app_email = "shyampandey1104@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------
app_include_css = "/assets/dyeing/css/dyeing.bundle.css"
app_include_js = "/assets/dyeing/js/dyeing.bundle.js"

# Document Events
# ---------------
doc_events = {
    "DocType Event": {
        "on_submit": "dyeing.engine.on_document_submit",
        "on_cancel": "dyeing.engine.on_document_cancel"
    }
}

# Scheduled Tasks
# ---------------
scheduler_events = {
    "daily": [
        "dyeing.engine.daily_scheduled_sync"
    ]
}
