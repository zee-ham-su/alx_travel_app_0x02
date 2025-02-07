# ALX Travel App

ALX Travel App is a Django-based web application designed to facilitate property listings and bookings for travelers in Ghana. The app supports user registration, property management, booking, and reviews.

## Features

<!-- - **User Registration and Authentication**: Users can sign up, log in, and manage their accounts. -->
- **Property Listings**: Hosts can list properties with details such as name, description, location, and price per night.
- **Booking Management**: Users can book properties, and hosts can manage bookings.
- **Reviews and Ratings**: Users can leave reviews and ratings for properties they have stayed in.
- **API Documentation**: Swagger UI is integrated for easy API exploration and testing.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/zee-ham-su/alx_travel_app_0x00.git
    cd alx_travel_app_0x00
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up the environment variables by creating a `.env` file in the project root and adding your database configuration:

    ```plaintext
    DATABASE_NAME=your_db_name
    DATABASE_USER=your_db_user
    DATABASE_PASSWORD=your_db_password
    DATABASE_HOST=your_db_host
    DATABASE_PORT=your_db_port
    ```

5. Run database migrations:

    ```bash
    python3 manage.py migrate
    ```

6. Seed the database with sample data (optional):

    ```bash
    python3 manage.py seed
    ```

7. Start the development server:

    ```bash
    python3 manage.py runserver
    ```

8. Access the application at `http://localhost:8000`.

9. Access the swagger documentation at `http://localhost:8000/swagger/`.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the BSD License. See the [LICENSE](LICENSE) file for details.

## Contact

For support or inquiries, please email [hsufiian@yahoo.com]
