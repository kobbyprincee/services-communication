#Use Python 3.12 slim image as the base image
FROM python:3.12-slim
#App working directory
WORKDIR /app

#Copy Requirements and Install Dependencies
#
# ENV PYTHONUNBUFFERED  1
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#Copy application files
COPY main.py .
#COPY service1.py .
COPY service2.py .

#Expose PORT for service2

EXPOSE 5001

#Run the main application
CMD ["python" , "main.py"]
