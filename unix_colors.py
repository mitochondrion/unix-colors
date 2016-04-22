def generateColorizeFunction(color):
	END_COLORING = '\033[0m'
	return lambda string: color + string + END_COLORING

GREY = generateColorizeFunction('\033[90m')
RED = generateColorizeFunction('\033[91m')
GREEN = generateColorizeFunction('\033[92m')
YELLOW = generateColorizeFunction('\033[93m')
BLUE = generateColorizeFunction('\033[94m')
MAGENTA = generateColorizeFunction('\033[95m')
CYAN = generateColorizeFunction('\033[96m')

BLACK = generateColorizeFunction('\033[30m')
D_RED = generateColorizeFunction('\033[31m')
D_GREEN = generateColorizeFunction('\033[32m')
D_YELLOW = generateColorizeFunction('\033[33m')
D_BLUE = generateColorizeFunction('\033[34m')
D_MAGENTA = generateColorizeFunction('\033[35m')
D_CYAN = generateColorizeFunction('\033[36m')

B_GREY = generateColorizeFunction('\033[100m')
B_RED = generateColorizeFunction('\033[101m')
B_GREEN = generateColorizeFunction('\033[102m')
B_YELLOW = generateColorizeFunction('\033[103m')
B_BLUE = generateColorizeFunction('\033[104m')
B_MAGENTA = generateColorizeFunction('\033[105m')
B_CYAN = generateColorizeFunction('\033[106m')

BOLD = generateColorizeFunction('\033[1m')
UNDERLINE = generateColorizeFunction('\033[4m')

CARRIAGE_RETURN = "\r"
CLEAR_LINE = "\033[2K"