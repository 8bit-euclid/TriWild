# Development container for TriWild
FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    git \
    libgmp3-dev \
    python3 \
    python3-dev \
    python3-pip \
    ninja-build \
    sudo \
    && rm -rf /var/lib/apt/lists/*

# Install essential Python packages
RUN pip3 install --no-cache-dir numpy pybind11[global]

# Create non-root user
ARG USERNAME=vscode
RUN useradd -m -s /bin/bash $USERNAME \
    && echo "$USERNAME ALL=(root) NOPASSWD:ALL" > /etc/sudoers.d/$USERNAME

USER $USERNAME
WORKDIR /workspace
