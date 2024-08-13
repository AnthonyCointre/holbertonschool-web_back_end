0-basic_async_syntax.py = An asynchronous coroutine that takes in an integer argument named wait_random that waits for a random delay between 0 and max_delay seconds and eventually returns it.

1-concurrent_coroutines.py = An async routine called wait_n that takes in 2 int arguments: n and max_delay. You will spawn wait_random n times with the specified max_delay.

2-measure_runtime.py = A measure_time function with integers n and max_delay as arguments that measures the total execution time for wait_n, and returns total_time / n.

3-tasks.py = A function task_wait_random that takes an integer max_delay and returns a asyncio.Task.

4-tasks.py = Take the code from wait_n and alter it into a new function task_wait_n.
