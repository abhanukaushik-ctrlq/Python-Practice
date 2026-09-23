print(0.1 + 0.2 == 0.3)            
# direct ==
print(round(0.1 + 0.2, 1) == 0.3)  # round first
import math
print(math.isclose(0.1 + 0.2, 0.3))  # tolerance-based
