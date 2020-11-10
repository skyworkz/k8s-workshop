FROM python:3.7-alpine

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

RUN addgroup -S appgroup && adduser -S appuser -G appgroup
USER appuser

EXPOSE 5000

CMD [ "python", "app.py" ]
