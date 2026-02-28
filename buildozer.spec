[app]

# (str) Title of your application
title = Apple Doctor

# (str) Package name
package.name = appledoctor

# (str) Package domain (needed for android packaging)
package.domain = org.rahilafzal

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,tflite

# (str) Application versioning
version = 1.0.0

# (list) Application requirements
# Yahan maine AI library aur image processing ki saari cheezein daal di hain
requirements = python3,kivy,google-generativeai,pillow,numpy,requests,charset-normalizer,idna,urllib3,certifi

# (str) Supported orientation (landscape, portrait or all)
orientation = portrait

# (list) Permissions
# Camera aur Gallery ke liye ye permissions bahut zaroori hain
android.permissions = INTERNET, CAMERA, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE

# (int) Target
