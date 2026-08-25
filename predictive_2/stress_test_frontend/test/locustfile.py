import time
import math
import csv
import numpy as np
import random
from datetime import datetime
import gevent
from locust import LoadTestShape, events, FastHttpUser,TaskSet, task, between, constant_pacing
from faker import Faker

fake = Faker()


# =========================================================
# 1. BIẾN TOÀN CỤC & LƯU TRỮ DỮ LIỆU
# =========================================================
response_times_bucket = []

# CÀI ĐẶT GIỜ MỤC TIÊU TẠI ĐÂY (Định dạng 24h: HH:MM:SS)
TARGET_START_TIME = "17:36:00" 


# =========================================================
# 2. HẸN GIỜ BẮT ĐẦU CHÍNH XÁC
# =========================================================
@events.test_start.add_listener
def delay_start(environment, **kwargs):
    """Đóng băng hệ thống chờ đến đúng giờ khai hỏa"""
    print(f"⏳ Hệ thống đã sẵn sàng. Đang chờ đến đúng {TARGET_START_TIME} để khai hỏa...")
    
    while True:
        current_time = datetime.now().strftime("%H:%M:%S")
        if current_time >= TARGET_START_TIME:
            print(f"🚀 Đã đến mốc {current_time}! BẮT ĐẦU BẮN TẢI!")
            # Kích hoạt luồng chạy ngầm (không cần truyền environment nữa)
            # gevent.spawn(calculate_and_save_p95_per_minute) 
            break
            
        time.sleep(0.5)


# --- 3. LỚP ĐỊNH NGHĨA HÌNH DẠNG TẢI (STEP-UP WORKLOAD) ---
class StepUpShape(LoadTestShape):
    step_time = 60 
    step_users = 1 
    spawn_rate = 1
    time_limit = 7200 
    start_timestamp = None 

    def tick(self):
        if datetime.now().strftime("%H:%M:%S") < TARGET_START_TIME:
            return (0, 0)
        if self.start_timestamp is None:
            self.start_timestamp = time.time()
        run_time = time.time() - self.start_timestamp
        if run_time > self.time_limit:
            return None
        current_step = math.floor(run_time / self.step_time)
        return ((current_step + 1) * self.step_users, self.spawn_rate)

products = [
    '0PUK6V6EV0',
    '1YMWWN1N4O',
    '2ZYFJ3GM2N',
    '66VCHSJNUP',
    '6E92ZMYYFZ',
    '9SIQT8TOJO',
    'L9ECAV7KIM',
    'LS4PSXUNUM',
    'OLJCESPC7Z']

def index(l):
    l.client.get("/")

def setCurrency(l):
    currencies = ['EUR', 'USD', 'JPY', 'CAD', 'GBP', 'TRY']
    l.client.post("/setCurrency",
        {'currency_code': random.choice(currencies)})

def browseProduct(l):
    l.client.get("/product/" + random.choice(products))

def viewCart(l):
    l.client.get("/cart")

def addToCart(l):
    product = random.choice(products)
    l.client.get("/product/" + product)
    l.client.post("/cart", {
        'product_id': product,
        'quantity': random.randint(1,10)})
    
def empty_cart(l):
    l.client.post('/cart/empty')

def checkout(l):
    addToCart(l)
    current_year = datetime.now().year+1
    l.client.post("/cart/checkout", {
        'email': fake.email(),
        'street_address': fake.street_address(),
        'zip_code': fake.zipcode(),
        'city': fake.city(),
        'state': fake.state_abbr(),
        'country': fake.country(),
        'credit_card_number': fake.credit_card_number(card_type="visa"),
        'credit_card_expiration_month': random.randint(1, 12),
        'credit_card_expiration_year': random.randint(current_year, current_year + 70),
        'credit_card_cvv': f"{random.randint(100, 999)}",
    })
    
    
def logout(l):
    l.client.get('/logout')  


class UserBehavior(TaskSet):

    def on_start(self):
        index(self)

    tasks = {index: 1,
        setCurrency: 2,
        browseProduct: 10,
        addToCart: 2,
        viewCart: 3,
        checkout: 1
        }


class WebsiteUser(FastHttpUser):
    tasks = [UserBehavior]
    host = "http://localhost:8080"
    wait_time = constant_pacing(1.0) 

    # wait_time = between(1, 10)
