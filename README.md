# monitoring_service

Создать контейнер:
  `make build`

Запустить приложение:
  `make run`
  
Остановить приложение:
  `make stop`
   
Взаимодействия с сервисом:
  1) Добавить событие `(POST)` - `host:port/event`, Необходимо передать `json` со следующими полями:
  
 
   ```json
      {
      "service_name": "название сервиса",
      "event_name": "название события",
      "description": "описание события"
      }
   ```
    
  2) Получить событие по его ID `(GET)` - `host:port/event?event_id=1`
  3) Получить список последних событий в необходимом количестве `(GET)` - `host:port/event_list?service=test1&chunk_size=10`
