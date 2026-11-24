# Copyright (c) 2026, Shyamkumar Pandey and contributors
# For license information, please see license.txt

app_name = "dyeing"
app_title = "Erpnext Textile Dyeing Recipe Manager"
app_publisher = "Shyamkumar Pandey"
app_description = "Erpnext Textile Dyeing Recipe Manager - Enterprise Multi-DocType Solution for Frappe & ERPNext"
app_email = "shyampandey1104@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------
app_include_css = "/assets/dyeing/css/dyeing.bundle.css"
app_include_js = "/assets/dyeing/js/dyeing.bundle.js"

# Document Events
# ---------------
doc_events = {
    "Erpnext Textile Dyeing Recipe Manager Entry": {
        "validate": "dyeing.services.validator.EnterpriseValidationEngine.validate_compliance_rules",
        "on_submit": "dyeing.services.integration_service.EnterpriseIntegrationService.verify_remote_status"
    }
}

# Scheduled Background Tasks
# --------------------------
scheduler_events = {
    "hourly": [
        "dyeing.tasks.hourly_sync"
    ],
    "daily": [
        "dyeing.tasks.daily_reconciliation"
    ],
    "weekly": [
        "dyeing.tasks.weekly_digest"
    ]
}
