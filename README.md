# PC Part Configurator

Web application designed to help users build a PC while automatically verifying component compatibility(the project features a Python Flask backend, an SQLite database, and a modern dark-themed frontend).

Visit the live project: https://pc-part-configurator.vercel.app/

<img width="568" height="516" alt="image" src="https://github.com/user-attachments/assets/762e1f1b-ef50-4310-89bd-a20820463e0f" />

## Features
* **Live Compatibility Engine:** Automatically checks if the CPU socket matches the Motherboard socket.
* **Wattage Validation:** Calculates system power consumption and verifies if the PSU capacity is sufficient.
* **Dynamic Database:** Components are fetched from an SQLite database instead of hardcoded arrays.
* **Real-time Price Calculation:** Summarizes the total cost of the selected build.
* **REST API Architecture:** Clean separation between the Vanilla JS frontend and the Flask backend.

## Tech Stack
* **Frontend:** HTML5, CSS3, JavaScript (Fetch API).
* **Backend:** Python (Flask), Flask-CORS.
* **Database:** SQLite3.
* **Deployment:** Vercel (Serverless Functions).

## How to Run Locally

### 1. Prerequisites
Make sure you have **Python 3.x** installed on your system.

### 2. Setup Backend
1) Clone the repository:
   ``bash
   git clone [https://github.com/kumowww/PC-Part-Configurator.git](https://github.com/kumowww/PC-Part-Configurator.git)
2) Install required Python libraries:
   Bash:
   pip install flask flask-cors
3) Bash:
   python app.py
4) Run  Frontend
   Open index.html in any modern web browser. Make sure the backend is running simultaneously for the data to load...
 ## Future Improvements
*Application extension, website appearance and more Backend
*Integrate a real PostgreSQL/MySQL database to replace mock dictionaries
*Add more hardware categories (RAM, GPU, Storage)
*Implement automated CI/CD pipeline for testing
