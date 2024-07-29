import os

import pytest

if __name__ == '__main__':

    pytest.main(["../case/hospital_sele.py","-k","hz","--alluredir","../report/data"]);

    os.system("allure generate ../report/data -o ../report/html --clean");