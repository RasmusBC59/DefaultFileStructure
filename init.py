import qcodes as qc
from qcodes.logger import start_all_logging
start_all_logging()

qc.config['user']['mainfolder'] = '.'
qc.config['core']['db_location'] = '.'
qc.initialise_database()

config_file = 'default.yaml'
scfg = qc.Station(config_file=config_file)

qc.load_or_create_experiment(experiment_name="default",
                             sample_name="default")

qdac = scfg.load_instrument('qdac')
