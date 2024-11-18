# 🍦 Ice Cream Distribution Web Application

**Duration**: March 2023  
**Technologies**: Django, HTML, SQLite

## 📋 Project Overview
This project is a web application built using Django to manage the distribution of ice cream across multiple stores. It allows users to view a list of stores, the tubs assigned to each store, and the total volume of ice cream available. The application utilizes Django's powerful ORM and templating system to provide a seamless user experience.

---

## 🚀 Features

### Backend Development
- **Django Models**: Developed models for `Store` and `Tub`, with relationships to manage data such as:
  - Store: `name`, `location`
  - Tub: `size`, `flavor`, `vegan` and `gluten-free` status.
- **Database**: Utilized SQLite as the database to store and manage information.
- **Migrations**: Created and applied migrations to maintain data integrity.
- **URL Routing**: Implemented routes for:
  - Listing all Tubs (`/tubs`)
  - Listing all Stores (`/stores`)
  - Viewing details of a single Store, including its assigned Tubs (`/store/<id>`).

### Frontend Development
- **HTML Templates**: Built dynamic templates to display:
  - List of Tubs and Stores.
  - Detailed view of individual Stores, showing assigned Tubs and total volume.
- **Template Inheritance**: Leveraged Django's template inheritance to create a reusable base template with consistent navigation links across pages.
  
### Business Logic
- **Volume Calculation**: Implemented logic to calculate the total volume of ice cream available at each store based on tub sizes.
  
### User Interface
- **HTML Structure**: Ensured proper structure with intuitive navigation and data presentation.
- **Dynamic Rendering**: Integrated database content into the frontend, providing real-time data views.

---

## 🔐 Security Considerations
In the project documentation:
- **Access Control**: Suggested appropriate access control strategies for CRUD operations, ensuring that:
  - **Store Managers** can manage tubs and store details.
  - **Visitors** can only view store and tub information.

---

## 🛠️ Getting Started

### Prerequisites
Ensure you have the following installed on your system:
- Python 3.x
- Django 4.x
- SQLite

### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/ice-cream-distribution.git
   cd ice-cream-distribution
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
4. Apply migrations and run the server:
    ```bash
    python manage.py migrate
    python manage.py runserver
## Usage
Access the application in your browser at http://localhost:8000/.
Explore the list of stores and tubs, or view details of a specific store.

## 📂 Project Structure
       ```bash
       ice-cream-distribution/
       ├── manage.py
       ├── ice_cream_app/
       │   ├── models.py
       │   ├── views.py
       │   ├── urls.py
       │   ├── templates/
       │   │   ├── base.html
       │   │   ├── store_list.html
       │   │   ├── tub_list.html
       │   │   └── store_detail.html
       │   ├── forms.py
       │   └── migrations/
       ├── db.sqlite3
       └── requirements.txt

## 🤝 Contributing
Contributions are welcome! If you have ideas for improving the project, please open an issue or create a pull request.

## 📜 License
This project is open-source and available under the MIT License.



