FROM python:3.11
EXPOSE 5000
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt  # only runs if requirements.txt has changed, else use its cache
COPY . /app
CMD ["flask", "run", "--host", "0.0.0.0"]