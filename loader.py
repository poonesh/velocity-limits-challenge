import json
from client import Client

def loader(filename):
	"""
	"""
    clients = {}

    with open(filename) as f:
        data = f.readlines()
        for i in range(2):
            load_data = json.loads(data[i])
            load_id = load_data["id"]
            customer_id = load_data["customer_id"]
            load_amount = load_data["load_amount"]
            date, time = load_data["time"][0:10], load_data["time"][11:19]
            print date, time

            if customer_id not in clients:
                client = Client(customer_id)
                clients[customer_id] = client
            print clients
#             A = clients[customer_id].daily_load_exceeded(load_amount, time)
#             B = clients[customer_id].weekly_load_exceeded(load_amount, time)
#             C = clients[customer_id].max_num_load_daily(load_amount, time)

#             if(A and B and C):
#                 print True
#             print False


if __name__ == '__main__':
	loader('./KOHO/input.txt')