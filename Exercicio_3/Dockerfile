FROM python:3.9
WORKDIR /usr/src/app

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0


COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt --user
EXPOSE 5000
COPY . .
CMD ["python", "./main.py"]







