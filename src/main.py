import datetime
from fastapi import FastAPI

from src.log.database_sink import DatabaseSink
from src.enum.log_level import LogLevel
from src.log.console_sink import ConsoleSink
from src.log.enum import ThreadModel, WriteMode
from src.log.file_sink import FileSink
from src.log.logger import Logger
from src.log.logger_config import LoggerConfig
from src.log.schemas.log_request import LogRequest

# Create an instance of the FastAPI class
app = FastAPI()

# Define a root route
@app.get("/health")
async def read_root():
    return {"message": "Welcome to FastAPI! You app is healthy"}

@app.post("/test_log")
async def test_log(log_request: LogRequest):
    thread_model = ThreadModel[log_request.thread_model]  
    write_mode = WriteMode[log_request.write_mode]     
    level = LogLevel(log_request.level)
    file_sink = FileSink(level=level, file_path="app.log", max_size_kb=50, backup_count=3)
    console_sink = ConsoleSink(level=level)
    db_sink = DatabaseSink(level=level, db_path="logs.db")

    config = LoggerConfig(
        timestamp_format=log_request.timestamp_format or "%Y-%m-%d %H:%M:%S",
        log_level=level,
        sinks=[file_sink, console_sink, db_sink],
        thread_model=thread_model,
        write_mode=write_mode
    )
    
    logger = Logger(config)
    timestamp = datetime.datetime.now().strftime(config.timestamp_format)
    logger.log(log_request.message, level, log_request.namespace)

    return {"message": f"Logged '{log_request.message}' with level {log_request.level} in namespace '{log_request.namespace}' at '{timestamp}'."}
