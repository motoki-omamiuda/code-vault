# python built-in
import logging
import time

# pip libraries
from tqdm import tqdm

# local modules
from utils.logger import CommonLogger

if __name__ == "__main__":
    logger: logging.Logger = CommonLogger(logging.INFO).console_logger("main")

    start: float = time.perf_counter()
    for i in tqdm(range(100)):
        time.sleep(0.01)
    end: float = time.perf_counter()

    logger.info(f"processing time: {end - start:.6f}sec")
