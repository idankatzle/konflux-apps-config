FROM registry.access.redhat.com/ubi9/python-312:latest
WORKDIR /opt/app-root/src
COPY dev/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY dev/app.py app.py
CMD ["python", "app.py"]

