# Import necessary modules and functions
from mage_ai.data_preparation.repo_manager import get_repo_path
from mage_ai.io.bigquery import BigQuery
from mage_ai.io.config import ConfigFileLoader
from pandas import DataFrame
from os import path

# Check if 'data_exporter' is not already defined in the global scope
if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

# Define a function to export data to BigQuery using the @data_exporter decorator
@data_exporter
def export_data_to_big_query(data, **kwargs) -> None:
    """
    Template for exporting data to a BigQuery warehouse.
    Specify your configuration settings in 'io_config.yaml'.

    Docs: https://docs.mage.ai/design/data-loading#bigquery
    """
    # Get the path to the configuration file
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    # Set the configuration profile name
    config_profile = 'default'

    # Loop through the data items and export each to a BigQuery table
    for key, value in data.items():
        # Define the BigQuery table ID (replace "data-engineering.uber_data_engineering" with the actual project and table names)
        table_id = 'data-engineering.uber_data_engineering.{}'.format(key)
        # Export the data to BigQuery, replacing the table if it already exists
        BigQuery.with_config(ConfigFileLoader(config_path, config_profile)).export(
            DataFrame(value),
            table_id,
            if_exists='replace',  # Specify resolution policy if table name already exists
        )