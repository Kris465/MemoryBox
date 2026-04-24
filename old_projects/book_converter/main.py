from loguru import logger
import sys
from converter import process_pdf

logger.add("file.log", rotation="500 MB")


def main():
    logger.info("Starting the application")

    if len(sys.argv) != 3:
        logger.error("Usage: python main.py <pdf_path> <markdown_path>")
        sys.exit(1)

    pdf_path = sys.argv[1]
    markdown_path = sys.argv[2]

    try:
        process_pdf(pdf_path, markdown_path)
        logger.info(f"Text extracted from {pdf_path} and saved to {markdown_path}")
    except Exception as e:
        logger.error(f"Failed to process PDF: {e}")
        sys.exit(1)

    logger.info("Application finished successfully")

if __name__ == "__main__":
    main()
