import csv
import json
import os
import pickle
import xml.etree.ElementTree as ET

from pipeline.stages import run_stages


def execute(config):
    return run_stages(config)
