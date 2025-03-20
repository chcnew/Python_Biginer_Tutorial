# !/usr/bin/env python3
# encoding: utf-8


"""
功 能：QLabel + QSpinBox 基础组件
"""

from dataclasses import dataclass

from PySide2.QtCore import QMetaObject, QSize
from PySide2.QtWidgets import QLabel, QSpinBox, QAbstractSpinBox

from ucmtools.base_widgets.base_widget import BaseWidget


@dataclass
class UiForm:
    """spinbox组件"""

    def __init__(self):
        self.label = None
        self.spin_box = None

    def setup_ui(self, form):
        """

        :param form: 父对象
        :return:
        """
        if not form.objectName():
            form.setObjectName(u"form")
        self.label = QLabel(form)
        self.label.setObjectName(u"label")
        self.spin_box = QSpinBox(form)
        self.spin_box.setObjectName(u"spin_box")
        self.spin_box.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spin_box.setMinimumSize(QSize(220, 40))
        self.spin_box.setToolTip(
            "Range：{} ~ {} ".format(self.spin_box.minimum(), self.spin_box.maximum()))
        QMetaObject.connectSlotsByName(form)


class IntWidget(BaseWidget):
    """IntWidget"""

    def __init__(self, verbose_name=None, default=None, drange=None):
        """
        :param verbose_name: Label标签文本
        :param default: 默认值
        """
        self._ui = UiForm()
        super().__init__(self._ui, verbose_name, default)
        self.drange = drange

    def set_range(self, value):
        """

        :param value: 范围
        :return:
        """
        self._ui.spin_box.setRange(*value)
        self._ui.spin_box.setToolTip(
            "Range：{} ~ {} ".format(self._ui.spin_box.minimum(), self._ui.spin_box.maximum()))
