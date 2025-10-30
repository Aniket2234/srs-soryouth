# Solar CRM SRS Documentation

## Project Overview
This project hosts the Software Requirements Specification (SRS) document for the Soryouth Solar CRM system. It's a static website that displays comprehensive documentation for a planned Solar Customer Relationship Management system.

## Current Status
- **Status**: Production Ready
- **Server**: Python 3.11 HTTP server with cache control
- **Port**: 5000 (configured for Replit webview)
- **Deployment**: Configured for autoscale deployment

## Project Structure
```
.
├── index.html           # Main SRS documentation (3901 lines)
├── logo.jpg            # Soryouth Mahindra Solarize logo
├── server.py           # Python HTTP server with cache control
├── .gitignore          # Python/IDE/OS ignore patterns
├── attached_assets/    # Original uploaded files (preserved)
│   ├── index_1760261871935.html
│   ├── logo_1760262256104.jpg
│   └── image_1760264738108.png
└── replit.md           # This file
```

## Technical Details

### Server Configuration
- **Language**: Python 3.11
- **Framework**: Built-in http.server module
- **Host**: 0.0.0.0 (accepts all connections)
- **Port**: 5000
- **Cache Control**: Disabled (no-cache headers)

### Features
- Static file serving
- Proper cache control headers for development
- Clean request logging
- Responsive design with mobile support
- Print-to-PDF functionality
- Interactive table of contents with smooth scrolling
- Professional green-themed UI

## Document Information
- **Title**: Software Requirements Specification - Solar CRM System
- **Company**: Soryouth Renewable Energy Pvt Ltd
- **Version**: 2.0
- **Date**: October 30, 2025
- **Project**: Comprehensive Solar CRM system

## SRS Document Contents
The documentation describes a complete Solar CRM system with these major modules:

### Core Features
1. **Lead Management** - Multi-source lead capture and tracking (JustDial, Google, WhatsApp integrations)
2. **Proposal & Quotation** - Automated proposal generation
3. **Project Management** - Visual project tracking
4. **Site Survey Management** - Survey scheduling and documentation
5. **Multi-Channel Communication** - Email, WhatsApp, SMS integration
6. **Task Management** - Team task assignment and tracking
7. **Document Management** - Centralized document storage for business documents
8. **Service Ticketing** - Cross-functional AMC and maintenance management
9. **DMS - Document Management System** - Barcode scanning for product tracking and inventory management

### Additional Features
- Invoicing & Billing
- Subsidy Management
- Vendor Management
- Employee Management
- Plant Monitoring Integration
- Analytics & Reporting
- GPS Tracking
- Role-based Access Control
- **Notification System** - Admin-to-executive task notifications and reminders
- **Customer Journey Management** - End-to-end customer lifecycle tracking

## Deployment
The project is configured for Replit autoscale deployment:
- **Type**: Autoscale (stateless web application)
- **Command**: `python3 server.py`
- **Port**: 5000 (automatically exposed)

## Recent Changes (October 30, 2025)
### Initial Setup (Earlier)
- Installed Python 3.11 toolchain
- Created HTTP server with cache control
- Configured workflow for webview on port 5000
- Set up deployment configuration
- Added .gitignore for Python projects

### Latest Updates (October 30, 2025)
- Updated document version from 1.0 to 2.0
- Updated document date to October 30, 2025
- Replaced Inventory Management module with DMS - Document Management System (includes barcode scanning for product tracking)
- Enhanced Lead Management module to emphasize multi-source integrations (JustDial, Google, WhatsApp)
- Added Notification System module (MOD-031) for admin-to-executive communications
- Added Customer Journey Management module (MOD-032) for end-to-end customer lifecycle tracking
- Updated Service Ticketing to be cross-functional across departments
- Removed Section 6 "Other Requirements" (including Future Enhancements, Training, Deployment, Support)
- Renumbered Appendices from Section 7 to Section 6
- Updated all references throughout document (user roles, API endpoints, dependency matrices, permission tables)
- Ensured document structure consistency across all sections

## User Preferences
None recorded yet.

## Next Steps
This is a documentation-only project. If you need to build the actual Solar CRM system described in the SRS, that would be a separate development effort involving:
- Full-stack application development
- Database design and implementation
- API integrations (WhatsApp, Email, RMS, etc.)
- Authentication and authorization
- Real-time monitoring systems
- And all other features outlined in the SRS document
