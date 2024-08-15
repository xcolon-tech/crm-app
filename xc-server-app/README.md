# Social Media Scheduling Tool
Hosts Server Django Application for Social Media Scheduling Tool

# User REgistration
curl -X POST http://127.0.0.1:8000/api/account/register/ \
-H "Content-Type: application/json" \
-d '{
        "username": "newuser",
        "password": "newpassword123",
        "email": "newuser@example.com",
        "first_name": "John",
        "last_name": "Doe",
        "profile": {
            "mobile": "1234567890"
        }
    }'

# User Login
curl -X POST http://127.0.0.1:8000/api/login/login/ \
-H "Content-Type: application/json" \
-d '{
        "username": "testuser",
        "password": "testpassword"
    }'

# Get list of Leads
curl -X GET http://127.0.0.1:8000/api/app/leads/

# Add New Lead
curl -X POST http://127.0.0.1:8000/api/app/leads/ \
-H "Content-Type: application/json" \
-d '{
        "name": "Lead 1",
        "status": "New"
    }'

# Get List of Deals
curl -X GET http://127.0.0.1:8000/api/app/deals/

# Add New Deal
curl -X POST http://127.0.0.1:8000/api/app/deals/ \
-H "Content-Type: application/json" \
-d '{
        "name": "Deal 1",
        "lead": 1,
        "status": "Ongoing"
    }'

# List All Customers
curl -X GET http://127.0.0.1:8000/api/customer/customers/

# Create New Customer
curl -X POST http://127.0.0.1:8000/api/customer/customers/ \
-H "Content-Type: application/json" \
-d '{
        "name": "Customer 1",
        "email": "customer1@example.com",
        "phone": "1234567890",
        "address": "123 Main St, Anytown, USA"
    }'

# Get Customer Details
curl -X GET http://127.0.0.1:8000/api/customer/customers/1/

# Update Customer
curl -X PUT http://127.0.0.1:8000/api/customer/customers/1/ \
-H "Content-Type: application/json" \
-d '{
        "name": "Customer 1 Updated",
        "email": "customer1updated@example.com",
        "phone": "0987654321",
        "address": "456 Main St, Anytown, USA"
    }'

# Delete Customer
curl -X DELETE http://127.0.0.1:8000/api/customer/customers/1/

# List All Leads
curl -X GET http://127.0.0.1:8000/api/lead/leads/

# Create New Lead
curl -X POST http://127.0.0.1:8000/api/lead/leads/ \
-H "Content-Type: application/json" \
-d '{
        "name": "Lead 1",
        "email": "lead1@example.com",
        "phone": "1234567890",
        "company": "Company A",
        "status": "New"
    }'

# Get Lead Details
curl -X GET http://127.0.0.1:8000/api/lead/leads/1/

# Update Lead
curl -X PUT http://127.0.0.1:8000/api/lead/leads/1/ \
-H "Content-Type: application/json" \
-d '{
        "name": "Lead 1 Updated",
        "email": "lead1updated@example.com",
        "phone": "0987654321",
        "company": "Company A Updated",
        "status": "Contacted"
    }'

# Delete Lead
curl -X DELETE http://127.0.0.1:8000/api/lead/leads/1/

# List Sales
curl -X GET http://127.0.0.1:8000/api/sale/sales-opportunities/

# Create New Sales
curl -X POST http://127.0.0.1:8000/api/sale/sales-opportunities/ \
-H "Content-Type: application/json" \
-d '{
        "name": "Opportunity 1",
        "description": "A potential sales opportunity.",
        "value": "10000.00",
        "status": "New",
        "close_date": "2024-12-31"
    }'

# Get Sales Opportunity Details
curl -X GET http://127.0.0.1:8000/api/sale/sales-opportunities/1/

# Update Sales Opportunity
curl -X PUT http://127.0.0.1:8000/api/sale/sales-opportunities/1/ \
-H "Content-Type: application/json" \
-d '{
        "name": "Opportunity 1 Updated",
        "description": "Updated description.",
        "value": "15000.00",
        "status": "In Progress",
        "close_date": "2024-11-30"
    }'

# Delete Sales Opportunity
curl -X DELETE http://127.0.0.1:8000/api/sale/sales-opportunities/1/

# List All Marketing Campaigns
curl -X GET http://127.0.0.1:8000/api/marketing/marketing-campaigns/

# New Marketing Campaign
curl -X POST http://127.0.0.1:8000/api/marketing/marketing-campaigns/ \
-H "Content-Type: application/json" \
-d '{
        "name": "Social Media Campaign",
        "type": "Social Media",
        "description": "A campaign to boost social media presence.",
        "start_date": "2024-05-01",
        "end_date": "2024-06-01",
        "budget": "5000.00"
    }'

# Get Marketing Campaigns
curl -X GET http://127.0.0.1:8000/api/marketing/marketing-campaigns/1/

# Update Marketing Campaign
curl -X PUT http://127.0.0.1:8000/api/marketing/marketing-campaigns/1/ \
-H "Content-Type: application/json" \
-d '{
        "name": "Updated Social Media Campaign",
        "type": "Social Media",
        "description": "Updated campaign description.",
        "start_date": "2024-05-01",
        "end_date": "2024-06-15",
        "budget": "6000.00"
    }'

# Delete Marketing Campaign
curl -X DELETE http://127.0.0.1:8000/api/marketing/marketing-campaigns/1/

# List All Sales Reports
curl -X GET http://127.0.0.1:8000/api/report/sales-reports/

# Create New Sales Report
curl -X POST http://127.0.0.1:8000/api/report/sales-reports/ \
-H "Content-Type: application/json" \
-d '{
        "title": "Sales Report Q1 2024",
        "content": "Detailed report on Q1 sales performance."
    }'

# Get Sales Report
curl -X GET http://127.0.0.1:8000/api/report/sales-reports/1/

# Update Sales Report
curl -X PUT http://127.0.0.1:8000/api/report/sales-reports/1/ \
-H "Content-Type: application/json" \
-d '{
        "title": "Updated Sales Report Q1 2024",
        "content": "Updated details on Q1 sales performance."
    }'

# Delete Sales Report
curl -X DELETE http://127.0.0.1:8000/api/report/sales-reports/1/

# List All Users
curl -X GET http://127.0.0.1:8000/api/settings/users/

# Create New Role
curl -X POST http://127.0.0.1:8000/api/settings/roles/ \
-H "Content-Type: application/json" \
-d '{
        "name": "Manager",
        "description": "Manages operations."
    }'

# Get App Settings
curl -X GET http://127.0.0.1:8000/api/settings/app-settings/

# Update App Settings
curl -X PUT http://127.0.0.1:8000/api/settings/app-settings/ \
-H "Content-Type: application/json" \
-d '{
        "leads_management": true,
        "sales_management": true,
        "media_campaign": false,
        "email_campaign": true,
        "user_management": true
    }'

# Request to Logout
curl -X POST http://127.0.0.1:8000/api/logout/ \
-H "Authorization: Token <your_token>"


