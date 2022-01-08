import logging
import logging.config
# logger = logging.getLogger(__name__)
# logging.basicConfig(format='%(levelname)s:%(message)s:%(asctime)s', level=logging.DEBUG,datefmt='%m-%d-%Y')

# logger.debug()
# logging.debug('第一行日志')
# logging.info('第二行日志')
# logging.warning('adn so on')


# 手动配置

# logger = logging.getLogger('simple_example')
# logger.setLevel(logging.DEBUG)
#
# sh = logging.StreamHandler()
# sh.setLevel(logging.INFO)
#
# fh = logging.FileHandler(filename='logging.log')
# fh.setLevel(logging.WARNING)
#
# formatter = logging.Formatter(fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#
# sh.setFormatter(formatter)
# fh.setFormatter(formatter)
#
# logger.addHandler(sh)
# logger.addHandler(fh)
#
# logger.debug('debug message')
# logger.info('info message')
# logger.warning('warn message')
# logger.error('error message')
# logger.critical('critical message')


# 配置文件的方式
# logging.config.fileConfig('logging.conf')
#
# logger = logging.getLogger('simpleExample')
# logger2 = logging.getLogger('root')

# logger.debug('debug message')
# logger.info('info message')
# logger.warning('warn message')
# logger.error('error message')
# logger.critical('critical message')


# 配置字典的方式
import yaml

with open('logging.conf.yaml') as f:

    dic = yaml.load(f)

logging.config.dictConfig(dic)


logger = logging.getLogger('simpleExample')

logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')