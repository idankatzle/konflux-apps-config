# משתמשים באימג' של Red Hat שמגיע כבר עם Python מותקן (הכי בטוח והכי קל)
FROM registry.access.redhat.com/ubi9/python-39:latest

# מעבר למשתמש root זמנית כדי להגדיר תיקיות (אם צריך)
USER root

# הגדרת תיקיית עבודה
WORKDIR /app

# 1. העתקת קובץ הדרישות ראשון (אופטימיזציה של Cache)
COPY src/requirements.txt .

# 2. התקנת הספריות (Flask, PyMySQL וכו')
RUN pip install --no-cache-dir -r requirements.txt

# 3. העתקת כל שאר הקוד מתיקיית src לתוך /app
COPY src/ .

# שינוי בעלות על התיקייה למשתמש הרגיל של התמונה (1001)
RUN chown -R 1001:0 /app

# חזרה למשתמש הלא-פריבילגי (סטנדרט אבטחה ב-OpenShift)
USER 1001

# חשיפת הפורט של Flask
EXPOSE 5000

# הפעלת האפליקציה
CMD ["python", "app.py"]
