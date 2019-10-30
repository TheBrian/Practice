def get_shape(matrix):
    return [len(r) for r in matrix]


def add(*matricies):
    shape_of_matrix = get_shape(matricies[0])
    if any(get_shape(m) != shape_of_matrix for m in matricies):
        raise ValueError("Given matrices are not the same size.")
    else:
        return [
            [sum(values) for values in zip(*rows)]
            for rows in zip(*matricies)
        ]

#  The loops down below was condensed into one return statment above
#  combined = []
#         for rows in zip(*matricies):
#             row = []
#             for values in zip(*rows):
#                 row.append(sum(values))
#             combined.append(row)
#         return combined
