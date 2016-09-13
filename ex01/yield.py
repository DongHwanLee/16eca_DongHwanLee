import math
import root_finding
def problem_to_solve(radius_m):
    """
    :param radius_m:
    :return:
    """
    safety_factor = 2.0
    stress_max_Pa = 207e6
    force_N = 100

    return stress_Pa

def main():
    x_l_init = root_finding.epsilon_global * 2
    x_h_init = 1.0
    result = root.finding.blsection(problem_to_solve, x_l_init, x_h_init, 1e-9)

    print "result =", result

if "__main__" == __name__:
    main()
    