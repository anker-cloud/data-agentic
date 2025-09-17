import os
# Identifier for the specific generative model to be used by the agent.(e.g., "gemini-2.5-pro-preview-03-25")
MODEL="gemini-2.5-pro-preview-03-25"

# The Google Cloud Project ID that contains the BigQuery datasets and tables to be analyzed.
# It is now loaded from an environment variable.
PROJECT_ID = os.environ.get("PROJECT_ID", "agentic-data")

# The geographical location of the BigQuery datasets and tables to be analyzed.
# It is now loaded from an environment variable.
LOCATION = os.environ.get("LOCATION", "asia-south1")

# The target BigQuery dataset name to be analyzed or for which data profiles are fetched.
# It is now loaded from an environment variable.
DATASET_NAME = os.environ.get("DATASET_NAME", "thelook_manufacturing")

# Optional list of specific table names within DATASET_NAME.
TABLE_NAMES=[]

# Optional: Full BigQuery table ID where data profiling results are stored.
# It is now loaded from an environment variable.
DATA_PROFILES_TABLE_FULL_ID = os.environ.get("DATA_PROFILES_TABLE_FULL_ID", "")

# The API key for the public Google AI API.
# The value is loaded from an environment variable.
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY", "")