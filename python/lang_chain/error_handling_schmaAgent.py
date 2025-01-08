import mysql.connector
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Establish database connection with error handling
def execute_query(query: str, host="localhost", database="Kap", user="root", password="rootpassword"):
    try:
        connection = mysql.connector.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )
        cursor = connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        connection.close()
        return results
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []

# Define the prompt template for the LLM with error handling
prompt_template = "Generate an SQL query to fetch data from the {table_name} table."

# Initialize the language model (make sure the API key is set)
def initialize_llm(api_key: str):
    try:
        llm = OpenAI(api_key=api_key, temperature=0.7)
        return llm
    except Exception as e:
        print(f"Error initializing LLM: {e}")
        return None

# Create an LLMChain with the prompt template and error handling
def create_llm_chain(llm):
    try:
        if llm is None:
            raise ValueError("LLM initialization failed. Cannot create LLMChain.")
        prompt = PromptTemplate(input_variables=["table_name"], template=prompt_template)
        llm_chain = LLMChain(prompt=prompt, llm=llm)
        return llm_chain
    except Exception as e:
        print(f"Error creating LLMChain: {e}")
        return None

# Input table name
table_name = "F"

# Initialize the LLM
api_key = "replace your api key here" #replace your own api key
llm = initialize_llm(api_key)

# Check if LLM was initialized successfully
if llm:
    # Create LLMChain
    llm_chain = create_llm_chain(llm)
    
    # If LLMChain creation was successful
    if llm_chain:
        # Generate the SQL query using the language model
        try:
            query = llm_chain.run({"table_name": table_name})
            print(f"Generated Query: {query}")
            
            # Execute the generated query and fetch results
            results = execute_query(query)
            
            if results:
                # Print results if query execution was successful
                print(f"Results for table {table_name}:")
                for row in results:
                    print(row)
            else:
                print("No results fetched or query execution failed.")
        except Exception as e:
            print(f"Error generating or executing query: {e}")
    else:
        print("Failed to create LLMChain. Exiting.")
else:
    print("LLM initialization failed. Exiting.")
