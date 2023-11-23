from parser.strategies.en_collector_ import EnCollector
from parser.strategies.xiaoshuo import XiaoShuo
from .en_stepper import EnStepper
from .wfxs_strategy_ import Wfxs
from .wx256_strategy import Wx256
from .zh_82zg_strategy import Zg
from .zh_shuka import ChiShuka


def strategy_class(class_name, *args, **kwargs):
    classes = {
        'EnStepper': EnStepper,
        'Wfxs': Wfxs,
        'Wx256': Wx256,
        'Zg': Zg,
        'ChiShuka': ChiShuka,
        'XiaoShuo': XiaoShuo,
        'EnCollector': EnCollector
    }
    cls = classes[class_name]
    return cls(*args, **kwargs)
