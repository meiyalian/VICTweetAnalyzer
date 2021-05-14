docker build -t test:latest .
docker run -d -p 5000:5000 test:latest