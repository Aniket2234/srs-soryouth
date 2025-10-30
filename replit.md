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
- **Date**: October 12, 2025
- **Project**: Comprehensive Solar CRM system

## SRS Document Contents
The documentation describes a complete Solar CRM system with these major modules:

### Core Features
1. **Lead Management** - Multi-source lead capture and tracking
2. **Proposal & Quotation** - Automated proposal generation
3. **Project Management** - Visual project tracking
4. **Site Survey Management** - Survey scheduling and documentation
5. **Multi-Channel Communication** - Email, WhatsApp, SMS integration
6. **Task Management** - Team task assignment and tracking
7. **Document Management** - Centralized document storage
8. **Service Ticketing** - AMC and maintenance management

### Additional Features
- Inventory Management
- Invoicing & Billing
- Subsidy Management
- Vendor Management
- Employee Management
- Plant Monitoring Integration
- Analytics & Reporting
- GPS Tracking
- Role-based Access Control

## Deployment
The project is configured for Replit autoscale deployment:
- **Type**: Autoscale (stateless web application)
- **Command**: `python3 server.py`
- **Port**: 5000 (automatically exposed)

## Recent Changes (October 30, 2025)
- Installed Python 3.11 toolchain
- Created HTTP server with cache control
- Configured workflow for webview on port 5000
- Set up deployment configuration
- Added .gitignore for Python projects
- Updated documentation

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
