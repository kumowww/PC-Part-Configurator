# PC Part Configurator

Web-based tool that allows users to select PC components (CPU, Motherboard, GPU) and automatically checks their compatibility using a backend logic system. 
** is still at a very early stage of development: **
**Client-Server Architecture**, **API communication**, and **E-commerce hardware logic**.

## Features
* **Dark Mode UI:** Modern, user-friendly interface with clear visual feedback.
* **Socket Compatibility Check:** Verifies if the selected CPU fits the chosen Motherboard socket.
* **Asynchronous API Calls:** The frontend (JS) communicates with the backend (PHP) without reloading the page using the `fetch` API.

## Tech Stack
Frontend:HTML5, CSS3, Vanilla JS
Backend:PHP
Data Structure:Mock JSON/Array Data

## How to Run Locally

To run this project on your local machine, you need a local web server (like XAMPP, WAMP, or MAMP) because it relies on PHP for backend processing...

1.  Clone this repository:
    bash
    git clone [https://github.com/kumowww/PC-Part-Configurator.git](https://github.com/kumowww/PC-Part-Configurator.git)

2.  Move the project folder into your server's root directory:
    * for XAMPP: Move to `xampp\htdocs\`
3.  Start the **Apache** module in your XAMPP Control Panel.
4.  Open your web browser and navigate to:
    http://localhost/PC-Part-Configurator/index.html

## Future Improvements
* Replace the PHP mock arrays with a real **SQL database** containing models from 2014 onwards.
* Add a Total Price calculator(MAYBE)
