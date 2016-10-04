# -*- coding: utf8 -*-

from math import cos, atan, sqrt, exp

def fwd_euler(f, x_init, t_start, t_end, delta_t):
    """

    :param f:
    :param x_init:
    :param t_start:
    :param t_end:
    :param delta_t:
    :return:
    """
    m_time_step = int((t_end - t_ start) * 1.0 / delta_t)
    n_states = len(x_init)
    list_k = tuple(range(m_time_step))
    list_t = tuple(([t_start + delta_t * i for i in list_k]))
    list_x = [tuple(x_init)]
    for k in list_t[1:]:
        list_x.append([0.0] * n_states)
    xk=x_init
    for k in list_k[:-1]:
        sk= f(xk, list_t[k])
        xk1 = list_x[k+1]
        for i in xrange