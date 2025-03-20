# !/usr/bin/env python3
# encoding: utf-8


"""
功 能：QPushButton 基础组件
"""

from functools import partial

from PySide2.QtCore import QMetaObject
from PySide2.QtWidgets import QPushButton, QWidget

from ucmtools.base_widgets.base_widget import BaseWidget


class UiForm:
    """button组件"""

    def __init__(self):
        self.push_button = None

    @staticmethod
    def btn_slot(para):
        """预留槽函数"""
        return para

    def setup_ui(self, form):
        """

        :param form: 父对象
        :return:
        """
        if not form.objectName():
            form.setObjectName("cpdUI")
        self.push_button = QPushButton(form)
        self.push_button.setObjectName(u"push_button")
        self.push_button.clicked.connect(partial(self.btn_slot, None))

        QMetaObject.connectSlotsByName(form)


class ButtonWidget(BaseWidget):
    """ButtonWidget"""

    def __init__(self, verbose_name=None):
        """
        :param verbose_name: Label标签文本
        """
        self._ui = UiForm()
        super().__init__(self._ui, verbose_name, None)

    def register(self, target: QWidget):
        """注册"""
        super().register(target)
        self.set_button_text(self.verbose_name)

    def set_label_attr(self, kw_attrs: dict):
        """不涉及关闭该功能"""

    def set_inbox_attr(self, kw_attrs: dict):
        """不涉及关闭该功能"""

    def get_hide_label_status(self):
        """不涉及关闭该功能"""

    def set_hide_label_status(self, value):
        """不涉及关闭该功能"""

    def get_label_text(self):
        """不涉及关闭该功能"""

    def set_label_text(self, text="LabelText"):
        """不涉及关闭该功能"""

    def get_inbox_value(self):
        """不涉及关闭该功能"""

    def set_inbox_value(self, value):
        """不涉及关闭该功能"""

    def set_button_attr(self, kw_attrs: dict):
        """

        :param kw_attrs: 设置属性字典
        :return:
        """
        self._set_ui_attr({"push_button": kw_attrs})

    def get_button_text(self):
        """获取标签"""
        return self._ui.push_button.text()

    def set_button_text(self, text="push_button"):
        """
        设置按钮文本

        :param text: 按钮文本
        :return:
        """
        self._ui.push_button.setText(text)
