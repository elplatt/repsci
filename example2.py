# Import the logging library
import repsci

# Create a config
import configparser
config = configparser.ConfigParser()
config['DEFAULT'] = {
    'message': 'Hello, World!'
}

# Create an experiment
exp_name = "hello_config"
exp = repsci.Experiment(exp_name, config=config)

# Get the logger and write a log message
log = exp.get_logger()
log.info(config['DEFAULT']['message'])

# Create an output file in the unique output directory
filename = exp.get_filename('output.csv')
with open(filename, "w") as f:
    f.write(config['DEFAULT']['message'] + '\n')
