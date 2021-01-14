"""
This is an average currency exchange rate over the selected time
Required following inputs from user
    - Start date <User select on calendar, the selected date will be shown as "red">
    - End date <User select on calendar, the selected date will be shown as "red">
    - Amount of money (domestic currency)
Output from this application:
    - Average exchange rate from 'start date' to 'end date'
Error exception:
    - ValueError -> amount of money must be a number
    - DateSelectionError -> 'start date' must be before 'end date'

Algorithm:
    - Get List of Supported Currency codes from forex-python
    - Create 2 dropdown items for domestic and foreign currency
    - Get selected currency from user
    - Get amount of money you need to convert
    - Calculate average exchange rate over the selected date
"""
from forex_python.converter import CurrencyRates
from forex_python.converter import CurrencyCodes
from tkinter import *
import sys
from tkcalendar import Calendar
from datetime import *


class CustomizeError(Exception):
    """Base class for exceptions in this module."""
    pass


class DateSelectionError(CustomizeError):
    """ DateSelectionError is a customized Exception """


def prepare_currency_data():
    """ Prepare currency data for showing in the dropdown list
        by following steps:
        1. Call get_rates() by USD, the output will be dictionary
        2. Collect all keys into currency_list
        3. Collect currency name by using keys in currency_list
        4. return result
        :return currency list as dictionary
    """
    # declare a returned parameter
    curr_list = {}

    # Prepare data: step 1
    cr = CurrencyRates()
    exchange_rate = cr.get_rates('USD')

    # Prepare data: step 2
    currency_code = list(exchange_rate.keys())
    currency_code.append("USD")

    # Prepare data: step 3
    cc = CurrencyCodes()
    for code in currency_code:
        curr_list[str(code)] = code + " - " + cc.get_currency_name(str(code))

    # Prepare data: step 4
    return curr_list


def show_result(text_result):
    out_result_lb.config(text=text_result, font=(None, 14), fg="blue")


def option_menu_selected(event):
    bc = base_currency_str.get()[:3]
    dc = dest_currency_str.get()[:3]
    in_money_lb.config(text="Domestic Currency Unit: ("+bc+"):")
    out_money_lb.config(text="Average exchange rate ("+dc+"):")


def cal_avg_exchange(base, dest, amount, st_date, en_date):
    """ This function call API and calculate average exchange rate """
    running_date = datetime(st_date.year, st_date.month, st_date.day, 0, 0, 0, 0)
    last_date = datetime(en_date.year, en_date.month, en_date.day, 0, 0, 0, 0)
    time_delta = timedelta(days=1)
    exch_rate_sum = 0.0

    while running_date <= last_date:
        # Do get exchange rate a day
        cr = CurrencyRates()
        temp = cr.convert(base, dest, amount, running_date)
        print(running_date.strftime("%Y/%m/%d"), "rate", temp)
        exch_rate_sum += temp
        running_date += time_delta

    avg = exch_rate_sum/((en_date - st_date).days + 1)
    return avg


def convert_button_clicked():
    err_amount_lb.config(text="")
    base_currency = base_currency_str.get()[:3]
    dest_currency = dest_currency_str.get()[:3]
    try:
        amount = float(money_entry.get())
        st_date = start_date.selection_get()
        en_date = end_date.selection_get()
        if en_date < st_date:
            raise DateSelectionError()
        avg_rate = cal_avg_exchange(base_currency, dest_currency, amount, st_date, en_date)
        show_result(str(avg_rate))
    except ValueError:
        err_amount_lb.config(text="ValueError: Amount must be a number", fg="red")
    except DateSelectionError:
        err_amount_lb.config(text="DateSelectionError: Start date must be before end date!", fg="red")
    else:
        err_amount_lb.config(text="Unexpected!! " + str(sys.exc_info()), fg="red")


currency_list = prepare_currency_data()
print(currency_list.values())

main_window = Tk()
main_window.title("Average exchange rate calculator")
current_row = 0

select_date_lb = Label(main_window,
                       text="Select date",
                       font=(None, 18),
                       anchor="n")
select_date_lb.grid(row=current_row, column=0)

current_row = current_row + 1

start_date_lb = Label(main_window,
                      text="From: ",
                      font=(None, 18),
                      anchor="n")
start_date_lb.grid(row=current_row, column=0)

start_date = Calendar(main_window,
                      selectmode="day",
                      selectforeground="red",
                      foreground="blue",
                      background="gray",
                      headersforeground="black",
                      showweeknumbers=False)
start_date.config(maxdate=start_date.datetime.now())
start_date.grid(row=current_row, column=1)

end_date_lb = Label(main_window,
                    text="To: ",
                    font=(None, 18),
                    anchor="n")
end_date_lb.grid(row=current_row, column=2)

end_date = Calendar(main_window,
                    selectmode="day",
                    selectforeground="red",
                    foreground="blue",
                    background="gray",
                    headersforeground="black",
                    showweeknumbers=False)
end_date.config(maxdate=end_date.datetime.now())
end_date.grid(row=current_row, column=3)

current_row = current_row + 1

base_currency_str = StringVar(main_window)
base_currency_str.set(currency_list["USD"])

select_currency_lb = Label(main_window,
                           text="Select currency",
                           font=(None, 18),
                           anchor="w"
                           )
select_currency_lb.grid(row=current_row, column=0)

current_row = current_row + 1

base_currency_lb = Label(main_window, text="Domestic Currency:")
base_currency_lb.grid(row=current_row, column=0)

base_currency_dropdown = OptionMenu(main_window,
                                    base_currency_str,
                                    *currency_list.values(),
                                    command=option_menu_selected)
base_currency_dropdown.config(width=30)
base_currency_dropdown.grid(row=current_row, column=1)

dest_currency_str = StringVar(main_window)
dest_currency_str.set(currency_list["THB"])

dest_currency_lb = Label(main_window, text="Foreign Currency:")
dest_currency_lb.grid(row=current_row, column=2)

dest_currency_dropdown = OptionMenu(main_window,
                                    dest_currency_str,
                                    *currency_list.values(),
                                    command=option_menu_selected)
dest_currency_dropdown.config(width=30)
dest_currency_dropdown.grid(row=current_row, column=3)

current_row = current_row + 1

# input field number
in_money_lb = Label(main_window,
                    text="Domestic Currency Unit: ("+base_currency_str.get()[:3]+"):")
in_money_lb.grid(row=current_row, column=0)
money_entry = Entry(main_window, width=30)
money_entry.grid(row=current_row, column=1)

button = Button(main_window,
                text="Avg. exchange rate",
                width=15,
                highlightbackground="cyan",
                command=convert_button_clicked)
button.grid(row=current_row, column=2)

current_row = current_row + 1

err_amount_lb = Label(main_window, text="")
err_amount_lb.grid(row=current_row, column=1)

current_row = current_row + 1

# output foreign currency
out_money_lb = Label(main_window,
                     text="Average exchange rate ("+dest_currency_str.get()[:3]+"):")
out_money_lb.grid(row=current_row, column=0)
out_result_lb = Label(main_window, text="")
out_result_lb.grid(row=current_row, column=1)

main_window.mainloop()
