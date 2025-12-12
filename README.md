# 🌦 Weather API

Django REST Framework asosida qurilgan, real vaqt rejimidagi ob-havo
ma'lumotlarini taqdim etuvchi API xizmati.\
Loyihada JWT Authentication, SMTP Email, Celery Background Tasks, HTTPS
(mkcert) va boshqa zamonaviy backend texnologiyalar qo'llangan.

## 🚀 Xususiyatlar

-   🔐 JWT Authentication (SimpleJWT)
-   📧 SMTP orqali email yuborish
-   ⏳ Celery + Redis yordamida background tasklar
-   🔒 HTTPS (mkcert -- localhost uchun SSL)
-   🌦 Ob-havo ma'lumotlari (Custom Weather endpoints)
-   📡 REST API (DRF)

## 📁 Loyihaning tuzilishi

Weather-API/ │── config/ │── weather/ │── user/ │── static/ │──
requirements.txt │── README.md

## 🔧 O'rnatish

### 1️⃣ Klonlash

git clone https://github.com/turdialixasanbayev/Weather-API.git

### 2️⃣ Virtual environment

python -m venv venv venv/Scripts/activate

### 3️⃣ Paketlarni o'rnatish

pip install -r requirements.txt

### 4️⃣ .env misol

SECRET_KEY=your-secret-key DEBUG=True EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587 EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_app_password EMAIL_USE_TLS=True
REDIS_URL=redis://127.0.0.1:6379

## 🗝 Migratsiyalar

python manage.py migrate

## 🔐 HTTPS uchun mkcert

mkcert -install mkcert localhost

## ⏳ Celery Worker & Beat

celery -A config worker -l info --pool=solo celery -A config beat -l
info

## 🔗 API Endpointlar

POST /api/auth/register/ POST /api/auth/login/ POST
/api/auth/verify-email/ GET /api/weather/ GET
/api/weather/`<id>`{=html}/

## 📧 Email yuborish (Celery)

send_notification_email_task.delay(to, subject, message)

## 📝 Lisensiya

MIT License

## 🧑‍💻 Muallif

Turdiali Xasanbayev
