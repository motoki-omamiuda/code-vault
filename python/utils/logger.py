"""Common Logger を提供するモジュール"""
# python built-in
import logging
import sys

ERROR_LOG_FILE_PATH = "./localstorage/error.log"


class CommonLogger:
    """共通ログ設定クラス"""

    def __init__(self, level: int = logging.INFO) -> None:
        """初期化

        Args:
            level (int): ログレベル（デフォルト: logging.INFO）
        """
        self.logger_level = level
        self.logger_formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

    def console_logger(self, name: str) -> logging.Logger:
        """コンソール出力用のログを設定

        Args:
            name (str): loggerの名前

        Returns:
            logging.Logger: 設定されたloggerインスタンス
        """
        console_logger: logging.Logger = logging.getLogger(name)
        console_logger.setLevel(self.logger_level)
        console_logger.propagate = False

        if console_logger.hasHandlers():
            console_logger.handlers.clear()

        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(self.logger_level)
        console_handler.setFormatter(self.logger_formatter)
        console_logger.addHandler(console_handler)

        return console_logger

    def file_logger(self, name: str, file: str) -> logging.Logger:
        """ファイルへの出力用のログを設定

        Args:
            name (str): loggerの名前
            file (str): ログファイルのパス

        Returns:
            logging.Logger: 設定されたloggerインスタンス
        """
        file_logger: logging.Logger = logging.getLogger(name)
        file_logger.setLevel(self.logger_level)
        file_logger.propagate = False

        if file_logger.hasHandlers():
            file_logger.handlers.clear()

        file_handler = logging.FileHandler(file, mode='a', encoding='utf-8')
        file_handler.setLevel(self.logger_level)
        file_handler.setFormatter(self.logger_formatter)
        file_logger.addHandler(file_handler)

        return file_logger
