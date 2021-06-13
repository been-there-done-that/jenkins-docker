FROM python:3.8
COPY requirements.txt /requirements.txt
COPY app.py /app.py

CMD [ "pip3 install -r requirements.txt" ]
