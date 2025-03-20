# !/usr/bin/env python3
# encoding: utf-8


"""
功 能：QLabel + QRadioButton 基础组件
"""

from dataclasses import dataclass

from PySide2.QtCore import QMetaObject
from PySide2.QtWidgets import QLabel, QRadioButton

from ucmtools.base_widgets.bool_widget import BaseWidget


@dataclass
class UiForm:
    """radiobutton组件"""

    def __init__(self):
        self.form = None
        self.label = None
        self.radio_button = None

    def setup_ui(self, form):
        """

        :param form: 父对象
        :return:
        """
        if not form.objectName():
            form.setObjectName(u"form")
        self.form = form
        self.label = QLabel(form)
        self.label.setObjectName(u"label")
        self.radio_button = QRadioButton(form)
        self.radio_button.setObjectName(u"radio_button")
        QMetaObject.connectSlotsByName(form)


class RadioWidget(BaseWidget):
    """RadioWidget"""

    def __init__(self, default=None, content=None):
        """
        :param default: 默认值 True Or False
        :param content: 选项文本内容
        """
        self._ui = UiForm()
        super().__init__(self._ui, None, default, content)

    @property
    def ret_inbox_obj(self):
        """返回单选按钮对象"""
        return self._ui.radio_button

    def register(self, target):
        super().register(target)
        # 设置选项文本
        self.set_inbox_text(self.choices)  # 父类中 self.choices = content

    def get_inbox_text(self):
        """
        获取选项文本

        :return: 选项文本
        """
        return self._ui.radio_button.text()

    def set_inbox_text(self, text):
        """
        设置选项文本

        :param text: 选项文本
        :return:
        """
        self._ui.radio_button.setText(text)
