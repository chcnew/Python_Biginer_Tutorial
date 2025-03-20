# !/usr/bin/env python3
# encoding: utf-8


"""
功 能：QLabel + QLineEdit 基础组件
"""

from dataclasses import dataclass

from PySide2.QtCore import QMetaObject, QSize
from PySide2.QtWidgets import QLabel, QLineEdit

from ucmtools.base_widgets.base_widget import BaseWidget


@dataclass
class UiForm:
    """lineedit组件"""

    def __init__(self):
        self.label = None
        self.line_edit = None

    def setup_ui(self, form):
        """

        :param form: 父对象
        :return:
        """
        if not form.objectName():
            form.setObjectName(u"form")
        self.label = QLabel(form)
        self.label.setObjectName(u"label")
        self.line_edit = QLineEdit(form)
        self.line_edit.setObjectName(u"line_edit")
        self.line_edit.setMinimumSize(QSize(220, 40))
        QMetaObject.connectSlotsByName(form)


class StrWidget(BaseWidget):
    """StrWidget"""

    def __init__(self, verbose_name=None, default=None):
        """
        :param verbose_name: Label标签文本
        :param default: 默认值
        """
        self._ui = UiForm()
        super().__init__(self._ui, verbose_name, default)
