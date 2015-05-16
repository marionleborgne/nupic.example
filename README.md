## How to Run

Make sure your CSV file is called `scalar_data.csv` and has the same headers as the file `scalar_data_template.csv`. First column should be named `timestamp` and second column should be `scalar_value`.

First, generate the model params:

    python example/generate_model_params.py

To run and output data to a local file:

    python example/run.py

To run and output data to a **matplotlib** graph:

    python example/run.py --plot

> You must have **matplotlib** properly installed for this option to work.

![Example Screenshot](https://raw.githubusercontent.com/marionleborgne/nupic.example/master/screenshot.png)

## Using your own data
* Clone the repository and replace the CSV file [scalar_data.csv](https://github.com/marionleborgne/nupic.example/blob/master/example/scalar_data.csv) with your own. 
* IMPORTANT: make sure to keep the same headers `timestamp, scalar_value`. 
* The first column needs to be *datetime* values, and the second column needs to be *scalar* values.

## More NuPIC examples

This example is a lightweight version of the NuPIC tutorial called [Hot Gym](https://github.com/numenta/nupic/tree/master/examples/opf/clients/hotgym). Check the tutorial out for more info.
