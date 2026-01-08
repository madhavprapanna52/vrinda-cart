import logging as log

# Loging config
log.basicConfig(
    filename="app.log",      # file name
    level=log.INFO,       # minimum level to record
    format="%(asctime)s | %(levelname)s | %(message)s"
)


