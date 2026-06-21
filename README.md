# Society Transparency Management System

A resident-first backend platform for transparent housing society 
management. Built to solve the real problem of maintenance fund 
mismanagement in Indian housing societies.

## Problem
Residents pay maintenance every month but have no visibility 
into how that money is spent. Committee members operate without 
accountability. This platform changes that.

## Solution
Every rupee spent is publicly logged with mandatory bill proof. 
Any resident can flag suspicious expenses. Management must respond 
publicly. Full audit trail visible to all residents.

## Tech Stack
- Python + FastAPI
- PostgreSQL + SQLAlchemy + Alembic
- JWT Authentication
- Cloudinary (file storage)
- Celery + Redis (background tasks)
- Railway (deployment)

## Architecture
- 13 modules
- 22 database tables
- 108 REST API endpoints
- 5 user roles with granular permissions

## Modules
- Authentication & User Management
- Society & Flat Directory
- Maintenance Collection Tracker
- Expense Ledger (public, transparent)
- Expense Flagging & Public Resolution
- Dashboard & Analytics
- Notice Board
- Complaint & Helpdesk
- Document Vault
- Polls & Voting
- Parking Management
- Amenity Booking
- Visitor Log

## Status
🚧 Active Development

## API Documentation
Run locally and visit http://localhost:8000/docsk