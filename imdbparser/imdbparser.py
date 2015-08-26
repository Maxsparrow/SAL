import logger as lg


class IMDBGetter:
    _logger = lg.get_logger(__name__)

    def __init__(self, base_url):
        self._logger.info('base url: ' + base_url)

        self.base_url = base_url

    def get_file(self, filename): pass
