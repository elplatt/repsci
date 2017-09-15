Import the logging library.

    import logbook

Create an experiment. A unique directory will be created with the experiment
name, a timestamp, and the current git hash.

    exp_name = "hello_world"
    exp = logbook.Experiment(exp_name)

Get the logger and write a log message.

    log = exp.get_logger()
    log.debug("Hello, World!")

Create an output file in the unique output directory.

    filename = exp.get_filename('output.csv')
    with open(filename, "wb") as f:
        f.write("Hello, World\n")
        
The Experiment constructor also has some optional parameters:
* `output_dir`: the subdirectory of the current directory to place experiment directories in.
* `suffix`: a string to append to the end of the trial's directory.
