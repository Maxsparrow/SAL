import logger as lg
from imdbparser import IMDBGetter

IMDB_FTP_URL = 'ftp://ftp.sunet.se/pub/tv+movies/imdb/'

QUOTES_FILENAME = 'quotes.list.gz'

def main():
    lg.set_logger('imdbparser')

    imdb = IMDBGetter(IMDB_FTP_URL)

    imdb.get_file(QUOTES_FILENAME)


if __name__=='__main__':
    main()
