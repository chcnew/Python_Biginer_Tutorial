# !/usr/bin/env python3
# encoding: utf-8


"""
功能：组织models调用和创建Model类
"""

import copy
from dataclasses import dataclass

from PySide2.QtCore import Qt
from PySide2.QtWidgets import QWidget, QScrollArea, QGroupBox, QGridLayout, QVBoxLayout

from ucmtools.base_widgets.base_widget import BaseWidget
from ucmtools.base_widgets.bool_widget import BoolWidget
from ucmtools.base_widgets.button_widget import ButtonWidget
from ucmtools.base_widgets.combobox_widget import ComboBoxWidget
from ucmtools.base_widgets.double_widget import DoubleWidget
from ucmtools.base_widgets.int_widget import IntWidget
from ucmtools.base_widgets.radio_widget import RadioWidget
from ucmtools.base_widgets.str_widget import StrWidget
from ucmtools.composite_widgets.box_widget import BoxWidget
from ucmtools.composite_widgets.composite_widget import CompositeWidget
from ucmtools.composite_widgets.openfile_widget import OpenFileBoxWidget
from ucmtools.composite_widgets.openfile_widget import OpenFileSingle
from ucmtools.composite_widgets.table_widget import TableWidget
from ucmtools.composite_widgets.tristate_box_widget import TristateWidget

__all__ = [
    "BaseWidget",
    "BoolWidget",
    "ButtonWidget",
    "ComboBoxWidget",
    "DoubleWidget",
    "IntWidget",
    "RadioWidget",
    "StrWidget",
    "BoxWidget",
    "CompositeWidget",
    "OpenFileSingle",
    "OpenFileBoxWidget",
    "TableWidget",
    "TristateWidget",
]


@dataclass
class CustomGroup:
    """Null CustomGroup"""


@dataclass
class Fields:
    """Null Fields"""


@dataclass
class Widgets:
    """Null Widgets"""


class MyType(type):
    """元类"""

    def __new__(cls, *args, **kwargs):
        """创建Model类时扩展"""
        new_cls = super().__new__(cls, *args, **kwargs)
        return new_cls

    def __call__(cls, *args, **kwargs):
        """实例化Model类时扩展"""
        empty_object = cls.__new__(cls, *args, **kwargs)

        empty_object._private_fields = Fields()
        empty_object.layout_widget = None

        for key, widget_cls_obj in cls.__dict__.items():
            if key == "layout_widget" and empty_object.layout_widget is None:
                empty_object.layout_widget = widget_cls_obj
                continue

            # 设置类对应属性
            # 判断创建的类中定义的属性是否为models的指定类
            type_tuple = (BaseWidget, CompositeWidget, TableWidget)

            if isinstance(widget_cls_obj, type_tuple):
                setattr(empty_object._private_fields, key, widget_cls_obj)

        cls.__init__(empty_object, *args, **kwargs)

        return empty_object


