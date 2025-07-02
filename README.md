# 🎟️ Event Registration System

A backend system for managing events and user registrations, built using Django and Django REST Framework (DRF).

## 🚀 Overview

This project provides a robust and modular event registration platform where users can:

- View a list of upcoming events
- View details of individual events
- Register for events
- View their own registrations
- Cancel a registration if needed

It also includes an admin interface for staff or event organizers to manage events and registrations efficiently.

---

## 🧰 Tech Stack

| Layer           | Technology                |
|-----------------|---------------------------|
| Framework       | Django (Python)           |
| API Layer       | Django REST Framework     |
| Database        | SQLite (easily swappable with PostgreSQL) |
| Admin Panel     | Django Admin              |

---

## ✅ Features

### 👥 User Features
- Browse and view event listings
- Register for an event
- Track personal registrations
- Cancel registrations (when needed)

### 🔐 Authentication
- Login required for registration-related actions
- Built using Django’s session-based authentication system
- Compatible with Django's built-in user model

### 🛠 Admin Features
- Full admin panel for managing events and registrations
- Secure access limited to staff or superusers
- Create, edit, or delete event entries
- View and manage user registrations

---

## 📦 Project Structure

- **Events App**  
  Contains all core logic: models, serializers, views, and URL configuration

- **API-Driven**  
  Uses DRF to expose endpoints for client-side consumption or testing via tools like Postman

---

## 🔧 Customization

This project is designed to be extensible. You can easily:

- Replace SQLite with PostgreSQL
- Integrate Token or JWT-based authentication
- Add user roles (e.g., event organizers, attendees)
- Build a frontend (React, Vue, or Django templates) to consume the API

---

## 📎 Requirements

- Python 3.12+
- Django 5.x
- Django REST Framework
- SQLite (default) or PostgreSQL

---

## 📌 Status

> ✅ **Core functionality is fully implemented**  
> 🧪 Ready for use or extension with frontend or more advanced auth systems

---

## 🤝 Contributing

Pull requests and feedback are welcome! This is a great base for learning Django backend architecture or building things.


