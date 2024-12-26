# constants.py

C_PORT = 8888


class Node_Config:
    def __init__(self):
        self.NODE_PORT = 8881
        self.NUMBER_OF_NODES_ACTIVATED = 0


node_config_instance= Node_Config()


def load_config():
    # Load the last configuration from a file
    try:
        with open("config.txt", "r") as file:
            lines = file.readlines()
            if lines:
                # Use the last line to get the latest configuration
                last_line = lines[-1]
                (
                    node_config_instance.NODE_PORT,
                    node_config_instance.NUMBER_OF_NODES_ACTIVATED,
                ) = map(int, last_line.split())
    except FileNotFoundError:
        pass


def save_current_config():
    with open("config.txt", "a") as file:
        file.write(
            f"{node_config_instance.NODE_PORT} {node_config_instance.NUMBER_OF_NODES_ACTIVATED}\n"
        )


load_config()  # Load the configuration when the module is imported


def get_node_details():
    load_config()  # Load the latest configuration before updating
    node_config_instance.NODE_PORT += 1
    node_config_instance.NUMBER_OF_NODES_ACTIVATED += 1
    save_current_config()  # Save the updated configuration
    return node_config_instance.NODE_PORT, node_config_instance.NUMBER_OF_NODES_ACTIVATED


def get_all_nodes():
    try:
        with open("config.txt", "r") as file:
            Node_Config = [tuple(map(int, line.split())) for line in file]
        return Node_Config
    except FileNotFoundError:
        return []
