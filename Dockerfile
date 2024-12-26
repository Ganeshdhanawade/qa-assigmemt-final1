FROM python:3.9-slim
WORKDIR /app
COPY . /app/
RUN apt-get update && apt-get install -y libgl1-mesa-glx
RUN pip install -r requirements.txt
CMD [ "uvicorn", "main.py", "--host", "", "--port", "8000" ]