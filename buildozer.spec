[app]
title = Apple Doctor
package.name = appledoctor
package.domain = org.rahilafzal
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0.0

# Zaroori Libraries (AI aur Images ke liye)
requirements = python3,kivy,google-generativeai,pillow,requests

orientation = portrait
android.permissions = INTERNET, CAMERA, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE
android.api = 31
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 1
