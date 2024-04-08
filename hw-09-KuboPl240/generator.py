from random import choices, randint


def generate_classroom(sorted_names):
    """
    Returns list of ordered strings generated from a dict of names.
    :param dict sorted_names: dict of names sorted by first character
    :rtype: list
    :return: ordered sequence of randomly selected names
    """
    random_keys = choices(
        list(sorted_names.keys()),
        k=randint(1 + len(sorted_names) // 4, 2 + len(sorted_names) // 2),
    )
    random_keys = list(set(random_keys))
    random_keys.sort()

    classroom = list()
    for key in random_keys:
        random_names = choices(
            sorted_names[key],
            k=randint(1, 1 + len(sorted_names[key]) // 4),
        )
        classroom.extend(random_names)

    return classroom


def main():
    """
    Test function
    :return:
    """
    print(generate_classroom({'A': ['Alzbeta', 'Amalie'], 'C': ['Cenda', 'Cecilka']}))


if __name__ == "__main__":
    main()
