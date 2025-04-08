[app]
title = MyApp
package.name = myapp
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,mp4,avi,mkv
version = 1.0
requirements = python3,kivy,ffpyplayer,plyer
orientation = portrait
fullscreen = 1
android.permissions = INTERNET,WAKE_LOCK
android.minapi = 21
android.ndk = 25b
android.ndk_path = 
android.sdk_path = 
android.entrypoint = main.py
android.archs = armeabi-v7a, arm64-v8a
android.api = 31
android.gradle_dependencies = 
android.gradle_plugins = 
android.enable_androidx = 1
android.use_android_native_api = False
p4a.branch = master
p4a.bootstrap = sdl2
p4a.local_recipes = 
android.additional_packages = 
android.extra_args = 
android.debug = 1
android.logcat_filters = *:S python:D
log_level = 2
strip = true
copy_libs = 1

[buildozer]
log_level = 2
warn_on_root = 1