class Model(metaclass=MyType):
    """使用元类MyType创建Model类"""

    def __init__(self):

        self._fields = Fields()
        self._widgets = Widgets()
        self._generate_ui = None
        self._scroll_area = None
        self.main_layout = None
        self.custom_group = CustomGroup()

        for field, obj in vars(self._private_fields).items():
            qwx = QWidget()
            qwx.setObjectName("cpdUI")
            deep_field = copy.deepcopy(obj)
            deep_field.register(qwx)
            setattr(self._fields, field, deep_field)
            setattr(self._widgets, field, qwx)

    @property
    def generate_ui(self) -> QWidget:
        """generate_ui 返回窗口"""
        self._generate_ui = QWidget()
        self._generate_ui.setObjectName("cpdUI")
        if not self.layout_widget:
            self.main_layout = QVBoxLayout(self._generate_ui)
            for item in vars(self._widgets).values():
                self.main_layout.addWidget(item)
        elif isinstance(getattr(self, "layout_widget"), (tuple, list)):
            self.main_layout = self.__ret_grid_layout(getattr(self, "layout_widget"))
            self._generate_ui.setLayout(self.main_layout)
        else:
            raise TypeError("The parameter is incorrect.")

        return self._generate_ui

    @property
    def scroll_area(self):
        """generate_ui增加滑块"""
        self._scroll_area = QScrollArea()
        self._scroll_area.setWidget(self.generate_ui)
        self._scroll_area.setWidgetResizable(True)
        return self._scroll_area

    @staticmethod
    def get_shape(layout_widget: list) -> tuple:
        """
        获取形状

        :param layout_widget: 形状设置
        :return:
        """
        coordinate_x = len(layout_widget)
        coordinate_y = 1
        for item in layout_widget:
            if isinstance(item, (tuple, list)) and coordinate_y < len(item):
                coordinate_y = len(item)
        return coordinate_x, coordinate_y

    @staticmethod
    def get_field_lcr(field: str) -> tuple:
        """
        获取靠左 居中 靠右字符

        :param field:
        :return:
        """
        if ":" not in field:
            return field, Qt.AlignVCenter

        field_lcr = field.split(":")
        lcr_lcr_dict = {
            "left": Qt.AlignLeft,
            "center": Qt.AlignCenter,
            "right": Qt.AlignRight,
            "left|top": Qt.AlignLeft | Qt.AlignTop,
            "left|center": Qt.AlignLeft | Qt.AlignCenter,
            "left|bottom": Qt.AlignLeft | Qt.AlignBottom,
            "center|top": Qt.AlignCenter | Qt.AlignTop,
            "center|center": Qt.AlignCenter | Qt.AlignCenter,
            "center|bottom": Qt.AlignCenter | Qt.AlignBottom,
            "right|top": Qt.AlignRight | Qt.AlignTop,
            "right|center": Qt.AlignRight | Qt.AlignCenter,
            "right|bottom": Qt.AlignRight | Qt.AlignBottom,
        }
        show_style = lcr_lcr_dict.get(field_lcr[1], None)
        if show_style:
            return field_lcr[0], show_style

        return field_lcr[0], Qt.AlignVCenter  # vcenter

    def mk_group(self, layout_widget: list, title: str = "") -> QGroupBox:
        """
        实例化一个QGroupBox \
        设置QGridLayout布局，将其作为MkGroupBox空类实例属性

        :param title: 分组标题
        :param layout_widget: 二维组件布局参数
        :return:
        """
        group_object = QGroupBox()
        group_object.setTitle(title)
        group_object.setObjectName("cpdUI")
        grid_layout = self.__ret_grid_layout(layout_widget)
        group_object.setLayout(grid_layout)
        if title != "":
            setattr(self.custom_group, title, group_object)
        return group_object

    def __ret_grid_layout(self, layout_widget) -> QGridLayout:
        """
        界面布局函数

        :param layout_widget: 定义界面布局 \
        参数形式1：["field1",["field2","field3:left"],["field4","field5","field6"]...] \
        参数形式2：["field1:left",["field2","field3"],["field4","field5","field6"]...] \
        参数形式3：["field1:",["field2","field3"],["field4","field5","field6"]...].
        """
        grid_layout = QGridLayout()
        shape = self.get_shape(layout_widget)
        points = []
        for i in range(shape[0]):
            for j in range(shape[1]):
                point = (i, j)
                points.append(point)

        for pos in points:
            coordinate_x = pos[0]
            coordinate_y = pos[1]
            if isinstance(layout_widget[coordinate_x], str):
                self.__excute_layout(grid_layout, layout_widget[coordinate_x], coordinate_x, coordinate_y)
            elif isinstance(layout_widget[coordinate_x], (list, tuple)):
                self.__excute_layout(grid_layout, layout_widget[coordinate_x][coordinate_y], coordinate_x, coordinate_y)
            else:
                raise TypeError("The parameter is incorrect.")

        return grid_layout

    def __excute_layout(self, glayout: QGridLayout, field: str or list, coordinate_x, coordinate_y):
        field, lcr = self.get_field_lcr(field)
        glayout.addWidget(getattr(self._widgets, field), coordinate_x, coordinate_y, alignment=lcr)
