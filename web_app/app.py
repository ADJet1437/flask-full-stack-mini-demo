from datetime import datetime

from flask import Flask, render_template, request

from web_app.lib.general import format_calculation_result, get_time_consumed
from web_app.models.ackermann import ackermann
from web_app.models.factorial import factorial
import web_app.models.fibonacci as fib

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/fibonacci')
def fibonacci_service():
    """Accept value n from user and provide fib
    function calculation result.

    :return:
    """
    start_time = datetime.now()
    n = request.args.get('fib_input', None)
    # for initializing
    if not n :
        return render_template("fibonacci.html")
    result = fib.general_formula(int(n))
    # do not show time if no result
    if not result:
        return render_template("fibonacci.html")

    time_consumed = get_time_consumed(start_time)
    return render_template("fibonacci.html", result=result, time_consumed=time_consumed)


@app.route('/ackermann')
def ackermann_service():
    """Accept value m, n provided by user, calculate ackermann
    function result and provide calculation time.

    :return:
    """
    start_time = datetime.now()
    m = request.args.get('ack_input_m')
    n = request.args.get('ack_input_n')

    if not (m and n):
        return render_template("ackermann.html")

    result = ackermann(int(m), int(n))
    time_consumed = get_time_consumed(start_time)

    return render_template("ackermann.html", result=result, time_consumed=time_consumed)


@app.route('/factorial')
def factorial_service():
    """Accept value n provided by user, calculate factorial
    function result and provide calculation time.

    :return:
    """
    start_time = datetime.now()
    n = request.args.get('fac_input_n')
    if not n:
        return render_template("factorial.html")
    result = factorial(int(n))
    result = format_calculation_result(result)


    time_consumed = get_time_consumed(start_time)

    return render_template("factorial.html", result=result, time_consumed=time_consumed)


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
