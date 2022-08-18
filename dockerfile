From python
Copy . /app
Workdir /app
copy requirements.txt .
Run pip install -r requirements.txt
CMD ["python", "app.py"]