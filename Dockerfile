FROM python:3.9-slim-buster
COPY . .
WORKDIR .
RUN python3 -m pip install requests
CMD ["python3", "main.py"]
