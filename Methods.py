import numpy as np


def f(u, a, b):
    return 2 * r0(u, a, b)


def r0(u, a, b):
    return a.dot(u) - b


def ar0(u, a, b):
    return a.dot(r0(u, a, b))


def matrix_to_vector(matrix):
    return np.squeeze(np.asarray(matrix))


def norma(r):
    sum = 0

    for i in range(len(r)):
        sum += float(r[i][0]) ** 2

    return sum


def find_tau_steepest_descent(ar, u, a, b):
    return matrix_to_vector(r0(u, a, b)).dot(matrix_to_vector(r0(u, a, b))) / matrix_to_vector(ar).dot(
        matrix_to_vector(ar))


def find_tau_minimal_residual_method(ar, u, a, b):
    return matrix_to_vector(r0(u, a, b)).dot(matrix_to_vector(ar)) / matrix_to_vector(ar).dot(matrix_to_vector(ar))


def find_tau_conjugation_gradients(ar, u, a, b):
    return matrix_to_vector(r0(u, a, b)).dot(matrix_to_vector(r0(u, a, b))) / matrix_to_vector(ar).dot(
        matrix_to_vector(r0(u, a, b)))


def steepest_descent(a, b, eps, condition):
    u1 = np.asmatrix(np.zeros(len(a))).transpose()
    u = u1 - 1

    iterations = 0

    if len(a) == 4:
        str = 1

    while condition(u, u1, eps) | (abs(norma(r0(u, a, b))) > eps ** 2):
        u = u1
        tau = find_tau_steepest_descent(ar0(u, a, b), u, a, b)

        u1 = u - tau * r0(u, a, b)
        iterations += 1

    return u1, norma(r0(u, a, b))


def minimal_residual(a, b, eps, condition):
    u1 = np.asmatrix(np.zeros(len(a))).transpose()
    u = u1 - 1

    iterations = 0

    while condition(u, u1, eps):
        u = u1
        tau = find_tau_minimal_residual_method(ar0(u, a, b), u, a, b)

        u1 = u - tau * r0(u, a, b)
        iterations += 1

    return u1, iterations


def conjugation_gradients(a, b, eps, condition):
    iterations = 2

    u0 = np.asmatrix(np.zeros(len(a))).transpose()
    alpha = 1
    e = np.eye(len(a))

    tau1 = find_tau_conjugation_gradients(ar0(u0, a, b), u0, a, b)
    u = (e - tau1 * a).dot(u0) + tau1 * b

    tau = tau1
    tau1 = find_tau_conjugation_gradients(ar0(u, a, b), u, a, b)
    alpha = (1 - tau1 / tau * matrix_to_vector(r0(u, a, b)).dot(matrix_to_vector(r0(u, a, b))) / matrix_to_vector(
        r0(u0, a, b)).dot(matrix_to_vector(r0(u0, a, b))) * 1 / alpha) ** -1
    u1 = alpha * (e - tau1 * a).dot(u) + (1 - alpha) * u0 + alpha * tau1 * b

    while condition(u, u1, eps):
        u0 = u
        u = u1
        tau = tau1

        tau1 = find_tau_conjugation_gradients(ar0(u, a, b), u, a, b)
        alpha = (1 - tau1 / tau * matrix_to_vector(r0(u, a, b)).dot(matrix_to_vector(r0(u, a, b))) / matrix_to_vector(
            r0(u0, a, b)).dot(matrix_to_vector(r0(u0, a, b))) * 1 / alpha) ** -1
        u1 = alpha * (e - tau1 * a).dot(u) + (1 - alpha) * u0 + alpha * tau1 * b

        iterations += 1

    return u1, iterations
