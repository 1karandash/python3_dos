This is a simple HTTP DoS script which continuously generates sockets and initiate connections to the target IPv4 address on port 80, sending a basic HTTP Header 
with a randomly generated spoofed IPv4 address (spoofed in application layer).

The user can choose the number of threads that he wishes to concurrently run the function which initiates the connections.
