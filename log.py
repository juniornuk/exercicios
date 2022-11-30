import logging

#mais opcoes de formarto de log no google =  python logging format
formato_log = ("%(asctime)s , %(levelname)s | %(message)s")

#CONFIGURACAO DO LOG
#filename, guarda o nome do arquivo
#level, guarda o nivel entre (10, 20, 30, 40, 50) onde nivel mais baixo é o DEBUG
#filemode, guarda opcao de w reescrever arquivo de log a cada execucao
#format, formata log com informacoes do sistema
logging.basicConfig(filename = "app.log", level = logging.DEBUG, filemode = "w", format= formato_log)

log = logging.getLogger()

log.debug("debug nivel 10")
log.info("info nivel 20")
log.warning("warning nivel 30")
log.error("error nivel 40")
log.critical("critical nivel 50")
#log.level

