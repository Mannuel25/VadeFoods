# VadeFoods 🍔🍕🍰

**VadeFoods** is a web application that simplifies the process of ordering food for customers. It provides a platform where users can browse through a variety of food items. The application facilitates easy management for administrators to add new items, set prices, and specify the available quantity.

## Technologies Used
- **Python 🐍**
- **Django 🌐**
- **HTML/CSS 🎨**
- **Bootstrap 🅱️**
- **PostgreSQL 🐘**

## Features 🚀

### User Roles
1. **Admin 👩‍💼👨‍💼:** 
    - Adds new food items.
    - Sets prices and available quantity.
    - Manages the entire menu.

2. **Normal User 👤:**
    - Browses through the available food items.
    - Places an order.
    - Downloads a receipt after purchase.

### Categories 📦
- The application organizes food items into five categories:
    - 🍲 Food
    - 🍗 Protein
    - 🥮 Pastries
    - 🥤 Drinks
    - 🍡 Morsels

### Receipt Download 📜
- After completing a purchase, users have the option to download a receipt for their records.

## Getting Started 🚗

### Prerequisites
- Ensure you have Python installed.
- Install Django: `pip install django`
- Install PostgreSQL and set up a database.

### Installation
1. Clone the repository: `git clone https://github.com/Mannuel25/VadeFoods.git`
2. Navigate to the project directory: `cd VadeFoods`
3. Install dependencies: `pip install -r requirements.txt`
4. Apply migrations: `python manage.py migrate`
5. Create a superuser (admin): `python manage.py createsuperuser`
6. Start the development server: `python manage.py runserver`

## Usage 🕹️  

1. Access the application at `http://localhost:8000`.
2. Log in as an admin or a normal user.
3. Explore the menu, add items to the cart, and complete the purchase.
4. Download the receipt for your purchase.

## License 📄
This project is licensed under the [MIT License](LICENSE).

