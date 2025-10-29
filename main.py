def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    user_input = input()
    string_list = user_input.split(",")
    print("string_list",string_list)
    float_list = []
    for string in string_list:
        float_num = float(string)
        float_list.append(float_num)
    return float_list

def calc_average_temperature(l):
    avg = sum(l)/len(l)
    return avg

def calc_min_max_temperature(m):
    maxtemp = max(m)
    mintemp = min(m)
    maxminlist = [mintemp, maxtemp]
    return maxminlist

def main():
    display_main_menu()
    x = get_user_input()
    print("my float list", x)
    print(calc_average_temperature(x))
    print(calc_min_max_temperature(x))


main()