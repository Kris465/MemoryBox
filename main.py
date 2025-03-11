import asyncio
from loguru import logger


async def main():
    logger.add("file.log",
            format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
            rotation="5 days",
            backtrace=True, diagnose=True)
    
    logger.info("...")


if __name__ == '__main__':
    asyncio.run(main())