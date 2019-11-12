# Import the logging library
import repsci

# Create an experiment
# A unique directory will be created with the experiment name, a timestamp,
# and the current git hash.
exp_name = "hello_world"
exp = repsci.Experiment(exp_name)

# Get the logger and write a log message
log = exp.get_logger()
log.debug("Hello, World!")

# Create an output file in the unique output directory
filename = exp.get_filename('output.csv')
with open(filename, "w", encoding='utf-8') as f:
    f.write("Hello, World\n")
