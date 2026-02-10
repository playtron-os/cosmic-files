ARG version=1.90
FROM rust:${version}
ARG version

RUN dpkg --add-architecture arm64
RUN apt-get update && apt-get install -y \
  cmake \
  libclang-dev \
  libglib2.0-dev \
  libglib2.0-dev:arm64 \
  libxkbcommon-dev \
  libxkbcommon-dev:arm64 \
  pkg-config

RUN apt-get install -y \
  g++-aarch64-linux-gnu \
  libc6-dev-arm64-cross

# Taskfile support
RUN curl -1sLf 'https://dl.cloudsmith.io/public/task/task/setup.deb.sh' | bash
RUN apt-get install -y task

# RPM support
RUN apt-get install -y rpm librpmbuild10 elfutils

RUN rustup target add aarch64-unknown-linux-gnu
RUN rustup toolchain install --force-non-host stable-aarch64-unknown-linux-gnu
RUN rustup component add clippy

ENV CARGO_TARGET_AARCH64_UNKNOWN_LINUX_GNU_LINKER=aarch64-linux-gnu-gcc
ENV CC_aarch64_unknown_linux_gnu=aarch64-linux-gnu-gcc
ENV CXX_aarch64_unknown_linux_gnu=aarch64-linux-gnu-g++
ENV PKG_CONFIG_PATH_aarch64_unknown_linux_gnu=/usr/lib/aarch64-linux-gnu/pkgconfig
