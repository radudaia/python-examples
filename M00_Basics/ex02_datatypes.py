
# ex02_datatypes.py
# In this example, we can see the most common basic datatypes in Python
# We also see how we can utilize the type() function

if __name__ == "__main__":
    my_int_num = 5
    my_string = "Hello World!"
    my_float_num = 5.5
    my_bool = True
    my_complex = 3 + 4j

    print(f"Variable my_int_num contains the value {my_int_num} and is of type {type(my_int_num)}")
    print(f"Variable my_float_num contains the value {my_float_num} and is of type {type(my_float_num)}")
    print(f"Variable my_string contains the value {my_string} and is of type {type(my_string)}")
    print(f"Variable my_bool contains the value {my_bool} and is of type {type(my_bool)}")
    print(f"Variable my_complex contains the value {my_complex} and is of type {type(my_complex)}")