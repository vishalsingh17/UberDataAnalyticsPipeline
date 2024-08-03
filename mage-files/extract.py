# Import necessary modules
import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

# Define a data loader function with the @data_loader decorator
@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from an API
    """
    # Define the URL of the CSV file
    url = 'https://storage.googleapis.com/uber-data-engineering-project/uber_data.csv'
    # Send a GET request to the URL
    response = requests.get(url)

    # Load the CSV data into a pandas DataFrame and return it
    return pd.read_csv(io.StringIO(response.text), sep=',')

# Define a test function with the @test decorator
@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    # Assert that the output is not None
    assert output is not None, 'The output is undefined'
