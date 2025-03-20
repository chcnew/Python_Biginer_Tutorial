# !/usr/bin/env python3
# encoding: utf-8


"""
功 能：复合组件基类
"""

from PySide2.QtWidgets import QGridLayout, QWidget, QGroupBox


class CompositeWidget:
    """
    复合组件公共基类，定义共性方法，

    | register()：外部注册至QWidget对象
    | get_hide_labe_status(): 获取组件标签是否隐藏
    | set_hide_label_status(): 设置组件标签是否隐藏
    | get_label_text(): 获取标签文本
    | set_label_text(): 设置标签文本
    | get_inbox_value(): 获取输入框或选框值
    | set_inbox_value(): 设置输入框或选框值
    | get_layout_style(): 获取基础组件当前设置布局
    | set_layout_style(): 设置基础组件当前设置布局，默认竖直布局
    | set_label_attr()：设置基础组件标签相关属性
    | set_inbox_attr()：设置基础组件输入框或选框相关属性
    """

    def __init__(self, base, shape=None, verbose_name=None, titles=None, choices=None, default=None,
                 dranges=None, group_tf=False, button_text=None):
        """
        :param base: 基础组件类
        :param shape: 形状
        :param verbose_name: 整体标签
        :param titles: 单个组件标签\
        参数形式_1 [索引, "标题"]：[[0, "title"],[1, "title1"], ...]\
        参数形式_2 ["标题", "标题1"]：["title", "title1"]
        :param choices: RadioWidget和BoolWidget的选项文本\
        参数形式_1 [索引, "文本"]：[[0, "text"],[1, "text1"], ...]\
        参数形式_2 ["文本", "文本1"]：["text", "text1"]
        :param default: 默认值（ComboBox组件该参数无效）
        :param dranges: 设置QSpinxBox、DoubleSpinBox组件的范围
        :param group_tf: 是否分组显示
        """
        self._main_layout = None
        self.group_box = None
        self._grid_layout = None
        self._layout_style = None
        self._widget_list = []
        self.target = None
        self.registered = None

        self.base = base
        self.shape = shape
        self.verbose_name = verbose_name
        self.titles = titles
        self.default = default
        self.dranges = dranges
        self.choices = choices
        self.group_tf = group_tf
        self.button_text = button_text

    @property
    def layout_style(self):
        """获取当前布局参数"""
        return self.get_layout_style()

    @layout_style.setter
    def layout_style(self, value: str):
        """
        设置box内全部的布局（不传入坐标）

        :param value: 布局方式："vertical" or "horizontal"
        :return: str
        """
        self.set_layout_style(value)

    def register(self, target):
        """
        :param target: QWidget
        :return:
        """
        self.target = target
        self.registered = True
        # 设置默认布局
        self.set_layout_style("vertical")

        if self.shape is None:
            self.shape = [1, 1]
        self._main_layout = QGridLayout(target)

        if self.base.__name__ == "ComboBoxWidget":
            # 是combobox组件
            parameter_list = [self.verbose_name, None]
        elif self.base.__name__ in ["BoolWidget", "RadioWidget"]:
            # 选框已取消label标签设置，先传入空值,之后再将默认值设置为列表对应值
            parameter_list = [None, None]
        elif isinstance(self.default, (list, tuple)):
            # 不是combobox组件且传入类型：list or tuple
            # 识别为历列表或元组时，先将默认值设置为初始值None,之后再将默认值设置为列表对应值
            parameter_list = [self.verbose_name, None]
        else:
            # 不是combobox组件且传入类型：str
            # 识别为历字符串时，将全部默认值设置为传入值
            parameter_list = [self.verbose_name, self.default]

        pos_list = []
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                pos = (i + 1, j + 1)
                pos_list.append(pos)

        # UI分组功能函数
        self.__init_group_tf_functional(pos_list, parameter_list)
        # 参数传入设置UI
        self.__init_parameter_functional(pos_list)

    def unregister(self):
        """
        清除注册的QWidget实例

        :return:
        """
        self.target = None
        self.registered = False
        for i in range(self._main_layout.count()):
            self._main_layout.itemAt(i).widget().deleteLater()

    def get_hide_label_status(self, *location):
        """
        获取是否隐藏布尔值
        | "BoolWidget", "RadioWidget"不涉及，返回一个值：True；其他类型子类返回一个列表

        :param location: 位置参数：[x, y]
        :return:
        """
        if self.base.__name__ not in ["BoolWidget", "RadioWidget"]:
            return self._get_sigle_obj("get_hide_label_status", *location)
        return True

    def set_hide_label_status(self, value: bool, *location):
        """
        设置是否隐藏布尔值

        :param value: True 或 False
        :param location: 位置参数：[x, y]
        :return:
        """
        if self.base.__name__ not in ["BoolWidget", "RadioWidget"]:
            self._set_sigle_obj("set_hide_label_status", value, *location)

    def get_label_text(self, *location):
        """
        获取Label文本
        | "BoolWidget", "RadioWidget"不涉及，返回一个空串；其他类型子类返回一个列表

        :param location: 位置参数\
        参数形式1：全部位置获取 无参数\
        参数形式2：单个位置获取 [1,1]\
        参数形式3：多个位置获取 [1,1],[1,2],...
        :return:
        """
        if self.base.__name__ not in ["BoolWidget", "RadioWidget"]:
            return self._get_sigle_obj("get_label_text", *location)
        return ""

    def set_label_text(self, text: str, *location):
        """
        设置Label文本

        :param text:
        :param location:
        :return:
        """
        if self.base.__name__ not in ["BoolWidget", "RadioWidget"]:
            self._set_sigle_obj("set_label_text", text, *location)

    def get_inbox_value(self, *location):
        """
        获取输入框或选框的值

        :param location: 位置列表
        :return:
        """
        return self._get_sigle_obj("get_inbox_value", *location)

    def set_inbox_value(self, value, *location):
        """
        设置输入框或选框的值

        :param value: 设置值
        :param location: 位置列表
        :return:
        """
        self._set_sigle_obj("set_inbox_value", value, *location)

    def get_layout_style(self, *location):
        """
        获取布局值（支持坐标）
        | "BoolWidget", "RadioWidget"不涉及，返回字符串："nolayout"；其他类型子类返回一个列表

        :param location:
        :return:
        """
        if self.base.__name__ not in ["BoolWidget", "RadioWidget"]:
            return self._get_sigle_obj("_get_layout_style", *location)
        return "nolayout"

    def set_layout_style(self, value, *location):
        """
        设置布局（支持坐标）

        :param value:
        :param location:
        :return:
        """
        if self.base.__name__ not in ["BoolWidget", "RadioWidget"]:
            self._set_sigle_obj("_set_layout_style", value, *location)
            self._layout_style = self.get_layout_style()

    def set_label_attr(self, kw_attrs: dict, *location):
        """

        :param kw_attrs:
        :param location:
        :return:
        """
        if self.base.__name__ not in ["BoolWidget", "RadioWidget"]:
            self._set_element_attr("set_label_attr", kw_attrs, *location)

    def set_inbox_attr(self, kw_attrs: dict, *location):
        """

        :param kw_attrs:
        :param location:
        :return:
        """
        if not location:
            self._set_element_attr("set_inbox_attr", kw_attrs)
        else:
            self._set_element_attr("set_inbox_attr", kw_attrs, *location)

    def _get_sigle_obj(self, attr, *location):
        value_layout_list = []
        if not location:
            for item in self._widget_list:
                func = getattr(item, attr)
                value_layout_list.append(func())
        else:
            for loc in location:
                if isinstance(loc, (list, tuple)) and len(loc) == 2:
                    # 列表元素是长度为2的列表
                    addr = (loc[0] - 1) * self.shape[1] + loc[1] - 1
                elif isinstance(loc, int):
                    # 列表元素是数字
                    addr = loc - 1
                else:
                    raise TypeError("The parameter is incorrect.")

                func = getattr(self._widget_list[addr], attr)
                value_layout_list.append(func())

        return value_layout_list

    def _set_sigle_obj(self, attr, value, *location):
        if not location:
            for item in self._widget_list:
                # 全部设置
                func = getattr(item, attr)
                func(value)
        else:
            for loc in location:
                if isinstance(loc, (list, tuple)) and len(loc) == 2:
                    # 列表元素是长度为2的列表
                    addr = (loc[0] - 1) * self.shape[1] + loc[1] - 1
                elif isinstance(loc, int):
                    # 列表元素是数字
                    addr = loc - 1
                else:
                    raise TypeError("The parameter is incorrect.")

                func = getattr(self._widget_list[addr], attr)
                func(value)

    def _set_element_attr(self, name, kw_attrs: dict, *location):
        if not location:
            for item in self._widget_list:
                func = getattr(item, name)
                func(kw_attrs)
        else:
            for loc in location:
                if isinstance(loc, (tuple, list)) and len(loc) == 2:
                    addr = (loc[0] - 1) * self.shape[1] + loc[1] - 1
                elif isinstance(loc, int):
                    addr = loc - 1
                else:
                    raise TypeError("The parameter is incorrect.")

                func = getattr(self._widget_list[addr], name)
                func(kw_attrs)

    def __set_inbox_attr_form_number(self, content: str or list or tuple, func_name="set_inbox_attr",
                                     attr_str="setText"):
        """
        :param content: 设置选项文本\
         | 按列表索引设置：[1, "text"]\
         | 全部设置："text"
        :param func_name: 函数名 默认值：set_inbox_attr
        :param attr_str: 属性名： setText
        :return:
        """
        if isinstance(content, (list, tuple)):
            for idx, item in enumerate(content):
                if isinstance(item, (list, tuple)):
                    func = getattr(self._widget_list[item[0]], func_name)
                    func({attr_str: item[1]})
                else:
                    func = getattr(self._widget_list[idx], func_name)
                    func({attr_str: item})
        else:
            func = getattr(self._widget_list[0], func_name)
            func({attr_str: content})

    def __init_group_tf_functional(self, pos_list, parameter_list):
        """
        分组功能函数

        :param pos_list: 位置坐标列表
        :param parameter_list: 参数列表
        :return:
        """
        if not self.group_tf:
            for pos in pos_list:
                qwidget = QWidget()
                # 分情况实例化基础组件
                base_widget = self.base(*parameter_list)
                # 默认显示标签
                base_widget.register(qwidget)
                self._main_layout.addWidget(qwidget, pos[0], pos[1])
                self._widget_list.append(base_widget)

        else:
            # 分组显示
            self.group_box = QGroupBox()
            self._grid_layout = QGridLayout(self.group_box)

            for pos in pos_list:
                qwidget = QWidget()
                # 分情况实例化基础组件
                base_widget = self.base(*parameter_list)
                self.group_box.setTitle(self.verbose_name)
                base_widget.register(qwidget)
                base_widget.hide_label = False
                self._main_layout.addWidget(self.group_box, 1, 1)
                self._grid_layout.addWidget(qwidget, pos[0], pos[1])  # 分组内部从[0,0]位置开始
                self._widget_list.append(base_widget)

    def __init_parameter_functional(self, pos_list):
        """
        特性功能参数处理函数

        :param pos_list: 位置坐标列表
        :return:
        """
        # 设置标签文本(RadioWidget/BoolWidget关闭该功能)
        if self.titles and self.base.__name__ not in ["RadioWidget", "BoolWidget"]:
            self.__set_inbox_attr_form_number(self.titles, "set_label_attr", "setText")

        # 设置选项文本
        if self.choices and self.base.__name__ in ["RadioWidget", "BoolWidget"]:
            self.__set_inbox_attr_form_number(self.choices, "set_inbox_attr", "setText")

        # 设置QSpinBox、QDoubleSpinbox范围
        if self.dranges and self.base.__name__ in ["IntWidget", "DoubleWidget"]:
            self.__init_intwidget_doublewidget()

        # 设置默认值
        self.__init_default_values(pos_list)

        # ComboBoxWidget组件根据choices形式进行设置选项
        if self.base.__name__ == "ComboBoxWidget":
            self.__init_comboboxwidget()

        # OpenFileSingle设置按钮文本
        if self.button_text and self.base.__name__ == "OpenFileSingle":
            self.__init_openfilesingle()

    def __init_intwidget_doublewidget(self):
        if isinstance(self.dranges, (list, tuple)):
            for idx, value in enumerate(self.dranges):
                # 传参形式：[[-10, 10],[-20, 20]...]
                self._widget_list[idx].set_range(value)

    def __init_comboboxwidget(self):
        if isinstance(self.choices, str):
            # self.choices为字符串
            self._widget_list[0].set_inbox_value(self.choices)
        else:
            tf_list = [isinstance(item, str) for item in self.choices]
            tf = all(tf_list)  # 判断列表是否全为str类型
            for idx, item in enumerate(self.choices):
                if tf:
                    # ["x","y","z"] 全为str类型,只设置1个
                    self._widget_list[0].set_inbox_value(self.choices)
                    break

                if isinstance(item, (list, tuple)) and \
                        isinstance(item[0], int) and \
                        isinstance(item[1], (list, tuple)):
                    # qwidget对象索引对应 [[0,["x","y","z"],...]
                    self._widget_list[item[0]].set_inbox_value(item[1])
                else:
                    # 按递增顺序设置 二维列表 [["x","y","z"],...]
                    # 按递增顺序设置 混合类型 ["x",["x","y","z"],...]
                    self._widget_list[idx].set_inbox_value(item)

    def __init_openfilesingle(self):
        if isinstance(self.button_text, str):
            for item in self._widget_list:
                item.set_button_text(self.button_text)
        else:
            for idx, text in enumerate(self.button_text):
                self._widget_list[idx].set_button_text(text)

    def __init_default_values(self, pos_list):
        if self.base.__name__ == "ComboBoxWidget" or not self.default:
            return

        if isinstance(self.default, (list, tuple)):
            for idx, value in enumerate(self.default):
                self.set_inbox_value(value, pos_list[idx])
        else:
            self.set_inbox_value(self.default)
