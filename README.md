#Address Book Application 


This project is a FastAPI-based Address Book Application where API users can create, update, delete and retrieve the addresses that are within a given distance and
location coordinates.

This project uses  SQLite database and Swagger UI for API interaction.

1. How to Execute the application:
    git clone https://github.com/dhanashreebabar/address-book-application-.git
    cd address-book-application-

2. Create Virtual Environment:
    python -m venv venv
    venv\scripts\activate
 
3. Install Dependencies:
    pip install -r requirements.txt

4. Run the Application:
    uvicorn app.main:app --reload

5. Swagger UI:
    You should see output at
    http://127.0.0.1:8000/docs     

