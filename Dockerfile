FROM python:3.7-slim

WORKDIR /app

ADD . /app

RUN pip install --trusted-host pypi.python.org flask requests

EXPOSE 5000

CMD ["python", "app.py"]
