# Personal Library Manager
# Version 0.1
# Author: Shah Faisal (faisal.islam.ceme@gmail.com)

import library_io

library: list = library_io.load_library()

print(library)

library.append("zeytoon")
library.append("eid mubarak")

library_io.save_library(library)