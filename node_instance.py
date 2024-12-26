import os
from xmlrpc.server import SimpleXMLRPCServer
from classes.Node import Node
from constants import get_node_details


def create_log_dir(node_identifier):
    log_dir_path = f"node_logs_directory/node_instance{node_identifier}"
    os.makedirs(log_dir_path, exist_ok=True)
    return log_dir_path


def initiate_node_server(port, node_identifier):
    rpc_server = SimpleXMLRPCServer(("localhost", port))
    print(f"Node is listening on port {port} with port id {str(node_identifier)}")
    node_instance = Node(create_log_dir(node_identifier), port)
    rpc_server.register_instance(node_instance)
    rpc_server.serve_forever()


def main():
    try:
        node_port, node_id = get_node_details()
        initiate_node_server(node_port, node_id)
    except Exception as error:
        print(error.args)


if __name__ == "__main__":
    main()
