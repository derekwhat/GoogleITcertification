"""Part Five of final assignment: Routine Health Check"""

# code is based on examples shown throughout the past 5 courses
# of the Google IT certification

#!/usr/bin/env python3
import socket
import shutil
import psutil
import emails
import os


def normal_cpu_usage():
    """check if unused CPU"""
    usage = psutil.cpu_percent(1)
    return usage < 80


def normal_disk_usage(disk):
    """check if enough free space on disk"""
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20


def normal_memory_usage():
    """check if enough free space on disk"""
    mu = psutil.virtual_memory().available
    total = mu / (1024.0 ** 2)
    return total > 500


def using_localhost():
    """check if host is 127.0.0.1"""
    localhost = socket.gethostbyname('localhost')
    return localhost == "127.0.0.1"


def send_email(subject):
    user = user = os.getenv('USER')
    recepient = "automation@example.com"
    sender = "{}@example.com".format(user)
    msg = "Please check your system and resolve the issue as soon as possible."

    email = emails.generate_email(recepient, sender, subject, msg, "")
    emails.send_email(email)


# health checks
if not normal_cpu_usage():
    subject = "Error - CPU usage is over 80%"
    send_email(subject)
if not normal_memory_usage():
    subject = "Error - Available memory is less than 500MB"
    send_email(subject)
if not normal_disk_usage('/'):
    subject = "Error - Available disk space is less than 20%"
    send_email(subject)
if not using_localhost():
    subject = "Error - localhost cannot be resolved to 127.0.0.1"
    send_email(subject)

""" to set up cronjob to run health_check.py every minute:
$ contab -e
$ select nano as editor
$ * * * * * /home/student-00-69ccdc05c775/health_check.py" <--full abs path
$ save and close editor
"""
