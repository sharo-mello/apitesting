# API TESTING

# step 1: Enter your API requirements in apitesting.json
  In this step you can mention the VUs and  time you gonna hit the test. for more details on load generation pattern please refer to https://k6.io/docs/using-k6/scenarios/executors/
# step 2: Run the python file

  python runtest.py
  
You will get the performance metrics as like this 

result = {
                "samples": (refers to the number of iterations has been made),
                "iteration_duration(avg)": (Avg time taken by an iteration (ms)),
                "p90(ms)": (90% of the sample is below that value and the rest of the values (that is, the other 10%) are above it),
                "throughput": (Req/sec sent by your model) 
                "Error(%)": (Error % other than 2xx)
                "datasent(bytes)": (amount of data you sent)
                "datareceived(bytes)": (amount of data received)
            }

Learn more about API testing using K6

https://k6.io/docs/
