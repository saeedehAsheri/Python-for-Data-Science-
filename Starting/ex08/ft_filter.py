def ft_filter(function, iterable):
    """Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    for item in iterable:
        if function is None:
            if item:
                yield item
        elif function(item):
            yield item


def main() -> None:
    """Run no standalone tests."""
    pass


if __name__ == "__main__":
    main()