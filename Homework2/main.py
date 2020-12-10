import recursion as rec
import input_function as infcn


def function(*argument, **keyargument):
    addition = 0
    for element in argument:
        if isinstance(element, int):
            addition += element

    # for element in keyargument.values():
    #   if isinstance(element, int):
    #        addition += element

    return addition


# * == unpacking operator
# in = [1 2 3]. print(in) => "[1 2 3]" > ONE list
# * unpacks the list => print(*in) => "1 2 3" => 3 different elements
# * works everywhere

# **kwargs = unpacking operator for dictionaries (key = value) structure
# kwargs.values(), kwargs.items()

if __name__ == '__main__':
    print('sum =', function(1, 5, -3, 'abc', [12, 56, 'cad']))
    print('sum =', function())
    print('sum =', function(2, 4, 'abc', param_1=2))

    print("total, even, odd sums: ", rec.return_recursion_result(6))

    infcn.input_function()