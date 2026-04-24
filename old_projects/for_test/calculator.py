from loguru import logger

class Calculator:
    def add(self, a, b):
        logger.info(f"Adding {a} and {b}")
        return a + b

    def subtract(self, a, b):
        logger.info(f"Subtracting {b} from {a}")
        return a - b

    def multiply(self, a, b):
        logger.info(f"Multiplying {a} and {b}")
        return a * b

    def divide(self, a, b):
        logger.info(f"Dividing {a} by {b}")
        if b == 0:
            logger.error("Cannot divide by zero")
            raise ValueError("Cannot divide by zero")
        return a / b
