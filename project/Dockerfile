FROM python:3.8-alpine

WORKDIR /project

COPY requirements.txt /project
RUN pip install -r requirements.txt

COPY . /project

ENV PYTHONUNBUFFERED 1

RUN echo Hey-hey!

RUN ls

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
