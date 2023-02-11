from pypi_examiner import examiner

pypi = examiner()
print(pypi.who_owns("httpxfaster"))
