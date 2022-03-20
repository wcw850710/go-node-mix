from distutils.util import strtobool

data = "21"
int_data = int(data)
print(type(int_data), int_data)

data_str = str(int_data)
print(type(data_str), data_str)

data_float = float(data_str)
print(type(data_float), data_float)

# 非空字符串都是 true
data_bool = bool("true11")
print(type(data_bool), data_bool)

data_bool2 = strtobool("true1")
print(type(data_bool2), data_bool2)