# repsci.py version 1.1.0
# Copyright 2016-2019, Edward L. Platt
# Distributed under BSD 3-Clause License
# See LICENSE for details

import configparser
import datetime
import errno
import logging
import random
import subprocess
import os.path
import pickle
import time

class Experiment(object):
    def __init__(
            self,
            exp_name,
            output_dir="output",
            suffix="",
            config=None,
            note=None,
            reproduce=None):
        # Set fields
        self.exp_name = exp_name
        self.output_dir = output_dir
        if reproduce is not None:
            self.exp_dir = os.path.join(
                self.output_dir,
                self.exp_name,
                reproduce)
            config_path = os.path.join(self.exp_dir, 'config.ini')
            self.config = configparser.ConfigParser()
            self.config.read(config_path)
            # Load previous RNG state
            rng_path = os.path.join(self.exp_dir, 'random_state.bin')
            with open(rng_path, 'rb') as f:
                random.setstate(pickle.load(f))
            
        else:
            start_ts = time.time()
            start_dt = datetime.datetime.fromtimestamp(start_ts)
            self.start_time = start_dt.strftime('%Y-%m-%d %H%M%S')
            self.git_hash = subprocess.getoutput(
                'git rev-parse HEAD').strip()
            self.git_short = subprocess.getoutput(
                'git rev-parse --short HEAD').strip()
            if len(suffix) > 0:
                self.suffix = " " + suffix
            else:
                self.suffix = ""
            self.config = config
            # Create output directory
            self.exp_dir = os.path.join(
                self.output_dir,
                self.exp_name,
                "{} {}{}".format(
                    self.start_time,
                    self.git_short,
                    self.suffix))
            self.create_output_dir()
            # Add copy of config to output directory
            if config is not None:
                config_path = os.path.join(self.exp_dir, 'config.ini')
                with open(config_path, 'w') as f:
                    config.write(f)
            # Add random number generator state
            rng_path = os.path.join(self.exp_dir, 'random_state.bin')
            with open(rng_path, 'wb') as f:
                pickle.dump(random.getstate(), f)
            # Write note to file
            if note is not None:
                note_path = os.path.join(self.exp_dir, 'note.txt')
                with open(note_path, 'w') as f:
                    f.write(note)
        
    def get_output_dir(self):
        return self.exp_dir
    
    def create_output_dir(self):
        try:
            os.makedirs(self.exp_dir)
        except OSError as exc:  # Python >2.5
            if exc.errno == errno.EEXIST and os.path.isdir(self.exp_dir):
                pass
            else:
                raise

    def get_logger(self, level=logging.INFO):
        path = self.get_output_dir()
        log_file = os.path.join(path, "%s.log" % self.exp_name)
        log = logging.getLogger(self.exp_name)
        log.propagate = False
        log.handlers = []
        handler = logging.FileHandler(log_file, "w")
        formatter = logging.Formatter('%(asctime)s\t%(message)s')
        handler.setFormatter(formatter)
        log.addHandler(handler)
        log.setLevel(level)
        return log
    
    def get_filename(self, basename):
        path = self.get_output_dir()
        return os.path.join(path, basename)
    
    def get_config(self):
        return self.config
    

