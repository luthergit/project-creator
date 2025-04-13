# Start with the official Python 3.13 image
FROM python:3.13

# Set working directory inside container
WORKDIR /app

# Copy all files from current directory to /app in container
COPY . .

# Install uv (ultra-fast Python package installer)
RUN pip install uv

# Synchronize Python dependencies using uv
RUN uv sync

# Install zsh with powerline10k theme using a popular installation script
# This adds a more feature-rich shell with better prompts and colors
RUN sh -c "$(wget -O- https://github.com/deluan/zsh-in-docker/releases/download/v1.2.1/zsh-in-docker.sh)"

# Install vim text editor
RUN apt install vim -y

# Default command to run when container starts (overridden by docker-compose)
CMD ["zsh"]
