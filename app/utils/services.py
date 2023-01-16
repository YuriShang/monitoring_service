from datetime import datetime

SERVICES = {
}

# Таймаут, по которому система мониторинга оценивает статус события
TIMEOUT = 5000


async def timeout_control(service_name):
    print(SERVICES)
    if SERVICES.get(service_name):
        timeout = datetime.now() - SERVICES[service_name]
        timeout = timeout.total_seconds() * 1000
        SERVICES[service_name] = datetime.now()
        result = TIMEOUT - timeout
        if result > 0:
            return 'GOOD', timeout
        return 'FAIL', timeout

    else:
        SERVICES[service_name] = datetime.now()
        return 'GOOD', 0
