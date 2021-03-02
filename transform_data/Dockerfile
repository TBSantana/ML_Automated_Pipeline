FROM python:3.6-slim
WORKDIR /app

# Good practice to copy just dependencies first; this helps
# layer caching when you repeat `docker build`.
# COPY source path is relative to the `docker build` directory,
# which we've set up to be the parent of the application source.
COPY transform_data/requirements.txt .
RUN pip install -r requirements.txt

# Now copy in the rest of the application
COPY transform_data .

# And also copy the shared data
COPY preprocessed_data ./preprocessed_data

# And have ordinary container startup metadata
CMD ["python3", "./transform_data.py", "$(pwd)"]

# docker build -t transform_image -f transform_data/Dockerfile .