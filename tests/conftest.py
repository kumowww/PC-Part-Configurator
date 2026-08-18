import threading
import time
import pytest

from werkzeug.serving import make_server

# Importing the Flask application
from app import app as flask_app

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="session", autouse=True)
def server():
    """
    Запускает Flask-приложение в фоне для тестов (http://localhost:5000).
    Scope=session и autouse=True — сервер автоматически поднимается один раз для всех тестов.
    """
    srv = make_server("127.0.0.1", 5000, flask_app)
    thread = threading.Thread(target=srv.serve_forever)
    thread.daemon = True
    thread.start()
    # A short pause whilst the server starts up (maybe need xd)
    time.sleep(0.5)
    yield
    srv.shutdown()
    thread.join(timeout=1)

@pytest.fixture
def driver():
    """
    Создаёт headless Chrome WebDriver с помощью webdriver-manager.
    Закрывается автоматически после теста.
    """
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")  # or "--headless" in old versions
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()
