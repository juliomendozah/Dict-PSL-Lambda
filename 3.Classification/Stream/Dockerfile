FROM public.ecr.aws/lambda/python:3.9
# Copy function code
COPY app.py ./
# Copy additional codes
COPY extract_keypoints.py ./
COPY extract_poseflow.py ./
COPY predict.py ./
COPY transforms.py ./
# Copy additional directories
COPY /checkpoints ./
COPY /data ./
COPY /models ./
# Install external dependencies
RUN apt-get update && \
apt-get install -y \
libgl1 \
cmake\
make\
g++\
unzip
# Install the function's dependencies using file requirements.txt
COPY requirements.txt ./
RUN pip3 install -r requirements.txt
# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD ["app.Lambda_handler"]
