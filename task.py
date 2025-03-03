import platform
import psutil
import os
from datetime import datetime

with open("result.txt", "w", encoding="utf-8") as file:
    file.write("Результат сохранен в result.txt")

print("Результат сохранен в result.txt")