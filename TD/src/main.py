# Import from existence package
from existence import Existence010
from existence import Existence020


def main():
    existence = Existence010()
    existence = Existence020()

    for i in range(0, 20):
        step_trace = existence.step()
        print('{0}: {1}'.format(i, step_trace))

if __name__ == '__main__':
    main()
