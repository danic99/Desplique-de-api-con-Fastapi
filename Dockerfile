FROM tiangolo/uvicorn-gunicorn:python3.8-slim
WORKDIR /APImovies
COPY . .
RUN pip install -r requirements.txt
ENV PORT =8080
CMD gunicorn APImovies:app --bind 0.0.0.0:$PORT --worker-class uvicorn.workers.Uvicornworker