import sys

print('Esta é a saída no STDOUT')
print('Esta é uma mensagem de erro no STDERR', file=sys.stderr)
sys.exit(1)
