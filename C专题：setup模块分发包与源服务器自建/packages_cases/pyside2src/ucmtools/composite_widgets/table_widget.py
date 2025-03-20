# !/usr/bin/env python3
# encoding: utf-8


"""
功 能：自定义表格组件，基于QGridLayout布局；结合组件或QtWidgets下的相关控件使用
"""

from PySide2.QtCore import Qt
from PySide2.QtWidgets import QGridLayout, QLabel, QLineEdit, QSpinBox, QDoubleSpinBox


class TableWidget:
    """
    Table复合组件

    set_all_label_attr()：所有的标题属性设置
    set_row_label_attr()：行标题属性设置
    set_column_label_attr：列标题属性设置
    set_inbox_attr()：表格单元格属性设置
    get_inbox_value()：获取单元格值,支持位置参数
    set_inbox_value()：设置单元格值,支持位置参数
    add_rows()：添加多行
    add_columns()：添加多列
    add_row()：添加一行
    add_column()：添加一列
    """

    def __init__(self, base=QLineEdit, shape=None, rows_text=None, columns_text=None):
        """
        :param base: 基础组件类
        :param shape: 形状设置
        :param rows_text: 行标签
        :param columns_text: 列标签
        """
        self.main_layout = None  # 主布局
        self._widget_list = []  # QWidget实例对象存入列表
        self.title = None  # 左上角单元格设置主题
        self.row_list = []  # 行标题存储列表
        self.column_list = []  # 列标题存储列表
        self.__base_tf(base)  # 判断是否为限定base，若否则抛出异常
        self.base = base
        self.shape = shape
        self.target = None
        self.registered = None
        self.rows_text = rows_text
        self.columns_text = columns_text

    @staticmethod
    def _get_column_letter(col_idx):
        """数字转为字母组合"""
        if not 1 <= col_idx <= 18278:
            raise ValueError("Invalid column index {0}".format(col_idx))
        letters = []
        while col_idx > 0:
            col_idx, remainder = divmod(col_idx, 26)

            if remainder == 0:
                remainder = 26
                col_idx -= 1
            letters.append(chr(remainder + 64))
        return ''.join(reversed(letters))

    @staticmethod
    def __get_inbox_value(item_obj):
        if isinstance(item_obj, QLineEdit):
            value = item_obj.text()
        elif isinstance(item_obj, (QSpinBox, QDoubleSpinBox)):
            value = item_obj.value()
        else:
            raise TypeError("The base is incorrect.")
        return value

    @staticmethod
    def __set_ui_attr(obj_list, kw_attrs: dict, serial_num=None):
        if not serial_num:
            for item in obj_list:
                for key, value in kw_attrs.items():
                    # 获取控件属性设置方法：attr_func
                    attr_func = getattr(item, key)  # 如：ui.spin_box.steRange(x,y)
                    TableWidget.__excute_func(attr_func, value)

        else:
            for key, value in kw_attrs.items():
                # 获取控件属性设置方法：attr_func
                attr_func = getattr(obj_list[serial_num], key)  # 如：ui.spin_box.steRange(x,y)
                TableWidget.__excute_func(attr_func, value)

    @staticmethod
    def __excute_func(func, value):
        if isinstance(value, (tuple, list)):
            func(*value)
        else:
            func(value)

    @staticmethod
    def __base_tf(base):
        if base not in (QLineEdit, QSpinBox, QDoubleSpinBox):
            raise TypeError("The parameter base must be one of 'QLineEdit,QSpinBox,QDoubleSpinBox'")

    @staticmethod
    def __set_inbox_value(item_obj, value):
        if not isinstance(item_obj, (QLineEdit, QSpinBox, QDoubleSpinBox)):
            raise TypeError("The base is incorrect.")

        if isinstance(item_obj, QLineEdit):
            item_obj.setText(value)
        else:
            item_obj.setValue(value)

    def register(self, target):
        """

        :param target: QWidget
        :return:
        """
        self.target = target
        self.registered = True

        if not self.shape:
            self.shape = [1, 1]
        self.main_layout = QGridLayout(target)

        # 行列（0，0）位置设置标题
        self.title = QLabel("")
        self.main_layout.addWidget(self.title, 0, 0)
        # 1行0列开始添加行标题
        self._add_row_label(1, self.shape[0] + 1)
        # 0行1列开始添加列标题
        self._add_column_label(1, self.shape[1] + 1)
        # 1行1列开始添加输入框
        self._add_source_widget(self.base, self.shape)
        # 设置全部列标题靠下居中,行标题居中靠右
        self.set_row_label_attr({"setAlignment": Qt.AlignRight | Qt.AlignCenter})
        self.set_column_label_attr({"setAlignment": Qt.AlignCenter | Qt.AlignBottom})

        if self.rows_text:
            for idx, text in enumerate(self.rows_text):
                self.row_list[idx].setText(text)

        if self.columns_text:
            for idx, text in enumerate(self.columns_text):
                self.column_list[idx].setText(text)

    def unregister(self):
        """反注册"""
        self.target = None
        self.registered = False
        for i in range(self.main_layout.count()):
            self.main_layout.itemAt(i).widget().deleteLater()

    def set_all_label_attr(self, kw_attrs: dict):
        """

        :param kw_attrs: 设置属性字典
        :return:
        """
        self.__set_ui_attr(self.row_list, kw_attrs, None)
        self.__set_ui_attr(self.column_list, kw_attrs, None)

    def set_row_label_attr(self, kw_attrs: dict, serial_num=None):
        """
        设置行名相关属性

        :param kw_attrs: 属性及设置值 如：{"setText":"日期"}
        :param serial_num: 索引数字
        :return:
        """
        self.__set_ui_attr(self.row_list, kw_attrs, serial_num)

    def set_column_label_attr(self, kw_attrs: dict, serial_num=None):
        """
        设置列名相关属性

        :param kw_attrs: 属性及设置值 如：{"setText":"日期"}
        :param serial_num: 索引数字
        :return:
        """
        self.__set_ui_attr(self.column_list, kw_attrs, serial_num)

    def get_inbox_value(self, *location):
        """

        :param location: 位置
        :return:
        """
        values_list = []
        if not location:
            for item in self._widget_list:
                values_list.append(self.__get_inbox_value(item))
        else:
            for item in location:
                if isinstance(item, (tuple, list)) and len(item) == 2:
                    # 减1是因为self._widget_list下标从0开始
                    loc = (item[0] - 1) * self.shape[1] + item[1] - 1
                elif isinstance(item, int):
                    loc = item - 1
                else:
                    raise TypeError("The parameter is incorrect.")
                obj = self._widget_list[loc]
                values_list.append(self.__get_inbox_value(obj))
        return values_list

    def set_inbox_value(self, value, *location):
        """
        2种情况：
        | location为空，
        | location不为空

        :param value: 类型 str, int, float
        :param location: 例如：[1,2], [2,2]
        :return:
        """

        # 设置全部
        if not location and isinstance(value, (str, int, float)):
            for item in self._widget_list:
                self.__set_inbox_value(item, value)

        # 按照位置顺序设置同一个值
        elif location and isinstance(value, (str, int, float)):
            for item in location:
                if isinstance(item, (tuple, list)) and len(item) == 2:
                    loc = (item[0] - 1) * self.shape[1] + item[1] - 1
                elif isinstance(item, int):
                    loc = item - 1
                else:
                    raise TypeError("The parameter is incorrect.")
                obj = self._widget_list[loc]
                self.__set_inbox_value(obj, value)

        else:
            raise TypeError("The parameter is incorrect.")

    def add_rows(self, num):
        """
        添加多行

        :param num: 添加行数
        :return:
        """
        old_row_num = self.shape[0]
        self.shape[0] += num
        for i in range(old_row_num + 1, self.shape[0] + 1):
            for j in range(1, self.shape[1] + 1):
                source_widget = self.base()
                self.main_layout.addWidget(source_widget, i, j)
                self._widget_list.append(source_widget)

        self._add_row_label(old_row_num + 1, self.shape[0] + 1)
        self.set_all_label_attr({"setAlignment": Qt.AlignCenter | Qt.AlignBottom})

    def add_columns(self, num):
        """
        添加多列

        :param num: 添加列数
        :return:
        """
        old_column_num = self.shape[1]
        self.shape[1] += num
        for i in range(1, self.shape[0] + 1):
            for j in range(old_column_num + 1, self.shape[1] + 1):
                source_widget = self.base()
                self.main_layout.addWidget(source_widget, i, j)
                addr = (i - 1) * self.shape[1] + j - 1
                self._widget_list.insert(addr, source_widget)

        self._add_column_label(old_column_num + 1, self.shape[1] + 1)
        self.set_all_label_attr({"setAlignment": Qt.AlignCenter | Qt.AlignBottom})

    def add_row(self):
        """添加1行"""
        self.add_rows(1)

    def add_column(self):
        """添加1列"""
        self.add_columns(1)

    def set_inbox_attr(self, kw_attrs: dict, *location):
        """
        设置表格框属性

        :param kw_attrs: 属性字典 例如：{setRange:[0,100]}
        :param location: 位置参数 [1,1],[1,2]
        :return:
        """
        if not location:
            self.__set_ui_attr(self._widget_list, kw_attrs, None)
        else:
            loc_widget_list = []
            for item in location:
                if isinstance(item, (tuple, list)) and len(item) == 2:
                    # 减1是因为self._widget_list下标从0开始
                    loc = (item[0] - 1) * self.shape[1] + item[1] - 1
                elif isinstance(item, int):
                    loc = item - 1
                else:
                    raise TypeError("The parameter is incorrect.")
                loc_widget_list.append(self._widget_list[loc])
            self.__set_ui_attr(loc_widget_list, kw_attrs, None)

    def _add_row_label(self, start, end):
        """添加行标题"""
        for num in range(start, end):
            row_label = QLabel(str(num))
            self.main_layout.addWidget(row_label, num, 0)
            self.row_list.append(row_label)

    def _add_column_label(self, start, end):
        """添加列标题"""
        for num in range(start, end):
            column_label = QLabel(self._get_column_letter(num))
            self.main_layout.addWidget(column_label, 0, num)
            self.column_list.append(column_label)

    def _add_source_widget(self, base, shape):
        """添加widget"""
        for i in range(1, shape[0] + 1):
            for j in range(1, shape[1] + 1):
                source_widget = base()
                self.main_layout.addWidget(source_widget, i, j)
                self._widget_list.append(source_widget)
