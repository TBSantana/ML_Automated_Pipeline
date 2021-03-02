FROM python:3.6-slim
WORKDIR /app

# Good practice to copy just dependencies first; this helps
# layer caching when you repeat `docker build`.
# COPY source path is relative to the `docker build` directory,
# which we've set up to be the parent of the application source.
COPY app_prediction/requirements.txt .

RUN pip install -r requirements.txt

# Now copy in the rest of the application
COPY app_prediction .

# And also copy the shared data
COPY preprocessed_data ./preprocessed_data
	
# And have ordinary container startup metadata
#CMD ["python3", "./app.py", "$(pwd)"]
CMD ["python3", "./app.py"]