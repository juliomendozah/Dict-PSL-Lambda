FROM public.ecr.aws/lambda/python:3.9
# Copy function code
COPY app.py ./
# Copy additional codes
COPY extract_keypoints.py ./
COPY extract poseflow.py ./
COPY predict.py ./
COPY transforms.py ./
# Copy additional directories
COPY /checkpoints ./
COPY /data/
COPY /models./
# Install the function's dependencies using file requirements.txt
COPY requirements.txt./
RUN pip3 install -r requirements.txt
RUN sudo apt-get update && sudo apt-get install libgl1 -y
# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD ["app.Lambda_handler"]
