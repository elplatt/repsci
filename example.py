# Import the logging library
import __init__ as logbook

# Create an experiment
# A unique, timestamped output directory will be created
exp_name = "hello_world"
exp = logbook.Experiment(exp_name)

# Get the logger and write a log message
log = exp.get_logger()
log.debug("Hello, World!")

# Create an output file in the unique output directory
filename = exp.get_filename('output.csv')
with open(filename, "wb") as f:
    f.write("Hello, World\n")
