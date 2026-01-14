# משתמשים באימג' מוכן של פייתון (מבוסס אובונטו/דביאן, קל מאוד)
#FROM python:3.12-slim
FROM quay.io/fedora/python-312:latest
# הגדרת תיקיית עבודה
WORKDIR /app

# העתקת קובץ הדרישות
COPY src/requirements.txt .

# התקנה גלובלית (בלי --user) כך שפייתון ימצא אותה מיד
RUN pip install --no-cache-dir -r requirements.txt

# העתקת הקוד
COPY src/ .

# יצירת משתמש לא-פריבילגי (חובה ל-OpenShift)
RUN useradd -m appuser && chown -R appuser /app
USER appuser

# הפעלה
EXPOSE 5000
CMD ["python", "app.py"]
