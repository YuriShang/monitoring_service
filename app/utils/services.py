from datetime import datetime

# Таймаут, по которому система мониторинга оценивает статус события,
# если выше указанного значения, приписываем событию статус FAIL
TIMEOUT = 5000  # ms


async def timeout_control(last_event_time):
    timeout = datetime.now() - last_event_time
    timeout = int(timeout.total_seconds() * 1000)
    result = TIMEOUT - timeout
    if result > 0:
        return 'GOOD', timeout
    return 'FAIL', timeout
