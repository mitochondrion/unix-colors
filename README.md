# unix-colors
Python functions for coloring/formatting command line output.  Have only tested on Bash.

## Example:
```python
from unix_colors import *

print D_RED("this will be dark red") + BOLD(B_GREEN("this will be bold and have a green background")) + "this will be the default color"

print "This line will get overwritten by the next print statement" + CARRIAGE_RETURN + CLEAR_LINE

print "This will overwrite the previous statement"
```
