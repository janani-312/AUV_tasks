    • For this question, the publisher node gives “Multiples of 2”. it continually outputs multiples of 2. it will send Int32 messages on a topic like /numbers.
    • The subscriber node acts like a processor, which means taking input and modifying it. It subscribes to /numbers,multiplies each number by 10 and then publishes the result on a new topic (/processed)
    • The second Subscriber Node does the “+5 and print” operation.  It listens to /processed ,adds 5 Prints the result. Here, we don’t publish further because this is the end of the processing chain.
