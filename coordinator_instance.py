import argparse
import os.path
import sys
import xmlrpc.client
from classes.Coordinator import Coordinator
from constants import C_PORT, get_all_nodes


if __name__ == "__main__":
    if len(sys.argv) == 2:
        testcase_number = int(sys.argv[1])
        logs_dir = "coordinator_logs_directory"
        os.makedirs(logs_dir, exist_ok=True)
        c_instance = Coordinator(
            os.path.join(logs_dir, "coordinator_logs")
        )
        node_urls = [f"http://localhost:{port}" for port, _ in get_all_nodes()]

        print("Nodes Are Running On :", node_urls)
        print("Connecting to Nodes: ")
        for node_endpoint in node_urls:
            try:
                node_proxy = xmlrpc.client.ServerProxy(node_endpoint)
                c_instance.node_connections.append(node_proxy)
            except Exception as connection_error:
                print("  Invalid node: " + connection_error)

        testcase_descriptions = {
            1: "Failure before commit message",
            2: "Failure after commit message",
            3: "TC Failure",
            4: "Success",
        }
        testcase_details = {
            1: "1",
            2: "Test 2",
            3: "Test 3",
            4: "Test 4",
        }

        if testcase_number in testcase_descriptions:
            print(testcase_descriptions[testcase_number] + ": ")
            if testcase_number == 1:
                c_instance.remove("1")
            else:
                c_instance.insert_data(
                    str(testcase_number), testcase_details[testcase_number]
                )
                print("Completed")
            print("\n")
        else:
            exit(0)

    else:
        print("Please Follow the below format : ")
        print("python coordinator.py <test-scenario-number> : ")
        print("\nAvailable test scenarios: ")
        print("  1 - Failure before commit message")
        print("  2 - Failure after commit message")
        print("  3 - Coordinator Failure")
        print("  4 - Success")
        print("  5 - Exit\n")
        exit(0)
