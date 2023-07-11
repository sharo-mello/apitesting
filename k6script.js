import http from 'k6/http';
import { check } from "k6";
import { Rate } from "k6/metrics";
const inputdata = JSON.parse(open('input.json'));

var api = inputdata['api'];
var req_method = inputdata['reqmethod'];
var req_headers = { headers: (inputdata['reqheaders']) };
var req_payload = JSON.stringify(inputdata['reqpayload']);
var api_name = inputdata['apiname'];

var errors = new Rate("errors");

export const options = {
    scenarios: {
        [api_name]: {
            //pls see "https://k6.io/docs/using-k6/scenarios/executors/" for more info . .
            //give the way of execution you want
            executor: "ramping-vus",
            stages: [
                { duration: '10s', target: 1 },
                // { duration: '20s', target: 20 },
                // { duration: '10s', target: 0 },
            ],
        }
    }


};


export default function () {

    if (req_method == "get") {
        var response = http.get(api, req_headers);
    }
    else if (req_method == "post") {
        var response = http.post(api, req_payload, req_headers);
    }
    // console.log(response.status_text)
    // console.log(api, req_payload, req_headers)
    let checkRes = check(response, {
        "response code was 200": (res) => res.status == 200,
        "response code was 400": (res) => res.status == 400,
    }

    )
    errors.add(!check(response, { "response is 200": (r) => r.status === 200 }));


}
