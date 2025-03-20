# !/usr/bin/env python3
# encoding: utf-8


"""
功 能：三态框复合组件
"""
from functools import partial
from typing import List

from PySide2.QtCore import Qt
from PySide2.QtWidgets import QCheckBox

import ucmtools as models


class TristateWidget(models.BoxWidget):
    """
     三态多选框类

     init_check_box_dict(): 初始化
     update_father_state(): 更新复选框
     clear_all(): 清空全部选项
     sub_selection_changed(): 子选框改变时
     overall_changed(): 父选框改变时
     get_selection(): 获取当前选框值
     set_inbox_value(): 设置选框值
    """

    def __init__(self, father_text=None, shape=None, verbose_name=None, titles=None, choices=None, default=None,
                 group_tf=True):
        """
        :param father_text: 三态选框（父选框）
        :param shape: 形状设置
        :param verbose_name: 标签设置
        :param choices: 选项设置（子选框文本）
        :param default: 默认值设置
        :param group_tf: 是否显示分组
        """
        super().__init__(models.BoolWidget, shape, verbose_name, titles, choices, default, None, group_tf, True)  # 多选

        self.father_text = father_text
        self.father_check_box = None
        self.childs_check_box_list = None
        self.overall_checkbox_dict = {}
        self.sub_checkbox_list_dict = {}

    @staticmethod
    def sub_selection_changed(overall_checkbox: QCheckBox):
        """

        :param overall_checkbox: QCheckBox
        :return:
        """
        checked_sum = 0
        sub_checkbox_list = overall_checkbox.children_checkbox_list
        last_state = sub_checkbox_list[0].checkState()
        for checkbox in sub_checkbox_list:
            checked_sum += checkbox.checkState()
            if last_state != checkbox.checkState():
                break
            last_state = checkbox.checkState()
        if checked_sum == 0:
            state = Qt.Unchecked
        elif checked_sum == len(sub_checkbox_list) * 2:
            state = Qt.Checked
        else:
            state = Qt.PartiallyChecked
        overall_checkbox.setCheckState(state)

    @staticmethod
    def overall_changed(overall_checkbox: QCheckBox):
        """

        :param overall_checkbox: QCheckBox
        :return:
        """
        sub_checkbox_list: List[QCheckBox] = overall_checkbox.children_checkbox_list
        # qt make Qt.PartiallyChecked achievable through click, we don't want it
        if overall_checkbox.checkState() == Qt.PartiallyChecked:
            overall_checkbox.setChecked(True)
            overall_checkbox.setFocus()
            overall_checkbox.clearFocus()
            if overall_checkbox.__dict__.__contains__('father') and isinstance(
                    overall_checkbox.father, QCheckBox):
                TristateWidget.sub_selection_changed(overall_checkbox.father)
        for sub_checkbox in sub_checkbox_list:
            sub_checkbox.setChecked(overall_checkbox.isChecked())
            sub_checkbox.setFocus()
            sub_checkbox.clearFocus()

    def register(self, target):
        """

        :param target: QWidget
        :return:
        """
        super().register(target)
        self.father_check_box = QCheckBox(self.verbose_name)
        self.father_check_box.setText(self.father_text)
        if self._grid_layout:
            self._grid_layout.addWidget(self.father_check_box, 0, 1)
        else:
            self._main_layout.addWidget(self.father_check_box, 0, 1)
        self.childs_check_box_list = [item.ret_inbox_obj for item in self._widget_list]
        self.init_check_box_dict(tristate_checkbox_groups=[[self.father_check_box, self.childs_check_box_list], ])
        self.update_father_state()  # 初始化完成后更新父选框状态

    def init_check_box_dict(self, tristate_checkbox_groups: list, name_list: list = None):
        """

        :param tristate_checkbox_groups: checkbox组
        :param name_list: 名称列表
        :return:
        """
        for i, checkbox_group in enumerate(tristate_checkbox_groups):  # [[father,[child1,child2]]]
            overall_checkbox: QCheckBox = checkbox_group[0]  # father
            overall_checkbox.setTristate(True)

            sub_checkbox_list = checkbox_group[1]
            overall_checkbox.children_checkbox_list = sub_checkbox_list

            for sub_checkbox in sub_checkbox_list:  # [child1,child2]
                sub_checkbox.father = overall_checkbox
                sub_checkbox.clicked.connect(partial(self.sub_selection_changed, overall_checkbox))

            overall_checkbox.clicked.connect(partial(self.overall_changed, overall_checkbox))
            key = None
            try:
                key = name_list[i]
            except TypeError:
                key = f'{i}'
            finally:
                self.overall_checkbox_dict[key] = overall_checkbox
                self.sub_checkbox_list_dict[key] = sub_checkbox_list

    def update_father_state(self):
        """更新父选框状态"""
        for _, overall_checkbox in self.overall_checkbox_dict.items():
            self.sub_selection_changed(overall_checkbox)

    def clear_all(self):
        """全部取消选择（值为False）"""
        for _, overall_checkbox in self.overall_checkbox_dict.items():
            overall_checkbox.setChecked(False)
            overall_checkbox.clicked.emit()

    def get_selection(self, name_list: list = None):
        """get sub checkbox check state.

        :param name_list: list[str] - query name part, should be the same name as provided when instance is created
        :return: dict [str: list] if name_list is provided, else list [bool]
        """
        if name_list is None:
            key_list = [key for key, _ in self.overall_checkbox_dict.items()]
            checked_dict = self._get_selection(key_list)
            checked_list = []
            for checked_sub_list in checked_dict.values():
                checked_list.extend(checked_sub_list)

            return checked_list

        return self._get_selection(name_list)

    def set_inbox_value(self, value, *location):
        """

        :param value: 设置值 True or False
        :param location: 位置
        :return:
        """
        super().set_inbox_value(value, *location)
        self.update_father_state()

    def get_hide_label_status(self, *location):
        """不涉及关闭该功能"""

    def set_hide_label_status(self, value: bool, *location):
        """不涉及关闭该功能"""

    def get_label_text(self, *location):
        """不涉及关闭该功能"""

    def set_label_text(self, text: str, *location):
        """不涉及关闭该功能"""

    def set_label_attr(self, kw_attrs: dict, *location):
        """不涉及 关闭该功能"""

    def _get_selection(self, name_list: list):
        """

        :param name_list:
        :return:
        """
        checked_dict = {}
        for name in name_list:
            overall_checkbox = self.overall_checkbox_dict.get(name)
            sub_checkbox_group = self.sub_checkbox_list_dict.get(name)
            if overall_checkbox.checkState() == 0:
                checked_dict[name] = [False] * len(sub_checkbox_group)
            elif overall_checkbox.checkState() == 2:
                checked_dict[name] = [True] * len(sub_checkbox_group)
            else:
                sub_checked_list = []
                for sub_checkbox in sub_checkbox_group:
                    sub_checked_list.append(sub_checkbox.isChecked())
                checked_dict[name] = sub_checked_list

        return checked_dict
