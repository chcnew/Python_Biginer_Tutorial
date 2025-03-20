# !/usr/bin/env python3
# encoding: utf-8


"""
功 能：
"""

from PySide2.QtCore import QMetaObject, QSize
from PySide2.QtWidgets import QFileDialog, QGridLayout, QLabel, QLineEdit, QPushButton

from ucmtools.base_widgets.base_widget import BaseWidget
from ucmtools.composite_widgets.composite_widget import CompositeWidget


class UiForm:
    """openfile组件"""

    def __init__(self):
        self.label = None
        self.line_edit = None
        self.push_button = None

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
        self.line_edit.setMinimumSize(QSize(240, 40))
        self.line_edit.setObjectName(u"line_edit")
        self.push_button = QPushButton(form)
        self.push_button.setObjectName(u"push_button")
        self.push_button.setMaximumHeight(40)
        self.push_button.clicked.connect(lambda: self.btn_slot(form))
        QMetaObject.connectSlotsByName(form)

    def btn_slot(self, form):
        """

        :param form:
        :return:
        """
        fpath, _ = QFileDialog.getOpenFileName(form, "Open File", "", 'All Files(*)')
        if fpath:
            self.line_edit.setText(fpath)


class OpenFileSingle(BaseWidget):
    """单个打开文件类，继承于基础组件基类"""

    def __init__(self, verbose_name=None, default=None, button_text=None):
        """
        :param verbose_name: Label标签文本
        :param default: 默认值
        :param button _name: 按钮文本
        """
        self._ui = UiForm()
        self.button_text = button_text
        self._grid_layout = None
        super().__init__(self._ui, verbose_name, default)

    def register(self, target):
        """

        :param target:
        :return:
        """
        super().register(target)
        if self.button_text:
            self.set_button_text(self.button_text)
        else:
            self.set_button_text("push_button")

    def get_button_text(self):
        """

        :return:
        """
        return self._ui.push_button.text()

    def set_button_text(self, value):
        """

        :param value: 文本
        :return:
        """
        self._ui.push_button.setText(value)

    def set_button_attr(self, kw_attrs: dict):
        """

        :param kw_attrs: 属性设置字典
        :return:
        """
        self._set_ui_attr({"push_button": kw_attrs})

    def _set_layout_style(self, value: str):
        """
        默认垂直布局

        :param value: "vertical", "horizontal"
        :return:
        """
        if value not in ["vertical", "horizontal"]:
            raise ValueError("The parameter can only be 'vertical' or 'horizontal'.")

        if self._main_layout is None:
            raise Exception("This object has not been registered.")

        self._grid_layout = QGridLayout()
        self._main_layout.addLayout(self._grid_layout, 0, 0, 1, 1)
        if value == "vertical":
            self._grid_layout.addWidget(self._ui.label, 0, 0, 1, 2)
            self._grid_layout.addWidget(self._ui.line_edit, 1, 0, 1, 1)
            self._grid_layout.addWidget(self._ui.push_button, 1, 1, 1, 1)
        else:
            self._grid_layout.addWidget(self._ui.label, 0, 0, 1, 1)
            self._grid_layout.addWidget(self._ui.line_edit, 0, 1, 1, 1)
            self._grid_layout.addWidget(self._ui.push_button, 0, 2, 1, 1)


class OpenFileBoxWidget(CompositeWidget):
    """继承复合组件基类"""

    def __init__(self, shape=None, verbose_name=None, titles=None, default=None, group_tf=False, button_text=None):
        """
        :param shape: 形状设置
        :param verbose_name: 整组标题
        :param titles: 全部或部分Label文本
        :param default: 默认值
        :param group_tf: 是否分组
        :param button_text: 选择按钮文本，默认为：Select
        """
        super().__init__(OpenFileSingle, shape, verbose_name, titles, None, default, None, group_tf, button_text)

    def get_button_text(self, *location):
        """

        :param location: 位置
        :return:
        """
        return self._get_sigle_obj("get_button_text", *location)

    def set_button_text(self, text, *location):
        """

        :param text: 文本
        :param location: 位置
        :return:
        """
        self._set_sigle_obj("set_button_text", text, *location)

    def set_button_attr(self, kw_attrs: dict, *location):
        """

        :param kw_attrs: 属性设置字典
        :param location: 位置
        :return:
        """
        self._set_element_attr("set_button_attr", kw_attrs, *location)
