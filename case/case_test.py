import pytest
from setting_info import excel_setting;
@pytest.mark.parametrize("ss",["你好","不好","哈哈"])
def test_pr(ss):

    print(ss)



if __name__ == '__main__':
    pytest.main(["case_test.py"])