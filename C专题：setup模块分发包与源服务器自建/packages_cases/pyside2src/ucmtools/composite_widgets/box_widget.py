# !/usr/bin/env python3
# encoding: utf-8


"""
功 能：基于基础组件实现按形状显示的复合组件
"""

from PySide2.QtWidgets import QButtonGroup

import ucmtools as models
from ucmtools.composite_widgets.composite_widget import CompositeWidget


class BoxWidget(CompositeWidget):
    """
    Box复合组件
    """

    def __init__(self, base=models.StrWidget, shape=None, verbose_name=None, titles=None, choices=None, default=None,
                 dranges=None, group_tf=False, multiselect=False, button_text=None):
        """
        :param base: 基础组件
        :param shape:  形状设置
        :param verbose_name: 标签
        :param titles: 设置标题文本
        :param choices: 设置选项文本
        :param default: 设置默认值
        :param dranges: 设置QSpinxBox、DoubleSpinBox组件的范围
        :param group_tf: 是否分组（布尔值）
        :param multiselect: 多选是否开启
        :return:
        """
        self.multiselect = multiselect
        super().__init__(base, shape, verbose_name, titles, choices, default, dranges, group_tf, button_text)

    def register(self, target):
        super().register(target)
        if self.choices and self.base.__name__ in ["RadioWidget", "BoolWidget"]:
            # 清空不涉及属性
            self.dranges = None
            self.button_text = None
            # 关闭多选
            if not self.multiselect:
                btn_group = QButtonGroup(self.target)
                for base_widget in self._widget_list:
                    btn_group.addButton(base_widget.ret_inbox_obj)

        if self.base.__name__ == "ComboBoxWidget":
            # 清空不涉及属性
            self.default = None
            self.dranges = None
            self.multiselect = None
            self.button_text = None

        if self.base.__name__ in ["IntWidget", "DoubleWidget", "StrWidget"]:
            # 清空不涉及属性
            self.choices = None
            self.multiselect = None
            self.button_text = None

        if self.base.__name__ == "StrWidget":
            # 清空不涉及属性
            self.dranges = None
            self.multiselect = None
            self.button_text = None
