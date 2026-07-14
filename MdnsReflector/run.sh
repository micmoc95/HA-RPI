#!/usr/bin/env bash

exec /usr/sbin/avahi-daemon \
    --no-chroot \
    --daemonize=no \
    --debug
