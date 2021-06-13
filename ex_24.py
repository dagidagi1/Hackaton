#Arkadi Yakubov 208064162
#Mikhail diachkov 336426176

def init_id_mat(size):
    id_mat = []
    for i in range(size):
        row = []
        for j in range(size):
            if i == j:
                row.append(1)
            else:
                row.append(0)
        id_mat.append(row)
    return id_mat

def print_vec(mat):
    for i in range(len(mat)):
        for j in mat[i]:
            print("%.3f" % j, end="\t")
        print()

def print_mat(mat, b):
    for i in range(len(mat)):
        for j in mat[i]:
            print("%.3f" % j, end="\t")
        print("%.3f" % b[i][0])

def way_A(mat, b):
    inv_mat = invert_mat(mat)
    return mul_mat(inv_mat, b)

def mul_mat(mat1, mat2):
    def get_col(mat, i):
        col = []
        for _ in mat:
            col.append(_[i])
        return col

    def mul_row_col(row, col):
        x = 0
        for i in range(len(row)):
            x += row[i] * col[i]
        return x

    if len(mat1[0]) != len(mat2):
        print("Can't multiply this matrix!")
        return None
    new_mat = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat2[0])):
            row.append(mul_row_col(mat1[i], get_col(mat2, j)))
        new_mat.append(row)
    return new_mat


def invert_mat(mat):
    inv_mat = init_id_mat(len(mat))
    for j in range(len(mat)):
        for i in range(j, len(mat)):
            elem_mat = init_id_mat(len(mat))
            if i == j:
                max_piv = abs(mat[i][i])
                max_index = i
                for k in range(i + 1, len(mat)):
                    if abs(mat[k][j]) > max_piv:
                        max_index = k
                        max_piv = abs(mat[k][j])
                if max_index != i:
                    mat[i], mat[max_index] = mat[max_index], mat[i]
                    inv_mat[i], inv_mat[max_index] = inv_mat[max_index], inv_mat[i]
                elem_mat[i][i] = 1/mat[i][i]
                mat = mul_mat(elem_mat, mat)
                inv_mat = mul_mat(elem_mat, inv_mat)
            else:
                elem_mat[i][j] = -mat[i][j]/mat[j][j]
                mat = mul_mat(elem_mat, mat)
                inv_mat = mul_mat(elem_mat, inv_mat)
    for j in range(len(mat)-1, 0, -1):
        for i in range(j-1, -1, -1):
            elem_mat = init_id_mat(len(mat))
            elem_mat[i][j] = -mat[i][j]/mat[j][j]
            mat = mul_mat(elem_mat, mat)
            inv_mat = mul_mat(elem_mat, inv_mat)
    return inv_mat


def determinant(mat):
    def sub_mat_for_det(piv):
        def remove_row(x, i):
            new_mat = x.copy()
            new_mat.pop(i)
            return new_mat

        def remove_col(x, i):
            new_mat = x.copy()
            for _ in range(len(new_mat)):
                new_mat[_] = new_mat[_][:i] + new_mat[_][i + 1:]
            return new_mat
        new_mat = remove_row(mat, 0)
        new_mat = remove_col(new_mat, piv)
        return new_mat
    if len(mat) == 2:
        return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
    sign = 1
    det = 0
    for i in range(len(mat[0])):
        det += sign * mat[0][i] * determinant(sub_mat_for_det(i))
        sign *= -1
    return det

def yakobi(mat, vec_b):
    global epsilon
    size = len(mat)
    index = 0
    def print_iteration(index, vec):
        print(index, end=" | ")
        for i in range(len(vec)):
            print("%.3f" % vec[i][0], end="\t")
        print()
    def init_zero_mat(size):
        mat = []
        for i in range(size):
            row = []
            for j in range(size):
                row.append(0)
            mat.append(row)
        return mat
    def init_def_vector(size):
        vec = []
        for i in range(size):
            row = [0]
            vec.append(row)
        return vec
    def decomposition(mat):
        #returns U matrix, L matrix, D matrix
        d_mat = init_zero_mat(size)
        u_mat = init_zero_mat(size)
        l_mat = init_zero_mat(size)
        for i in range(size):
            for j in range(size):
                if j == i:
                    d_mat[i][j] = mat[i][j]
                elif j<i:
                    l_mat[i][j] = mat[i][j]
                else:
                    u_mat[i][j] = mat[i][j]
        return u_mat, l_mat, d_mat
    def add_mat(mat1, mat2):
        new_mat = mat1
        for i in range(len(mat1)):
            for j in range(len(mat1[i])):
                new_mat[i][j] += mat2[i][j]
        return new_mat
    def minus_mat(mat):
        for i in range(size):
            for j in range(len(mat[i])):
                if mat[i][j] != 0:
                    mat[i][j] = -mat[i][j]
        return mat
    def check_eps(vec1, vec2):
        for i in range(len(vec1)):
            if abs(vec2[i][0] - vec1[i][0]) > epsilon:
                return False
        return True
    def step(x_r):
        nonlocal index
        index += 1
        next_x_r = add_mat(mul_mat(g_mat, x_r), mul_mat(h_mat, vec_b))
        print_iteration(index, next_x_r)
        if(check_eps(x_r, next_x_r)):
            return next_x_r
        return step(next_x_r)

    u_mat, l_mat, d_mat = decomposition(mat)
    d_mat = invert_mat(d_mat)#we use only inverted D.
    #yakobi G and H mats
    g_mat = minus_mat(mul_mat(d_mat, add_mat(l_mat, u_mat)))
    h_mat = d_mat
    #gaos G and H mats, dont work, dividing by zero error
    #g_mat =mul_mat(minus_mat(add_mat(l_mat,d_mat)), u_mat)
    #h_mat =invert_mat(add_mat(l_mat,d_mat))
    print("", end="\t")
    for i in range(size):
        print(f"X{i + 1}", end="\t\t")
    print()
    return step(init_def_vector(size)), index



def example(example_mat, vector_b):
    print_mat(example_mat, vector_b)
    if determinant(example_mat) == 0:
        print("determinant = 0, cant find A ^ (-1)")
    else:
        print("===========================================")
        print("A_inv * b:\n")
        print_vec(way_A(example_mat,vector_b))
        print("===========================================")
    t1, t2 = yakobi(example_mat, vector_b)
    print("Jacobi solved in {0} attempts.".format(t2))
    print_vec(t1)

epsilon = 0
print("ex- 24")
mat24 = [[0.04, 0.01, -0.01], [0.2, 0.5, -0.2], [1, 2, 4] ]
b24 = [[0.06], [0.3], [11]]
#example(mat24, b24)

