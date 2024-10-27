FROM python:3.12

WORKDIR /app

COPY . /app

RUN pip install poetry==1.8.3

RUN poetry install

EXPOSE 8000

CMD ["poetry", "run", "uvicorn", "main:app", "--workers", "4", "--host", "0.0.0.0", "--port", "8000"]