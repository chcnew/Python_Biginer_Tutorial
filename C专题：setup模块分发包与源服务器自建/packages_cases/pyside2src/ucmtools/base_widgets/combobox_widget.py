# !/usr/bin/env python3
# encoding: utf-8


"""
功 能：QLabel + QComboBox 基础组件
"""

from dataclasses import dataclass

from PySide2.QtCore import QMetaObject, QSize
from PySide2.QtWidgets import QLabel, QComboBox

from ucmtools.base_widgets.base_widget import BaseWidget


@dataclass
class UiForm:
    """combobox组件"""

    def __init__(self):
        self.label = None
        self.combo_box = None

    def setup_ui(self, form):
        """

        :param form: 父对象
        :return:
        """
        if not form.objectName():
            form.setObjectName(u"form")
        self.label = QLabel(form)
        self.label.setObjectName(u"label")
        self.combo_box = QComboBox(form)
        self.combo_box.setObjectName(u"combo_box")
        self.combo_box.setMinimumSize(QSize(220, 40))
        QMetaObject.connectSlotsByName(form)


class ComboBoxWidget(BaseWidget):
    """ComboBox基础组件"""

    def __init__(self, verbose_name=None, choices=None):
        """
        :param verbose_name: Label标签文本
        :param choices: 选项设置：类型 - str or list
        """
        self._ui = UiForm()
        super().__init__(self._ui, verbose_name, None, choices)

    def set_inbox_value(self, value: int or str or bool):
        """
        ComboBox组件设置选项：先清空再设置值,实现添加使用set_inbox_attr()函数

        value参数形式

        ::

            末尾添加一个 传参形式1："x"
            列表添加多个 传参形式2：["x", "y", "z"]

        :param value: 设置选项参数

        :return:
        """
        if value is None:
            return

        self._ui.combo_box.clear()

        if isinstance(value, str):
            self._ui.combo_box.addItem(value)
        elif isinstance(value, (list, tuple)):
            self._ui.combo_box.addItems(value)
        else:
            raise TypeError("The parameter is incorrect.")
