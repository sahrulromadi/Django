# 1. Kloning Repository

# 2. Membuat Virtual Environment

python -m venv venv

venv\Scripts\activate

# 3. Install Dependencies

pip install -r requirements.txt

# 4. Konfigurasi Database

python manage.py migrate

# 6. Buat Superuser untuk Admin

python manage.py createsuperuser

# 7. Jalankan Server Django

python manage.py runserver
