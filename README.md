# PC Part Configurator

Web-based tool that allows users to select PC components (CPU, Motherboard, PSU) and automatically checks their compatibility using a Python-based backend logic system.

<img width="1920" height="990" alt="image" src="https://github.com/user-attachments/assets/2450cacc-132f-4a83-8b63-ff5f09a2eb44" />


## Features
* **Dark Mode UI:** Modern, user-friendly interface with clear visual feedback.
* **Socket Compatibility Check:** Verifies if the selected CPU fits the chosen Motherboard socket.
* **Wattage Verification:** Checks if the Power Supply Unit (PSU) can handle the system load.
* **Real-time Price Calculation:** Summarizes the total cost of selected components.
* **REST API Communication:** The frontend (Vanilla JS) communicates with the backend (Flask) using asynchronous `fetch` calls.

## Tech Stack
- **Frontend:** HTML5, CSS3, Vanilla JS
- **Backend:** Python (Flask)
- **Data Structure:** JSON Objects (Ready for SQL integration)
- **Testing:** Selenium WebDriver (Automated test scripts included)

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
