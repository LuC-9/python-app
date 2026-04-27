From python:3.10-alpine
COPY requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt
Copy src /app
CMD python /app/app.py

