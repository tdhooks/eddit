FROM python:3

ENV PYTHONUNBUFFERED=1

RUN mkdir /usr/src/eddit
WORKDIR /usr/src/eddit

COPY eddit/ .
RUN pip install --no-cache-dir -r requirements.txt
RUN python manage.py migrate

CMD [ "python", "manage.py", "runserver", "0:8000" ]