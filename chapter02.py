import marimo

__generated_with = "0.23.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # A Crash Course in Python
    """)
    return


@app.cell
def _():
    long_winded_computation = (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 +
    13 + 14 + 15 + 16 + 17 + 18 + 19 + 20)
    print(long_winded_computation)
    return


@app.cell
def _():
    def double(x):
        return x * 2

    def apply_to_one(f):
        return f(1)

    my_double = double
    x = apply_to_one(my_double)
    x
    return (apply_to_one,)


@app.cell
def _(apply_to_one):
    y = apply_to_one(lambda x: x + 4)
    y
    return


@app.cell
def _():
    assert 1 == 2
    return


@app.cell
def _():
    def smallest_item(xs):
        return min(xs)

    assert smallest_item([10,20,40,5,30]) == 50
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
