# 1. Use the official Playwright Python image
FROM mcr.microsoft.com/playwright/python:v1.40.0-jammy

# 2. Set the working directory
WORKDIR /app

# 3. Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy your application code
COPY . .

# 5. Run the script
ENTRYPOINT [ "python" ]
CMD ["main.py"]