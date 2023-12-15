from reactpy import component, hooks, html, utils, web
from collections import namedtuple
import locale

locale.setlocale(locale.LC_ALL, '')

products = [{'emoji':'🍦','name':'ice cream','price':5},
            {'emoji':'🍩','name':'donuts','price':2.5},
            {'emoji':'🍉','name':'watermelon','price':4}]

@component  
def Product():
    #cart, set_cart = hooks.use_state([])

    action = namedtuple("action", ["product","type"])
    def cartReducer(state, action): 
        if action.type == "add":
            new_state = state + [action.product]
            return new_state
        elif action.type == "remove":
            try:
                i = state.index(action.product)
            except:
                return state
            new_state = state[:i] + state[i + 1:]
            return new_state
        else:
            return state

    [cart, set_cart] = hooks.use_reducer(cartReducer, [])

    def add_button(product):
        def handle_add(event):
            set_cart(action(product=product,type='add'))

        return html.button({'onClick':handle_add}, "Add")

    def remove_button(product):
        def handle_remove(event):
            set_cart(action(product=product,type='remove'))

        return html.button({'onClick':handle_remove}, "Remove")


    def getTotal(cart):
        total = 0
        for item in cart:
            total = total + item['price']
        return locale.currency(total, grouping=True)

    def product_divs():
        return [html.div(
                html.div({'key':product['name'], 'class_name': 'product'},
                    html.span({'role':'img','aria-label':product['name']},product['emoji']),
                ),
                add_button(product),
                remove_button(product),
                ) for product in products]

    return html.div(
        {'class_name': 'wrapper'},
        html.div("Shopping Cart: " + str(len(cart)) + " total items."),
        html.div("Total: " +getTotal(cart)),
        html.div(
            product_divs(),
        ),
    )