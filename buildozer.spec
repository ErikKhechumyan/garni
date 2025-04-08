[app]

# Title of your application
title = garni

# Package name and domain
package.name = garni
package.domain = org.test

# Source location
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,mp4

# Application version
version = 0.1

# Requirements for building
requirements = python3,kivy,ffpyplayer

# Orientation
orientation = portrait

# Fullscreen mode (0 = off, 1 = on)
fullscreen = 0

# Android settings
android.ndk_path = /usr/local/lib/android/sdk/ndk/25.1.8937393
android.ndk = 23b
android.api = 31
android.minapi = 21
android.ndk_api = 21
android.accept_sdk_license = True
android.skip_update = False
# Architectures to build for
android.archs = arm64-v8a, armeabi-v7a

# Ensure libraries are copied correctly
android.copy_libs = 1

# Allow auto-backup
android.allow_backup = True

# Logcat filter (optional, useful for debugging)
android.logcat_filters = *:S python:D
