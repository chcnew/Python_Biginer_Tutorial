# !/usr/bin/env python3
# encoding: utf-8


"""
功 能：QLabel + QCheckBox 基础组件
"""

from dataclasses import dataclass

from PySide2.QtCore import QMetaObject, QSize
from PySide2.QtWidgets import QLabel, QCheckBox

from ucmtools.base_widgets.base_widget import BaseWidget


@dataclass
class UiForm:
    """chechbox组件"""

    def __init__(self):
        self.label = None
        self.check_box = None

    def setup_ui(self, form):
        """

        :param form: 父对象
        :return:
        """
        if not form.objectName():
            form.setObjectName(u"form")
        self.label = QLabel(form)
        self.label.setObjectName(u"label")
        self.check_box = QCheckBox(form)
        self.check_box.setObjectName(u"check_box")
        self.check_box.setMinimumSize(QSize(220, 40))
        QMetaObject.connectSlotsByName(form)


class BoolWidget(BaseWidget):
    """BoolWidget"""

    def __init__(self, default=None, content=None):
        """
        :param verbose_name: Label标签文本
        :param default: 默认值：True Or False
        :param content: BaseWidget里面就是choice，选项文本内容
        """
        self._ui = UiForm()
        super().__init__(self._ui, None, default, content)

    @property
    def ret_inbox_obj(self):
        """返回单选按钮对象"""
        return self._ui.check_box

    def register(self, target):
        """

        :param target: 目标QWidget
        :return:
        """
        super().register(target)
        # 设置选项文本
        self.set_inbox_text(self.choices)  # 父类中 self.choices = content

    def get_inbox_text(self):
        """
        获取选项文本

        :return:
        """
        return self._ui.check_box.text()

    def set_inbox_text(self, value):
        """
        设置选项文本

        :param value:
        :return:
        """
        self._ui.check_box.setText(value)
