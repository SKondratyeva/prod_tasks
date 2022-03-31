FROM python:3.4
RUN pip install Flask==0.10.1
RUN useradd -m techproguser
USER techproguser
WORKDIR /cmake-with-flask
COPY cmake-with-flask /cmake-with-flask
CMD ["python", "./app.py"]
