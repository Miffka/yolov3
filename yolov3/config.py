import os
import os.path as osp

class Config():
    CURRENT_PATH = osp.dirname(osp.realpath(__file__))
    root_dir = osp.join(CURRENT_PATH, '..')

    data_dir = osp.join(root_dir, 'data')
    weights_dir = osp.join(root_dir, 'weights')
    config_dir = osp.join(root_dir, 'cfg')
    output_dir = osp.join(root_dir, 'output')

config = Config()
