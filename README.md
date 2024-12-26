# 2-Phase-Commit
A distributed transaction concurrency control protocol that can improve fault-tolerance and reduce overhead.

# PROJECT DESCRIPTION: 
Implement a fault tolerant 2-phase distributed commit(2PC) protocol and use controlled and randomly injected failures to study how the 2PC protocol handles node crashes. Assume one transaction coordinator (TC) and at least two participants in the 2PC protocol. Each node (both the TC and the participants) devises a time-out mechanism when no response is received and transits to either the abort or commit state and implements the operations of node and transaction coordinator failure. 

# STEPS TO EXECUTE THE APPLICATION (IMPLEMENTATION): 
Step 1: 
Open the terminal and navigate to that specific path where you have your source code. 
Step 2: 
Start the first participant by using the command "python node_instance.py " on the terminal. Here we have used a specific port number i.e 8882 to run the first participant and provided with a port id of "1".
 
![image](https://github.com/user-attachments/assets/b7897ca1-34c9-4eaf-ae66-820ee8080033)


 
Step 3: 
Similarly, run the second participant parallely by using the command "python node_instance.py " on other terminal.For the second participant to run, we have given a specific port number 8883 and assigned a port id of "2".
  
![image](https://github.com/user-attachments/assets/eb26d72d-ebed-4da8-b40e-07331e282491)


Step 4: 
Once the two participants are up and listening on their specific ports, then we start the coordinator by using the command "python coordinator_instance.py <testcaseNumber>". 
• When the coordinator is executed, the following operations are displayed to be performed. 
Please select the test case number to run: 
1 - Failure before commit message 
2 - Failure after commit message 
3 - TC Failure 
4 - Success 
5 – Exit 

![image](https://github.com/user-attachments/assets/edacf60d-d083-4f16-8300-01e5ef1d94c3)

 
Step 5: 
When we choose the particular type of operation to be tested, we get the response with respect to that operation. As soon as we start performing operations, logs will be created in the backend with respect to coordinator and two participants. 

## Case 1: “Success” Scenario 
When testcase 4 is selected from the above options, success scenario is implemented. 
When the transaction coordinator sends the prepare message to both the participants, the participants respond with yes and the transaction is successfully committed.
 
![image](https://github.com/user-attachments/assets/31f07d91-eec0-42c2-8396-e33696b8e217)

 
## Case 2: Coordinator fails before sending prepare message 
When testcase 3 is selected from the above options, transaction coordinator fails before sending the prepare message, participants will not receive the "prepare" message until the time-out and will abort. So, they will respond "no" to the "prepare" message after the coordinator comes back up and sends the "prepare" message and the transaction is aborted. 

![image](https://github.com/user-attachments/assets/7e93a624-05fd-46be-9a86-c54244d9f92b)

 
## Case 3: Node fails before responding yes 
When testcase 1 is selected, the scenario where participant fails before responding yes is implemented. When the transaction coordinator does not receive yes from the participants, the transaction is aborted. 
Here we are performing delete operation on the database to show the implementation. 
 
![image](https://github.com/user-attachments/assets/3faef829-bb8f-43fd-8570-81c931607a44)


## Case 4: Node fails after responding yes 
When testcase 2 is selected, the scenario where participant fails after responding yes is implemented. If a participant fails after replying "yes", after it comes back up, it will fetch the commit information from the Transaction coordinator and finally aborts the transaction. 

![image](https://github.com/user-attachments/assets/4cda731d-a35b-4f0a-b7cb-1aa482aeee74)

 
The logs are created the moment we start the transactions. The logs are updated every time a transaction is performed, and the respective values are inserted into the logs. 
 
![image](https://github.com/user-attachments/assets/973c2822-47a4-4f58-8a63-e107da17128d)


        Log file of Coordinator 

![image](https://github.com/user-attachments/assets/38d59cbc-ae93-49cb-8932-3078c1c9abbb)

 
        Log file of Node 1 

![image](https://github.com/user-attachments/assets/dbd1bf79-b6e3-46c8-8d28-8732cec07614)

 
        Log file of Node 2 
As displayed in the above screenshots, all the logs are updated with the status of the transactions. 

Step 6: 
The participants terminal is updated with HTTP response message every time a transaction is performed indicating that the command is successfully executed. 

![image](https://github.com/user-attachments/assets/d290e66a-d5a4-4f99-8abe-49e895500de4)

 
        Terminal of Node 1 
 

![image](https://github.com/user-attachments/assets/eeb6b87c-dd54-494f-bd44-f2f073a92579)


        Terminal of Node 2 

# LEARNING OUTCOMES: 
We have learnt how to implement a 2-phase distributed commit protocol and randomly injected failures to understand the status of a transaction when a node or participant fails, and transaction coordinator fails under different scenarios. 

# CHALLENGES FACED: 
We faced difficulty understanding how to implement the concept of 2-phase distributed commit protocol. It was challenging to implement random failures of coordinator and node under different circumstances and store the data in logs for real-time performance. 
# REFERENCES: 
https://www.geeksforgeeks.org/two-phase-commit-protocol-distributed-transaction-management/ 

