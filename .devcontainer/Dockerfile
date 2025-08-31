# Development container for TriWild
FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies (excluding cmake - we'll install a newer version)
RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    libgmp3-dev \
    python3 \
    python3-dev \
    python3-pip \
    ninja-build \
    sudo \
    wget \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Install CMake 4.1.0 from official binaries
RUN wget -O cmake.tar.gz https://github.com/Kitware/CMake/releases/download/v4.1.0/cmake-4.1.0-linux-x86_64.tar.gz \
    && tar -xzf cmake.tar.gz -C /opt \
    && mv /opt/cmake-4.1.0-linux-x86_64 /opt/cmake \
    && ln -s /opt/cmake/bin/cmake /usr/local/bin/cmake \
    && ln -s /opt/cmake/bin/ctest /usr/local/bin/ctest \
    && ln -s /opt/cmake/bin/cpack /usr/local/bin/cpack \
    && rm cmake.tar.gz

# Install essential Python packages
RUN pip3 install --no-cache-dir numpy pybind11[global]

# Create non-root user
ARG USERNAME=vscode
RUN useradd -m -s /bin/bash $USERNAME \
    && echo "$USERNAME ALL=(root) NOPASSWD:ALL" > /etc/sudoers.d/$USERNAME

USER $USERNAME
WORKDIR /workspace
