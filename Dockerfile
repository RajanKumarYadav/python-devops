From python
Copy . /app
Workdir /app
Copy requirements.txt .
Run pip install -r requirements.txt
CMD ["python", "app.py"]
