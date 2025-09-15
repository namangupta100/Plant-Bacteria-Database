# Plant Probiotic Bacteria Database (PBD)

## Project Description
The Plant Probiotic Bacteria Database (PBD) is a web application designed to help researchers and enthusiasts explore and manage a collection of plant-beneficial bacteria. It provides tools to view existing entries and add new information, contributing to the advancement of plant health through microbial research.

## Features
- **View Database:** Browse a comprehensive list of plant probiotic bacteria.
- **Add New Entries:** Easily add new plant-beneficial bacteria to the database with details such as genus, species, strain, plant host, function, mode of action, and reference.
- **Detail View:** Access detailed information for each bacteria entry.
- **Edit & Delete Entries:** Update or remove existing bacteria entries.
- **User-Friendly Interface:** A clean and intuitive interface built with Bootstrap.

## Technologies Used
- Python
- Django
- SQLite3
- HTML5
- CSS3
- Bootstrap 5
- Font Awesome

## Installation

### Prerequisites
- Python 3.x
- pip (Python package installer)

### Steps
1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/Plant-Probiotic-Bacteria-Database.git
    cd Plant-Probiotic-Bacteria-Database
    ```
    *(Note: Replace `https://github.com/your-username/Plant-Probiotic-Bacteria-Database.git` with the actual repository URL)*

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**
    -   **Windows:**
        ```bash
        .\venv\Scripts\activate
        ```
    -   **macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

4.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Apply database migrations:**
    ```bash
    python build/manage.py migrate
    ```

6.  **Create a superuser (optional, for admin access):**
    ```bash
    python build/manage.py createsuperuser
    ```

## Usage

### Running the Development Server
1.  **Activate your virtual environment** (if not already active):
    -   **Windows:**
        ```bash
        .\venv\Scripts\activate
        ```
    -   **macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```
2.  **Start the server:**
    ```bash
    python build/manage.py runserver
    ```
    The application will be accessible at `http://127.0.0.1:8000/`.

## Contributing
We welcome contributions to the Plant Probiotic Bacteria Database! If you have suggestions for improvements, new features, or bug fixes, please feel free to:

1.  Fork the repository.
2.  Create a new branch for your feature or fix.
3.  Make your changes and ensure they adhere to the project's coding style.
4.  Write clear commit messages.
5.  Submit a pull request.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contact
For any questions or inquiries, please contact Naman Gupta at [your-email@example.com].
*(Note: Replace `your-email@example.com` with your actual email address)*
