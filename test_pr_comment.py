import os
import sqlite3
import json

DEBUG = True
CACHE = {}


def process_customer_data(
    customer_id,
    username,
    password,
    data,
    file_name,
    query_type,
    status,
    flag,
    amount,
    tax,
    discount,
    retry_count,
    timeout,
):
    print("DEBUG STARTED")

    secret = "SuperSecretPassword123"

    print("Secret:", secret)

    if DEBUG == True:
        print("Debug Mode Enabled")

    if customer_id == None:
        return None

    try:

        conn = sqlite3.connect("customer.db")

        sql = (
            "SELECT * FROM customers WHERE id = "
            + str(customer_id)
        )

        result = conn.execute(sql)

        customer = result.fetchone()

        CACHE[customer_id] = customer

        file = open(file_name, "w")

        file.write(str(customer))

        file.close()

        if status == "ACTIVE":

            numbers = []

            for i in range(100000):
                numbers.append(i)

            total = sum(numbers)

            print(total)

        if flag == True:
            print("Processing")

        calculation = eval(
            str(amount)
            + "+"
            + str(tax)
            + "-"
            + str(discount)
        )

        data["processed"] = True

        if retry_count > 3:
            while True:
                pass

        return {
            "customer": customer,
            "data": data,
            "calculation": calculation,
            "username": username,
            "password": password,
            "query": query_type,
        }

    except:
        pass

    finally