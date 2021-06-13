#Arkadi Yakubov 208064162
#Mikhail diachkov 336426176
from main import suffix
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
def neville_interpulation(points, x_f):
    def poly(m, n):
        if m == n:
            if points[m][0] == x_f:
                return points[m][1]
            else:
                return points[n][1]
        return (((x_f - points[m][0]) * poly(m + 1, n)) - ((x_f - points[n][0]) * poly(m, n - 1))) \
               / (points[n][0] - points[m][0])
    return poly(0, len(points) - 1)


def polynomial_interpulation(points, x_f):
    poly_deg = len(points) - 1
    p_x = 0.0
    mat = []
    vec_b = []
    for p in points:
        mat.append([p[0] ** 2, p[0], 1])
        vec_b.append([p[1]])
    factor_vec = way_A(mat, vec_b)
    for fac in factor_vec:
        p_x += fac[0] * (x_f ** poly_deg)
        poly_deg -= 1
    return p_x

def main():
    x_f = 1.37
    point1 = [1.2,3.5095]
    point2 = [1.3, 3.6984]
    point3 = [1.4, 3.9043]
    point4 = [1.5, 4.1293]
    point5 = [1.6, 4.3756]
    points = []
    points.append(point2)
    points.append(point3)
    points.append(point4)
    print("Polynomial interpulation:")
    print(suffix(polynomial_interpulation(points,x_f), 131648))
    points.append(point5)
    points.append(point1)
    print("Neville interpulation:")
    print(suffix(neville_interpulation(points,x_f), 131648))

main()