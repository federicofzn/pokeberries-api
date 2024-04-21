# Python image.
FROM python:3.10

# Copy dependencies file to working directory.
COPY requirements.txt .

# Install dependencies.
RUN pip install -r requirements.txt

# Copy the rest of the app.
COPY . .

# Final configuration.
ENV FLASK_APP="app"
EXPOSE 8000
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "8000"]