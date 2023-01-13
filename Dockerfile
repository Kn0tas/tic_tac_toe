FROM ubuntu:20.04

# update the package manager and install python, pip and xvfb
RUN apt-get update && apt-get install -y python3 python3-pip xvfb

# Set the working directory
WORKDIR /app

# Copy the requirements file and install the dependencies
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Copy the rest of the application files
COPY . .

# Environment variable to use xvfb
ENV SDL_VIDEODRIVER=x11

# Run the script inside xvfb
CMD xvfb-run -s "-screen 0 800x600x24" python3 main.py
