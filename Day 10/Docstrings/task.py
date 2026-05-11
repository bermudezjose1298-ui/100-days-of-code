def format_name(f_name, l_name):
    """This function will take the first and last name and format the name
    and then will place uppercases in just the first letters"""
    def other_function(first,second):
        return f_name.upper() + l_name.upper()
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return other_function(formated_f_name,formated_l_name)


formatted_name = format_name("AnGeLa", "yU")

length = len(formatted_name)



