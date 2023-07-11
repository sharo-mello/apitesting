import subprocess
import json
import os

directory = os.getcwd()


def run():
    k6script = directory + "\k6script.js"
    summary_file = "summaryfile.json"
    process = subprocess.Popen('k6 run  \"{0}\" --summary-export=\"{1}\"'.format(k6script, summary_file),
                               stdout=subprocess.PIPE,
                               universal_newlines=True,
                               encoding='utf-8',
                               shell=True)
    while True:
        output = process.stdout.readline()
        print(output.strip())
        return_code = process.poll()
        if return_code is not None:
            for output in process.stdout.readlines():
                print(output.strip())
            break

    with open(summary_file, 'r') as outputfile:
        output = json.load(outputfile)
        try:
            result = {
                "samples": output['metrics']['iterations']['count'],
                "iteration_duration(avg)": output['metrics']['iteration_duration']['avg'],
                "p90(ms)": output['metrics']['iteration_duration']['p(90)'],
                "throughput/sec": output['metrics']['iterations']['rate'],
                "Error(%)": (((output['metrics']['errors']['passes']) / (
                output['metrics']['http_reqs']['count'])) * 100),
                "datasent(bytes)": output['metrics']['data_sent']['rate'],
                "datareceived(bytes)": output['metrics']['data_received']['rate']
            }
            print(result)
        except Exception as e:
            print(e)
    os.remove(summary_file)


if __name__ == "__main__":
    run()
