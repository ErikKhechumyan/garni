[app]

# (str) Title of your application
title = garni

# (str) Package name
package.name = garni

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,mp4

# (str) Application versioning
version = 0.1

# (list) Application requirements
requirements = python3,kivy,ffpyplayer

# (list) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (str) Android SDK directory (if empty, it will be automatically downloaded)
android.sdk_path = $ANDROID_SDK_ROOT

# (list) Permissions
android.permissions = android.permission.READ_EXTERNAL_STORAGE,android.permission.WRITE_EXTERNAL_STORAGE

# (list) The Android archs to build for
android.archs = arm64-v8a, armeabi-v7a

# (bool) Enable backup
android.allow_backup = True

# (bool) Copy library instead of making a libpymodules.so
android.copy_libs = 1

# (str) The format used to package the app for debug mode
android.debug_artifact = apk

# (str) The format used to package the app for release mode
android.release_artifact = apk

# (int) Minimum API your APK / AAB will support
android.minapi = 21

# (int) Target Android API
android.api = 31

# (int) Android NDK API to use
android.ndk_api = 21

# (str) Android NDK version to use
android.ndk = 23b

# (str) Bootstrap to use for android builds
p4a.bootstrap = sdl2

# (str) Python for android fork and branch
p4a.fork = kivy
p4a.branch = master
