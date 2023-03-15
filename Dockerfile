FROM python:3.10 as python-base

RUN mkdir app

WORKDIR  /app

COPY /src/requirements.txt /app

RUN pip3 install -r requirements.txt

COPY . .

CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "src.main:create_app", "--bind", "0.0.0.0:8000"]