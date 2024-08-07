import datetime
import traceback
import os
from Gaggar.settings import BASE_DIR

def log_access(request):
    access_txt_path = os.path.join(BASE_DIR, 'logs', 'Access.txt')
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        client_ip = x_forwarded_for.split(',')[0].strip()
    else:
        client_ip = request.META.get('REMOTE_ADDR')
    
    url = request.get_full_path()

    user_agent = str(request.META.get('HTTP_USER_AGENT', ''))
    with open(access_txt_path,'a') as access_log:
        date_time = datetime.datetime.now().strftime("%d/%m/%Y - %H:%M:%S")
        access_log.write(f"[{date_time}] : [{url}]/[{request.method}] - {client_ip} - {user_agent}\n")

def log_info(text):
    access_txt_path = os.path.join(BASE_DIR, 'logs', 'Access.txt')
    current_datetime = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    with open(access_txt_path, 'a') as file:
        file.write(f"[{current_datetime}] : {text}\n")

def log_error(request, exception):
    error_txt_path = os.path.join(BASE_DIR, 'logs', 'Error.txt')
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        client_ip = x_forwarded_for.split(',')[0].strip()
    else:
        client_ip = request.META.get('REMOTE_ADDR')
    
    url = request.get_full_path()

    user_agent = str(request.META.get('HTTP_USER_AGENT', ''))
    traceback_info = traceback.format_exc()
    line_breaker = '## ---------------------------------------------------------------------- ##'
    with open(error_txt_path, 'a') as error_log:
        date_time = datetime.datetime.now().strftime("%d/%m/%Y - %H:%M:%S")
        error_log.write(f"[{date_time}] : [{url}]/[{request.method}] - {client_ip} - {user_agent}\n{traceback_info}{line_breaker}\n")
        
