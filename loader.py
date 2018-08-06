import json
from client import Client

def loader(filename):
    """
    Reads the input file and register the loads based on the criteria.
    """
    clients = {}
    customer_load_ids = {}
    output = open('result.txt', 'w')
    with open(filename) as f:
        data = f.readlines()
        for i in range(len(data)):
            load_data = json.loads(data[i])
            load_id = load_data["id"]
            customer_id = load_data["customer_id"]
            load_amount = float(load_data["load_amount"][1::])
            load_date = load_data["time"][0:10]
            if customer_id not in customer_load_ids:
                customer_load_ids[customer_id] = set()
            
            dic = {}
            # ensure this is not a duplicate load_id for the same customer
            if load_id not in customer_load_ids[customer_id]:
                customer_load_ids[customer_id].add(load_id)
                if customer_id not in clients:
                    client = Client(customer_id)
                    clients[customer_id] = client
                else:
                    client = clients[customer_id]
                
                if client.load(load_amount, load_date):
                    dic["accepted"] = True
                    
                else:
                    dic["accepted"] = False
                dic["id"] = load_id
                dic["customer_id"] = customer_id
                if i == len(data)-1:
                    output.write(json.dumps(dic))
                else:
                    output.write(json.dumps(dic)+'\n')
    
    output.close()

if __name__ == '__main__':
	loader('./Challenge/input.txt')