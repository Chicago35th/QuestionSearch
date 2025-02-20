[app]
title = 题库搜索
package.name = questionsearch
package.domain = org.example
source.dir = app
source.include_exts = py,png,jpg,kv,ttf,csv
version = 1.0.0
requirements = 
    python3,
    kivy==2.3.0,
    pandas==2.2.1,
    pypinyin==0.50.0,
    openpyxl==3.1.2,
    Cython==3.0.8
orientation = portrait
osx.python_version = 3
android.api = 34
android.ndk = 26.2.11394342
android.archs = armeabi-v7a
android.system_libs = openssl,zlib

[buildozer]
log_level = 2
