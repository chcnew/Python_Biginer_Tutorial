# !/usr/bin/env python3
# encoding: utf-8


"""
功 能：基础组件基类
"""

from PySide2.QtWidgets import QWidget, QGridLayout


class BaseWidget:
    """
    基础组件公共基类，定义公共属性方法说明，

    | layout_style = "vertical" or "horizontal"  label和控件的布局方式
    | hide_label = True or False  是否隐藏标签

    | register()：注册到QWidget对象
    | unregister()：反注册
    | get_label_text(): 获取标签文本
    | set_label_text(): 设置标签文本
    | get_inbox_value(): 获取输入框或选框值
    | set_inbox_value(): 设置输入框或选框值
    | get_inbox_text(): 针对QRadioButton或QCheckBox获取选项文本
    | set_inbox_text()：针对QRadioButton或QCheckBox设置选项文本
    | set_label_attr()：设置标签属性
    | set_inbox_attr()：设置输入框或选框等的属性
    """

    def __init__(self, user_interface, verbose_name=None, default=None, choices=None):
        """
        :param user_interface: ui预设控件
        :param verbose_name: 标签设置
        :param default: 默认值设置
        :param choices: combobox的值设置
        """
        self.target = None  # 目标
        self.registered = False  # 注册标识
        self._main_layout = None  # 主布局QGridLayout
        self._layout_style = None  # 设置布局
        self._hide_label = None  # 隐藏标签

        self._ui = user_interface
        self.verbose_name = verbose_name
        self.default = default
        self.choices = choices

    @property
    def get_inbox_type(self):
        """获取当前组件类别"""
        str_list = ["line_edit", "radio_button", "spin_box", "double_spin_box", "combo_box", "check_box", "push_button"]
        for item in str_list:
            if hasattr(self._ui, item):
                return item
        return ""

    @property
    def layout_style(self):
        """获取当前布局参数"""
        return self._layout_style

    @property
    def hide_label(self):
        """返回是否隐藏label"""
        return self._hide_label

    @layout_style.setter
    def layout_style(self, value: str):
        """
        设置当前布局参数

        :param value: 布局方式："vertical" or "horizontal"
        :return: str
        """
        if value not in ["vertical", "horizontal"]:
            raise ValueError("The parameter can only be 'vertical' or 'horizontal'！")

        if value == "vertical":
            for idx, item in enumerate(vars(self._ui).values()):
                self._main_layout.addWidget(item, idx, 0, 1, 1)
        else:
            for idx, item in enumerate(vars(self._ui).values()):
                self._main_layout.addWidget(item, 0, idx, 1, 1)

        self._layout_style = value

    @hide_label.setter
    def hide_label(self, value: bool):
        """
        设置是否隐藏label

        :param value: True Or False
        :return:
        """
        self._ui.label.setHidden(value)
        self._hide_label = value

    def register(self, target: QWidget):
        """
        注册至QWidget对象

        :param target: QWidget对象
        :return:
        """
        self._ui.setup_ui(target)
        self.target = target
        self.registered = True
        self._main_layout = QGridLayout(self.target)
        self._hide_label = False
        self._set_layout_style("vertical")
        self._layout_style = "vertical"
        self.set_label_text(self.verbose_name)

        if self.get_inbox_type != "combo_box":
            self.set_inbox_value(self.default)
        else:
            self.set_inbox_value(self.choices)

        if self.get_inbox_type in ["spin_box", "double_spin_box"]:
            if self.drange and isinstance(self.drange, (tuple, list)):
                if len(self.drange) != 2:
                    raise TypeError("The parameter'drange' length is incorrect.")
                self.set_range(self.drange)

    def unregister(self):
        """反注册，即删除组件"""
        self.target = None
        self.registered = False
        if self._main_layout is not None:
            for i in range(self._main_layout.count()):
                self._main_layout.itemAt(i).widget().deleteLater()

    def get_hide_label_status(self):
        """
        获取是否隐藏label状态
        | RadioWidget、BoolWidget、ButtonWidget三种子类无该方法，返回True

        :return: True Or False
        """
        if self.get_inbox_type not in ["radio_button", "check_box", "push_button"]:
            return self._hide_label
        return True

    def get_label_text(self):
        """
        获取标签文本
        | RadioWidget、BoolWidget、ButtonWidget三种子类无该方法，返回""

        :return: 返回label内容
        """
        if self.get_inbox_type not in ["radio_button", "check_box", "push_button"]:
            return self._ui.label.text()
        return ""

    def set_label_text(self, text="LabelText"):
        """
        设置标签文本
        | RadioWidget、BoolWidget、ButtonWidget三种子类无该方法

        :param text: 文本内容
        :return:
        """
        if self.get_inbox_type not in ["radio_button", "check_box", "push_button"]:
            self._ui.label.setText(text)

    def get_inbox_value(self):
        """获取输入框或选框的值"""
        obj = getattr(self._ui, self.get_inbox_type)

        if self.get_inbox_type == "combo_box":
            return obj.currentText()

        if self.get_inbox_type in ["spin_box", "double_spin_box"]:
            return obj.value()

        if self.get_inbox_type in ["check_box", "radio_button"]:
            return obj.isChecked()

        return obj.text()

    def set_inbox_value(self, value):
        """
        设置输入框或选框的值

        :param value: int or str or bool
        :return:
        """
        current_obj = getattr(self._ui, self.get_inbox_type)
        ui_attr_dict = {}

        if self.get_inbox_type in ["spin_box", "double_spin_box"]:
            if value is None:
                value = 0
            if current_obj.minimum() <= value <= current_obj.maximum():
                ui_attr_dict["setValue"] = value
            else:
                # 设置值不在可设置范围，抛出异常
                raise ValueError("The value range is incorrect.")

        elif self.get_inbox_type in ["check_box", "radio_button"]:
            if value is None:
                value = bool(value)
            ui_attr_dict["setChecked"] = value

        elif self.get_inbox_type != "combo_box":
            ui_attr_dict["setText"] = value

        else:  # combo_box类型直接跳过,具体在其模块中实现
            pass

        self.set_inbox_attr(ui_attr_dict)

    def set_hide_label_status(self, value):
        """
        设置隐藏label
        | RadioWidget、BoolWidget、ButtonWidget三种子类无该方法

        :param value: True Or False
        :return:
        """
        if self.get_inbox_type not in ["radio_button", "check_box", "push_button"]:
            self._ui.label.setHidden(value)
            self._hide_label = value

    def set_label_attr(self, kw_attrs: dict):
        """设置label相关属性"""
        if self.get_inbox_type not in ["radio_button", "check_box", "push_button"]:
            self._set_ui_attr({"label": kw_attrs})

    def set_inbox_attr(self, kw_attrs: dict):
        """
        设置输入框或选框的相关属性

        :param kw_attrs:
        :return:
        """
        self._set_ui_attr({self.get_inbox_type: kw_attrs})

    def _set_ui_attr(self, kw_attrs: dict):
        # 设置基础组件单元（如：label） -> 组件注册之后调用
        for widget_name, attrs_dict in kw_attrs.items():
            # 获取component_ui下的控件对象
            ui_attr = getattr(self._ui, widget_name)
            for key, value in attrs_dict.items():
                # 获取控件属性设置方法：attr_func
                # 执行形式 例如：ui.spin_box.setRange(x,y)
                attr_func = getattr(ui_attr, key)
                if isinstance(value, (list, tuple)):
                    attr_func(*value)
                else:
                    attr_func(value)

    def _get_layout_style(self):
        """_get_layout_style"""
        return self.layout_style

    def _set_layout_style(self, value: str):
        """_set_layout_style"""
        self.layout_style = value
